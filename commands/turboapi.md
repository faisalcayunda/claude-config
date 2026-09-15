---
name: turboapi
description: Expert knowledge base for TurboAPI — FastAPI-compatible Python web framework with Zig HTTP core (v1.0.27+). Triggers: "turboapi", "from turboapi import", "dhi model", "turbopg", "migrate from fastapi", "zig http", "turbonet", questions about fast Python API, TurboAPI route scaffolding, build/test guidance.
argument-hint: "[--route <name>] [--method GET|POST|PUT|DELETE] [--db] [--migrate] [--build] [--test] [pattern]"
---

EXECUTE IMMEDIATELY — do not deliberate.

You are a TurboAPI expert. Read the knowledge base below, parse $ARGUMENTS, then act.

---

## Argument Parsing

Extract from `$ARGUMENTS`:

- `--route <name>` → scaffold a plain HTTP route for resource `<name>`
- `--method <VERB>` → HTTP verb for route scaffold (default: GET + POST CRUD)
- `--db` → scaffold a TurboPG database-backed route (use with --route)
- `--migrate` → produce FastAPI → TurboAPI migration guide for the current project
- `--build` → produce build instructions (debug or --release)
- `--test [pattern]` → produce test run instructions, optionally scoped to pattern
- `--perf` → produce performance tuning guide
- no flag → answer the user's question from the knowledge base below

---

## KNOWLEDGE BASE: TurboAPI v1.0.27

### 1. Identity

TurboAPI is a Python web framework with a **Zig HTTP core**. It is API-compatible with FastAPI — same decorators, same `Depends()`, same middleware interface. The difference is the runtime: instead of Python's ASGI stack (uvicorn → Starlette), TurboAPI routes all HTTP parsing, routing, JSON validation, and response writing through a compiled Zig extension (`turbonet.*.so`).

**Performance (cache disabled, Docker, M3 Pro):**

| Workload | TurboAPI | FastAPI | Speedup |
|---|---|---|---|
| GET / (HTTP-only) | 149,930/s | 11,252/s | 13.3x |
| POST /items (dhi model) | 155,687/s | 8,667/s | 18.0x |
| GET /users/{id} (DB, uncached) | 80,791/s | 5,203/s | 15.5x |
| Average HTTP-only | — | — | 14.1x |

**Status:** Alpha. 380+ passing tests. Not production-ready without a reverse proxy (Caddy/nginx) for TLS.

---

### 2. Requirements

- **Python 3.14t** (free-threaded build) — `uv python install 3.14t`
- **Zig 0.16.0** (pinned — not 0.15.x, not later until repo upgrades)
- Reverse proxy for HTTPS (Caddy with Let's Encrypt is recommended)

---

### 3. Installation

**PyPI (prebuilt binary):**
```bash
pip install turboapi
```

**Docker (easiest — builds everything):**
```bash
git clone https://github.com/justrach/turboAPI.git
cd turboAPI
docker compose up
# Hit http://localhost:8000
```

**Build from source:**
```bash
git clone https://github.com/justrach/turboAPI.git
cd turboAPI
uv python install 3.14t
python3.14t zig/build_turbonet.py --install        # debug build
# python3.14t zig/build_turbonet.py --install --release  # for benchmarks/prod
pip install -e ".[dev]"
make hooks     # pre-commit hook
make test      # verify
```

Verify the native backend:
```bash
uv run --python 3.14t python -c "from turboapi import turbonet; print(turbonet.hello())"
```

Build modes:
- `--install` → copies `.so` into Python package dir (required for dev)
- `--release` → ReleaseFast optimizations (for benchmarks/production)
- no flags → compile check only

---

### 4. Minimal App

```python
from turboapi import TurboAPI
from dhi import BaseModel

app = TurboAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: int = 1

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": "Widget"}

@app.post("/items")
def create_item(item: Item):
    return {"item": item.model_dump(), "created": True}

if __name__ == "__main__":
    app.run()          # uses Zig backend (fast)
    # app.run(host="0.0.0.0", port=8000)
```

Run: `python3.14t app.py`  
Output: `TurboNet-Zig server listening on 127.0.0.1:8000`

ASGI fallback also exists (`uvicorn main:app`) for testing route definitions without compiling Zig — but it's pure-Python and slow. Use `app.run()` for the actual Zig backend.

---

### 5. Migration from FastAPI

**Step 1 — Swap imports (ONLY change needed for most apps):**

```python
# Before
from fastapi import FastAPI, Depends, HTTPException, Query, Path, APIRouter
from pydantic import BaseModel, Field

# After
from turboapi import TurboAPI as FastAPI, Depends, HTTPException, Query, Path, APIRouter
from dhi import BaseModel, Field          # NOT pydantic
```

**Step 2 — Use the built-in server:**

```python
# FastAPI way (still works, slower)
uvicorn.run(app, host="0.0.0.0", port=8000)

# TurboAPI way (20x faster via Zig)
app.run(host="0.0.0.0", port=8000)
```

**Step 3 — Run with free-threaded Python:**

```bash
python3.14t app.py
```

**Key difference — dhi vs pydantic:**

`dhi` is Pydantic-compatible but validates in Zig before acquiring the Python GIL. Invalid POST bodies return 422 without touching Python. Supported: `str`, `int`, `float`, `bool`, `list`, `dict`, nested models, `Field(min_length=..., max_length=..., gt=..., ge=..., lt=..., le=...)`.

**Extension — implicit header binding (not in FastAPI):**

```python
@app.get("/headers")
def read_headers(authorization: str = "missing", x_request_id: str = "missing"):
    return {"auth": authorization, "rid": x_request_id}
# TurboAPI: Authorization + X-Request-ID headers populate these automatically
# FastAPI: requires Header() / Annotated — use Header() for shared code
```

---

### 6. dhi Models (Zig-native Validation)

```python
from dhi import BaseModel, Field

class CreateUser(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str
    age: int = Field(gt=0, le=150)
    tags: list[str] = []

class Address(BaseModel):
    street: str
    city: str

class UserWithAddress(BaseModel):
    name: str
    address: Address         # nested models supported
```

**What dhi does at runtime:**
1. At startup: model schema compiled into Zig validator
2. On each POST: JSON parsed + validated in Zig, BEFORE acquiring GIL
3. On validation failure: 422 returned immediately, Python never called
4. On success: Zig builds a Python dict (`body_dict`) from parsed JSON → `model_class(**data)` → handler receives real model instance

**Result:** no `json.loads` in Python, no GIL contention on validation, no wasted handler calls on bad data.

---

### 7. Handler Classification

At startup, each route is analyzed once and assigned the fastest possible dispatch path. You don't configure this — it's automatic based on function signature.

| Handler type | When used | What it skips |
|---|---|---|
| `native_ffi` | C/Zig shared library handlers | Python entirely, no GIL at all |
| `simple_sync_noargs` | `GET` with zero parameters | GIL lookup, tuple/kwargs alloc, uses `PyObject_CallNoArgs` |
| `model_sync` | `POST` with a `dhi.BaseModel` param | `json.loads`, validates+parses in Zig |
| `simple_sync` | `GET` with path/query params | Header parsing, body parsing, regex |
| `body_sync` | `POST` without model params | Header parsing, regex |
| `enhanced` | `Depends()`, middleware, complex types | Nothing — full Python dispatch |

**Implications for code:**
- A `GET /health` with no params → `simple_sync_noargs` → fastest
- A `POST /users` with `dhi.BaseModel` → `model_sync` → Zig validates before GIL
- Adding `Depends()` to any route → `enhanced` → slower but full Python power
- Middleware downgrades Zig fast-path to enhanced for all routes it wraps

**Native FFI handler (skip Python entirely):**
```python
app.add_native_route("GET", "/fast", "./libhandler.so", "handle_request")
```

---

### 8. Caching Layers

TurboAPI has two optional caching layers, both on by default.

| Cache | Behavior | Env var to disable |
|---|---|---|
| Response cache | noargs handlers: result cached after first call, subsequent skip Python | `TURBO_DISABLE_CACHE=1` |
| DB result cache | SELECT results cached 30s TTL, 10K max entries, per-table invalidation on writes | `TURBO_DISABLE_DB_CACHE=1` |
| DB cache TTL | Override the 30s default | `TURBO_DB_CACHE_TTL=<seconds>` |

**Benchmarking correctly:**
```bash
# Pure HTTP benchmark (no caching)
TURBO_DISABLE_CACHE=1 python3.14t app.py

# DB benchmark (no caching at any layer)
TURBO_DISABLE_CACHE=1 TURBO_DISABLE_DB_CACHE=1 TURBO_DISABLE_RATE_LIMITING=1 python3.14t app.py
```

---

### 9. Security Stack

```python
from turboapi import Depends, HTTPException
from turboapi.security import (
    OAuth2PasswordBearer,
    OAuth2AuthorizationCodeBearer,
    HTTPBearer,
    HTTPBasic,
    APIKeyHeader,
    APIKeyQuery,
    APIKeyCookie,
)

# OAuth2 Bearer
oauth2 = OAuth2PasswordBearer(tokenUrl="/token")

@app.get("/protected")
def protected_route(token: str = Depends(oauth2)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user": "authenticated"}

# API Key
api_key_header = APIKeyHeader(name="X-API-Key")

@app.get("/api/data")
def api_data(api_key: str = Depends(api_key_header)):
    if api_key != "secret-key":
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"data": "..."}
```

JWT helper (built-in):
```python
from turboapi.jwt_auth import create_access_token, verify_access_token

token = create_access_token(data={"sub": "user123"}, secret="my-secret")
payload = verify_access_token(token, secret="my-secret")
```

Password hashing (built-in, exported at top level):
```python
from turboapi import hash_password, verify_password

hashed = hash_password("mypassword")
ok = verify_password("mypassword", hashed)
```

---

### 10. Middleware

```python
from turboapi.middleware.cors import CORSMiddleware
from turboapi.middleware.gzip import GZipMiddleware
from turboapi.middleware.sessions import SessionMiddleware
from turboapi.middleware.trustedhost import TrustedHostMiddleware
from turboapi.middleware.httpsredirect import HTTPSRedirectMiddleware

# CORS — Zig-native (pre-rendered headers, 0% overhead, OPTIONS handled in Zig)
app.add_middleware(CORSMiddleware,
    allow_origins=["https://example.com"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)

# GZip
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Sessions
app.add_middleware(SessionMiddleware, secret_key="change-me")
```

**CORS performance note:** CORS headers are pre-rendered once at startup and injected via `memcpy`. Overhead is 0% (was 24% with Python middleware). OPTIONS preflight handled entirely in Zig.

**Middleware throughput caveat:** Adding any middleware downgrades Zig fast-path routes to `enhanced` dispatch. For max throughput on specific routes, avoid middleware on them or use Zig-native options (CORSMiddleware is already Zig-native).

---

### 11. TurboPG (Zig-native Postgres)

TurboPG is a Zig-native Postgres driver. It ships with turboapi as `python/turbopg/`.

```python
from turbopg import Database

db = Database("postgres://user:pass@localhost/mydb", pool_size=16)

# Multiple rows
rows = await db.query("SELECT * FROM users WHERE age > $1", [18])

# Single row
user = await db.query_one("SELECT * FROM users WHERE id = $1", [user_id])

# Write (returns affected row count)
affected = await db.execute("INSERT INTO users (name, email) VALUES ($1, $2)", [name, email])

# Unix socket (50% lower latency)
db = Database("postgres://user:pass@/var/run/postgresql/mydb")
```

**With TurboAPI route (Zig end-to-end, fastest path):**
```python
from turboapi import TurboAPI
from turbopg import Database
from dhi import BaseModel

app = TurboAPI()
db = Database("postgres://user:pass@localhost/mydb")

class UserCreate(BaseModel):
    name: str
    email: str

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await db.query_one("SELECT * FROM users WHERE id = $1", [user_id])
    if not user:
        raise HTTPException(status_code=404)
    return user

@app.post("/users")
async def create_user(user: UserCreate):
    await db.execute("INSERT INTO users (name, email) VALUES ($1, $2)",
                     [user.name, user.email])
    return {"created": True}
```

**Parameterized syntax:** Always use `$1`, `$2`, etc. (Postgres-native) — never string interpolation.

**Type coercions:** Decimals → float, datetimes → ISO string, memoryview → string.

**Performance (DB + HTTP, cache disabled):**

| Query | TurboAPI + pg.zig | FastAPI + asyncpg | FastAPI + SQLAlchemy |
|---|---|---|---|
| GET /health | 266,351/s | 9,161/s | 5,010/s |
| GET /users/{id} varying 1000 IDs | 80,791/s | 5,203/s | 1,983/s |
| GET /users?age_min=20 | 71,650/s | 3,162/s | 1,427/s |
| GET /search?q=... | 13,245/s | 3,915/s | 1,742/s |

---

### 12. Observability

Handlers are regular Python functions — standard tools work without adapters.

**OpenTelemetry:**
```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

provider = TracerProvider()
provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

@app.get("/users/{user_id}")
def get_user(user_id: int):
    with tracer.start_as_current_span("get_user") as span:
        span.set_attribute("user.id", user_id)
        return db.get(user_id)
```

**Prometheus:**
```python
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

REQUEST_COUNT = Counter("http_requests_total", "Total requests", ["method", "path", "status"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Latency", ["path"])

class MetricsMiddleware:
    async def __call__(self, request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        duration = time.perf_counter() - start
        REQUEST_COUNT.labels(request.method, request.url.path, response.status_code).inc()
        REQUEST_LATENCY.labels(request.url.path).observe(duration)
        return response

app.add_middleware(MetricsMiddleware)

@app.get("/metrics")
def metrics():
    from turboapi import Response
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
```

**Caveat:** Middleware-based tracing covers `enhanced`-path routes. Zig fast-path routes bypass the Python middleware stack. To trace every route, add middleware and accept ~24% throughput overhead.

---

### 13. Async Handlers

```python
@app.get("/async-data")
async def async_handler():
    data = await fetch_from_database()
    return {"data": data}
```

Async handlers are auto-detected and awaited via `asyncio.run()`. Mix sync and async freely.

---

### 14. Responses & Exceptions

```python
from turboapi import Response, JSONResponse, HTMLResponse, RedirectResponse, HTTPException
from turboapi.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

@app.get("/custom")
def custom():
    return JSONResponse(content={"key": "val"}, status_code=HTTP_201_CREATED)

@app.get("/redirect")
def redir():
    return RedirectResponse(url="/new-path")

@app.get("/html")
def html():
    return HTMLResponse("<h1>Hello</h1>")

@app.get("/error")
def error():
    raise HTTPException(status_code=404, detail="Not found")
```

---

### 15. APIRouter (Prefix Routing)

```python
from turboapi import TurboAPI, APIRouter

router = APIRouter(prefix="/api/v1")

@router.get("/users")
def list_users():
    return {"users": []}

@router.post("/users")
def create_user():
    return {"created": True}

app = TurboAPI()
app.include_router(router)
```

---

### 16. Background Tasks

```python
from turboapi import BackgroundTasks

@app.post("/send")
def send_email(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_func, "user@example.com")
    return {"message": "Email queued"}
```

---

### 17. Static Files

```python
from turboapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")
```

---

### 18. SSE (Server-Sent Events)

```python
from turboapi.sse import EventSourceResponse

@app.get("/stream")
async def stream():
    async def generator():
        for i in range(10):
            yield {"data": f"event {i}"}
    return EventSourceResponse(generator())
```

---

### 19. TestClient

```python
from turboapi.testclient import TestClient

app = TurboAPI()

@app.get("/")
def root():
    return {"ok": True}

client = TestClient(app)
r = client.get("/")
assert r.status_code == 200
assert r.json() == {"ok": True}
```

Use TestClient for all tests — it exercises the same route/dispatch logic without a running server.

---

### 20. Architecture Summary

**Request lifecycle (Zig handles everything except business logic):**
```
HTTP request
  └─ TCP accept (24-thread pool)
  └─ Header parse (8KB buffer)
  └─ Route match (radix trie, turboapi-core)
  └─ Body read (dynamic alloc, 16MB cap)
  └─ Dispatch:
       ├─ native_ffi: C function call, no GIL
       ├─ model_sync: JSON parse+validate in Zig → PyDict → handler(model)
       ├─ simple_sync_noargs: PyObject_CallNoArgs → handler()
       ├─ simple_sync: Zig extracts path/query params → handler(params)
       ├─ body_sync: handler(body)
       └─ enhanced: full Python dispatch (Depends, middleware)
  └─ Response: PyUnicode_AsUTF8 → direct write() to socket (zero-copy)
```

**Shared Zig core (`turboapi-core`):**
- Radix trie router with path params + wildcards
- `percentDecode`, `queryStringGet`, `statusText`, `formatHttpDate`
- Bounded thread-safe response cache
- Also used by [merjs](https://github.com/justrach/merjs)

**Zero-copy responses:** `PyUnicode_AsUTF8()` gets a pointer to the Python string's internal buffer, then `write()` directly on the socket. No `memcpy`, no temp buffers.

---

### 21. Alpha Limitations (as of v1.0.27)

- **No native TLS / HTTP/2 / HTTP/3** — use Caddy/nginx/cloudflared in front
- **16MB hardcoded body size limit** (no config)
- **WebSocket support in progress** — not production-ready
- **Free-threaded Python 3.14t** is new — some C extensions may not be thread-safe
- **30s read timeout** for basic slow-loris protection; use reverse proxy for stricter limits

---

### 22. When to Use TurboAPI vs Alternatives

| Scenario | Recommendation |
|---|---|
| Existing FastAPI codebase, need 10-20x throughput | **TurboAPI** |
| Heavy Python ML/data dependencies (PyTorch, LangChain) | **TurboAPI** |
| Background workers + AI inference + HTTP | **TurboAPI** |
| Pure JSON proxy, no business logic | Go (net/http or Gin) |
| Need >200k req/s with <0.1ms p99 | Native server, no Python |
| Need HTTP/2, gRPC today natively | Go (mature ecosystem) |
| Embedded systems, <1MB binary | Rust |
| Existing Go/Rust team | Stay in your stack |

---

### 23. Feature Parity vs FastAPI

| Feature | Status |
|---|---|
| Route decorators (@get, @post, etc.) | ✅ |
| Path parameters with type coercion | ✅ |
| Query parameters | ✅ |
| JSON request body | ✅ |
| Async handlers | ✅ |
| Dependency injection (Depends()) | ✅ |
| OAuth2 (Password, AuthCode) | ✅ |
| HTTP Bearer / Basic auth | ✅ |
| API Key (Header / Query / Cookie) | ✅ |
| CORS middleware (Zig-native, 0% overhead) | ✅ |
| GZip middleware | ✅ |
| HTTPException with status codes | ✅ |
| Custom responses (JSON, HTML, Redirect) | ✅ |
| Background tasks | ✅ |
| APIRouter with prefixes | ✅ |
| Native FFI handlers (C/Zig, no Python) | ✅ |
| Zig-native JSON schema validation (dhi) | ✅ |
| Large body support (up to 16MB) | ✅ |
| Python 3.14t free-threaded | ✅ |
| Static files | ✅ |
| SSE | ✅ |
| TestClient | ✅ |
| WebSocket | 🔧 In progress |
| Native HTTP/2 + TLS | 🔧 Future |
| Native HTTP/3 + QUIC | 🔧 Tracked in #138 |

---

## Workflow

### Mode: Answer (no flags)

Answer the user's TurboAPI question using the knowledge base above. Cite specific sections. Provide working code examples. Flag alpha limitations if relevant.

### Mode: Scaffold Route (`--route <name>`)

Generate a complete route for resource `<name>`. Unless `--method` is specified, generate full CRUD (GET list, GET by ID, POST create, PUT update, DELETE):

```python
from turboapi import TurboAPI, HTTPException, APIRouter
from dhi import BaseModel, Field

router = APIRouter(prefix="/<name>s")

class <Name>Create(BaseModel):
    # fields here

class <Name>Update(BaseModel):
    # optional fields here

@router.get("/")
def list_<name>s():
    return {"<name>s": []}

@router.get("/{<name>_id}")
def get_<name>(<name>_id: int):
    # fetch logic
    return {"id": <name>_id}

@router.post("/")
def create_<name>(data: <Name>Create):
    return {"created": True, "data": data.model_dump()}

@router.put("/{<name>_id}")
def update_<name>(<name>_id: int, data: <Name>Update):
    return {"updated": True}

@router.delete("/{<name>_id}")
def delete_<name>(<name>_id: int):
    return {"deleted": True}
```

Also generate a `tests/test_<name>_routes.py` with TestClient smoke tests covering 200/404/422.

### Mode: Scaffold DB Route (`--route <name> --db`)

Generate a TurboPG-backed route:

```python
from turboapi import TurboAPI, HTTPException, APIRouter
from turbopg import Database
from dhi import BaseModel, Field

router = APIRouter(prefix="/<name>s")
db = Database("postgres://user:pass@localhost/mydb")

class <Name>Create(BaseModel):
    # fields

@router.get("/{<name>_id}")
async def get_<name>(<name>_id: int):
    row = await db.query_one(
        "SELECT * FROM <name>s WHERE id = $1", [<name>_id]
    )
    if not row:
        raise HTTPException(status_code=404, detail="<Name> not found")
    return row

@router.post("/")
async def create_<name>(data: <Name>Create):
    await db.execute(
        "INSERT INTO <name>s (...) VALUES (...)", [...]
    )
    return {"created": True}
```

### Mode: Migration Guide (`--migrate`)

1. Swap imports (pydantic → dhi, FastAPI → TurboAPI).
2. Replace `uvicorn.run(app, ...)` with `app.run(...)`.
3. Run with `python3.14t app.py`.
4. Check for `pydantic.BaseModel` usage — replace with `dhi.BaseModel`.
5. Check for `pydantic.validator` / `@field_validator` — rewrite as dhi Field constraints.
6. Test with `TestClient` — behavior should be identical.
7. Verify implicitly bound headers use `Header()` if you need FastAPI-compatible semantics.

### Mode: Build (`--build`)

```bash
# Debug build (dev)
uv run --python 3.14t python zig/build_turbonet.py --install

# Release build (benchmarks/prod)
uv run --python 3.14t python zig/build_turbonet.py --install --release

# Verify
uv run --python 3.14t python -c "from turboapi import turbonet; print(turbonet.hello())"

# Or use Makefile
make build      # debug
make release    # ReleaseFast
```

Troubleshooting:
- Dependency hash mismatch → run `zig fetch --save <dep-url>`
- "Native core not available" → rebuild with `--install`
- Wrong Python → ensure `python3.14t` not `python3`

### Mode: Test (`--test`)

```bash
# Full suite (excludes WebSocket — known pre-existing failures)
uv run --python 3.14t python -m pytest tests/ -p no:anchorpy \
    --deselect tests/test_fastapi_parity.py::TestWebSocket -v

# Targeted
uv run --python 3.14t python -m pytest tests/test_<pattern>.py -v

# Zig unit tests
cd zig && zig build test

# Security fuzz (run for a few minutes on security-sensitive changes)
cd zig && zig build fuzz

# Quick smoke test
uv run --python 3.14t python -c "
from turboapi import TurboAPI
from turboapi.testclient import TestClient
app = TurboAPI()
@app.get('/')
def root(): return {'ok': True}
client = TestClient(app)
assert client.get('/').status_code == 200
print('OK')
"
```

### Mode: Performance Tuning (`--perf`)

Priority order for max throughput:

1. **Use `app.run()` not uvicorn** — Zig backend only activates with `app.run()`
2. **Avoid `Depends()` on hot routes** — forces `enhanced` dispatch
3. **Remove middleware from hot routes** — any middleware downgrades to `enhanced`
4. **Zero-param GET handlers** → `simple_sync_noargs` (fastest Python path)
5. **dhi models on POST** → `model_sync` (Zig validates, no Python json.loads)
6. **Use `TURBO_DISABLE_CACHE=0`** (default) — noargs handlers cached after first call
7. **TurboPG with Unix socket** → 50% lower DB latency than TCP: `postgres://user:pass@/var/run/postgresql/mydb`
8. **DB cache** → `TURBO_DISABLE_DB_CACHE=0` (default) — 30s TTL cache, 10K entries
9. **Release build** → `python3.14t zig/build_turbonet.py --install --release`
10. **Native FFI** → `app.add_native_route("GET", "/hot", "./libhandler.so", "fn")` — no Python at all

---

## Output Format

- Working, copy-paste-ready Python code
- Use `dhi.BaseModel` not `pydantic.BaseModel`
- Use `app.run()` not `uvicorn.run()`
- Include `python3.14t` in shell commands
- Flag alpha limitations inline when relevant
- For DB routes: always use `$1`, `$2` placeholders

## Hard Constraints

- Never use `pydantic` — always `dhi`
- Never recommend `uvicorn` for production Zig backend
- Never claim WebSocket is production-ready
- Never claim native TLS/HTTP/2/HTTP/3 without a reverse proxy
- Never recommend body size > 16MB (hardcoded limit)
- Always use parameterized queries with `$N` syntax for TurboPG

Stream all output live — never run in background.
