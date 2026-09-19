#!/usr/bin/env python3
"""
render_query_map.py — turn an actually-explain-query spec (JSON) into a
single self-contained HTML page: an interactive SQL logic map with a
plain-language node for every step, a data funnel, and a details panel.

Usage:
    python3 render_query_map.py spec.json -o query_map.html
    python3 render_query_map.py spec.json -o out.html --validate-only

The spec contract lives in ../references/spec-schema.md. This script owns
layout + rendering so that every explanation comes out looking the same;
you own the analysis that fills the spec.
"""

import argparse
import json
import os
import re
import sys
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ICONS = json.load(open(os.path.join(HERE, "..", "assets", "icons.json")))

NODE_W = 240.0
DUMMY_W = 90.0
NODE_SEP = 44.0
RANK_SEP = 120.0

# ── Flexoki palette: one colour per node kind (matches actuallyEXPLAIN) ──
COLORS = {
    "table": "#879A39", "catalog": "#879A39", "subquery": "#879A39",
    "insert_target": "#879A39", "create": "#879A39",
    "join": "#3AA99F", "cte": "#3AA99F", "unnest": "#3AA99F", "semijoin": "#3AA99F",
    "where": "#D0A215", "having": "#D0A215", "qualify": "#D0A215",
    "set": "#D0A215", "alter": "#D0A215",
    "select": "#4385BE", "window": "#4385BE", "operation": "#4385BE", "result": "#4385BE",
    "orderby": "#8B7EC8", "values": "#8B7EC8", "union": "#8B7EC8",
    "intersect": "#8B7EC8", "except": "#8B7EC8", "action": "#8B7EC8",
    "groupby": "#CE5D97", "aggregate": "#CE5D97", "returning": "#CE5D97",
    "update": "#DA702C", "insert": "#DA702C", "merge": "#DA702C",
    "delete": "#D14D41", "drop": "#D14D41",
    "limit": "#9F9D96", "distinct": "#9F9D96", "column": "#9F9D96",
}
DEFAULT_COLOR = "#4385BE"

ICON_FOR_KIND = {
    "table": "database", "catalog": "boxes", "subquery": "list-tree",
    "insert_target": "database", "create": "square-plus", "column": "columns-3",
    "join": "link", "semijoin": "search-check", "unnest": "unfold-vertical",
    "where": "filter", "having": "filter", "qualify": "filter",
    "select": "square-dashed-mouse-pointer", "window": "frame",
    "groupby": "group", "aggregate": "sigma", "distinct": "copy-minus",
    "orderby": "arrow-up-down", "limit": "scissors",
    "cte": "repeat-2", "union": "squares-unite", "intersect": "squares-intersect",
    "except": "squares-exclude", "values": "braces",
    "insert": "between-horizontal-start", "update": "square-pen",
    "delete": "trash-2", "merge": "replace", "set": "replace",
    "returning": "arrow-left-from-line", "result": "crosshair",
    "operation": "cog", "action": "cog", "alter": "cog", "drop": "trash-2",
}

DOCS = {
    "postgres": ("PostgreSQL Docs", {
        "table": "https://www.postgresql.org/docs/current/sql-select.html#SQL-FROM",
        "join": "https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-JOIN",
        "where": "https://www.postgresql.org/docs/current/sql-select.html#SQL-WHERE",
        "having": "https://www.postgresql.org/docs/current/sql-select.html#SQL-HAVING",
        "select": "https://www.postgresql.org/docs/current/sql-select.html#SQL-SELECT-LIST",
        "groupby": "https://www.postgresql.org/docs/current/sql-select.html#SQL-GROUPBY",
        "orderby": "https://www.postgresql.org/docs/current/sql-select.html#SQL-ORDERBY",
        "limit": "https://www.postgresql.org/docs/current/sql-select.html#SQL-LIMIT",
        "cte": "https://www.postgresql.org/docs/current/queries-with.html",
        "union": "https://www.postgresql.org/docs/current/queries-union.html",
        "window": "https://www.postgresql.org/docs/current/tutorial-window.html",
        "unnest": "https://www.postgresql.org/docs/current/functions-array.html",
        "distinct": "https://www.postgresql.org/docs/current/sql-select.html#SQL-DISTINCT",
        "insert": "https://www.postgresql.org/docs/current/sql-insert.html",
        "update": "https://www.postgresql.org/docs/current/sql-update.html",
        "delete": "https://www.postgresql.org/docs/current/sql-delete.html",
        "merge": "https://www.postgresql.org/docs/current/sql-merge.html",
        "values": "https://www.postgresql.org/docs/current/sql-values.html",
        "returning": "https://www.postgresql.org/docs/current/dml-returning.html",
        "create": "https://www.postgresql.org/docs/current/sql-createtable.html",
        "_": "https://www.postgresql.org/docs/current/sql-commands.html",
    }),
    "mysql": ("MySQL Docs", {
        "table": "https://dev.mysql.com/doc/refman/8.4/en/select.html",
        "join": "https://dev.mysql.com/doc/refman/8.4/en/join.html",
        "where": "https://dev.mysql.com/doc/refman/8.4/en/where-optimization.html",
        "having": "https://dev.mysql.com/doc/refman/8.4/en/group-by-handling.html",
        "select": "https://dev.mysql.com/doc/refman/8.4/en/select.html",
        "groupby": "https://dev.mysql.com/doc/refman/8.4/en/group-by-modifiers.html",
        "orderby": "https://dev.mysql.com/doc/refman/8.4/en/order-by-optimization.html",
        "limit": "https://dev.mysql.com/doc/refman/8.4/en/limit-optimization.html",
        "cte": "https://dev.mysql.com/doc/refman/8.4/en/with.html",
        "union": "https://dev.mysql.com/doc/refman/8.4/en/union.html",
        "window": "https://dev.mysql.com/doc/refman/8.4/en/window-functions.html",
        "unnest": "https://dev.mysql.com/doc/refman/8.4/en/json-table-functions.html",
        "distinct": "https://dev.mysql.com/doc/refman/8.4/en/distinct-optimization.html",
        "insert": "https://dev.mysql.com/doc/refman/8.4/en/insert.html",
        "update": "https://dev.mysql.com/doc/refman/8.4/en/update.html",
        "delete": "https://dev.mysql.com/doc/refman/8.4/en/delete.html",
        "merge": "https://dev.mysql.com/doc/refman/8.4/en/insert-on-duplicate.html",
        "values": "https://dev.mysql.com/doc/refman/8.4/en/values.html",
        "create": "https://dev.mysql.com/doc/refman/8.4/en/create-table.html",
        "_": "https://dev.mysql.com/doc/refman/8.4/en/sql-statements.html",
    }),
    "trino": ("Trino Docs", {
        "table": "https://trino.io/docs/current/sql/select.html#from-clause",
        "catalog": "https://trino.io/docs/current/overview/concepts.html#catalog",
        "join": "https://trino.io/docs/current/sql/select.html#join-clause",
        "where": "https://trino.io/docs/current/sql/select.html#where-clause",
        "having": "https://trino.io/docs/current/sql/select.html#having-clause",
        "select": "https://trino.io/docs/current/sql/select.html#select-clause",
        "groupby": "https://trino.io/docs/current/sql/select.html#group-by-clause",
        "orderby": "https://trino.io/docs/current/sql/select.html#order-by-clause",
        "limit": "https://trino.io/docs/current/sql/select.html#limit-clause",
        "qualify": "https://trino.io/docs/current/sql/select.html#qualify-clause",
        "cte": "https://trino.io/docs/current/sql/select.html#with-clause",
        "union": "https://trino.io/docs/current/sql/select.html#union-intersect-and-except-clause",
        "intersect": "https://trino.io/docs/current/sql/select.html#union-intersect-and-except-clause",
        "except": "https://trino.io/docs/current/sql/select.html#union-intersect-and-except-clause",
        "window": "https://trino.io/docs/current/functions/window.html",
        "unnest": "https://trino.io/docs/current/sql/select.html#unnest",
        "distinct": "https://trino.io/docs/current/sql/select.html#select-clause",
        "insert": "https://trino.io/docs/current/sql/insert.html",
        "update": "https://trino.io/docs/current/sql/update.html",
        "delete": "https://trino.io/docs/current/sql/delete.html",
        "merge": "https://trino.io/docs/current/sql/merge.html",
        "values": "https://trino.io/docs/current/sql/values.html",
        "create": "https://trino.io/docs/current/sql/create-table.html",
        "_": "https://trino.io/docs/current/sql.html",
    }),
}
DOCS["generic"] = DOCS["postgres"]
DOCS["postgresql"] = DOCS["postgres"]

ID_NAMES = {"id", "in", "ind", "idn", "indonesia", "indonesian", "bahasa",
            "bahasa indonesia", "id-id", "id_id"}


def resolve_lang(value):
    """Accept the spellings people actually write for Indonesian."""
    v = str(value or "en").strip().lower()
    return "id" if (v in ID_NAMES or v.startswith("id")) else "en"


DIALECT_LABEL = {
    "postgres": "PostgreSQL", "postgresql": "PostgreSQL", "mysql": "MySQL",
    "trino": "Trino", "generic": "SQL",
}

# ── Encyclopedia: what each kind of step means, independent of this query ──
ENCY_EN = {
    "table":   ("FROM (Table Source)", "The FROM clause names the source table a query reads. It is the starting point of the pipeline — every later step operates on rows that come out of here."),
    "catalog": ("Cross-catalog Source", "A table read from a different catalog (a separate underlying system). The engine federates the read, so rows travel across systems before they can be joined."),
    "subquery":("Inline Subquery", "A full query nested inside FROM that behaves like a temporary table. It is materialised or inlined by the planner, then used as an ordinary source."),
    "join":    ("JOIN", "A JOIN combines rows from two sources on a matching condition. The join type (INNER, LEFT, RIGHT, FULL, CROSS) decides what happens to rows that find no match — and whether row count can grow."),
    "semijoin":("Semi / Anti Join (EXISTS · IN)", "An EXISTS, IN or NOT IN subquery used as a filter. Unlike a normal join it never duplicates rows: it only asks whether a match exists, so it can shrink the input but never grow it."),
    "unnest":  ("UNNEST · LATERAL (Row Expansion)", "Expands an array, map or correlated subquery into rows. This is one of the few steps that multiplies row count: one input row becomes as many rows as the collection holds."),
    "where":   ("WHERE (Row Filter)", "WHERE drops individual rows before any grouping happens. Only rows for which the condition is true survive — NULL comparisons count as not-true and are dropped too."),
    "having":  ("HAVING (Group Filter)", "HAVING filters whole groups after GROUP BY has run. It is the place for conditions on aggregates, which WHERE cannot see."),
    "qualify": ("QUALIFY (Window Filter)", "QUALIFY filters rows using the result of a window function, after the window has been computed. It is the window-function counterpart of HAVING."),
    "select":  ("SELECT (Projection)", "The SELECT list decides which columns and expressions leave this step. It changes the shape of each row — the number of columns — but on its own never changes how many rows there are."),
    "window":  ("Window Function (OVER)", "A window function computes a value across a frame of related rows (PARTITION BY … ORDER BY …) while keeping every input row. Row count is unchanged; each row simply gains a ranking, running total or lag/lead value."),
    "groupby": ("GROUP BY (Aggregation)", "GROUP BY collapses rows that share the same key values into one row per group. Aggregates (COUNT, SUM, AVG) then summarise each group — this is usually the biggest single reduction in a pipeline."),
    "aggregate":("Global Aggregate", "An aggregate with no GROUP BY collapses the entire input into exactly one row."),
    "distinct":("DISTINCT (De-duplication)", "DISTINCT removes duplicate rows from the result. It can only shrink the row count, and it forces the engine to sort or hash the whole set."),
    "orderby": ("ORDER BY (Sort)", "ORDER BY sorts the result. It never adds or removes rows; without it the engine gives no ordering guarantee at all."),
    "limit":   ("LIMIT / FETCH (Row Cap)", "LIMIT caps how many rows are returned. With OFFSET it paginates; with ORDER BY it answers top-N questions."),
    "cte":     ("WITH / CTE", "A Common Table Expression is a named, temporary result set that lives only for this query. It makes long queries readable and lets one result be referenced several times."),
    "union":   ("UNION / UNION ALL", "UNION stacks two result sets on top of each other — the only common operation that adds rows. UNION ALL keeps duplicates and is cheap; UNION de-duplicates and is not."),
    "intersect":("INTERSECT", "INTERSECT keeps only rows present in both result sets, removing duplicates."),
    "except":  ("EXCEPT / MINUS", "EXCEPT keeps rows from the first result set that do not appear in the second."),
    "values":  ("VALUES (Literal Rows)", "A VALUES clause supplies explicit, hard-coded rows as input — commonly the source of an INSERT or a small lookup table written inline."),
    "insert":  ("INSERT", "INSERT writes new rows into a target table, either from literal VALUES or from the result of a query."),
    "insert_target":("Insert Target", "The table that receives the inserted rows."),
    "update":  ("UPDATE", "UPDATE changes values in rows that already exist. Without a WHERE clause it rewrites every row in the table."),
    "delete":  ("DELETE", "DELETE removes rows from a table. Without a WHERE clause it removes all of them."),
    "merge":   ("MERGE / UPSERT", "MERGE applies inserts, updates and deletes in one pass by matching source rows against target rows."),
    "set":     ("SET (Assignment)", "The SET clause of an UPDATE lists which columns change and what they change to."),
    "returning":("RETURNING", "RETURNING makes an INSERT, UPDATE or DELETE hand back the affected rows, so no second query is needed to see what happened."),
    "create":  ("CREATE TABLE", "CREATE TABLE defines a new table: its columns, their types and their constraints."),
    "column":  ("Column Definition", "One column of a table definition — name, data type and any constraints."),
    "result":  ("Final Result", "What the query hands back to the caller after every step above has run."),
    "operation":("SQL Operation", "A statement that acts on data or schema. See the engine's documentation for the exact semantics."),
}
ENCY_ID = {
    "table":   ("FROM (Sumber Tabel)", "Klausa FROM menyebut tabel sumber yang dibaca kueri. Ini titik awal pipeline — semua langkah setelahnya bekerja pada baris yang keluar dari sini."),
    "catalog": ("Sumber Lintas Katalog", "Tabel yang dibaca dari katalog lain (sistem penyimpanan yang berbeda). Mesin kueri menggabungkan bacaan lintas sistem, sehingga baris harus berpindah antar sistem sebelum bisa di-join."),
    "subquery":("Subkueri Inline", "Kueri utuh yang ditanam di dalam FROM dan berperilaku seperti tabel sementara, lalu dipakai sebagai sumber biasa."),
    "join":    ("JOIN", "JOIN menggabungkan baris dari dua sumber berdasarkan kondisi pencocokan. Jenis join (INNER, LEFT, RIGHT, FULL, CROSS) menentukan nasib baris yang tidak menemukan pasangan — dan apakah jumlah baris bisa membengkak."),
    "semijoin":("Semi / Anti Join (EXISTS · IN)", "Subkueri EXISTS, IN atau NOT IN yang dipakai sebagai filter. Berbeda dari join biasa, langkah ini tidak pernah menggandakan baris: ia hanya menanyakan ada/tidaknya pasangan, jadi hanya bisa menyusutkan."),
    "unnest":  ("UNNEST · LATERAL (Pemekaran Baris)", "Memekarkan array, map atau subkueri berkorelasi menjadi baris. Ini salah satu dari sedikit langkah yang melipatgandakan jumlah baris: satu baris masukan menjadi sebanyak isi koleksinya."),
    "where":   ("WHERE (Filter Baris)", "WHERE membuang baris satu per satu sebelum pengelompokan terjadi. Hanya baris yang kondisinya bernilai benar yang lolos — perbandingan dengan NULL dianggap tidak benar dan ikut terbuang."),
    "having":  ("HAVING (Filter Grup)", "HAVING menyaring grup utuh setelah GROUP BY berjalan. Di sinilah kondisi atas nilai agregat ditempatkan, karena WHERE belum bisa melihatnya."),
    "qualify": ("QUALIFY (Filter Window)", "QUALIFY menyaring baris memakai hasil window function, setelah window dihitung. Ia adalah padanan HAVING untuk window function."),
    "select":  ("SELECT (Proyeksi)", "Daftar SELECT menentukan kolom dan ekspresi apa yang keluar dari langkah ini. Ia mengubah bentuk baris — jumlah kolom — tetapi tidak mengubah jumlah baris."),
    "window":  ("Window Function (OVER)", "Window function menghitung nilai atas sekumpulan baris terkait (PARTITION BY … ORDER BY …) tanpa membuang satu baris pun. Jumlah baris tetap; tiap baris hanya bertambah kolom peringkat, total berjalan, atau lag/lead."),
    "groupby": ("GROUP BY (Agregasi)", "GROUP BY meringkas baris berkunci sama menjadi satu baris per grup. Fungsi agregat (COUNT, SUM, AVG) lalu merangkum tiap grup — biasanya ini penyusutan terbesar dalam satu pipeline."),
    "aggregate":("Agregat Global", "Agregat tanpa GROUP BY meringkas seluruh masukan menjadi tepat satu baris."),
    "distinct":("DISTINCT (Penghilang Duplikat)", "DISTINCT membuang baris kembar. Hanya bisa menyusutkan jumlah baris, dan memaksa mesin mengurutkan atau meng-hash seluruh data."),
    "orderby": ("ORDER BY (Pengurutan)", "ORDER BY mengurutkan hasil. Tidak menambah atau mengurangi baris; tanpanya mesin tidak menjamin urutan apa pun."),
    "limit":   ("LIMIT / FETCH (Batas Baris)", "LIMIT membatasi jumlah baris yang dikembalikan. Dengan OFFSET ia jadi paginasi; dengan ORDER BY ia menjawab pertanyaan top-N."),
    "cte":     ("WITH / CTE", "Common Table Expression adalah hasil sementara bernama yang hidup hanya selama kueri ini. Ia membuat kueri panjang terbaca dan bisa dirujuk berulang kali."),
    "union":   ("UNION / UNION ALL", "UNION menumpuk dua hasil — satu-satunya operasi umum yang menambah baris. UNION ALL mempertahankan duplikat dan murah; UNION membuang duplikat dan mahal."),
    "intersect":("INTERSECT", "INTERSECT hanya menyisakan baris yang ada di kedua hasil, tanpa duplikat."),
    "except":  ("EXCEPT / MINUS", "EXCEPT menyisakan baris hasil pertama yang tidak muncul di hasil kedua."),
    "values":  ("VALUES (Baris Literal)", "Klausa VALUES memasok baris tetap yang ditulis langsung — biasanya sumber INSERT atau tabel rujukan kecil."),
    "insert":  ("INSERT", "INSERT menulis baris baru ke tabel tujuan, dari VALUES literal atau dari hasil sebuah kueri."),
    "insert_target":("Tabel Tujuan", "Tabel yang menerima baris hasil INSERT."),
    "update":  ("UPDATE", "UPDATE mengubah nilai pada baris yang sudah ada. Tanpa WHERE, seluruh isi tabel ditulis ulang."),
    "delete":  ("DELETE", "DELETE menghapus baris dari tabel. Tanpa WHERE, semuanya terhapus."),
    "merge":   ("MERGE / UPSERT", "MERGE menerapkan insert, update dan delete sekaligus dengan mencocokkan baris sumber ke baris tujuan."),
    "set":     ("SET (Penugasan Nilai)", "Klausa SET pada UPDATE menyebut kolom mana yang berubah dan menjadi apa."),
    "returning":("RETURNING", "RETURNING membuat INSERT, UPDATE atau DELETE mengembalikan baris yang terdampak, sehingga tak perlu kueri kedua."),
    "create":  ("CREATE TABLE", "CREATE TABLE mendefinisikan tabel baru: kolom, tipe data dan batasannya."),
    "column":  ("Definisi Kolom", "Satu kolom dalam definisi tabel — nama, tipe data dan batasan."),
    "result":  ("Hasil Akhir", "Yang dikembalikan kueri ke pemanggil setelah seluruh langkah di atas berjalan."),
    "operation":("Operasi SQL", "Pernyataan yang bekerja pada data atau skema. Lihat dokumentasi mesin untuk semantik persisnya."),
}

UI_EN = {
    "sql": "SQL", "funnel": "Data funnel", "brief": "Brief", "diagram": "Diagram",
    "definition": "definition", "inquery": "in this query", "rows": "row funnel",
    "columns": "columns involved", "notes": "assumptions & warnings",
    "summary": "what this query does", "legend": "legend",
    "stage": "stage", "rowsout": "rows out", "change": "change",
    "why": "why it changes", "unknown": "not measured", "start": "start",
    "final": "final result", "kept": "kept", "ofinput": "of the starting rows",
    "nodata": "No row counts were provided for this query.",
    "logscale": "bar lengths use a log scale", "of": "of",
    "nofunnel": "No row counts were available for this query, so this page maps its logic only — "
                "it makes no claim about how many rows each step touches.",
    "grounded": {"live": "row counts measured against the live database",
                 "stated": "row counts come from the figures you supplied",
                 "schema": "row counts from catalog statistics, not exact counts",
                 "estimate": "row counts are reasoned estimates, not measured",
                 "none": "no database access — logic only"},
    "close": "Close", "fit": "Fit to view", "zin": "Zoom in", "zout": "Zoom out",
    "dirLR": "Lay it out left to right", "dirTB": "Lay it out top to bottom",
    "print": "Print · save as PDF", "steps": "Every step", "docof": "Query logic map",
    "hint": "Click any step for the full explanation · drag to pan · scroll to zoom",
}
UI_ID = {
    "sql": "SQL", "funnel": "Funnel data", "brief": "Ringkasan", "diagram": "Diagram",
    "definition": "definisi", "inquery": "di kueri ini", "rows": "funnel baris",
    "columns": "kolom yang terlibat", "notes": "asumsi & peringatan",
    "summary": "apa yang dilakukan kueri ini", "legend": "legenda",
    "stage": "tahap", "rowsout": "baris keluar", "change": "perubahan",
    "why": "kenapa berubah", "unknown": "belum diukur", "start": "awal",
    "final": "hasil akhir", "kept": "tersisa", "ofinput": "dari baris awal",
    "nodata": "Tidak ada angka baris yang disertakan untuk kueri ini.",
    "logscale": "panjang bar memakai skala logaritmik", "of": "dari",
    "nofunnel": "Tidak ada angka baris yang bisa diperoleh untuk kueri ini, jadi halaman ini hanya "
                "memetakan logikanya — tanpa klaim apa pun soal berapa baris yang lewat di tiap langkah.",
    "grounded": {"live": "angka baris diukur langsung ke database",
                 "stated": "angka baris berasal dari data yang Anda sebutkan",
                 "schema": "angka baris dari statistik katalog, bukan hitungan persis",
                 "estimate": "angka baris adalah perkiraan bernalar, bukan hasil ukur",
                 "none": "tanpa akses database — hanya logika kueri"},
    "close": "Tutup", "fit": "Paskan tampilan", "zin": "Perbesar", "zout": "Perkecil",
    "dirLR": "Ubah arah jadi kiri ke kanan", "dirTB": "Ubah arah jadi atas ke bawah",
    "print": "Cetak · simpan sebagai PDF", "steps": "Rincian tiap langkah", "docof": "Peta logika kueri",
    "hint": "Klik langkah mana pun untuk penjelasan penuh · seret untuk geser · gulir untuk zoom",
}


# ─────────────────────────── layout ───────────────────────────
# A small top-to-bottom layered layout in the spirit of dagre: rank by longest
# path, order each rank with the median heuristic to cut crossings, then place
# x with the priority method. Heights are measured in the browser (text wraps
# differently per device), so this only fixes x, rank and edge routing lanes.

GROUP_PAD = 18      # breathing room between a cluster box and its own members
GROUP_GAP = 30      # clearance a non-member must keep from someone else's box


class Lay:
    """Layered layout on one cross axis. For a top-to-bottom diagram the cross
    axis is x and every node is 240 wide; for left-to-right it is y and the
    extent is the card's estimated height. Everything else is identical."""

    def __init__(self, nodes, edges, cross=None, sep=NODE_SEP, dummy=DUMMY_W):
        self.ids = [n["id"] for n in nodes]
        self.w = {n["id"]: (cross[n["id"]] if cross else NODE_W) for n in nodes}
        self.base_sep = sep
        self.dummy_w = dummy
        self.group = {n["id"]: n.get("group") or None for n in nodes}
        self.succ = {i: [] for i in self.ids}
        self.pred = {i: [] for i in self.ids}
        self.edges = []
        for e in edges:
            if e.get("recursive"):
                continue
            s, t = e["from"], e["to"]
            if s not in self.succ or t not in self.pred or s == t:
                continue
            self.edges.append(e)
            self.succ[s].append(t)
            self.pred[t].append(s)
        self.rank = {}
        self.dummies = {}          # dummy id -> {rank, x}
        self.route = {}            # (from,to) -> [dummy ids]

    # rank: longest path from any source, cycles broken by first-seen order
    def rank_nodes(self):
        state = {i: 0 for i in self.ids}   # 0 unseen, 1 on stack, 2 done
        order = []
        def visit(n):
            if state[n] == 1:              # back edge: ignore to keep a DAG
                return
            if state[n] == 2:
                return
            state[n] = 1
            for m in self.succ[n]:
                visit(m)
            state[n] = 2
            order.append(n)
        for i in self.ids:
            visit(i)
        for n in order:                    # reverse topological
            self.rank[n] = 0
        for n in reversed(order):
            for m in self.succ[n]:
                if m in self.rank:
                    self.rank[m] = max(self.rank[m], self.rank[n] + 1)
        # tighten: a source node with no predecessors is pulled down to sit just
        # above whatever consumes it, so a lookup table joined late in the query
        # does not hover at the top of the diagram behind a seven-rank edge.
        for n in self.ids:
            if not self.pred.get(n) and self.succ.get(n):
                self.rank[n] = min(self.rank[m] for m in self.succ[n]) - 1

    # long edges get a chain of dummy nodes so they travel in their own lane
    def make_dummies(self):
        for e in self.edges:
            s, t = e["from"], e["to"]
            span = self.rank[t] - self.rank[s]
            chain = []
            if span > 1:
                for r in range(self.rank[s] + 1, self.rank[t]):
                    did = f"__d{len(self.dummies)}"
                    self.dummies[did] = r
                    self.rank[did] = r
                    self.w[did] = self.dummy_w
                    self.group[did] = None
                    self.succ[did] = []
                    self.pred[did] = []
                    chain.append(did)
                prev = s
                for d in chain + [t]:
                    self.succ[prev] = [x for x in self.succ[prev]]
                    if d in chain or d == t:
                        pass
                    prev = d
                # rewire adjacency for ordering purposes
                self.succ[s] = [x for x in self.succ[s] if x != t] + [chain[0]]
                self.pred[t] = [x for x in self.pred[t] if x != s] + [chain[-1]]
                for a, b in zip(chain, chain[1:]):
                    self.succ[a].append(b)
                    self.pred[b].append(a)
                self.pred[chain[0]].append(s)
                self.succ[chain[-1]].append(t)
            self.route[(s, t)] = chain

    def order_ranks(self):
        maxr = max(self.rank.values()) if self.rank else 0
        layers = [[] for _ in range(maxr + 1)]
        seen = set()
        # seed with a depth-first sweep from the roots: keeps related steps adjacent
        roots = [i for i in self.rank if not self.pred.get(i)]
        stack = list(reversed(roots or list(self.rank)))
        while stack:
            n = stack.pop()
            if n in seen:
                continue
            seen.add(n)
            layers[self.rank[n]].append(n)
            for m in reversed(self.succ.get(n, [])):
                if m not in seen:
                    stack.append(m)
        for n in self.rank:
            if n not in seen:
                layers[self.rank[n]].append(n)

        def median(n, ref):
            xs = sorted(ref.index(m) for m in (self.pred[n] if ref is not None else []) if m in ref)
            return xs

        for it in range(10):
            down = it % 2 == 0
            rng = range(1, len(layers)) if down else range(len(layers) - 2, -1, -1)
            for r in rng:
                ref = layers[r - 1] if down else layers[r + 1]
                pos = {n: k for k, n in enumerate(ref)}
                def key(n):
                    adj = self.pred[n] if down else self.succ[n]
                    xs = sorted(pos[m] for m in adj if m in pos)
                    if not xs:
                        return layers[r].index(n) + 0.0
                    mid = len(xs) // 2
                    return xs[mid] if len(xs) % 2 else (xs[mid - 1] + xs[mid]) / 2.0
                layers[r] = sorted(layers[r], key=lambda n: (key(n), layers[r].index(n)))

        # Cluster contiguity: a CTE reads as one block only if its members sit
        # next to each other in every rank they appear in. Without this the box
        # drawn around them can swallow a node that belongs to another block.
        for r, layer in enumerate(layers):
            pos = {n: i for i, n in enumerate(layer)}
            mean = {}
            for n in layer:
                g = self.group.get(n)
                if g:
                    mean.setdefault(g, []).append(pos[n])
            mean = {g: sum(v) / len(v) for g, v in mean.items()}
            layers[r] = sorted(layer, key=lambda n: (mean.get(self.group.get(n), pos[n]), pos[n]))
        self.layers = layers

    def assign_x(self):
        x = {}
        for layer in self.layers:
            cur = 0.0
            prev = None
            for n in layer:
                if prev is not None:
                    cur += self.sep(prev, n) - self.base_sep
                x[n] = cur + self.w[n] / 2
                cur += self.w[n] + self.base_sep
                prev = n
        for it in range(16):
            if it and it % 5 == 0:
                self.cluster_pull(x)
            down = it % 2 == 0
            rng = range(1, len(self.layers)) if down else range(len(self.layers) - 2, -1, -1)
            for r in rng:
                layer = self.layers[r]
                prio = {}
                want = {}
                for n in layer:
                    adj = [m for m in (self.pred[n] if down else self.succ[n]) if m in x]
                    prio[n] = (2 if n in self.dummies else 1) * (len(adj) + 1)
                    if adj:
                        xs = sorted(x[m] for m in adj)
                        mid = len(xs) // 2
                        want[n] = xs[mid] if len(xs) % 2 else (xs[mid - 1] + xs[mid]) / 2.0
                for n in sorted(layer, key=lambda n: -prio[n]):
                    if n not in want:
                        continue
                    self._shift(layer, x, prio, n, want[n] - x[n])
        self.cluster_pull(x)
        # normalise to a left margin
        minx = min(x[n] - self.w[n] / 2 for n in x) if x else 0
        for n in x:
            x[n] -= minx - 40
        self.x = x

    def sep(self, a, b):
        ga, gb = self.group.get(a), self.group.get(b)
        return self.base_sep + (2 * GROUP_PAD + 10 if ga != gb and (ga or gb) else 0)

    def _gap(self, x, layer, i, j):
        return ((x[layer[j]] - self.w[layer[j]] / 2)
                - (x[layer[i]] + self.w[layer[i]] / 2)
                - self.sep(layer[i], layer[j]))

    def _push(self, layer, x, prio, i, delta, base):
        """Move layer[i] by delta, cascading into lower-priority neighbours only
        as far as they actually need to move. Returns the signed distance applied."""
        step = 1 if delta > 0 else -1
        mag = abs(delta)
        k = i + step
        if 0 <= k < len(layer):
            gap = max(0.0, self._gap(x, layer, min(i, k), max(i, k)))
            if gap < mag:
                if prio[layer[k]] >= base:
                    mag = gap
                else:
                    moved = self._push(layer, x, prio, k, (mag - gap) * step, base)
                    mag = gap + abs(moved)
        x[layer[i]] += mag * step
        return mag * step

    def _shift(self, layer, x, prio, node, delta):
        if abs(delta) < 0.5:
            return
        self._push(layer, x, prio, layer.index(node), delta, prio[node])

    def cluster_pull(self, x):
        """Draw every member of a cluster toward the cluster's own median.

        Ordering keeps a CTE's nodes adjacent within each rank, but nothing
        stops the chain from drifting sideways rank by rank. A staircase-shaped
        CTE then needs a box wide enough to cover the whole stagger, which
        shoves the next cluster further right — and with seven or eight CTEs
        that compounds into a canvas nobody can read. Pulling members onto a
        shared column keeps each box about one node wide."""
        groups = {}
        for n in self.ids:
            g = self.group.get(n)
            if g:
                groups.setdefault(g, []).append(n)
        for g, members in groups.items():
            xs = sorted(x[m] for m in members)
            mid = xs[len(xs) // 2] if len(xs) % 2 else (xs[len(xs) // 2 - 1] + xs[len(xs) // 2]) / 2.0
            # move the outliers first; they have the furthest to travel
            for m in sorted(members, key=lambda m: -abs(x[m] - mid)):
                layer = self.layers[self.rank[m]]
                prio = {k: (6 if self.group.get(k) == g else 1) for k in layer}
                self._push(layer, x, prio, layer.index(m), mid - x[m], 6)

    def boxes(self):
        """x-extent and rank-extent of every cluster, from its members only."""
        b = {}
        for n in self.ids:
            g = self.group.get(n)
            if not g:
                continue
            x0, x1, r = self.x[n] - self.w[n] / 2, self.x[n] + self.w[n] / 2, self.rank[n]
            if g in b:
                o = b[g]
                b[g] = [min(o[0], x0), max(o[1], x1), min(o[2], r), max(o[3], r)]
            else:
                b[g] = [x0, x1, r, r]
        return b

    def _force(self, node, delta):
        """Move one node, letting it push anything in its rank out of the way."""
        layer = self.layers[self.rank[node]]
        prio = {m: (99 if m == node else 1) for m in layer}
        self._push(layer, self.x, prio, layer.index(node), delta, 99)

    def separate_groups(self):
        """A cluster box is drawn from its members, so anything else that lands
        inside the same rectangle gets sliced by its border. Evict those nodes
        sideways, and keep two boxes that share ranks from overlapping."""
        for _ in range(6):
            moved = False
            b = self.boxes()

            for g, (x0, x1, r0, r1) in b.items():
                left, right = x0 - GROUP_PAD, x1 + GROUP_PAD
                for n in list(self.ids) + list(self.dummies):
                    if self.group.get(n) == g or not (r0 <= self.rank[n] <= r1):
                        continue
                    half = self.w[n] / 2
                    if self.x[n] + half <= left - GROUP_GAP or self.x[n] - half >= right + GROUP_GAP:
                        continue
                    to_left = (left - GROUP_GAP) - (self.x[n] + half)
                    to_right = (right + GROUP_GAP) - (self.x[n] - half)
                    self._force(n, to_left if abs(to_left) < abs(to_right) else to_right)
                    moved = True

            names = sorted(b, key=lambda g: b[g][0])
            for i, g1 in enumerate(names):
                for g2 in names[i + 1:]:
                    a, c = b[g1], b[g2]
                    if a[3] < c[2] or c[3] < a[2]:          # no shared ranks
                        continue
                    overlap = (a[1] + GROUP_PAD + GROUP_GAP) - (c[0] - GROUP_PAD)
                    if overlap <= 0:
                        continue
                    for r in range(c[2], c[3] + 1):
                        members = [n for n in self.layers[r] if self.group.get(n) == g2]
                        for n in sorted(members, key=lambda n: -self.layers[r].index(n)):
                            self._force(n, overlap)
                    moved = True
                    b = self.boxes()

            if not moved:
                break

        minx = min(self.x[n] - self.w[n] / 2 for n in self.x) if self.x else 0
        for n in self.x:
            self.x[n] -= minx - 40

    def run(self):
        self.rank_nodes()
        self.make_dummies()
        self.order_ranks()
        self.assign_x()
        self.separate_groups()
        return self


CPL = 30          # characters that fit on one line of a card at 240px
CROSS_SEP_LR = 30


def est_height(n):
    body = max(1, -(-len(str(n.get("plain", ""))) // CPL)) * 16
    foot = 26 if (n.get("rows_in") is not None or n.get("rows_out") is not None
                  or n.get("badges")) else 0
    return max(80.0, 34 + body + 12 + foot)


def layout(nodes, edges, direction="TB"):
    if direction == "LR":
        l = Lay(nodes, edges, cross={n["id"]: est_height(n) for n in nodes},
                sep=CROSS_SEP_LR, dummy=26).run()
    else:
        l = Lay(nodes, edges).run()
    out_nodes = {n["id"]: {"cross": l.x[n["id"]], "rank": l.rank[n["id"]],
                           "size": l.w[n["id"]],
                           "order": l.layers[l.rank[n["id"]]].index(n["id"])}
                 for n in nodes}
    dummies = {d: {"cross": l.x[d], "rank": r} for d, r in l.dummies.items()}
    routes = {f'{s}>{t}': ids for (s, t), ids in l.route.items()}
    extent = max([l.x[n] + l.w[n] / 2 for n in l.x] or [400]) + 40
    return out_nodes, dummies, routes, extent, (max(l.rank.values()) + 1 if l.rank else 1)


# ─────────────────────── SQL syntax highlighting ───────────────────────
KEYWORDS = set("""
select from where group by having order limit offset fetch first next rows only
join inner left right full outer cross lateral natural on using union all intersect
except minus with recursive as distinct case when then else end and or not null is
in exists between like ilike similar to any some asc desc nulls insert into values
update set delete truncate merge matched using returning create table view schema
materialized index drop alter add column constraint primary key foreign references
unique check default cast over partition range rows groups preceding following
unbounded current row window filter within qualify tablesample bernoulli system
unnest ordinality array map row struct if elseif while begin end commit rollback
explain analyze describe show catalog catalogs schemas tables grant revoke
""".split())
FUNCS = set("""
count sum avg min max round abs coalesce nullif greatest least now current_date
current_timestamp date_trunc date_diff date_add date_format extract cast try_cast
row_number rank dense_rank ntile lag lead first_value last_value nth_value
percent_rank cume_dist string_agg array_agg listagg group_concat approx_distinct
concat substr substring lower upper trim length replace split split_part regexp_like
json_extract json_extract_scalar cardinality element_at contains array_join sequence
coalesce ifnull isnull nvl to_char to_date to_timestamp from_unixtime generate_series
sum_if count_if stddev variance median approx_percentile histogram
""".split())

TOKEN_RE = re.compile(r"""
  (?P<comment>--[^\n]*|/\*.*?\*/)
| (?P<string>'(?:''|[^'])*')
| (?P<quoted>"(?:""|[^"])*"|`[^`]*`)
| (?P<number>\b\d+\.?\d*([eE][-+]?\d+)?\b)
| (?P<word>[A-Za-z_][A-Za-z_0-9$]*)
| (?P<op>[-+*/%<>=!|&^~]+)
| (?P<punc>[(),;.\[\]{}:@?])
| (?P<ws>\s+)
""", re.X | re.S)


def highlight_sql(sql):
    out = []
    i = 0
    for m in TOKEN_RE.finditer(sql):
        if m.start() > i:
            out.append(('', sql[i:m.start()], i, m.start()))
        kind = m.lastgroup
        text = m.group()
        s, e = m.start(), m.end()
        cls = ''
        if kind == 'comment':
            cls = 'c'
        elif kind == 'string':
            cls = 's'
        elif kind == 'quoted':
            cls = 'id'
        elif kind == 'number':
            cls = 'n'
        elif kind == 'op':
            cls = 'o'
        elif kind == 'punc':
            cls = 'p'
        elif kind == 'word':
            low = text.lower()
            nxt = sql[e:e + 1]
            if low in KEYWORDS:
                cls = 'k'
            elif low in FUNCS or nxt == '(':
                cls = 'f'
            else:
                cls = 'id'
        out.append((cls, text, s, e))
        i = e
    if i < len(sql):
        out.append(('', sql[i:], i, len(sql)))
    parts = []
    for cls, text, s, e in out:
        t = escape(text)
        if cls:
            parts.append(f'<span class="{cls}" data-s="{s}" data-e="{e}">{t}</span>')
        else:
            parts.append(f'<span data-s="{s}" data-e="{e}">{t}</span>')
    return ''.join(parts)


# ─────────────────────────── helpers ───────────────────────────
def icon(name, size=16, cls="ic"):
    body = ICONS.get(name) or ICONS["cog"]
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" '
            f'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{body}</svg>')


def num(v):
    """12400000 -> '12.400.000'-ish, locale-neutral with thin spacing."""
    if v is None:
        return None
    if isinstance(v, str):
        return v
    try:
        n = float(v)
    except (TypeError, ValueError):
        return str(v)
    if n != n:
        return None
    if abs(n - round(n)) < 1e-9:
        return f"{int(round(n)):,}".replace(",", " ")
    return f"{n:,.2f}".replace(",", " ")


def compact(v):
    if v is None:
        return "?"
    if isinstance(v, str):
        return v
    try:
        n = float(v)
    except (TypeError, ValueError):
        return str(v)
    a = abs(n)
    for lim, suf in ((1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")):
        if a >= lim:
            q = n / lim
            return (f"{q:.1f}".rstrip("0").rstrip(".")) + suf
    return f"{int(n):,}".replace(",", " ") if abs(n - round(n)) < 1e-9 else f"{n:.2f}"


def as_number(v):
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return float(v)
    return None


def md_inline(text):
    """`code` and **bold** inside explanation text."""
    t = escape(text or "")
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    return t


CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Inclusive+Sans:ital,wght@0,300..700;1,300..700&family=Martian+Mono:wght@100..800&display=swap');
:root{
  --bg:#100F0F; --bg-2:#1C1B1A; --ui:#282726; --ui-2:#343331; --ui-3:#403E3C;
  --tx:#E6E4D9; --tx-2:#9F9D96; --tx-3:#6F6E69;
  --re:#E8705F; --or:#EC8B49; --ye:#DFB431; --gr:#A0AF54; --cy:#5ABDAC;
  --bl:#66A0C8; --pu:#A699D0; --ma:#E47DA8;
  --br-sm:.1875rem; --br-md:.3125rem; --br-lg:.5rem; --br-xl:.8125rem;
  --sans:'Inclusive Sans',system-ui,-apple-system,sans-serif;
  --mono:'Martian Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
  color-scheme:dark;
}
*,*::before,*::after{box-sizing:border-box}
[hidden]{display:none!important}
body{margin:0;background:var(--bg);color:var(--tx);font-family:var(--sans);
  font-weight:450;line-height:1.375;-webkit-font-smoothing:antialiased}
.ae{display:grid;grid-template-columns:minmax(300px,34%) 1fr;grid-template-rows:minmax(0,1fr);
  height:calc(100dvh - env(safe-area-inset-top,0px) - env(safe-area-inset-bottom,0px));
  min-height:520px;overflow:hidden;position:relative}

/* ── left pane ── */
.pane{display:flex;flex-direction:column;min-width:0;min-height:0;overflow:hidden;
  border-right:1px solid var(--ui-3);background:var(--bg)}
.paneHead{display:flex;align-items:baseline;gap:.75rem;flex-wrap:wrap;padding:.85rem 1rem}
.brand{font-size:1.05rem;font-weight:575;margin:0;letter-spacing:.01em;white-space:nowrap}
.brand b{text-transform:uppercase;font-weight:575}
.sub{font-size:.8rem;color:var(--tx-2)}
.chip{font-family:var(--mono);font-size:.6rem;font-weight:500;text-transform:uppercase;
  letter-spacing:.06em;padding:.25em .5em;border-radius:var(--br-sm);
  color:var(--cy);background:color-mix(in srgb,var(--cy) 16%,transparent)}
.tabs{display:flex;gap:.25rem;padding:0 .75rem;border-bottom:1px solid var(--ui-3)}
.tab{font-family:var(--sans);font-size:.8rem;color:var(--tx-2);background:none;border:none;
  border-bottom:2px solid transparent;padding:.5rem .6rem;cursor:pointer;transition:color .15s}
.tab:hover{color:var(--tx)}
.tab[aria-selected="true"]{color:var(--tx);border-bottom-color:var(--cy)}
.tabBody{flex:1;overflow:auto;min-height:0}
.tabBody[hidden]{display:none!important}

/* ── sql ── */
pre.sql{font-family:var(--mono);font-size:.72rem;font-weight:475;line-height:1.55;
  margin:0;padding:.85rem 1rem 3rem;white-space:pre-wrap;word-break:break-word;color:var(--tx)}
pre.sql .k{color:var(--bl)} pre.sql .s{color:var(--or)} pre.sql .n{color:var(--ye)}
pre.sql .c{color:var(--gr);font-style:italic} pre.sql .o{color:var(--pu)}
pre.sql .f{color:var(--cy)} pre.sql .p{color:var(--tx-2)} pre.sql .id{color:var(--tx)}
pre.sql .hl{background:color-mix(in srgb,var(--cy) 25%,transparent);
  border-bottom:2px solid var(--cy);border-radius:var(--br-sm) var(--br-sm) 0 0}

/* ── funnel ── */
.fTop{padding:1rem 1rem .75rem;border-bottom:1px solid var(--ui-3)}
.fTopRow{display:flex;align-items:flex-end;gap:.6rem;flex-wrap:wrap}
.fBig{font-family:var(--mono);font-size:1.4rem;font-weight:500;line-height:1}
.fArrow{color:var(--tx-3);font-size:1.1rem}
.fNote{font-size:.78rem;color:var(--tx-2);margin:.5rem 0 0}
.funnel{list-style:none;margin:0;padding:.5rem .5rem 3rem}
.fStep{padding:.6rem .5rem;border-radius:var(--br-md);cursor:pointer;transition:background .15s}
.fStep:hover{background:var(--bg-2)}
.fStep.on{background:var(--bg-2);outline:1px solid var(--ui-3)}
.fHead{display:flex;align-items:center;gap:.45rem;min-width:0}
.fHead .ic{color:var(--nc,var(--cy));flex:none}
.fName{font-family:var(--mono);font-size:.66rem;font-weight:475;flex:1;min-width:0;
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--tx)}
.fNum{font-family:var(--mono);font-size:.72rem;font-weight:500;color:var(--tx);flex:none}
.fNum.q{color:var(--tx-3)}
.fBar{height:7px;margin:.4rem 0 .35rem;border-radius:99px;background:var(--ui);overflow:hidden}
.fBar i{display:block;height:100%;border-radius:99px;background:var(--nc,var(--cy));min-width:2px}
.fBar.q i{background:repeating-linear-gradient(135deg,var(--ui-3) 0 4px,transparent 4px 8px);width:100%}
.fMeta{display:flex;gap:.4rem;align-items:center;flex-wrap:wrap;font-family:var(--mono);font-size:.6rem}
.dlt{padding:.15em .4em;border-radius:var(--br-sm)}
.dlt.dn{color:var(--re);background:color-mix(in srgb,var(--re) 15%,transparent)}
.dlt.up{color:var(--gr);background:color-mix(in srgb,var(--gr) 15%,transparent)}
.dlt.eq{color:var(--tx-3);background:var(--ui)}
.fKept{color:var(--tx-3)}
.fWhy{font-size:.78rem;color:var(--tx-2);margin:.35rem 0 0;line-height:1.35}
.fWhy code{font-family:var(--mono);font-size:.72em;padding:.1em .25em;border-radius:var(--br-sm);
  color:var(--tx-2);background:color-mix(in srgb,var(--tx-2) 20%,transparent)}

/* ── brief ── */
.brief{padding:1rem 1rem 3rem}
.brief h3{font-size:.8rem;font-weight:425;text-transform:lowercase;color:var(--tx-2);
  margin:1.4rem 0 .6rem}
.brief h3:first-child{margin-top:0}
.brief p{font-size:.92rem;margin:0 0 .75rem;color:var(--tx)}
.brief ul{margin:0;padding-left:1.1rem;font-size:.85rem;color:var(--tx-2)}
.brief li{margin-bottom:.4rem}
.brief code{font-family:var(--mono);font-size:.75em;padding:.1em .3em;border-radius:var(--br-sm);
  color:var(--tx-2);background:color-mix(in srgb,var(--tx-2) 20%,transparent)}
.legend{display:flex;flex-wrap:wrap;gap:.35rem}
.lg{display:inline-flex;align-items:center;gap:.3rem;font-family:var(--mono);font-size:.6rem;
  padding:.25em .5em;border-radius:var(--br-sm);border:1px solid var(--nc);color:var(--nc)}

/* ── canvas ── */
.flow{position:relative;overflow:hidden;min-height:0;background:var(--bg);
  background-image:radial-gradient(var(--ui-2) 1.1px,transparent 1.1px);
  background-size:24px 24px;touch-action:none}
.canvas{position:absolute;top:0;left:0;transform-origin:0 0;will-change:transform}
.edges{position:absolute;top:0;left:0;overflow:visible;pointer-events:none}
.edges path{fill:none;stroke-width:2;stroke-dasharray:6 6;animation:dash 1s linear infinite}
@keyframes dash{to{stroke-dashoffset:-12}}
@media (prefers-reduced-motion:reduce){.edges path{animation:none}}
.node{position:absolute;width:240px;background:var(--bg-2);color:var(--tx);
  border:2px solid var(--nc);border-radius:var(--br-lg);overflow:hidden;cursor:pointer;
  box-shadow:0 .5em .5em .25em rgba(0,0,0,.3);font-family:var(--mono)}
.node.on{outline:2px solid var(--cy);outline-offset:2px;box-shadow:0 0 16px 6px rgba(90,189,172,.7)}
.nHead{display:flex;align-items:center;gap:.25em;min-width:0;padding:.5rem .5rem .35rem .75rem;color:var(--nc)}
.nHead .ic{flex:none}
.nLabel{font-size:.625rem;font-weight:475;flex:1;min-width:0;overflow:hidden;
  text-overflow:ellipsis;white-space:nowrap}
.nBody{font-size:.75rem;font-weight:325;line-height:1.35;padding:0 .75rem .6rem;margin:0;color:var(--tx)}
.nFoot{display:flex;align-items:center;gap:.3rem;flex-wrap:wrap;padding:.35rem .75rem .5rem;
  border-top:1px solid var(--ui);font-size:.6rem;color:var(--tx-2)}
.nFoot b{font-weight:500;color:var(--tx)}
.nTag{font-size:.55rem;padding:.15em .4em;border-radius:var(--br-sm);
  color:var(--nc);background:color-mix(in srgb,var(--nc) 14%,transparent)}
.grp{position:absolute;border:1px dashed var(--ui-3);border-radius:var(--br-xl);
  background:color-mix(in srgb,var(--bg-2) 55%,transparent);pointer-events:none}
.grpLab{position:absolute;font-family:var(--mono);font-size:.6rem;letter-spacing:.04em;
  color:var(--tx-3);padding:.15em .45em;border-radius:var(--br-sm);background:var(--bg);
  border:1px solid var(--ui-3);pointer-events:none;white-space:nowrap}

/* ── controls ── */
.ctrls{position:absolute;left:1rem;bottom:1rem;display:flex;flex-direction:column;
  border:1px solid var(--ui);border-radius:var(--br-md);overflow:hidden;background:var(--bg);z-index:4}
.ctrls button{width:2.25rem;height:2.25rem;display:flex;align-items:center;justify-content:center;
  border:none;border-bottom:1px solid var(--ui);background:var(--bg);color:var(--tx-2);cursor:pointer}
.ctrls button:last-child{border-bottom:none}
.ctrls button:hover{background:var(--bg-2);color:var(--tx)}
.hint{position:absolute;left:50%;transform:translateX(-50%);bottom:1rem;z-index:3;
  font-size:.68rem;color:var(--tx-3);background:color-mix(in srgb,var(--bg) 85%,transparent);
  padding:.35em .7em;border-radius:99px;pointer-events:none;text-align:center;max-width:90%}

/* ── details ── */
.details{position:absolute;top:0;right:0;width:23rem;max-width:100%;height:100%;z-index:10;
  background:var(--bg);border-left:1px solid var(--ui-3);overflow-y:auto;
  animation:slide .25s ease-out;display:flex;flex-direction:column}
@keyframes slide{from{transform:translateX(100%);opacity:0}to{transform:none;opacity:1}}
.dHead{display:flex;align-items:center;justify-content:space-between;gap:.5rem;padding:.5rem .5rem .5rem 1rem}
.dTitle{display:flex;align-items:center;gap:.5rem;min-width:0;font-size:1.05rem;font-weight:525;
  margin:0;color:var(--nc)}
.dClose{width:2.25rem;height:2.25rem;display:flex;align-items:center;justify-content:center;
  border:none;border-radius:var(--br-md);background:none;color:var(--tx-2);cursor:pointer;flex:none}
.dClose:hover{background:var(--bg-2);color:var(--tx)}
.dSql{font-family:var(--mono);font-size:.72rem;font-weight:375;padding:.75rem 1rem;margin:0;
  color:var(--tx-2);background:var(--bg-2);border-top:1px solid var(--ui-3);
  white-space:pre-wrap;word-break:break-word}
.dSec{padding:1rem 1rem 1.15rem;border-top:1px solid var(--ui-3)}
.dSec h4{font-size:.8rem;font-weight:425;text-transform:lowercase;color:var(--tx-2);margin:0 0 .8rem}
.dSec p{font-size:.95rem;font-weight:375;margin:0 0 .8rem;color:var(--tx)}
.dSec p:last-child{margin-bottom:0}
.dSec code{font-family:var(--mono);font-size:.78em;padding:.12em .28em;border-radius:var(--br-sm);
  color:var(--tx-2);background:color-mix(in srgb,var(--tx-2) 20%,transparent);word-break:break-word}
.dLink{display:inline-flex;align-items:center;gap:.35em;font-size:.85rem;color:var(--cy);text-decoration:none}
.dLink:hover{color:var(--tx)}
.dRows{display:flex;align-items:center;gap:.5rem;flex-wrap:wrap;font-family:var(--mono);font-size:.85rem}
.dCols{display:flex;flex-wrap:wrap;gap:.3rem}
.dCols span{font-family:var(--mono);font-size:.62rem;padding:.2em .45em;border-radius:var(--br-sm);
  color:var(--tx-2);background:var(--ui)}

/* ── print / PDF ──
   The screen design is dark by choice, but a PDF gets read on paper and in
   other people's viewers, so printing swaps to the light half of the same
   palette and lays the page out as a document: the diagram at the top, then
   the funnel, every step written out, the findings and the SQL. Nothing is
   lost — the interactive page just stops being interactive. */
.doc{display:none}
@media print{
  :root{
    --bg:#FFFCF0; --bg-2:#F2F0E5; --ui:#E6E4D9; --ui-2:#DAD8CE; --ui-3:#CECDC3;
    --tx:#100F0F; --tx-2:#6F6E69; --tx-3:#B7B5AC;
    --re:#AF3029; --or:#BC5215; --ye:#AD8301; --gr:#66800B; --cy:#24837B;
    --bl:#205EA6; --pu:#5E409D; --ma:#A02F6F;
    color-scheme:light;
  }
  *{ -webkit-print-color-adjust:exact !important; print-color-adjust:exact !important }
  @page{ size:A4 portrait; margin:14mm 12mm }
  body{background:#FFFCF0}
  .ae{display:block;height:auto;min-height:0;overflow:visible}
  .pane,.details,.ctrls,.hint,.mnav{display:none !important}
  /* A4 is narrower than the mobile breakpoint, so the phone rules would
     otherwise hide the diagram pane while printing. */
  .flow{display:block !important;position:static;overflow:visible;height:auto;
    background:none;border:none}
  .canvas{position:relative;transform:none !important;zoom:var(--pk,1);
    width:var(--pcw,auto);height:var(--pch,auto)}
  .flow{height:auto !important}
  .node{box-shadow:none;break-inside:avoid}
  .doc{display:block;max-width:100%;break-before:page}
  .doc h1{font-size:19pt;margin:0 0 .2em}
  .doc .docSub{font-size:9pt;color:var(--tx-2);margin:0 0 1.4em}
  .doc h2{font-size:12pt;margin:1.6em 0 .6em;padding-bottom:.25em;border-bottom:1px solid var(--ui-3);
    break-after:avoid}
  .doc p{font-size:10pt;margin:0 0 .7em}
  .doc code{font-family:var(--mono);font-size:8.5pt;background:var(--ui);padding:.1em .3em;border-radius:3px}
  .doc table{width:100%;border-collapse:collapse;font-size:8.5pt}
  .doc th{text-align:left;color:var(--tx-2);font-weight:500;border-bottom:1px solid var(--ui-3);padding:.35em .4em}
  .doc td{border-bottom:1px solid var(--ui-2);padding:.35em .4em;vertical-align:top}
  .doc td.n{font-family:var(--mono);text-align:right;white-space:nowrap}
  .doc .step{break-inside:avoid;margin:0 0 .9em;padding-left:.7em;border-left:3px solid var(--nc,var(--cy))}
  .doc .stepH{font-family:var(--mono);font-size:8.5pt;font-weight:500;color:var(--nc,var(--tx));
    word-break:break-word;margin-bottom:.2em}
  .doc .stepP{font-size:10pt;margin:0 0 .3em}
  .doc .stepD{font-size:9pt;color:var(--tx-2);margin:0}
  .doc .stepR{font-family:var(--mono);font-size:8pt;color:var(--tx-2);margin-top:.25em}
  .doc ul{font-size:9.5pt;padding-left:1.1em;margin:0}
  .doc li{margin-bottom:.45em;break-inside:avoid}
  .doc pre{font-family:var(--mono);font-size:7.5pt;line-height:1.45;white-space:pre-wrap;
    word-break:break-word;background:var(--bg-2);padding:.7em;border-radius:4px;color:var(--tx)}
  .docBreak{break-before:page}
}

/* ── mobile ── */
.mnav{display:none}
@media (max-width:860px){
  .ae{grid-template-columns:1fr}
  .pane{border-right:none}
  .ae[data-view="diagram"] .pane{display:none}
  .ae[data-view="panel"] .flow{display:none}
  .flow{min-height:0}
  .mnav{display:flex;position:absolute;left:0;right:0;bottom:0;z-index:20;
    border-top:1px solid var(--ui-3);background:var(--bg);
    padding-bottom:env(safe-area-inset-bottom,0px)}
  .mnav button{flex:1;display:flex;flex-direction:column;align-items:center;gap:.15rem;
    padding:.5rem;border:none;background:none;color:var(--tx-3);font-size:.65rem;cursor:pointer}
  .mnav button.on{color:var(--cy)}
  .tabBody,.pane{padding-bottom:0}
  .ctrls{bottom:4.5rem}
  .hint{display:none}
  .details{width:100%}
  .funnel,.brief,pre.sql{padding-bottom:5rem}
}
"""


JS = r"""
(function(){
const D = window.__AE__;
const flow = document.getElementById('aeFlow');
const canvas = document.getElementById('aeCanvas');
const svg = document.getElementById('aeEdges');
const details = document.getElementById('aeDetails');
const root = document.getElementById('aeRoot');
const RANK_SEP = D.rankSep, PAD = 40, W = D.nodeW;
let view = {k:1, x:0, y:0}, bounds={w:1000,h:1000}, active=null, dir = D.dir || 'TB';
const el = n => document.getElementById('nd-'+n.id);

/* ── 1. placement: ranks run down (TB) or across (LR); the cross axis is
      resolved against the real card heights, which only the browser knows ── */
function place(){
  const L = D.layouts[dir], byRank = {};
  D.nodes.forEach(n=>{
    const p = L.nodes[n.id];
    n.rank = p.rank; n.cross = p.cross;
    (byRank[p.rank] = byRank[p.rank] || []).push(n);
  });
  const ranks = Object.keys(byRank).map(Number).sort((a,b)=>a-b);
  D.bandPos = {};

  if(dir === 'TB'){
    let top = PAD;
    const bandTop = {}, bandH = {};
    ranks.forEach(r=>{
      /* a hidden pane measures as 0 (mobile starts on the code tab), so fall
         back to a sane height rather than poisoning the layout with NaN */
      const h = Math.max(...byRank[r].map(n=>el(n).offsetHeight||110));
      bandTop[r]=top; bandH[r]=h; top += h + RANK_SEP;
    });
    D.nodes.forEach(n=>{
      const e = el(n), h = e.offsetHeight||110;
      n.w = W; n.h = h; n.x = n.cross; n.y = bandTop[n.rank] + (bandH[n.rank]-h)/2;
      e.style.left = (n.x - n.w/2)+'px'; e.style.top = n.y+'px';
    });
    ranks.forEach(r=>{ D.bandPos[r] = bandTop[r] + bandH[r]/2; });
  } else {
    const colX = {};
    ranks.forEach(r=>{ colX[r] = PAD + r*(W + RANK_SEP) + W/2; });
    D.nodes.forEach(n=>{
      n.w = W; n.h = el(n).offsetHeight||110; n.x = colX[n.rank]; n.y = n.cross - n.h/2;
    });
    /* the planned cross positions used estimated heights — keep the planned
       order and the column's centre of mass, just push apart what overlaps */
    ranks.forEach(r=>{
      const col = byRank[r].slice().sort((a,b)=>a.cross-b.cross), S = D.crossSepLR;
      for(let i=1;i<col.length;i++){
        const need = (col[i-1].y + col[i-1].h + S) - col[i].y;
        if(need > 0) col[i].y += need;
      }
      const plan = col.reduce((s,n)=>s+n.cross,0)/col.length;
      const now  = col.reduce((s,n)=>s+n.y+n.h/2,0)/col.length;
      col.forEach(n=>{ n.y -= (now - plan); });
    });
    const minY = Math.min(...D.nodes.map(n=>n.y));
    D.nodes.forEach(n=>{
      n.y += PAD - minY;
      const e = el(n); e.style.left = (n.x - n.w/2)+'px'; e.style.top = n.y+'px';
    });
    ranks.forEach(r=>{ D.bandPos[r] = colX[r]; });
  }

  bounds = {
    w: Math.max(...D.nodes.map(n=>n.x + n.w/2)) + PAD,
    h: Math.max(...D.nodes.map(n=>n.y + n.h)) + PAD,
  };
  svg.setAttribute('width', bounds.w + 220);
  svg.setAttribute('height', bounds.h + 220);

  /* Printing must not depend on a beforeprint event firing — headless PDF
     exporters often skip it. So the page scale is published as a CSS variable
     the print stylesheet picks up on its own: A4 portrait minus the margins
     is ~703 CSS px wide at 96dpi. */
  const pk = Math.min(1, 703 / bounds.w);
  canvas.style.setProperty('--pk', pk);
  canvas.style.setProperty('--pcw', bounds.w + 'px');
  canvas.style.setProperty('--pch', bounds.h + 'px');
}

/* ── 2. groups (CTE clusters) drawn behind the nodes ── */
function groups(){
  canvas.querySelectorAll('.grp,.grpLab').forEach(e=>e.remove());
  (D.groups||[]).forEach(g=>{
    const members = D.nodes.filter(n=>n.group===g.id);
    if(!members.length) return;
    const P = D.groupPad;
    const x1 = Math.min(...members.map(n=>n.x - n.w/2)) - P;
    const x2 = Math.max(...members.map(n=>n.x + n.w/2)) + P;
    const y1 = Math.min(...members.map(n=>n.y)) - (P + 8);
    const y2 = Math.max(...members.map(n=>n.y + n.h)) + P;
    const box = document.createElement('div');
    box.className='grp';
    box.style.cssText=`left:${x1}px;top:${y1}px;width:${x2-x1}px;height:${y2-y1}px`;
    const lab = document.createElement('div');
    lab.className='grpLab'; lab.textContent=g.label;
    lab.style.cssText=`left:${x1+10}px;top:${y1-9}px`;
    canvas.insertBefore(box, canvas.firstChild);
    canvas.appendChild(lab);
  });
}

/* ── 3. edges ── */
function pathFor(pts){
  let d = `M ${pts[0][0]},${pts[0][1]}`;
  for(let i=1;i<pts.length;i++){
    const [x0,y0]=pts[i-1], [x1,y1]=pts[i];
    if(dir==='TB'){
      const dy = Math.max(24,(y1-y0)*0.5);
      d += ` C ${x0},${y0+dy} ${x1},${y1-dy} ${x1},${y1}`;
    } else {
      const dx = Math.max(24,(x1-x0)*0.5);
      d += ` C ${x0+dx},${y0} ${x1-dx},${y1} ${x1},${y1}`;
    }
  }
  return d;
}
function edges(){
  const L = D.layouts[dir];
  const colors = new Set(D.edges.map(e=>e.color));
  let defs = '<defs>';
  colors.forEach(c=>{
    defs += `<marker id="ar-${c.slice(1)}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5.2" `+
            `markerHeight="5.2" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="${c}"/></marker>`;
  });
  defs += '</defs>';
  const byId = {}; D.nodes.forEach(n=>byId[n.id]=n);
  let paths='';
  D.edges.forEach((e,i)=>{
    const s = byId[e.from], t = byId[e.to];
    if(!s||!t) return;
    if(e.recursive){
      /* excluded from the layout, drawn as a loop clear of the diagram */
      let d;
      if(dir==='TB'){
        const loopX = bounds.w + 70, fy = s.y + s.h/2, ty = t.y + t.h/2;
        d = `M ${s.x+s.w/2},${fy} C ${loopX},${fy} ${loopX},${ty} ${t.x+t.w/2},${ty}`;
      } else {
        const loopY = bounds.h + 70;
        d = `M ${s.x},${s.y+s.h} C ${s.x},${loopY} ${t.x},${loopY} ${t.x},${t.y+t.h}`;
      }
      paths += `<path d="${d}" stroke="${e.color}" marker-end="url(#ar-${e.color.slice(1)})"/>`;
      return;
    }
    const via = (L.via[e.key]||[]).map(id=>L.dummies[id]).filter(Boolean);
    let pts;
    if(dir==='TB'){
      pts = [[s.x, s.y + s.h]];
      via.forEach(dm=>pts.push([dm.cross, D.bandPos[dm.rank]]));
      pts.push([t.x, t.y - 6]);
    } else {
      pts = [[s.x + s.w/2, s.y + s.h/2]];
      via.forEach(dm=>pts.push([D.bandPos[dm.rank], dm.cross]));
      pts.push([t.x - t.w/2 - 6, t.y + t.h/2]);
    }
    paths += `<path d="${pathFor(pts)}" stroke="${e.color}" marker-end="url(#ar-${e.color.slice(1)})"/>`;
  });
  svg.innerHTML = defs + paths;
}

/* ── 4. pan + zoom ── */
function apply(){ canvas.style.transform = `translate(${view.x}px,${view.y}px) scale(${view.k})`; }
function fit(readable){
  const r = flow.getBoundingClientRect();
  const kw = (r.width-40)/(bounds.w+140), kh = (r.height-40)/bounds.h;
  let k = Math.min(kw, kh, 1.05);
  /* a long pipeline outgrows any screen along the axis it runs on; squeezing
     it all in makes the text unreadable, so the first view stays legible and
     scrolls along that axis, and the fit button is what zooms all the way out */
  if(readable) k = Math.max(k, Math.min(0.52, dir==='TB' ? kw : kh));
  view.k = Math.max(0.1, k);
  view.x = (r.width - bounds.w*view.k)/2;
  view.y = bounds.h*view.k <= r.height-24 ? (r.height - bounds.h*view.k)/2 : 12;
  if(bounds.w*view.k > r.width-24) view.x = 12;
  apply();
}
function zoom(f, cx, cy){
  const r = flow.getBoundingClientRect();
  cx = cx==null ? r.width/2 : cx; cy = cy==null ? r.height/2 : cy;
  const k2 = Math.min(2.5, Math.max(0.12, view.k*f));
  view.x = cx - (cx - view.x)*(k2/view.k);
  view.y = cy - (cy - view.y)*(k2/view.k);
  view.k = k2; apply();
}
flow.addEventListener('wheel', e=>{
  e.preventDefault();
  const r = flow.getBoundingClientRect();
  zoom(Math.pow(0.999, e.deltaY*(e.ctrlKey?3:1)), e.clientX-r.left, e.clientY-r.top);
},{passive:false});
let drag=null;
flow.addEventListener('pointerdown', e=>{
  if(e.target.closest('.node')||e.target.closest('.ctrls')) return;
  drag={x:e.clientX,y:e.clientY,vx:view.x,vy:view.y}; flow.setPointerCapture(e.pointerId);
});
flow.addEventListener('pointermove', e=>{
  if(!drag) return;
  view.x = drag.vx + (e.clientX-drag.x); view.y = drag.vy + (e.clientY-drag.y); apply();
});
['pointerup','pointercancel'].forEach(ev=>flow.addEventListener(ev, ()=>{drag=null;}));
document.getElementById('aeIn').onclick = ()=>zoom(1.25);
document.getElementById('aeOut').onclick = ()=>zoom(0.8);
document.getElementById('aeFit').onclick = ()=>fit(false);
const dirBtn = document.getElementById('aeDir');
function paintDir(){
  dirBtn.innerHTML = dir==='TB' ? D.iconLR : D.iconTB;
  dirBtn.title = dir==='TB' ? D.labelLR : D.labelTB;
  dirBtn.setAttribute('aria-label', dirBtn.title);
}
dirBtn.onclick = ()=>{ dir = dir==='TB' ? 'LR' : 'TB'; paintDir(); redraw(); };
paintDir();
document.getElementById('aePrint').onclick = ()=>{ try{ window.print(); }catch(e){} };

/* ── 5. selection: node ⇄ sql ⇄ funnel ── */
const sqlEl = document.getElementById('aeSql');
function markSql(span){
  sqlEl.querySelectorAll('.hl').forEach(el=>el.classList.remove('hl'));
  if(!span) return;
  let first=null;
  sqlEl.querySelectorAll('[data-s]').forEach(el=>{
    const s=+el.dataset.s, e=+el.dataset.e;
    if(e>span[0] && s<span[1]){ el.classList.add('hl'); if(!first) first=el; }
  });
  if(first) first.scrollIntoView({block:'center', behavior:'smooth'});
}
function select(id){
  if(active===id){ close(); return; }
  active = id;
  document.querySelectorAll('.node').forEach(n=>n.classList.toggle('on', n.id==='nd-'+id));
  document.querySelectorAll('.fStep').forEach(n=>n.classList.toggle('on', n.dataset.node===id));
  const n = D.nodes.find(n=>n.id===id);
  details.hidden = false;
  details.style.setProperty('--nc', n.color);
  details.innerHTML = D.details[id];
  details.querySelector('.dClose').onclick = close;
  markSql(n.span);
  const fs = document.querySelector('.fStep[data-node="'+CSS.escape(id)+'"]');
  if(fs) fs.scrollIntoView({block:'nearest'});
}
function close(){
  active=null; details.hidden=true; details.innerHTML='';
  document.querySelectorAll('.node.on,.fStep.on').forEach(n=>n.classList.remove('on'));
  markSql(null);
}
document.querySelectorAll('.node').forEach(el=>{
  el.addEventListener('click', ()=>select(el.dataset.id));
});
document.querySelectorAll('.fStep').forEach(el=>{
  el.addEventListener('click', ()=>{
    const id = el.dataset.node;
    select(id);
    const n = D.nodes.find(n=>n.id===id);
    if(n && window.innerWidth>860){
      const r = flow.getBoundingClientRect();
      view.x = r.width/2 - n.x*view.k - 180;
      view.y = r.height/2 - (n.y + n.h/2)*view.k;
      apply();
    }
  });
});
document.addEventListener('keydown', e=>{ if(e.key==='Escape') close(); });

/* ── 6. tabs + mobile nav ── */
document.querySelectorAll('.tab').forEach(t=>{
  t.onclick = ()=>{
    document.querySelectorAll('.tab').forEach(o=>o.setAttribute('aria-selected', o===t));
    document.querySelectorAll('.tabBody').forEach(b=>{ b.hidden = b.id !== 'tb-'+t.dataset.tab; });
  };
});
document.querySelectorAll('.mnav button').forEach(b=>{
  b.onclick = ()=>{
    document.querySelectorAll('.mnav button').forEach(o=>o.classList.toggle('on', o===b));
    if(b.dataset.view==='diagram'){ root.dataset.view='diagram'; requestAnimationFrame(redraw); }
    else{
      root.dataset.view='panel';
      const tab = document.querySelector('.tab[data-tab="'+b.dataset.view+'"]');
      if(tab) tab.click();
    }
  };
});

/* ── boot ── */
function redraw(){ place(); groups(); edges(); fit(true); }
redraw();
if(document.fonts && document.fonts.ready){ document.fonts.ready.then(redraw); }
let rt; window.addEventListener('resize', ()=>{ clearTimeout(rt); rt=setTimeout(redraw,150); });
})();
"""


# ─────────────────────────── render ───────────────────────────
def kind_color(kind):
    return COLORS.get(kind, DEFAULT_COLOR)


def find_span(sql, node):
    if isinstance(node.get("span"), (list, tuple)) and len(node["span"]) == 2:
        return [int(node["span"][0]), int(node["span"][1])]
    frag = node.get("sql_span")
    if not frag or not sql:
        return None
    pat = r"\s+".join(re.escape(p) for p in frag.split())
    m = re.search(pat, sql, re.I)
    return [m.start(), m.end()] if m else None


def delta_chip(prev, cur, ui):
    p, c = as_number(prev), as_number(cur)
    if p is None or c is None:
        return f'<span class="dlt eq">{escape(ui["unknown"])}</span>'
    if p == c:
        return '<span class="dlt eq">=</span>'
    diff = c - p
    pct = (diff / p * 100) if p else 0
    cls = "up" if diff > 0 else "dn"
    sign = "+" if diff > 0 else "−"
    if p and abs(pct) < 1000:
        return f'<span class="dlt {cls}">{sign}{abs(pct):.1f}% · {sign}{compact(abs(diff))}</span>'
    fac = (c / p) if p else 0
    return f'<span class="dlt {cls}">×{fac:.2f} · {sign}{compact(abs(diff))}</span>'


def render(spec):
    lang = resolve_lang(spec.get("lang"))
    ui = UI_ID if lang == "id" else UI_EN
    ency = ENCY_ID if lang == "id" else ENCY_EN
    dialect = (spec.get("dialect") or "generic").lower()
    docs_label, docs_map = DOCS.get(dialect, DOCS["generic"])
    if lang == "id":
        docs_label = "Dokumentasi " + docs_label.replace(" Docs", "")
    dlabel = DIALECT_LABEL.get(dialect, "SQL")
    sql = spec.get("sql", "") or ""
    nodes = spec.get("nodes", [])

    # A row count is a claim about the reader's data. When the query arrived
    # with no way to look anything up, there is nothing to claim — so
    # grounding "none" strips the numbers rather than trusting every caller to
    # leave them out. The map still teaches; it just stops pretending to count.
    if str(spec.get("grounding", "")).lower() == "none":
        stripped = sum(1 for n in nodes if n.get("rows_in") is not None or n.get("rows_out") is not None)
        if stripped or spec.get("funnel"):
            print(f"warning: grounding is \"none\", so the row funnel and the row counts on "
                  f"{stripped} node(s) were dropped. Numbers belong on the page only when they come "
                  f"from a measurement, a catalog statistic, or a figure the user gave you.",
                  file=sys.stderr)
        for n in nodes:
            n.pop("rows_in", None)
            n.pop("rows_out", None)
        spec = dict(spec, funnel=[])
    edges = spec.get("edges", [])
    groups = spec.get("groups", [])
    by_id = {n["id"]: n for n in nodes}

    for e in edges:
        for side in ("from", "to"):
            if e[side] not in by_id:
                raise SystemExit(f"spec error: edge {e['from']}→{e['to']} references unknown node '{e[side]}'")

    layouts = {}
    for d in ("TB", "LR"):
        pos, dummies, routes, extent, nranks = layout(nodes, edges, d)
        layouts[d] = {"nodes": {k: {"cross": round(v["cross"], 1), "rank": v["rank"],
                                    "size": round(v["size"], 1)} for k, v in pos.items()},
                      "dummies": {k: {"cross": round(v["cross"], 1), "rank": v["rank"]}
                                  for k, v in dummies.items()},
                      "via": routes, "extent": round(extent, 1), "ranks": nranks}

    # A cluster box is drawn around its members; anything else inside that
    # rectangle gets sliced by the border. The layout evicts such nodes, but
    # if a group is scattered across the diagram it can run out of room —
    # worth knowing about rather than shipping a broken-looking box.
    warned = set()
    for d in ("TB", "LR"):
        pos = layouts[d]["nodes"]
        boxes = {}
        for n in nodes:
            g = n.get("group")
            if not g:
                continue
            p = pos[n["id"]]
            c0, c1, r = p["cross"] - p["size"] / 2, p["cross"] + p["size"] / 2, p["rank"]
            o = boxes.get(g)
            boxes[g] = [min(o[0], c0), max(o[1], c1), min(o[2], r), max(o[3], r)] if o else [c0, c1, r, r]
        for g, (c0, c1, r0, r1) in boxes.items():
            for n in nodes:
                if n.get("group") == g or (n["id"], g) in warned:
                    continue
                p = pos[n["id"]]
                half = p["size"] / 2
                if r0 <= p["rank"] <= r1 and p["cross"] + half > c0 - GROUP_PAD and p["cross"] - half < c1 + GROUP_PAD:
                    warned.add((n["id"], g))
                    print(f"warning: node '{n['id']}' sits inside the '{g}' cluster box without belonging to it. "
                          f"Either add \"group\": \"{g}\" to it (a source feeding only that block usually belongs "
                          f"in it) or drop the group.", file=sys.stderr)

    gwidth, nranks = layouts["TB"]["extent"], layouts["TB"]["ranks"]

    # ── node cards ──
    cards = []
    payload_nodes = []
    detail_html = {}
    for n in nodes:
        nid = n["id"]
        kind = n.get("kind", "operation")
        color = kind_color(kind)
        ri, ro = n.get("rows_in"), n.get("rows_out")
        foot = ""
        bits = []
        if ri is not None or ro is not None:
            if ri is not None and ro is not None:
                bits.append(f'{compact(ri)} <span style="color:var(--tx-3)">→</span> <b>{compact(ro)}</b>')
                bits.append(delta_chip(ri, ro, ui))
            elif ro is not None:
                bits.append(f'<b>{compact(ro)}</b>')
        for b in n.get("badges", []) or []:
            bits.append(f'<span class="nTag">{escape(str(b))}</span>')
        if bits:
            foot = f'<div class="nFoot">{"".join(bits)}</div>'
        cards.append(
            f'<div class="node" id="nd-{escape(nid)}" data-id="{escape(nid)}" '
            f'style="--nc:{color}">'
            f'<div class="nHead">{icon(ICON_FOR_KIND.get(kind, "cog"))}'
            f'<span class="nLabel" title="{escape(n.get("label", ""))}">{escape(n.get("label", ""))}</span></div>'
            f'<p class="nBody">{escape(n.get("plain", ""))}</p>{foot}</div>'
        )
        payload_nodes.append({"id": nid, "color": color,
                              "group": n.get("group"), "span": find_span(sql, n)})

        # ── details panel markup ──
        title, definition = ency.get(kind, ency["operation"])
        if n.get("title"):
            title = n["title"]
        url = docs_map.get(kind, docs_map["_"])
        sec = [
            f'<div class="dHead"><h3 class="dTitle">{icon(ICON_FOR_KIND.get(kind, "cog"), 20)}'
            f'<span>{escape(title)}</span></h3>'
            f'<button class="dClose" aria-label="{escape(ui["close"])}">{icon("x", 20)}</button></div>',
            f'<pre class="dSql">{escape(n.get("label", ""))}</pre>',
            f'<section class="dSec"><h4>{escape(ui["definition"])}</h4><p>{escape(definition)}</p>'
            f'<a class="dLink" href="{url}" target="_blank" rel="noopener noreferrer">{docs_label} {icon("external-link", 15)}</a></section>',
            f'<section class="dSec"><h4>{escape(ui["inquery"])}</h4>'
            f'<p>{md_inline(n.get("detail") or n.get("plain", ""))}</p></section>',
        ]
        if ri is not None or ro is not None or n.get("delta_note"):
            rowline = ""
            if ri is not None and ro is not None:
                rowline = (f'<div class="dRows"><span>{num(ri)}</span><span style="color:var(--tx-3)">→</span>'
                           f'<span><b>{num(ro)}</b></span>{delta_chip(ri, ro, ui)}</div>')
            elif ro is not None:
                rowline = f'<div class="dRows"><b>{num(ro)}</b></div>'
            sec.append(f'<section class="dSec"><h4>{escape(ui["rows"])}</h4>{rowline}'
                       f'<p style="margin-top:.7rem">{md_inline(n.get("delta_note", ""))}</p></section>')
        if n.get("columns"):
            chips = "".join(f'<span>{escape(str(c))}</span>' for c in n["columns"])
            sec.append(f'<section class="dSec"><h4>{escape(ui["columns"])}</h4><div class="dCols">{chips}</div></section>')
        detail_html[nid] = "".join(sec)

    # ── edges payload ──
    payload_edges = []
    for e in edges:
        ek = e.get("kind") or by_id[e["to"]].get("kind", "operation")
        payload_edges.append({"from": e["from"], "to": e["to"], "key": f'{e["from"]}>{e["to"]}',
                              "color": kind_color(ek), "recursive": bool(e.get("recursive"))})

    # ── funnel ──
    funnel = spec.get("funnel") or []
    steps = []
    vals = [as_number(f.get("rows")) for f in funnel]
    mx = max([v for v in vals if v is not None] or [1])
    prev = None
    for i, f in enumerate(funnel):
        nid = f.get("node")
        n = by_id.get(nid, {})
        kind = n.get("kind", f.get("kind", "operation"))
        color = kind_color(kind)
        v = as_number(f.get("rows"))
        # a funnel that runs from 400M to 20 rows is unreadable on a linear
        # scale — every stage after the first collapses to a sliver — so the
        # bar length is logarithmic while the printed number stays exact.
        if v is not None and mx:
            import math
            pct_w = max(math.log10(max(v, 1) + 1) / math.log10(mx + 1), 0.02) * 100
        else:
            pct_w = 100
        barcls = "fBar" if v is not None else "fBar q"
        bar = f'<div class="{barcls}"><i style="width:{pct_w:.2f}%"></i></div>'
        numcls = "fNum" if v is not None else "fNum q"
        shown = num(f.get("rows")) if f.get("rows") is not None else "?"
        chip = delta_chip(prev, f.get("rows"), ui) if i else f'<span class="dlt eq">{escape(ui["start"])}</span>'
        kept = ""
        first_v = next((x for x in vals if x is not None), None)
        if v is not None and first_v:
            kept = f'<span class="fKept">{v / first_v * 100:.2f}% {escape(ui["ofinput"])}</span>'
        steps.append(
            f'<li class="fStep" data-node="{escape(str(nid))}" style="--nc:{color}">'
            f'<div class="fHead">{icon(ICON_FOR_KIND.get(kind, "cog"), 14)}'
            f'<span class="fName">{escape(f.get("stage") or n.get("label", ""))}</span>'
            f'<span class="{numcls}">{escape(str(shown))}</span></div>{bar}'
            f'<div class="fMeta">{chip}{kept}</div>'
            f'<p class="fWhy">{md_inline(f.get("why", ""))}</p></li>')
        if v is not None:
            prev = f.get("rows")
    if funnel:
        firstv = next((v for v in vals if v is not None), None)
        lastv = next((v for v in reversed(vals) if v is not None), None)
        ratio = ""
        if firstv and lastv is not None and firstv:
            share = lastv / firstv
            if share > 1:
                ratio = f'×{share:.2f}'
            elif share >= 0.0001:
                ratio = f'{escape(ui["kept"])} {share * 100:.3g}%'
            elif lastv:
                ratio = f'1 {escape(ui["of"])} {compact(firstv / lastv)}'
            else:
                ratio = f'{escape(ui["kept"])} 0'
        ftop = (f'<div class="fTop"><div class="fTopRow">'
                f'<span class="fBig">{compact(funnel[0].get("rows"))}</span>'
                f'<span class="fArrow">→</span>'
                f'<span class="fBig" style="color:var(--cy)">{compact(funnel[-1].get("rows"))}</span>'
                f'<span class="chip">{ratio}</span></div>'
                f'<p class="fNote">{escape(ui["grounded"].get(spec.get("grounding", "estimate"), ""))} · {escape(ui["logscale"])}</p></div>')
        funnel_html = ftop + f'<ol class="funnel">{"".join(steps)}</ol>'
    else:
        funnel_html = ""
    has_funnel = bool(funnel)

    # ── brief ──
    kinds_present = []
    for n in nodes:
        k = n.get("kind", "operation")
        if k not in kinds_present:
            kinds_present.append(k)
    legend = "".join(
        f'<span class="lg" style="--nc:{kind_color(k)}">{icon(ICON_FOR_KIND.get(k, "cog"), 12)}{escape(k)}</span>'
        for k in kinds_present)
    notes = spec.get("notes") or []
    notes_html = ""
    if notes:
        notes_html = (f'<h3>{escape(ui["notes"])}</h3><ul>'
                      + "".join(f"<li>{md_inline(x)}</li>" for x in notes) + "</ul>")
    nofunnel_html = "" if has_funnel else f'<p class="fNote" style="margin:0 0 1rem">{escape(ui["nofunnel"])}</p>'
    brief = (f'<div class="brief"><h3>{escape(ui["summary"])}</h3>'
             f'<p>{md_inline(spec.get("summary", ""))}</p>{nofunnel_html}{notes_html}'
             f'<h3>{escape(ui["legend"])}</h3><div class="legend">{legend}</div></div>')

    # ── printable document (hidden on screen, laid out by the print stylesheet) ──
    order = sorted(nodes, key=lambda n: (layouts["TB"]["nodes"][n["id"]]["rank"],
                                         layouts["TB"]["nodes"][n["id"]]["cross"]))
    steps_html = []
    for n in order:
        kind = n.get("kind", "operation")
        rows = ""
        ri, ro = n.get("rows_in"), n.get("rows_out")
        if ri is not None and ro is not None:
            rows = f'<p class="stepR">{num(ri)} → {num(ro)}</p>'
        elif ro is not None:
            rows = f'<p class="stepR">{num(ro)}</p>'
        detail = n.get("detail") or ""
        det_html = '<p class="stepD">' + md_inline(detail) + '</p>' if detail else ""
        steps_html.append(
            f'<div class="step" style="--nc:{kind_color(kind)}">'
            f'<div class="stepH">{escape(n.get("label", ""))}</div>'
            f'<p class="stepP">{escape(n.get("plain", ""))}</p>'
            f'{det_html}{rows}</div>')

    doc_funnel = ""
    if has_funnel:
        rows_html = []
        prev = None
        for i, f in enumerate(funnel):
            nn = by_id.get(f.get("node"), {})
            chip = delta_chip(prev, f.get("rows"), ui) if i else ""
            chip = re.sub(r"<[^>]+>", "", chip)
            shown = num(f.get("rows")) if f.get("rows") is not None else "—"
            rows_html.append(
                f'<tr><td>{escape(f.get("stage") or nn.get("label", ""))}</td>'
                f'<td class="n">{escape(str(shown))}</td><td class="n">{escape(chip)}</td>'
                f'<td>{md_inline(f.get("why", ""))}</td></tr>')
            if as_number(f.get("rows")) is not None:
                prev = f.get("rows")
        doc_funnel = (f'<h2>{escape(ui["funnel"])}</h2>'
                      f'<table><thead><tr><th>{escape(ui["stage"])}</th><th class="n">{escape(ui["rowsout"])}</th>'
                      f'<th class="n">{escape(ui["change"])}</th><th>{escape(ui["why"])}</th></tr></thead>'
                      f'<tbody>{"".join(rows_html)}</tbody></table>')

    doc_notes = ""
    if notes:
        doc_notes = (f'<h2>{escape(ui["notes"])}</h2><ul>'
                     + "".join(f"<li>{md_inline(x)}</li>" for x in notes) + "</ul>")
    grounding_line = ui["grounded"].get(str(spec.get("grounding", "")).lower(), "")
    nofunnel_doc = "" if has_funnel else f'<p>{escape(ui["nofunnel"])}</p>'
    doc = (f'<article class="doc"><h1>{escape(spec.get("title") or "SQL Logic Map")}</h1>'
           f'<p class="docSub">{escape(ui["docof"])} · {escape(dlabel)}'
           f'{" · " + escape(grounding_line) if grounding_line else ""}</p>'
           f'<h2>{escape(ui["summary"])}</h2><p>{md_inline(spec.get("summary", ""))}</p>'
           f'{nofunnel_doc}'
           f'{doc_funnel}'
           f'<h2>{escape(ui["steps"])}</h2>{"".join(steps_html)}'
           f'{doc_notes}'
           f'<h2 class="docBreak">{escape(ui["sql"])}</h2><pre>{escape(sql)}</pre></article>')

    payload = {"nodes": payload_nodes, "edges": payload_edges, "layouts": layouts,
               "groups": groups, "details": detail_html, "rankSep": RANK_SEP,
               "groupPad": GROUP_PAD, "nodeW": NODE_W, "crossSepLR": CROSS_SEP_LR,
               "iconTB": icon("chevrons-down", 14), "iconLR": icon("chevrons-right", 14),
               "labelTB": ui["dirTB"], "labelLR": ui["dirLR"],
               "dir": "LR" if str(spec.get("direction", "TB")).upper() == "LR" else "TB"}

    title = spec.get("title") or "SQL Logic Map"
    head = (f'<div class="paneHead"><h1 class="brand">actually<b>explain</b></h1>'
            f'<span class="sub">{escape(dlabel)} · {escape(title)}</span></div>')
    funnel_tab = (f'<button class="tab" data-tab="funnel" aria-selected="false">{escape(ui["funnel"])}</button>'
                  if has_funnel else "")
    tabs = (f'<nav class="tabs" role="tablist">'
            f'<button class="tab" data-tab="sql" aria-selected="true">{escape(ui["sql"])}</button>'
            f'{funnel_tab}'
            f'<button class="tab" data-tab="brief" aria-selected="false">{escape(ui["brief"])}</button></nav>')

    html_out = f"""<title>{escape(title)}</title>
<style>{CSS}</style>
<div class="ae" id="aeRoot" data-view="panel">
  <aside class="pane">
    {head}
    {tabs}
    <div class="tabBody" id="tb-sql"><pre class="sql" id="aeSql">{highlight_sql(sql)}</pre></div>
    {f'<div class="tabBody" id="tb-funnel" hidden>{funnel_html}</div>' if has_funnel else ''}
    <div class="tabBody" id="tb-brief" hidden>{brief}</div>
  </aside>
  <main class="flow" id="aeFlow">
    <div class="canvas" id="aeCanvas">
      <svg class="edges" id="aeEdges"></svg>
      {''.join(cards)}
    </div>
    <div class="ctrls">
      <button id="aeIn" title="{escape(ui['zin'])}" aria-label="{escape(ui['zin'])}">{icon('plus', 14)}</button>
      <button id="aeOut" title="{escape(ui['zout'])}" aria-label="{escape(ui['zout'])}">{icon('minus', 14)}</button>
      <button id="aeDir"></button>
      <button id="aePrint" title="{escape(ui['print'])}" aria-label="{escape(ui['print'])}">{icon('printer', 14)}</button>
      <button id="aeFit" title="{escape(ui['fit'])}" aria-label="{escape(ui['fit'])}">{icon('maximize', 14)}</button>
    </div>
    <p class="hint">{escape(ui['hint'])}</p>
  </main>
  <aside class="details" id="aeDetails" hidden></aside>
  <nav class="mnav">
    <button data-view="sql" class="on">{icon('code', 18)}<span>{escape(ui['sql'])}</span></button>
    <button data-view="diagram">{icon('workflow', 18)}<span>{escape(ui['diagram'])}</span></button>
    {f"<button data-view='funnel'>{icon('funnel', 18)}<span>{escape(ui['funnel'])}</span></button>" if has_funnel else ''}
  </nav>
</div>
{doc}
<script>window.__AE__ = {json.dumps(payload)};</script>
<script>{JS}</script>
"""
    return html_out, {"nodes": len(nodes), "edges": len(edges), "ranks": nranks,
                      "width": int(gwidth), "funnel": len(funnel)}


def main():
    ap = argparse.ArgumentParser(description="Render an actually-explain-query spec into a self-contained HTML page.")
    ap.add_argument("spec", help="path to the spec JSON")
    ap.add_argument("-o", "--out", default="query_map.html")
    ap.add_argument("--validate-only", action="store_true")
    ap.add_argument("--standalone", action="store_true",
                    help="wrap the output in a full HTML document so it can be opened as a local file; "
                         "omit when publishing as an artifact, which supplies its own document shell")
    a = ap.parse_args()
    spec = json.load(open(a.spec, encoding="utf-8"))
    missing = [k for k in ("nodes", "edges") if k not in spec]
    if missing:
        raise SystemExit(f"spec error: missing key(s) {missing}")
    if not spec.get("sql"):
        print("warning: spec has no 'sql' — the code pane will be empty", file=sys.stderr)
    # Language sanity: the page's own labels follow spec["lang"], so a spec
    # written in Indonesian with lang left at the default renders a bilingual
    # mess. Cheap to detect, easy to forget.
    prose = " ".join(str(n.get("plain", "")) + " " + str(n.get("detail", "")) for n in spec["nodes"])
    prose += " " + str(spec.get("summary", ""))
    words = re.findall(r"[a-z]+", prose.lower())
    id_hits = sum(w in {"yang", "dan", "ini", "tidak", "dari", "untuk", "baris", "dengan",
                        "karena", "hanya", "jumlah", "kueri", "tiap", "menjadi"} for w in words)
    en_hits = sum(w in {"the", "and", "this", "rows", "from", "with", "because", "only",
                        "each", "query", "into", "every"} for w in words)
    lang = resolve_lang(spec.get("lang"))
    if words:
        if lang == "en" and id_hits > en_hits * 2 and id_hits > 5:
            print('warning: the explanations look like Indonesian but "lang" is not set to "id" — '
                  'the page labels, definitions and funnel headings will render in English.', file=sys.stderr)
        elif lang == "id" and en_hits > id_hits * 2 and en_hits > 5:
            print('warning: "lang" is "id" but the explanations look like English — '
                  'write every sentence in the language you set.', file=sys.stderr)

    unknown = sorted({n.get("kind", "operation") for n in spec["nodes"]} - set(COLORS))
    if unknown:
        print(f"warning: unknown node kind(s) {unknown} — rendered with the default colour. "
              f"Use a kind from references/spec-schema.md.", file=sys.stderr)
    html_out, stats = render(spec)
    if a.validate_only:
        print(json.dumps(stats))
        return
    if a.standalone:
        html_out = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
                    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
                    + html_out + "\n</head></html>")
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"wrote {a.out}  ({stats['nodes']} nodes, {stats['edges']} edges, "
          f"{stats['ranks']} levels, {stats['funnel']} funnel stages, {len(html_out) // 1024} KB)")


if __name__ == "__main__":
    main()
