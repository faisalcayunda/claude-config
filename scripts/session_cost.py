#!/usr/bin/env python3
"""
session_cost.py -- measure the USD cost of one Claude Code session from its
JSONL transcript(s), using official per-model billing rates.

Usage:
  session_cost.py <session_id> [--as MODEL ...]
  session_cost.py --selftest

Stdlib only. Must run on /usr/bin/python3 (3.9) -- no backslashes inside
f-string expressions anywhere in this file, for that reason.

Rates (USD per 1M tokens), verified against
https://platform.claude.com/docs/en/about-claude/pricing on 2026-09-15.
Columns: in (input), cache5m (5-minute cache write), cache1h (1-hour cache
write), cacheRead (cache read), out (output).
NOTE: keep this table in sync with scripts/hooks/cost-tracker.js -- both
were derived from the same pricing page on the same date, and a plugin
update to that hook does not touch this file (or vice versa).
"""

import argparse
import glob
import json
import os
import shutil
import sys
import tempfile

RATE_TABLE = {
    "fable51":   {"in": 10.00, "cache5m": 12.50, "cache1h": 20.00, "cacheRead": 0.25, "out": 50.0},
    "fable5":    {"in": 10.00, "cache5m": 12.50, "cache1h": 20.00, "cacheRead": 1.00, "out": 50.0},
    "opusNew":   {"in": 5.00,  "cache5m": 6.25,  "cache1h": 10.00, "cacheRead": 0.50, "out": 25.0},
    "opusOld":   {"in": 15.00, "cache5m": 18.75, "cache1h": 30.00, "cacheRead": 1.50, "out": 75.0},
    "sonnet5":   {"in": 2.00,  "cache5m": 2.50,  "cache1h": 4.00,  "cacheRead": 0.20, "out": 10.0},
    "sonnetOld": {"in": 3.00,  "cache5m": 3.75,  "cache1h": 6.00,  "cacheRead": 0.30, "out": 15.0},
    "haiku45":   {"in": 1.00,  "cache5m": 1.25,  "cache1h": 2.00,  "cacheRead": 0.10, "out": 5.0},
}

# --as shortcut name -> RATE_TABLE key.
AS_MODELS = {
    "opus5": "opusNew",
    "fable51": "fable51",
    "sonnet5": "sonnet5",
    "haiku45": "haiku45",
}


def get_rate_key(model):
    """Most-specific-match-first model id -> RATE_TABLE key. Mirrors
    getRates() in scripts/hooks/cost-tracker.js -- keep the two in sync."""
    m = (model or "").lower()
    if "fable-5-1" in m:
        return "fable51"
    if "fable-5" in m:
        return "fable5"
    if "sonnet-5" in m:
        return "sonnet5"
    if "opus-4-1" in m or "opus-4-2" in m or m.endswith("opus-4"):
        return "opusOld"
    if "opus" in m:
        return "opusNew"
    if "sonnet" in m:
        return "sonnetOld"
    if "haiku" in m:
        return "haiku45"
    sys.stderr.write(
        "session_cost: unrecognized model " + repr(model)
        + ", pricing at most expensive known rate (Fable 5)\n"
    )
    return "fable5"


def cost_usd(rate_key, input_tokens, cache5m, cache1h, cache_read, output_tokens):
    r = RATE_TABLE[rate_key]
    return (
        input_tokens / 1e6 * r["in"]
        + cache5m / 1e6 * r["cache5m"]
        + cache1h / 1e6 * r["cache1h"]
        + cache_read / 1e6 * r["cacheRead"]
        + output_tokens / 1e6 * r["out"]
    )


def _num(v):
    return v if isinstance(v, (int, float)) else 0


def load_usage_rows(path):
    """Parse one transcript JSONL file. Returns {requestId: row}.

    A request can appear on several lines as it streams (see the header
    comment in cost-tracker.js). Dedup by requestId, keeping the line with
    the largest output_tokens -- that is the final, fully-populated usage
    snapshot for the request. Models starting with '<' (e.g. <synthetic>)
    are skipped, matching the transcript-format contract.
    """
    best = {}
    try:
        fh = open(path, "r", encoding="utf-8")
    except OSError:
        return best
    with fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            if entry.get("type") != "assistant":
                continue
            msg = entry.get("message") or {}
            usage = msg.get("usage")
            if not usage:
                continue
            model = msg.get("model") or "unknown"
            if model.startswith("<"):
                continue

            request_id = entry.get("requestId") or msg.get("id")
            if not request_id:
                continue

            output_tokens = _num(usage.get("output_tokens"))
            prev = best.get(request_id)
            if prev is not None and prev["output_tokens"] >= output_tokens:
                continue

            cc = usage.get("cache_creation") or {}
            if "ephemeral_5m_input_tokens" in cc or "ephemeral_1h_input_tokens" in cc:
                cache5m = _num(cc.get("ephemeral_5m_input_tokens"))
                cache1h = _num(cc.get("ephemeral_1h_input_tokens"))
            else:
                cache5m = _num(usage.get("cache_creation_input_tokens"))
                cache1h = 0

            best[request_id] = {
                "model": model,
                "input_tokens": _num(usage.get("input_tokens")),
                "output_tokens": output_tokens,
                "cache5m": cache5m,
                "cache1h": cache1h,
                "cache_read": _num(usage.get("cache_read_input_tokens")),
            }
    return best


def aggregate(rows):
    """rows: iterable of row dicts (already deduped). Returns {model: totals}."""
    agg = {}
    for row in rows:
        t = agg.setdefault(row["model"], {
            "requests": 0, "input": 0, "cache5m": 0, "cache1h": 0,
            "cache_read": 0, "output": 0,
        })
        t["requests"] += 1
        t["input"] += row["input_tokens"]
        t["cache5m"] += row["cache5m"]
        t["cache1h"] += row["cache1h"]
        t["cache_read"] += row["cache_read"]
        t["output"] += row["output_tokens"]
    return agg


def find_transcript(session_id):
    """Glob ~/.claude/projects/*/<session_id>.jsonl for the main transcript,
    then look for its subagents folder next to it."""
    home = os.path.expanduser("~")
    pattern = os.path.join(home, ".claude", "projects", "*", session_id + ".jsonl")
    matches = glob.glob(pattern)
    if not matches:
        return None, []
    main_path = matches[0]
    subagents_dir = os.path.join(os.path.dirname(main_path), session_id, "subagents")
    subagent_files = sorted(glob.glob(os.path.join(subagents_dir, "*.jsonl")))
    return main_path, subagent_files


def fmt_money(x):
    return "{:.2f}".format(x)


def _row(cells, widths):
    parts = []
    for i, cell in enumerate(cells):
        w = widths[i] if i < len(widths) else 12
        text = str(cell)
        parts.append(text.ljust(w) if i < 2 else text.rjust(w))
    return " ".join(parts)


def print_report(main_path, subagent_files, main_rows, subagent_rows, as_models):
    print("main transcript: " + main_path)
    print("subagent transcripts: " + str(len(subagent_files)))
    print("")

    headers = ["GROUP", "MODEL", "REQS", "INPUT", "5M_WRITE", "1H_WRITE", "CACHE_READ", "OUTPUT", "COST_USD"]
    for alt in as_models:
        headers.append("AS_" + alt.upper())
    widths = [10, 20, 5, 10, 10, 10, 11, 9, 10] + [12] * len(as_models)
    print(_row(headers, widths))

    session_total = 0.0
    session_total_as = dict((alt, 0.0) for alt in as_models)

    for group_name, rows in (("main", main_rows), ("subagents", subagent_rows)):
        agg = aggregate(rows)
        group_total = 0.0
        group_total_as = dict((alt, 0.0) for alt in as_models)

        for model in sorted(agg):
            t = agg[model]
            rate_key = get_rate_key(model)
            native = cost_usd(rate_key, t["input"], t["cache5m"], t["cache1h"], t["cache_read"], t["output"])
            group_total += native
            cells = [group_name, model, t["requests"], t["input"], t["cache5m"],
                      t["cache1h"], t["cache_read"], t["output"], fmt_money(native)]
            for alt in as_models:
                alt_cost = cost_usd(AS_MODELS[alt], t["input"], t["cache5m"], t["cache1h"], t["cache_read"], t["output"])
                group_total_as[alt] += alt_cost
                cells.append(fmt_money(alt_cost))
            print(_row(cells, widths))

        total_cells = [group_name, "TOTAL", "", "", "", "", "", "", fmt_money(group_total)]
        for alt in as_models:
            total_cells.append(fmt_money(group_total_as[alt]))
        print(_row(total_cells, widths))
        print("")

        session_total += group_total
        for alt in as_models:
            session_total_as[alt] += group_total_as[alt]

    total_cells = ["SESSION", "TOTAL", "", "", "", "", "", "", fmt_money(session_total)]
    for alt in as_models:
        total_cells.append(fmt_money(session_total_as[alt]))
    print(_row(total_cells, widths))


def selftest():
    tmpdir = tempfile.mkdtemp(prefix="session_cost_selftest_")
    try:
        path = os.path.join(tmpdir, "fake.jsonl")

        def assistant_line(request_id, model, usage):
            entry = {"type": "assistant", "requestId": request_id, "message": {"model": model, "usage": usage}}
            return json.dumps(entry)

        lines = []

        # req_A streams twice; output_tokens grows. Dedup must keep the
        # larger (final) line, not sum both.
        lines.append(assistant_line("req_A", "claude-opus-5", {
            "input_tokens": 10, "output_tokens": 50,
            "cache_read_input_tokens": 1000, "cache_creation_input_tokens": 0,
        }))
        lines.append(assistant_line("req_A", "claude-opus-5", {
            "input_tokens": 10, "output_tokens": 120,
            "cache_read_input_tokens": 1000, "cache_creation_input_tokens": 0,
        }))

        # req_B carries an explicit 5m/1h split.
        lines.append(assistant_line("req_B", "claude-sonnet-5", {
            "input_tokens": 5, "output_tokens": 5, "cache_read_input_tokens": 0,
            "cache_creation_input_tokens": 1000,
            "cache_creation": {"ephemeral_5m_input_tokens": 300, "ephemeral_1h_input_tokens": 700},
        }))

        # req_C has no split -- must fall back to counting it as a 5m write.
        lines.append(assistant_line("req_C", "claude-sonnet-5", {
            "input_tokens": 1, "output_tokens": 1, "cache_read_input_tokens": 0,
            "cache_creation_input_tokens": 500,
        }))

        # Synthetic-model lines must be skipped entirely.
        lines.append(assistant_line("req_D", "<synthetic>", {
            "input_tokens": 999999, "output_tokens": 999999,
        }))

        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

        rows = load_usage_rows(path)

        assert "req_D" not in rows, "synthetic model line was not skipped"

        assert rows["req_A"]["output_tokens"] == 120, "dedup did not keep the max-output line"
        assert rows["req_A"]["input_tokens"] == 10, "dedup picked the wrong line's fields"

        assert rows["req_B"]["cache5m"] == 300, "5m/1h split not respected (5m)"
        assert rows["req_B"]["cache1h"] == 700, "5m/1h split not respected (1h)"

        assert rows["req_C"]["cache5m"] == 500, "missing split did not fall back to a full 5m write"
        assert rows["req_C"]["cache1h"] == 0, "missing split leaked into the 1h bucket"

        # Fable 5.1 cache read is $0.25/MTok (0.025x input), not the
        # general Fable $1/MTok cache-read rate.
        fable_cost = cost_usd("fable51", 0, 0, 0, 1000000, 0)
        assert abs(fable_cost - 0.25) < 1e-9, "Fable 5.1 cache read rate is wrong: got " + repr(fable_cost)

        # Sanity on the match order itself.
        assert get_rate_key("claude-sonnet-5") == "sonnet5"
        assert get_rate_key("claude-sonnet-4-6") == "sonnetOld"
        assert get_rate_key("claude-opus-5") == "opusNew"
        assert get_rate_key("claude-opus-4-8") == "opusNew"
        assert get_rate_key("claude-opus-4-1") == "opusOld"
        assert get_rate_key("claude-opus-4") == "opusOld"
        assert get_rate_key("claude-fable-5-1") == "fable51"
        assert get_rate_key("claude-fable-5") == "fable5"
        assert get_rate_key("claude-haiku-4-5-20251001") == "haiku45"

        print("selftest: OK")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def build_parser():
    p = argparse.ArgumentParser(description="Measure the USD cost of one Claude Code session from its transcript(s).")
    p.add_argument("session_id", nargs="?", help="Session id (matches ~/.claude/projects/*/<session_id>.jsonl)")
    p.add_argument("--as", dest="as_models", action="append", default=[], choices=sorted(AS_MODELS),
                    metavar="MODEL", help="Also re-price the same tokens as this model (repeatable): " + ", ".join(sorted(AS_MODELS)))
    p.add_argument("--selftest", action="store_true", help="Run the built-in self-check and exit")
    return p


def main():
    args = build_parser().parse_args()

    if args.selftest:
        selftest()
        return 0

    if not args.session_id:
        build_parser().error("session_id is required unless --selftest is given")

    main_path, subagent_files = find_transcript(args.session_id)
    if not main_path:
        sys.stderr.write("session_cost: no transcript found for session " + args.session_id + "\n")
        return 1

    as_models = list(dict.fromkeys(args.as_models))  # dedup, keep order

    main_rows = list(load_usage_rows(main_path).values())
    subagent_rows = []
    for fp in subagent_files:
        subagent_rows.extend(load_usage_rows(fp).values())

    print_report(main_path, subagent_files, main_rows, subagent_rows, as_models)
    return 0


if __name__ == "__main__":
    sys.exit(main())
