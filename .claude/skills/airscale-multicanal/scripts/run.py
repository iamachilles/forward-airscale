#!/usr/bin/env python3
"""Coordonnees multicanal via Airscale : email pro + email perso + mobile.

Pour chaque URL LinkedIn du CSV, appelle les endpoints des `channels` demandes :
/email, /personal-email, /phone. Ecrit le CSV d'origine + email, personal_email, phone.

Usage:
    python scripts/run.py --config config.yaml [--out chemin.csv]
"""
from __future__ import annotations

import argparse
import csv
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from lib.airscale_helpers import load_config, post, unwrap  # noqa: E402

DEFAULT_OUT = ROOT / "examples" / "multicanal.csv"
ENRICH = ["email", "personal_email", "phone"]


def fetch_channel(channel: str, li: str) -> str:
    """Retourne la valeur du canal pour une URL LinkedIn, '' si echec."""
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
    ap = argparse.ArgumentParser(description="Coordonnees multicanal Airscale")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    li_col = cfg.get("linkedin_column", "linkedin_url")
    channels = cfg.get("channels") or ENRICH
    input_csv = Path(cfg.get("input_csv") or "")
    if not input_csv.is_absolute():
        cand = Path(args.config).resolve().parent / input_csv
        input_csv = cand if cand.exists() else ROOT / input_csv
    if not input_csv.exists():
        sys.exit(f"input_csv introuvable : {input_csv}")

    with open(input_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        in_rows = list(reader)
        in_cols = reader.fieldnames or []
    if not in_rows:
        sys.exit("CSV d'entree vide.")

    out_rows = []
    for row in in_rows:
        enriched = dict(row)
        li = (row.get(li_col) or "").strip()
        for ch in ENRICH:
            enriched[ch] = ""
        if not li:
            print(f"  ! ligne sans URL LinkedIn (colonne {li_col})", file=sys.stderr)
            out_rows.append(enriched)
            continue
        print(f"[multicanal] {li}", file=sys.stderr)
        for ch in channels:
            if ch in ENRICH:
                enriched[ch] = fetch_channel(ch, li)
                time.sleep(0.2)
        out_rows.append(enriched)

    out_cols = list(in_cols) + [c for c in ENRICH if c not in in_cols]
    dest = Path(args.out or cfg.get("output_path") or DEFAULT_OUT)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_cols)
        w.writeheader()
        w.writerows(out_rows)
    print(f"[ok] {len(out_rows)} contacts -> {dest}", file=sys.stderr)


if __name__ == "__main__":
    main()
