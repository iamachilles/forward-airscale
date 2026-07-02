#!/usr/bin/env python3
"""Pipeline outbound Airscale : sourcing ICP + waterfall coordonnees en un job.

1) /find-people/count -> volume (gratuit)
2) /find-people -> leads matchant l'ICP
3) pour chaque lead, waterfall sur les `channels` demandes via son profileUrl :
   /email, /phone, /personal-email
Ecrit un CSV pret a sequencer :
firstname, lastname, jobTitle, companyName, profileUrl, email, phone, personal_email.

Usage:
    python scripts/run.py --config config.yaml [--out chemin.csv]
"""
from __future__ import annotations

import argparse
import sys
import time
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

DEFAULT_OUT = ROOT / "examples" / "pipeline-outbound.csv"
BASE_COLS = ["firstname", "lastname", "jobTitle", "companyName", "profileUrl"]
CHANNEL_COLS = ["email", "phone", "personal_email"]
COLS = BASE_COLS + CHANNEL_COLS


def build_query(cfg: dict) -> dict:
    """Construit le `query` /find-people a partir des filtres ICP de la config."""
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


def fetch_channel(channel: str, li: str) -> str:
    """Retourne la valeur du canal pour une URL LinkedIn, '' si echec.

    Un canal qui echoue ne casse pas le batch (try/except par appel).
    """
    try:
        if channel == "email":
            return unwrap(post("email", {"linkedin_profile_url": li})).get("email", "")
        if channel == "personal_email":
            return unwrap(post("personal-email", {"linkedin_profile_url": li})).get("email", "")
        if channel == "phone":
            r = unwrap(post("phone", {"linkedin_profile_url": li}))
            return r.get("phone_numbers", r.get("phone", ""))
    except Exception as e:
        print(f"  ! {channel} echoue : {e}", file=sys.stderr)
    return ""


def main() -> None:
    ap = argparse.ArgumentParser(description="Pipeline outbound Airscale")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    query = build_query(cfg)
    if not query:
        sys.exit("config: renseigne au moins job_titles, locations ou keywords.")
    size = int(cfg.get("size", 10))
    channels = cfg.get("channels") or CHANNEL_COLS

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
        row = {c: ld.get(c, "") for c in BASE_COLS}
        for c in CHANNEL_COLS:
            row[c] = ""
        li = (ld.get("profileUrl") or "").strip()
        if not li:
            print("  ! lead sans profileUrl, coordonnees ignorees", file=sys.stderr)
            rows.append(row)
            continue
        print(f"[waterfall] {li}", file=sys.stderr)
        for ch in channels:
            if ch in CHANNEL_COLS:
                row[ch] = fetch_channel(ch, li)
                time.sleep(0.2)
        rows.append(row)

    dest = Path(args.out or cfg.get("output_path") or DEFAULT_OUT)
    path = write_csv(rows, COLS, dest)
    print(f"[ok] {len(rows)} leads prets a sequencer -> {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
