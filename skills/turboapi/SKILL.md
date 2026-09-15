---
name: turboapi-knowledge
type: reference
version: 1.0.27
source: https://github.com/justrach/turboAPI
ingested: 2026-05-18
tags: [turboapi, fastapi, zig, dhi, turbopg, python, web-framework, high-performance]
---

# TurboAPI Knowledge Base

Full knowledge is embedded in the command file:
`/Users/isal/.claude/commands/turboapi.md`

This file serves as the skill manifest and quick reference.

## Quick Triggers

Invoke `/turboapi` when:
- User asks about TurboAPI (any aspect)
- Code contains `from turboapi import` or `from dhi import BaseModel`
- User asks to migrate from FastAPI to something faster
- User asks about dhi models, turbopg, turbonet, or "Zig HTTP"
- User asks for high-performance Python API options

## Key Facts for Quick Reference

| Fact | Value |
|---|---|
| Python version required | 3.14t (free-threaded) |
| Zig version required | 0.16.0 (pinned) |
| Throughput (HTTP-only, cache off) | ~140-155k req/s |
| Speedup vs FastAPI (avg) | 14.1x HTTP, 15x+ with DB |
| Max body size | 16MB (hardcoded) |
| TLS support | No (reverse proxy required) |
| WebSocket | In progress |
| Status | Alpha |
| Model library | dhi (NOT pydantic) |
| Server command | `app.run()` (NOT uvicorn for Zig backend) |
| Install | `pip install turboapi` |
| GitHub | https://github.com/justrach/turboAPI |

## Common Mistakes to Avoid

1. Using `pydantic.BaseModel` instead of `dhi.BaseModel`
2. Using `uvicorn.run(app)` instead of `app.run()` for Zig backend
3. Running with `python3` instead of `python3.14t`
4. Claiming native TLS/HTTP2 support (needs reverse proxy)
5. Using string interpolation in TurboPG queries (must use `$1`, `$2`)
6. Adding `Depends()` to hot routes without knowing it forces `enhanced` dispatch
