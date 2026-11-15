"""Pull phones and countryside events out of paper text. Stdlib only."""

from __future__ import annotations

import argparse
import csv
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
        create table if not exists rows (
          id integer primary key,
          paper text, week text, date text, kommun text,
          page integer, page_hint text not null,
          kind text check (kind in ('business', 'event', 'notice')),
          name text, what text, when_ text,
          phone text, phone_status text, source text
        );
        """
    )
    return con


PHONE_SPLIT = re.compile(r"\s*[;,/]\s*")
PLUS46 = re.compile(r"\+46\s*(\(0\))?\s*")


def phones(cell: str) -> str:
    """Split a cell into numbers, +46 becomes 0, joined by '; '."""
    out = []
    for part in PHONE_SPLIT.split(cell.strip()):
        if part:
            out.append(PLUS46.sub("0", part))
    return "; ".join(out)


def load_tsv(path: Path) -> dict:
    """Load one paper-week of rows. Rows without page_hint are not loaded."""
    con = connect()
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    kept = [r for r in rows if r["page_hint"].strip()]
    for paper, week in {(r["paper"], r["week"]) for r in kept}:
        con.execute("delete from rows where paper = ? and week = ?", (paper, week))
    con.executemany(
        "insert into rows(paper, week, date, kommun, page, page_hint, kind, name,"
        " what, when_, phone, phone_status, source) values (?,?,?,?,?,?,?,?,?,?,?,?,?)",
        [
            (r["paper"], r["week"], r["date"], r["kommun"], int(r["page"]),
             r["page_hint"].strip(), r["kind"], r["name"], r["what"], r["when"],
             phones(r["phone"]), r["phone_status"], r["source"])
            for r in kept
        ],
    )
    con.commit()
    con.close()
    return {"loaded": len(kept), "skipped_no_page_hint": len(rows) - len(kept), "db": str(DB)}


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
    p.add_argument("--tsv", type=Path, help="load rows, e.g. data/veckovis-2026-v46.tsv")
    args = p.parse_args()
    if args.demo:
        demo()
    if args.tsv:
        print(load_tsv(args.tsv))
