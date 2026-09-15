#!/usr/bin/env node
/**
 * Cost Tracker Hook (v2)
 *
 * Reads transcript_path from Stop hook stdin, sums usage across all
 * assistant turns in the session JSONL (main transcript + any subagent
 * transcripts under <session_id>/subagents/*.jsonl next to it), and
 * appends one row to ~/.claude/metrics/costs.jsonl.
 *
 * Stop hook stdin payload: { session_id, transcript_path, cwd, hook_event_name, ... }
 * The Stop payload does NOT include `usage` or `model` directly. The previous
 * version of this hook expected those fields and silently produced zero-filled
 * rows (verified: 2,340 rows captured with 0.0% non-zero token rate over 52
 * days). The fix is to read the transcript file Claude Code already passes us.
 *
 * JSONL assistant entry shape (per Claude Code):
 *   { type: "assistant", requestId, message: { model, usage: { input_tokens,
 *     output_tokens, cache_creation_input_tokens, cache_read_input_tokens,
 *     cache_creation: { ephemeral_5m_input_tokens, ephemeral_1h_input_tokens } } } }
 * A request can appear on several lines as it streams — dedup by requestId,
 * keeping the line with the largest output_tokens (the final snapshot).
 * Each line is priced at its own message.model: a subagent running a
 * different model than the main session must not be priced at the main
 * model's rate.
 *
 * Cumulative behavior: Stop fires per assistant response, not per session.
 * Each row therefore represents the cumulative session total up to that point.
 * To get per-session cost, take the last row per session_id. To get per-day
 * spend, aggregate.
 *
 * Harness-cost contract (optional, opt-in by the statusline):
 *   If the user's statusline (which receives `cost.total_cost_usd` directly
 *   from Claude Code) writes `{ts, cost_usd}` to
 *   `<os.tmpdir()>/harness-cost-<session_id>.json` on each render, this hook
 *   prefers that authoritative value over the transcript-sum estimate when
 *   the cache is fresh (≤ 300s). The transcript-sum is kept as a safe
 *   fallback because:
 *     - the hard-coded rate table cannot represent Opus 4.7's >200K-token
 *       2x tier or the 1h-cache 2x tier (under-counts on long sessions);
 *     - summing the full transcript double-counts work done across
 *       `--resume` boundaries while `cost.total_cost_usd` is per-process.
 *   Absent a writer, behavior is unchanged.
 */

'use strict';

const fs = require('fs');
const os = require('os');
const path = require('path');
const { randomUUID } = require('crypto');
const { ensureDir, appendFile, getClaudeDir } = require('../lib/utils');
const { sanitizeSessionId } = require('../lib/session-bridge');

const HARNESS_COST_MAX_AGE_SECONDS = 300;

/**
 * Read authoritative harness cost from the per-session cache file.
 * @param {string} sessionId
 * @param {number} maxAgeSeconds
 * @returns {number|null} cost in USD, or null on miss / stale / parse error
 */
function readHarnessCost(sessionId, maxAgeSeconds) {
  if (!sessionId) return null;
  try {
    const fp = path.join(os.tmpdir(), `harness-cost-${sessionId}.json`);
    if (!fs.existsSync(fp)) return null;
    const obj = JSON.parse(fs.readFileSync(fp, 'utf8'));
    const ts = Number(obj && obj.ts);
    const cost = Number(obj && obj.cost_usd);
    if (!Number.isFinite(ts) || !Number.isFinite(cost) || cost < 0) return null;
    const age = Math.floor(Date.now() / 1000) - ts;
    if (age < 0 || age > maxAgeSeconds) return null;
    return cost;
  } catch {
    return null;
  }
}

// Per-1M-token billing rates (USD), verified against
// https://platform.claude.com/docs/en/about-claude/pricing on 2026-09-15.
// Columns: in (input), cache5m (5-minute cache write), cache1h (1-hour
// cache write), cacheRead (cache read), out (output).
// NOTE: this hook ships as part of the ECC plugin — a plugin update can
// silently overwrite this table. Re-verify the rates above after any
// plugin update touching scripts/hooks/cost-tracker.js.
const RATE_TABLE = {
  fable51:   { in: 10.00, cache5m: 12.50, cache1h: 20.00, cacheRead: 0.25, out: 50.0 },
  fable5:    { in: 10.00, cache5m: 12.50, cache1h: 20.00, cacheRead: 1.00, out: 50.0 },
  opusNew:   { in: 5.00,  cache5m: 6.25,  cache1h: 10.00, cacheRead: 0.50, out: 25.0 },
  opusOld:   { in: 15.00, cache5m: 18.75, cache1h: 30.00, cacheRead: 1.50, out: 75.0 },
  sonnet5:   { in: 2.00,  cache5m: 2.50,  cache1h: 4.00,  cacheRead: 0.20, out: 10.0 },
  sonnetOld: { in: 3.00,  cache5m: 3.75,  cache1h: 6.00,  cacheRead: 0.30, out: 15.0 },
  haiku45:   { in: 1.00,  cache5m: 1.25,  cache1h: 2.00,  cacheRead: 0.10, out: 5.0 }
};

// Unrecognized models are logged once each (per process), not once per
// usage line — a chatty subagent on an unknown model would otherwise
// flood stderr with an identical warning per turn.
const warnedUnknownModels = new Set();

/**
 * Most-specific-match-first model -> rate lookup.
 * An id that matches nothing recognized is priced at the most expensive
 * known rate (Fable 5) and logged to stderr, instead of silently falling
 * back to Sonnet rates (the old behavior under-priced unknown/new models,
 * e.g. Opus by ~3x and Fable 5.1 by ~3x).
 */
function getRates(model) {
  const m = String(model || '').toLowerCase();
  if (m.includes('fable-5-1'))   return RATE_TABLE.fable51;
  if (m.includes('fable-5'))     return RATE_TABLE.fable5;
  if (m.includes('sonnet-5'))    return RATE_TABLE.sonnet5;
  if (m.includes('opus-4-1') || /opus-4$/.test(m)) {
    return RATE_TABLE.opusOld;
  }
  if (m.includes('opus'))        return RATE_TABLE.opusNew;
  if (m.includes('sonnet'))      return RATE_TABLE.sonnetOld;
  if (m.includes('haiku'))       return RATE_TABLE.haiku45;

  if (!warnedUnknownModels.has(model)) {
    warnedUnknownModels.add(model);
    process.stderr.write(`[Hook] cost-tracker: unrecognized model "${model}", pricing at most expensive known rate (Fable 5)\n`);
  }
  return RATE_TABLE.fable5;
}

function toNumber(v) {
  const n = Number(v);
  return Number.isFinite(n) ? n : 0;
}

/**
 * Parse the usage-bearing assistant lines out of one transcript's JSONL
 * content. Dedups by requestId, keeping the line with the largest
 * output_tokens (a request can stream across several lines before the
 * final usage snapshot lands). A line with no requestId can't be matched
 * to a sibling, so it gets its own synthetic key and is kept as-is.
 * Models starting with '<' (e.g. <synthetic>) are skipped.
 *
 * Returns { rows, lastModel }, where each row is
 * { model, inputTokens, outputTokens, cacheWrite5m, cacheWrite1h, cacheReadTokens }.
 */
function parseUsageContent(content) {
  const byRequestId = new Map();
  let lastModel = null;

  for (const line of content.split('\n')) {
    if (!line.trim()) continue;
    let entry;
    try { entry = JSON.parse(line); } catch { continue; }

    if (entry.type !== 'assistant') continue;
    const msg = entry.message;
    if (!msg || !msg.usage) continue;

    const model = msg.model || 'unknown';
    if (model.startsWith('<')) continue; // e.g. <synthetic> — not real billed usage

    const u = msg.usage;
    const outputTokens = toNumber(u.output_tokens);

    // Split cache writes into 5m/1h buckets when the breakdown is present;
    // otherwise count the whole cache_creation_input_tokens as a 5m write.
    const cc = u.cache_creation;
    const hasSplit = cc && (cc.ephemeral_5m_input_tokens != null || cc.ephemeral_1h_input_tokens != null);

    const row = {
      model,
      inputTokens: toNumber(u.input_tokens),
      outputTokens,
      cacheWrite5m: hasSplit ? toNumber(cc.ephemeral_5m_input_tokens) : toNumber(u.cache_creation_input_tokens),
      cacheWrite1h: hasSplit ? toNumber(cc.ephemeral_1h_input_tokens) : 0,
      cacheReadTokens: toNumber(u.cache_read_input_tokens)
    };

    const requestId = entry.requestId || randomUUID();
    const prev = byRequestId.get(requestId);
    if (!prev || outputTokens > prev.outputTokens) {
      byRequestId.set(requestId, row);
    }

    if (model !== 'unknown') lastModel = model;
  }

  return { rows: Array.from(byRequestId.values()), lastModel };
}

/** Cost of one usage row, priced at that row's own model rate. */
function costForRow(row) {
  const rates = getRates(row.model);
  return (
    (row.inputTokens     / 1e6) * rates.in +
    (row.outputTokens    / 1e6) * rates.out +
    (row.cacheWrite5m    / 1e6) * rates.cache5m +
    (row.cacheWrite1h    / 1e6) * rates.cache1h +
    (row.cacheReadTokens / 1e6) * rates.cacheRead
  );
}

/**
 * List a main transcript's subagent transcript files:
 * <dir>/<session_id>/subagents/*.jsonl next to <dir>/<session_id>.jsonl.
 * Returns [] when there is no subagents folder (older sessions, or a
 * session that never spawned a subagent) — that is not an error.
 */
function listSubagentFiles(transcriptPath) {
  const dir = path.dirname(transcriptPath);
  const sessionId = path.basename(transcriptPath, '.jsonl');
  const subagentsDir = path.join(dir, sessionId, 'subagents');
  try {
    return fs.readdirSync(subagentsDir)
      .filter(f => f.endsWith('.jsonl'))
      .map(f => path.join(subagentsDir, f));
  } catch {
    return [];
  }
}

/**
 * Scan the session JSONL — main transcript plus any subagent transcripts —
 * and sum token usage and cost across all assistant turns. Each row is
 * priced at its own message.model (a subagent on a different model than
 * the main session is priced at that model's rate, not the main model's).
 * `model` in the result is the main transcript's own last-seen model —
 * what the emitted row's `model` field records — not a per-line value.
 * Returns { inputTokens, outputTokens, cacheWriteTokens, cacheReadTokens,
 * costUsd, model } or null on read failure of the main transcript.
 */
function sumUsageFromTranscript(transcriptPath) {
  let mainContent;
  try {
    mainContent = fs.readFileSync(transcriptPath, 'utf8');
  } catch {
    return null;
  }

  const main = parseUsageContent(mainContent);

  let subagentRows = [];
  for (const file of listSubagentFiles(transcriptPath)) {
    let content;
    try {
      content = fs.readFileSync(file, 'utf8');
    } catch {
      continue; // one unreadable subagent file shouldn't sink the whole estimate
    }
    subagentRows = subagentRows.concat(parseUsageContent(content).rows);
  }

  const allRows = main.rows.concat(subagentRows);

  let inputTokens = 0;
  let outputTokens = 0;
  let cacheWriteTokens = 0;
  let cacheReadTokens = 0;
  let costUsd = 0;

  for (const row of allRows) {
    inputTokens      += row.inputTokens;
    outputTokens     += row.outputTokens;
    cacheWriteTokens += row.cacheWrite5m + row.cacheWrite1h;
    cacheReadTokens  += row.cacheReadTokens;
    costUsd          += costForRow(row);
  }

  return { inputTokens, outputTokens, cacheWriteTokens, cacheReadTokens, costUsd, model: main.lastModel || 'unknown' };
}

// 1MB, matching the other Stop hooks. The Stop payload carries
// last_assistant_message, which routinely exceeded the old 64KB cap and
// made this hook echo a JSON document cut mid-stream (#2090).
const MAX_STDIN = 1024 * 1024;
let raw = '';
let truncated = false;

process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => {
  if (raw.length < MAX_STDIN) {
    const remaining = MAX_STDIN - raw.length;
    raw += chunk.substring(0, remaining);
    if (chunk.length > remaining) truncated = true;
  } else {
    truncated = true;
  }
});

process.stdin.on('end', () => {
  try {
    const input = raw.trim() ? JSON.parse(raw) : {};

    const transcriptPath = (typeof input.transcript_path === 'string' && input.transcript_path)
      ? input.transcript_path
      : process.env.CLAUDE_TRANSCRIPT_PATH || null;

    const sessionId =
      sanitizeSessionId(input.session_id) ||
      sanitizeSessionId(process.env.ECC_SESSION_ID) ||
      sanitizeSessionId(process.env.CLAUDE_SESSION_ID) ||
      'default';

    let usageTotals = null;
    if (transcriptPath && fs.existsSync(transcriptPath)) {
      usageTotals = sumUsageFromTranscript(transcriptPath);
    }

    const {
      inputTokens = 0,
      outputTokens = 0,
      cacheWriteTokens = 0,
      cacheReadTokens = 0,
      costUsd = 0,
      model = 'unknown'
    } = usageTotals || {};

    // Each row (main transcript + any subagent transcripts) was already
    // priced at its own message.model inside sumUsageFromTranscript — do
    // not re-price the aggregate totals against a single model's rate,
    // that would mis-price subagent turns run on a different model than
    // the main session.
    const transcriptCostUsd = Math.round(costUsd * 1e6) / 1e6;

    // Prefer the harness's authoritative `cost.total_cost_usd` when the
    // statusline has written it to the per-session cache (see contract in
    // the file header). The harness number reflects API-billed truth
    // (correct rates, 1h-cache 2x, >200K tier 2x) and is per-process so it
    // does not drift across `--resume`. Cache miss → transcript-sum.
    const harnessCost = readHarnessCost(sessionId, HARNESS_COST_MAX_AGE_SECONDS);
    const estimatedCostUsd = harnessCost !== null
      ? Math.round(harnessCost * 1e6) / 1e6
      : transcriptCostUsd;

    const metricsDir = path.join(getClaudeDir(), 'metrics');
    ensureDir(metricsDir);

    const row = {
      timestamp:          new Date().toISOString(),
      session_id:         sessionId,
      transcript_path:    transcriptPath || '',
      model,
      input_tokens:       inputTokens,
      output_tokens:      outputTokens,
      cache_write_tokens: cacheWriteTokens,
      cache_read_tokens:  cacheReadTokens,
      estimated_cost_usd: estimatedCostUsd
    };

    appendFile(path.join(metricsDir, 'costs.jsonl'), `${JSON.stringify(row)}\n`);
  } catch {
    // Non-blocking — never fail the Stop hook.
  }

  // Pass stdin through (ECC hook convention) — but never echo truncated
  // stdin: invalid JSON on stdout is reported as a Stop hook failure (#2090).
  if (truncated) {
    process.stderr.write('[Hook] cost-tracker: stdin exceeded 1MB; suppressing pass-through (fail-open)\n');
    return;
  }
  process.stdout.write(raw);
});
