#!/usr/bin/env python3
"""Les décideurs de tes comptes cibles via Airscale /find-people.

Pour chaque domaine du CSV : /find-people (companyDomain + JobTitle) -> décideurs.
Écrit un CSV : domaine + contacts.

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
from lib.airscale_helpers import load_config, post, unwrap, write_csv  # noqa: E402

DEFAULT_OUT = ROOT / "examples" / "decideurs-comptes.csv"
COLS = ["domain", "firstname", "lastname", "jobTitle", "companyName", "profileUrl"]


def main() -> None:
    ap = argparse.ArgumentParser(description="Décideurs des comptes cibles Airscale")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    dom_col = cfg.get("domain_column", "domain")
    titles = cfg.get("job_titles") or ["Head", "VP", "Chief", "Director", "CEO", "Founder"]
    per_company = int(cfg.get("per_company", 3))

    input_csv = Path(cfg.get("input_csv") or "")
    if not input_csv.is_absolute():
        cand = Path(args.config).resolve().parent / input_csv
        input_csv = cand if cand.exists() else ROOT / input_csv
    if not input_csv.exists():
        sys.exit(f"input_csv introuvable : {input_csv}")

    with open(input_csv, newline="", encoding="utf-8") as f:
        domains = [(r.get(dom_col) or "").strip() for r in csv.DictReader(f)]
    domains = [d for d in domains if d]
    if not domains:
        sys.exit(f"Aucun domaine dans la colonne '{dom_col}'.")

    rows = []
    for dom in domains:
        print(f"[find-people] {dom}", file=sys.stderr)
        query = {
            "companyDomain": {"include": [dom]},
            "JobTitle": {"include": titles},
        }
        try:
            resp = post("find-people", {"query": query, "size": per_company})
        except Exception as e:  # un compte qui échoue ne casse pas le batch
            print(f"  ! échec : {e}", file=sys.stderr)
            resp = {}
        leads = resp.get("leads") or unwrap(resp).get("leads") or []
        if not leads:
            print(f"  (aucun décideur trouvé pour {dom})", file=sys.stderr)
        for ld in leads:
            rows.append({
                "domain": dom,
                "firstname": ld.get("firstname", ""),
                "lastname": ld.get("lastname", ""),
                "jobTitle": ld.get("jobTitle", ld.get("headline", "")),
                "companyName": ld.get("companyName", ""),
                "profileUrl": ld.get("profileUrl", ""),
            })
        time.sleep(0.2)

    dest = Path(args.out or cfg.get("output_path") or DEFAULT_OUT)
    path = write_csv(rows, COLS, dest)
    print(f"[ok] {len(rows)} décideurs sur {len(domains)} comptes -> {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
