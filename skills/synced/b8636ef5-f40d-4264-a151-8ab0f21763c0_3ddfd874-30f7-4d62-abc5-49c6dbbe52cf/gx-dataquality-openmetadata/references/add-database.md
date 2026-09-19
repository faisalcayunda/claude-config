# Adding a database (new source) or scaffolding a new repo

## Add a new source to an existing repo (no new Python)
1. `config/connections.yaml` → add under `sources:` a friendly name → env var:
   ```yaml
   sources:
     scm:  {env: SCM_DB_DSN}
     hris: {env: HRIS_DB_DSN}   # new
   ```
2. `.env` → add the real DSN: `HRIS_DB_DSN=postgresql://user:pass@host:5432/dbname`
3. Table YAMLs then use `source: hris`.

Caveats:
- **Same OpenMetadata instance.** `OM_HOST` / `OM_TOKEN` point at one catalog. The new
  tables must be catalogued there; their `fqn` just points at wherever OM has them (a
  different service prefix). A *different* OM server would need extra work — flag it to the
  user, don't assume.
- **Postgres only.** `db.py` uses psycopg2. A non-Postgres source needs a driver added —
  that's a `db.py` change, outside the "just add config" path, so tell the user.

## Scaffold a brand-new repo (no pipeline exists yet)
1. Copy `assets/template_repo/` to the target folder. It's the working engine (`src/`,
   `run_all.py`, `config/connections.yaml`, `requirements.txt`, `.env.example`) with an
   empty `config/tables/`.
2. `cp .env.example .env` and fill in the real DSN(s) + `OM_HOST` + `OM_TOKEN`.
3. Edit `config/connections.yaml` so `sources:` names your database(s) and `om:` points at
   your catalog's host/token env vars.
4. `pip install -r requirements.txt` (ideally a fresh venv/conda env — Great Expectations
   has heavy pinned dependencies, so isolate it).
5. Add the first table with the add-table workflow.

The bundled engine is a copy of a real, working deployment (including the GET-first,
permission-aware `om.py`), so this is copy-and-adjust, not a rewrite. Do not paste the
`.env` (secrets) into the skill or anywhere shared — only `.env.example` is a template.
