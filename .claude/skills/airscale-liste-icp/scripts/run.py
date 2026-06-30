#!/usr/bin/env python3
"""Liste de prospects ICP : genere une liste de cibles via Airscale /find-people.

1) /find-people/count -> volume (gratuit)
2) /find-people -> leads matchant l'ICP
Ecrit un CSV.

Usage:
    python scripts/run.py --config config.yaml [--out chemin.csv]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from lib.airscale_helpers import (  # noqa: E402
    count_people,
    load_config,
    post,
    unwrap,
    write_csv,
)

DEFAULT_OUT = ROOT / "examples" / "liste-icp.csv"
COLS = ["firstname", "lastname", "jobTitle", "companyName",
        "companySize", "companyIndustry", "profileUrl"]


def build_query(cfg: dict) -> dict:
    query: dict = {}
    titles = cfg.get("job_titles") or []
    excl = cfg.get("exclude_titles") or []
    if titles or excl:
        query["JobTitle"] = {}
        if titles:
            query["JobTitle"]["include"] = titles
        if excl:
            query["JobTitle"]["exclude"] = excl
    locations = cfg.get("locations") or []
    if locations:
        query["location"] = {"include": locations}
    keywords = cfg.get("keywords") or []
    if keywords:
        query["keyword"] = {"include": keywords}
    return query


def main() -> None:
    ap = argparse.ArgumentParser(description="Liste ICP Airscale")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    query = build_query(cfg)
    if not query:
        sys.exit("config: renseigne au moins job_titles, locations ou keywords.")
    size = int(cfg.get("size", 10))

    print("[count] preflight gratuit /find-people/count", file=sys.stderr)
    total = count_people(query)
    if total is not None:
        print(f"[count] {total} personnes correspondent. Recuperation de {size}.", file=sys.stderr)

    print("[search] /find-people", file=sys.stderr)
    resp = post("find-people", {"query": query, "size": size})
    leads = resp.get("leads") or unwrap(resp).get("leads") or []
    if not leads:
        sys.exit("Aucun lead retourne. Elargis les filtres.")

    rows = []
    for ld in leads:
        rows.append({c: ld.get(c, "") for c in COLS})

    dest = Path(args.out or cfg.get("output_path") or DEFAULT_OUT)
    path = write_csv(rows, COLS, dest)
    print(f"[ok] {len(rows)} cibles -> {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
