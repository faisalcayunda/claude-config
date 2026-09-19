"""
om.py -- everything needed to mirror a GX validation result into
OpenMetadata: resolve the Test Case's fully-qualified name (reading it, and
creating it only if it's genuinely missing AND the token is allowed to),
then push a result onto it. Idempotent, safe to call on every run.

--- CURRENT DESIGN, in one paragraph (2026-07-13) ---
The bot's token ('testsuite-bot') can READ test cases and PUSH results onto
them, but CANNOT create test cases (POST /v1/dataQuality/testCases -> 403).
OpenMetadata checks that create-permission BEFORE it checks whether the case
already exists, so any POST -- even one targeting an already-existing case --
is refused outright. ensure_test_case() therefore resolves each case by
GET-ting it first (never re-POSTing an existing one), and only attempts a POST
for a genuinely new check; if that POST is refused it raises a clear,
actionable error. All 28 checks across the two current tables already exist,
so the normal run never POSTs and never hits the 403. See ensure_test_case().

--- Why this file looks the way it does (read this if you're debugging) ---

An earlier version of this file tried to create a brand-new custom Test
Definition per check (POST /v1/dataQuality/testDefinitions) before creating
the Test Case itself. That hit a real 403 Forbidden: this bot's token can
push results onto EXISTING test cases, and can create new test CASES, but
does not have permission to create new test DEFINITIONS -- a different,
more restricted action in OpenMetadata's RBAC model.

Rather than chase down broadening that bot's role/policy, this version
sidesteps the problem entirely: it never creates a custom Test Definition.
Every check's GX expectation is mapped (via BUILTIN_DEFINITIONS below) onto
one of OpenMetadata's own built-in test definitions instead -- the full set
of which was pulled live from this server via get_test_definitions. Most
checks map onto an obvious built-in (not-null, unique, regex, in-set,
between). The three multi-column / cross-column checks in these two tables
(compound uniqueness, seller<>buyer pair inequality, updated_at>=created_at)
have no direct built-in equivalent, so they map onto the generic
`tableCustomSQLQuery` definition instead, with a real, readable SQL
expression describing the check for anyone reading it in OpenMetadata's UI.
That SQL is documentation only -- OpenMetadata's own engine never executes
it. Great Expectations still computes the actual pass/fail, exactly as for
every other check; only the *result* gets pushed onto this Test Case.

Also changed: this version never guesses a Test Case's fully-qualified name
client-side. On first creation (POST returns 200/201) it reads the real
`fullyQualifiedName` straight from OpenMetadata's response body. Only when
the test case already exists (409) does it fall back to looking one up --
via GET .../testCases?entityLink=..., matching on name -- rather than
constructing a guessed FQN string. (That GET-based lookup is a
reasonable-confidence design choice, not yet empirically exercised against
the live server as of this writing -- if `entityLink` turns out not to be
the right filter param for this OpenMetadata version, `_find_existing_fqn`
will raise a clear error instead of silently pushing a result onto a
wrong/guessed FQN. If that happens, it's a small, contained thing to fix --
see that function.)

One more thing this version adds, also a real error hit against this exact
server: creating a Test Case 400'd on a table that had never had one before
(client_partnership, order_transaction). Root cause, confirmed by reading
OpenMetadata's own server source (TestCaseRepository.java /
TestSuiteResource.java) rather than guessing: every Test Case belongs to a
"basic" Test Suite scoped to its table (named "{table_fqn}.testSuite"), and
versions before 1.8.0 require that suite to already exist -- 1.8.0+ creates
it for you automatically as a side effect of creating the first Test Case,
but there's no downside to also doing it explicitly, since the endpoint is a
true upsert. `_ensure_test_suite()` calls
    PUT /v1/dataQuality/testSuites/basic
    {"name": "{table_fqn}.testSuite", "basicEntityReference": "{table_fqn}"}
once per table before its first Test Case is created (memoized so it's not
repeated 13+ times per run) -- always 200, nothing to catch. On a pre-1.6.2
server that endpoint won't exist yet (404), so it falls back to the older
    POST /v1/dataQuality/testSuites/executable
    {"name": "{table_fqn}.testSuite", "executableEntityReference": "{table_fqn}"}
which does need a 409 (already exists) tolerated on every re-run.

Note on the OpenMetadata API (learned across several real 404s while
building 07_gx_clients_to_openmetadata.py -- see that script's history if
you're curious): pushing a *result* is FQN-based, always -- never a UUID.
What changed across OpenMetadata versions is the endpoint itself:
    PUT  .../testCases/{fqn}/testCaseResult          (pre-1.8.0, removed)
    POST .../testCases/testCaseResults/{fqn}         (1.8.0 onward)
Since this server's exact version isn't guaranteed, push_result() tries the
current route first and falls back to the legacy one only on a 404.
"""
import json
import os
import time
import urllib.parse

import requests
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONNECTIONS_PATH = os.path.join(REPO_ROOT, "config", "connections.yaml")

_session = None
_host = None


def _client():
    global _session, _host
    if _session is None:
        with open(CONNECTIONS_PATH) as f:
            om_cfg = yaml.safe_load(f)["om"]
        host = os.environ.get(om_cfg["host_env"])
        token = os.environ.get(om_cfg["token_env"])
        if not host or not token:
            raise RuntimeError(
                f"{om_cfg['host_env']} / {om_cfg['token_env']} must both be set in "
                f".env -- see .env.example."
            )
        s = requests.Session()
        s.headers.update({"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
        _session, _host = s, host.rstrip("/")
    return _session, _host


_ensured_suites = set()  # table FQNs whose basic Test Suite we've already confirmed this run


def _ensure_test_suite(table_cfg):
    """Make sure this table's basic/executable Test Suite exists before
    creating any Test Case on it -- required on OpenMetadata < 1.8.0 (a plain
    POST .../testCases 400s without it, confirmed against this exact server);
    harmless on 1.8.0+, which would create it for you anyway. Memoized so
    it's only actually sent once per table per run, not once per check."""
    if table_cfg["fqn"] in _ensured_suites:
        return
    session, host = _client()
    suite_fqn = f"{table_cfg['fqn']}.testSuite"

    resp = session.put(
        f"{host}/v1/dataQuality/testSuites/basic",
        json={"name": suite_fqn, "basicEntityReference": table_cfg["fqn"]},
    )
    if resp.status_code in (200, 201):
        _ensured_suites.add(table_cfg["fqn"])
        return
    if resp.status_code == 404:
        # Pre-1.6.2 server -- .../testSuites/basic doesn't exist yet, only
        # the older .../testSuites/executable path (a plain POST, not an
        # upsert, so 409-already-exists is expected and tolerated).
        resp = session.post(
            f"{host}/v1/dataQuality/testSuites/executable",
            json={"name": suite_fqn, "executableEntityReference": table_cfg["fqn"]},
        )
        if resp.status_code in (200, 201, 409):
            _ensured_suites.add(table_cfg["fqn"])
            return
    resp.raise_for_status()


# ---------------------------------------------------------------------------
# BUILTIN_DEFINITIONS -- maps every "expectation" value used in config/tables/
# YAML onto one of OpenMetadata's existing built-in test definitions, so this
# file never needs Create permission on testDefinitions.
#
# Each entry is {"level": "COLUMN" or "TABLE", "definition": <OM built-in
# name>, "params": <function(check, table_cfg) -> parameterValues list>}.
# Add a new entry here whenever a table config starts using a GX expectation
# that isn't in this dict yet -- ensure_test_case() raises a clear error if
# it hits one that's missing, rather than trying to invent a new definition.
# ---------------------------------------------------------------------------

def _no_params(check, table_cfg):
    return []


def _regex_params(check, table_cfg):
    return [{"name": "regex", "value": check["kwargs"]["regex"]}]


def _in_set_params(check, table_cfg):
    if "value_set_from" in check:
        ref = check["value_set_from"]
        # The real allowed set here can be thousands of live UUIDs (e.g. every
        # clients.id) -- GX resolves and checks the real set at run time, but
        # baking that whole list into OpenMetadata's stored parameters would
        # be both huge and stale the moment a new client is added. A
        # documentation placeholder is enough since OM never executes this
        # test itself.
        allowed = [f"<dynamic set, resolved at run time by Great Expectations: {ref['query']}>"]
    else:
        allowed = list(check["kwargs"].get("value_set", []))
    return [{"name": "allowedValues", "value": json.dumps(allowed)}]


def _between_params(check, table_cfg):
    kwargs = check.get("kwargs", {})
    params = []
    if kwargs.get("min_value") is not None:
        params.append({"name": "minValue", "value": str(kwargs["min_value"])})
    if kwargs.get("max_value") is not None:
        params.append({"name": "maxValue", "value": str(kwargs["max_value"])})
    return params


def _not_in_future_params(check, table_cfg):
    # "now" has to be computed fresh on every run (that's the whole point of
    # this recipe -- see runner.py's _build_expectation) so there's no single
    # real max_value to store here; this is documentation only.
    return [{"name": "maxValue", "value": "<= now(), computed fresh by Great Expectations on every run>"}]


def _compound_unique_sql(check, table_cfg):
    cols = check["kwargs"]["column_list"]
    cols_sql = ", ".join(cols)
    return (
        f"SELECT {cols_sql} FROM {table_cfg['schema']}.{table_cfg['name']} "
        f"GROUP BY {cols_sql} HAVING COUNT(*) > 1"
    )


def _select_unique_within_record_sql(check, table_cfg):
    cols = check["kwargs"]["column_list"]
    conditions = [
        f"{cols[i]} = {cols[j]}"
        for i in range(len(cols))
        for j in range(i + 1, len(cols))
    ]
    where_clause = " OR ".join(conditions)
    return f"SELECT * FROM {table_cfg['schema']}.{table_cfg['name']} WHERE {where_clause}"


def _pair_gt_sql(check, table_cfg):
    kwargs = check["kwargs"]
    column_a, column_b = kwargs["column_A"], kwargs["column_B"]
    or_equal = kwargs.get("or_equal", False)
    # We want the SQL that finds VIOLATING rows (tableCustomSQLQuery's own
    # description: "test if a custom SQL returns 0 row"). The expectation
    # asserts column_A >= column_B (or_equal=True) or column_A > column_B
    # (or_equal=False), so a violation is the strict opposite of that.
    violation_op = "<" if or_equal else "<="
    return (
        f"SELECT * FROM {table_cfg['schema']}.{table_cfg['name']} "
        f"WHERE {column_a} {violation_op} {column_b}"
    )


def _sql_params(build_sql):
    def _params(check, table_cfg):
        return [{"name": "sqlExpression", "value": build_sql(check, table_cfg)}]
    return _params


BUILTIN_DEFINITIONS = {
    "ExpectColumnValuesToNotBeNull": {
        "level": "COLUMN", "definition": "columnValuesToBeNotNull", "params": _no_params,
    },
    "ExpectColumnValuesToBeUnique": {
        "level": "COLUMN", "definition": "columnValuesToBeUnique", "params": _no_params,
    },
    "ExpectColumnValuesToMatchRegex": {
        "level": "COLUMN", "definition": "columnValuesToMatchRegex", "params": _regex_params,
    },
    "ExpectColumnValuesToBeInSet": {
        "level": "COLUMN", "definition": "columnValuesToBeInSet", "params": _in_set_params,
    },
    "ExpectColumnValuesToBeBetween": {
        "level": "COLUMN", "definition": "columnValuesToBeBetween", "params": _between_params,
    },
    "not_in_future": {
        "level": "COLUMN", "definition": "columnValuesToBeBetween", "params": _not_in_future_params,
    },
    "ExpectCompoundColumnsToBeUnique": {
        "level": "TABLE", "definition": "tableCustomSQLQuery",
        "params": _sql_params(_compound_unique_sql),
    },
    "ExpectSelectColumnValuesToBeUniqueWithinRecord": {
        "level": "TABLE", "definition": "tableCustomSQLQuery",
        "params": _sql_params(_select_unique_within_record_sql),
    },
    "ExpectColumnPairValuesAToBeGreaterThanB": {
        "level": "TABLE", "definition": "tableCustomSQLQuery",
        "params": _sql_params(_pair_gt_sql),
    },
}


def _find_existing_fqn(entity_link, rule_name, raise_if_missing=True):
    """Look up the test case OpenMetadata already has for this entity/column
    by listing test cases filtered by entityLink and matching on name, then
    read its real fullyQualifiedName back rather than guessing one
    client-side.

    This is the PRIMARY resolution path now (see ensure_test_case): the bot's
    token can READ test cases but cannot CREATE them, so every already-existing
    case is resolved here without ever attempting a POST. The entityLink filter
    is an exact match (a table-level link returns only table-level tests; a
    column-level link returns only that column's tests -- verified against this
    server), so filtering by the same entityLink the case was created with, then
    matching on name, uniquely identifies it.

    With raise_if_missing=False, returns None when nothing matches (lets the
    caller decide whether a miss is fatal); with the default True it raises."""
    session, host = _client()
    resp = session.get(
        f"{host}/v1/dataQuality/testCases",
        params={"entityLink": entity_link, "limit": 100},
    )
    resp.raise_for_status()
    for item in resp.json().get("data", []):
        if item.get("name") == rule_name:
            return item["fullyQualifiedName"]
    if raise_if_missing:
        raise RuntimeError(
            f"Test case '{rule_name}' not found via GET .../testCases?entityLink="
            f"{entity_link} -- check OpenMetadata's Data Quality tab for this table "
            f"directly."
        )
    return None


def ensure_test_case(check, table_cfg, column):
    """Return the fully-qualified name of the Test Case for this check,
    mapped onto one of OpenMetadata's own built-in Test Definitions (never a
    custom one -- see module docstring for why).

    GET-FIRST BY DESIGN. This bot's token can READ test cases but has no
    permission to CREATE them: POST /v1/dataQuality/testCases returns
    403 "User does not have ANY of the required permissions" -- confirmed live
    against this exact server, on both new and already-existing cases. The
    non-obvious part is that OpenMetadata runs that permission check BEFORE its
    "does this already exist" (409) check, so the older "POST first, treat 409
    as already-exists" design 403'd even for cases that were already present.

    So we resolve the case by READING first and only ever attempt a POST when
    it genuinely does not exist yet (a brand-new table/check on its first run).
    For the current two tables all 28 cases already exist, so no POST is ever
    attempted and the 403 never occurs. If a future new check IS missing and
    the bot still can't create it, we raise a clear, actionable error instead
    of an opaque HTTPError. (If an OpenMetadata admin later grants this bot
    Create permission on TestCase, this same code auto-creates missing cases --
    zero further changes needed.)
    """
    rule_name = check["name"]
    defn = BUILTIN_DEFINITIONS.get(check["expectation"])
    if defn is None:
        raise KeyError(
            f"No BUILTIN_DEFINITIONS mapping for expectation '{check['expectation']}' "
            f"(check '{rule_name}'). This bot's token can only attach test cases to "
            f"OpenMetadata's existing built-in test definitions -- add a mapping in "
            f"BUILTIN_DEFINITIONS above instead of trying to POST a new custom "
            f"testDefinition (that's the 403 this file was rewritten to avoid)."
        )

    entity_link = (
        f"<#E::table::{table_cfg['fqn']}::columns::{column}>"
        if defn["level"] == "COLUMN"
        else f"<#E::table::{table_cfg['fqn']}>"
    )

    # --- Normal path: the case already exists -> resolve by reading, never POST.
    # This is the whole fix for the 403: an existing case is never re-POSTed, so
    # the create-permission check that used to reject every attempt is never hit.
    existing_fqn = _find_existing_fqn(entity_link, rule_name, raise_if_missing=False)
    if existing_fqn:
        return existing_fqn

    # --- Only reached for a genuinely new check/table. Try to create it; the
    # test suite must exist first on older servers, so ensure it here (the bot
    # DOES have permission to upsert test suites -- only test-case create is
    # blocked). This whole branch is skipped entirely when the case exists.
    _ensure_test_suite(table_cfg)
    session, host = _client()
    body = {
        "name": rule_name,
        "entityLink": entity_link,
        "testDefinition": defn["definition"],
        "parameterValues": defn["params"](check, table_cfg),
        "description": (
            f"{check['expectation']} -- computed by Great Expectations and mirrored "
            f"here; OpenMetadata's own engine never executes this test."
        ),
    }
    resp = session.post(f"{host}/v1/dataQuality/testCases", json=body)
    if resp.status_code in (200, 201):
        return resp.json()["fullyQualifiedName"]
    if resp.status_code == 409:
        # Exists after all (created concurrently, or our filter missed it) --
        # now a miss really is fatal, so let the lookup raise.
        return _find_existing_fqn(entity_link, rule_name, raise_if_missing=True)
    if resp.status_code == 403:
        raise RuntimeError(
            f"Can't create test case '{rule_name}' on {table_cfg['fqn']}: it doesn't "
            f"exist yet and this bot's OpenMetadata token ('testsuite-bot') has no "
            f"permission to create test cases. Seed it once -- either via the "
            f"OpenMetadata UI (open the table, Data Quality tab, Add Test, test type "
            f"'{defn['definition']}', name '{rule_name}'), or have someone with create "
            f"access add it -- then re-run; result-pushing works fine once it exists. "
            f"For a fully hands-off flow, ask an OpenMetadata admin to grant this bot "
            f"Create permission on the TestCase resource. "
            f"(Server said: {resp.text.strip()})"
        )
    # Any other 4xx/5xx: surface OpenMetadata's own message before raising, so
    # the real reason is visible, not just the status code.
    print(f"  OpenMetadata rejected the request body for '{rule_name}':")
    print(f"    {resp.text}")
    resp.raise_for_status()


def push_result(fqn, gx_result):
    session, host = _client()
    r = gx_result["result"]
    unexpected = r.get("unexpected_count", 0)
    total = r.get("element_count", 0)
    body = {
        "timestamp": int(time.time() * 1000),
        "testCaseStatus": "Success" if gx_result["success"] else "Failed",
        "result": f"{unexpected}/{total} rows failed. Examples: {r.get('partial_unexpected_list')}",
        "testResultValue": [
            {"name": "failedRows", "value": str(unexpected)},
            {"name": "passedRows", "value": str(total - unexpected)},
        ],
    }
    encoded_fqn = urllib.parse.quote(fqn, safe="")

    resp = session.post(f"{host}/v1/dataQuality/testCases/testCaseResults/{encoded_fqn}", json=body)
    via = "POST testCaseResults (current API, >=1.8.0)"
    if resp.status_code == 404:
        resp = session.put(f"{host}/v1/dataQuality/testCases/{encoded_fqn}/testCaseResult", json=body)
        via = "PUT testCaseResult (legacy API, <1.8.0)"
    resp.raise_for_status()
    status = "PASS" if gx_result["success"] else "FAIL"
    rule_name = fqn.rsplit(".", 1)[-1]
    print(f"  [{status}] {rule_name}  ({unexpected}/{total} failed)  [{via}]")
