"""Tiny read-only MCP-shaped tools. JSON on stdin, one call per line.

Not a full MCP transport. Weekend shape: three tools, SQLite only.
Wire to a real MCP SDK after the fixture feels right.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

DB = Path(__file__).resolve().parents[1] / "data" / "brevladan.sqlite"


def q(sql: str, params: tuple) -> list[dict]:
    if not DB.exists():
        return []
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = [dict(r) for r in con.execute(sql, params).fetchall()]
    con.close()
    return rows


def vad_hander(kommun: str, limit: int = 7) -> list[dict]:
    return q(
        "select when_, what, paper from events where kommun like ? order by id desc limit ?",
        (f"%{kommun}%", limit),
    )


def ring(namn: str) -> list[dict]:
    return q(
        "select name, number, context, paper from phones where name like ? or context like ? limit 5",
        (f"%{namn}%", f"%{namn}%"),
    )


def senaste(paper: str) -> list[dict]:
    return q(
        "select when_, what, kommun from events where paper = ? order by id desc limit 5",
        (paper,),
    )


TOOLS = {"vad_hander": vad_hander, "ring": ring, "senaste": senaste}


def main() -> None:
    for line in sys.stdin:
        call = json.loads(line)
        fn = TOOLS[call["tool"]]
        sys.stdout.write(json.dumps(fn(**call.get("args", {})), ensure_ascii=False) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
