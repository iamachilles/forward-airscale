#!/usr/bin/env python3
"""Mobiles pour cold calling via Airscale /phone.

Pour chaque URL LinkedIn du CSV : /phone -> numero de mobile.
Ecrit le CSV d'origine + phone, provider.

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

DEFAULT_OUT = ROOT / "examples" / "telephones.csv"
ENRICH = ["phone", "provider"]


def main() -> None:
    ap = argparse.ArgumentParser(description="Enrichissement telephone Airscale")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    li_col = cfg.get("linkedin_column", "linkedin_url")
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
        if not li:
            print(f"  ! ligne sans URL LinkedIn (colonne {li_col})", file=sys.stderr)
            for k in ENRICH:
                enriched[k] = ""
            out_rows.append(enriched)
            continue
        print(f"[phone] {li}", file=sys.stderr)
        try:
            resp = unwrap(post("phone", {"linkedin_profile_url": li}))
        except Exception as e:
            print(f"  ! echec : {e}", file=sys.stderr)
            resp = {}
        enriched["phone"] = resp.get("phone_numbers", resp.get("phone", ""))
        enriched["provider"] = resp.get("provider", "")
        out_rows.append(enriched)
        time.sleep(0.2)

    out_cols = list(in_cols) + [c for c in ENRICH if c not in in_cols]
    dest = Path(args.out or cfg.get("output_path") or DEFAULT_OUT)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_cols)
        w.writeheader()
        w.writerows(out_rows)
    found = sum(1 for r in out_rows if r.get("phone"))
    print(f"[ok] {found}/{len(out_rows)} mobiles -> {dest}", file=sys.stderr)


if __name__ == "__main__":
    main()
