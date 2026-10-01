"""Pull phones and countryside events out of paper text. Stdlib only."""

from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "brevladan.sqlite"

PHONE = re.compile(r"\b0\d{1,3}[\s-]?\d{2,3}[\s-]?\d{2}[\s-]?\d{2}\b")
EVENT_LINE = re.compile(
    r"(?P<what>.{8,80})\s+(?P<when>måndag|tisdag|onsdag|torsdag|fredag|lördag|söndag|\d{1,2}/\d{1,2})",
    re.IGNORECASE,
)


def connect() -> sqlite3.Connection:
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.executescript(
        """
        create table if not exists events (
          id integer primary key,
          paper text, kommun text, when_ text, what text, source text
        );
        create table if not exists phones (
          id integer primary key,
          paper text, name text, number text, context text, source text
        );
        """
    )
    return con


def extract(text: str, paper: str, kommun: str, source: str) -> dict:
    con = connect()
    phones, events = [], []
    for m in PHONE.finditer(text):
        start = max(0, m.start() - 40)
        ctx = " ".join(text[start:m.end() + 20].split())
        number = m.group(0)
        name = ctx.split(number)[0].strip(" ,.-" )[-40:]
        phones.append((paper, name, number, ctx, source))
        con.execute(
            "insert into phones(paper, name, number, context, source) values (?,?,?,?,?)",
            phones[-1],
        )
    for line in text.splitlines():
        em = EVENT_LINE.search(line)
        if em:
            row = (paper, kommun, em.group("when"), em.group("what").strip(), source)
            events.append(row)
            con.execute(
                "insert into events(paper, kommun, when_, what, source) values (?,?,?,?,?)",
                row,
            )
    con.commit()
    con.close()
    return {"phones": len(phones), "events": len(events), "db": str(DB)}


def demo() -> None:
    sample = (ROOT / "fixtures" / "veckovis-tanum.txt").read_text()
    print(extract(sample, "veckovis", "Tanum", "fixtures/veckovis-tanum.txt"))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--demo", action="store_true")
    args = p.parse_args()
    if args.demo:
        demo()
