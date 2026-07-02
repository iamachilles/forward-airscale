#!/usr/bin/env python3
"""Enrichir un fichier en emails pro vérifiés via Airscale /email.

Pour chaque ligne : /email (par URL LinkedIn, sinon prénom+nom+domaine).
Écrit le CSV d'origine + email, email_status, provider.

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

DEFAULT_OUT = ROOT / "examples" / "emails-fichier.csv"
ENRICH = ["email", "email_status", "provider"]


def build_body(row: dict, cfg: dict) -> dict | None:
    li = (row.get(cfg.get("linkedin_column", "linkedin_url")) or "").strip()
    if li:
        return {"linkedin_profile_url": li}
    fn = (row.get(cfg.get("firstname_column", "first_name")) or "").strip()
    ln = (row.get(cfg.get("lastname_column", "last_name")) or "").strip()
    dom = (row.get(cfg.get("domain_column", "domain")) or "").strip()
    if fn and ln and dom:
        return {"first_name": fn, "last_name": ln, "domain": dom}
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description="Enrichissement emails Airscale")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
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
        body = build_body(row, cfg)
        enriched = dict(row)
        if not body:
            print("  ! ligne ignorée (ni LinkedIn, ni nom+domaine)", file=sys.stderr)
            for k in ENRICH:
                enriched[k] = ""
            out_rows.append(enriched)
            continue
        label = body.get("linkedin_profile_url") or f"{body.get('first_name')} {body.get('last_name')}"
        print(f"[email] {label}", file=sys.stderr)
        try:
            resp = unwrap(post("email", body))
        except Exception as e:  # une ligne qui échoue ne casse pas le batch
            print(f"  ! échec : {e}", file=sys.stderr)
            resp = {}
        enriched["email"] = resp.get("email", "")
        enriched["email_status"] = resp.get("email_status", "")
        enriched["provider"] = resp.get("provider", "")
        out_rows.append(enriched)
        time.sleep(0.2)  # courtoisie rate limit

    out_cols = list(in_cols) + [c for c in ENRICH if c not in in_cols]
    dest = Path(args.out or cfg.get("output_path") or DEFAULT_OUT)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_cols)
        w.writeheader()
        w.writerows(out_rows)
    found = sum(1 for r in out_rows if r.get("email"))
    print(f"[ok] {found}/{len(out_rows)} emails -> {dest}", file=sys.stderr)


if __name__ == "__main__":
    main()
