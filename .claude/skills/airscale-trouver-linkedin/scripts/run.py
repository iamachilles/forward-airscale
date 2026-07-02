#!/usr/bin/env python3
"""Retrouver les URLs LinkedIn manquantes via Airscale /url-search-people.

Pour chaque ligne (prénom + nom + entreprise) : /url-search-people -> URL profil.
Écrit le CSV d'origine + linkedin_url.

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

DEFAULT_OUT = ROOT / "examples" / "trouver-linkedin.csv"


def main() -> None:
    ap = argparse.ArgumentParser(description="Recherche URL LinkedIn Airscale")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    fn_col = cfg.get("firstname_column", "first_name")
    ln_col = cfg.get("lastname_column", "last_name")
    co_col = cfg.get("company_column", "company")
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
        sys.exit("CSV d'entrée vide.")

    out_rows = []
    for row in in_rows:
        enriched = dict(row)
        fn = (row.get(fn_col) or "").strip()
        ln = (row.get(ln_col) or "").strip()
        co = (row.get(co_col) or "").strip()
        if not (fn and ln and co):
            print(f"  ! ligne incomplète (prénom/nom/entreprise requis)", file=sys.stderr)
            enriched["linkedin_url"] = ""
            out_rows.append(enriched)
            continue
        print(f"[url] {fn} {ln} @ {co}", file=sys.stderr)
        try:
            resp = unwrap(post("url-search-people", {
                "first_name": fn, "last_name": ln, "company_name": co,
            }))
        except Exception as e:
            print(f"  ! échec : {e}", file=sys.stderr)
            resp = {}
        enriched["linkedin_url"] = resp.get("url", "")
        out_rows.append(enriched)
        time.sleep(0.2)

    out_cols = list(in_cols) + (["linkedin_url"] if "linkedin_url" not in in_cols else [])
    dest = Path(args.out or cfg.get("output_path") or DEFAULT_OUT)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_cols)
        w.writeheader()
        w.writerows(out_rows)
    found = sum(1 for r in out_rows if r.get("linkedin_url"))
    print(f"[ok] {found}/{len(out_rows)} URLs -> {dest}", file=sys.stderr)


if __name__ == "__main__":
    main()
