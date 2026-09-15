---
name: airflow-log-parse
description: Deterministic Airflow task log parser — extracts {error_class, task_id, run_id, traceback, operator_type} as structured data. Group B skill: surface as recommendation when user pastes Airflow logs. No routing, no diagnosis, no fixes.
argument-hint: "[--log <text-or-path>]"
---

EXECUTE IMMEDIATELY — do not deliberate.

## Hard Constraints

- PURE PARSER — no diagnosis, no fix suggestions, no routing decisions.
- If a field cannot be extracted with confidence, set it to null. Never fabricate values.
- Do NOT call any other tools or agents from within this skill.
- Routing to debugger or error-detective is the orchestrator's job (CLAUDE.md §16.5). This skill only provides structured input for that decision.

## Argument Parsing

Extract from $ARGUMENTS:
- `--log` — path to log file OR inline log text.

If `--log` is absent AND no Airflow log text is visible in the conversation: ask exactly once:

> "Paste Airflow task log or provide --log <path>."

Do not proceed until log is available.

## Parse Workflow

Execute steps in order. Do not skip steps.

### Step 1: Read stack context

Read the Stack line in `/Users/isal/.claude/CLAUDE.md`: the active stack is Airflow 3.1.7. Use this as context for `airflow_version_hint` in the output.

### Step 2: Accept log input

- If `--log` is a file path: read the file.
- If `--log` is inline text: use the text directly.
- If neither: log text must already be visible in conversation — use it.

### Step 3: Extract fields

Use pattern matching only. Do NOT infer or guess. If a field cannot be found, set it to `null`.

| Field | Pattern |
|---|---|
| `dag_id` | Line matching `dag_id: <value>` or `running Task(dag_id='<value>'` |
| `task_id` | Line matching `task_id: <value>` or `task_id='<value>'` |
| `run_id` | Line matching `run_id: <value>` or `dag_run_id: <value>` |
| `map_index` | Line matching `map_index: <value>` (dynamically mapped tasks; `null` if absent) |
| `operator` | Line matching `operator: <ClassName>` or `class <ClassName>` in traceback |
| `exception_type` | Exception class name from the first line of the exception block (e.g., `airflow.exceptions.AirflowException`, `ModuleNotFoundError`, `KeyError`) |
| `exception_message` | Message on the same line as `exception_type`, or the immediately following line |
| `traceback_tail` | Last 10 lines of the traceback block (lines before "The above exception" or before log stream ends) |

### Step 4: Classify error_class

Assign EXACTLY ONE bucket using `exception_type` and `exception_message`. Match in order — use the first match:

| Bucket | Match condition |
|---|---|
| `IMPORT_ERROR` | `exception_type` contains `ModuleNotFoundError` or `ImportError` |
| `XCOM_ERROR` | `exception_type` or message contains `xcom`, `XCom`, `serialization`, or `json serializable` |
| `CONNECTION_ERROR` | `exception_type` contains `ConnectionError`, `OperationalError`; or message contains `could not connect`, `Connection refused`, `hook`, `provider` |
| `PERMISSION_ERROR` | `exception_type` contains `PermissionError` or `FileNotFoundError` |
| `TIMEOUT_ERROR` | `exception_type` contains `AirflowTaskTimeout`, `AirflowSensorTimeout`, or `TaskDeferred`; or message contains `timed out` |
| `LOGIC_ERROR` | `exception_type` contains `KeyError`, `TypeError`, `ValueError`, `AttributeError`, or `IndexError` |
| `SCHEDULER_ERROR` | `exception_type` contains `DagProcessingException` or `DagFilesSyntaxError`; or message contains `parse error` or `DAG file` |
| `ASSET_ERROR` | `exception_type` or message contains `Asset`, `Dataset`, `URI`, or `asset uri` |
| `UNKNOWN` | None of the above match |

### Step 5: Output

Output ONLY the JSON block below. No prose before it. No prose after it. No diagnosis. No suggestions.

```json
{
  "dag_id": "<value or null>",
  "task_id": "<value or null>",
  "run_id": "<value or null>",
  "map_index": "<value or null>",
  "operator": "<class name or null>",
  "error_class": "<BUCKET>",
  "exception_type": "<FullyQualifiedExceptionClass or null>",
  "exception_message": "<first line of exception message or null>",
  "traceback_tail": [
    "<line 1>",
    "...",
    "<line 10>"
  ],
  "airflow_version_hint": "3.1.7"
}
```

Stream all output live — never run in background.
