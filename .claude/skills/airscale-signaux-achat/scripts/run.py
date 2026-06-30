#!/usr/bin/env python3
"""Comptes en signal d'achat : leads-finder filtre sur funding / croissance d'equipe.

1) /leads-finder/preview -> total estime (gratuit)
2) /leads-finder -> lignes (decideur + compte)
Compose une colonne `signal` et ecrit un CSV.

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
    load_config,
    post,
    preview_leads,
    unwrap,
    write_csv,
)

DEFAULT_OUT = ROOT / "examples" / "signaux-achat.csv"
COLS = ["company", "industry", "companySize", "signal",
        "firstname", "lastname", "jobTitle", "profileUrl"]


def build_filters(cfg: dict) -> dict:
    f: dict = {}
    if cfg.get("job"):
        f["job"] = cfg["job"]
    if cfg.get("people_location"):
        f["peopleLocation"] = cfg["people_location"]
    if cfg.get("industry"):
        f["industry"] = cfg["industry"]
    if cfg.get("company_size"):
        f["size"] = cfg["company_size"]
    if cfg.get("funding"):
        f["funding"] = True
        if cfg.get("funding_date_months"):
            f["fundingDateMonths"] = cfg["funding_date_months"]
    if cfg.get("growth_department"):
        f["growth"] = cfg["growth_department"]
        f["department"] = cfg["growth_department"]
    return f


def signal_label(cfg: dict) -> str:
    parts = []
    if cfg.get("funding"):
        m = cfg.get("funding_date_months")
        parts.append(f"Levee de fonds < {m} mois" if m else "Levee de fonds")
    if cfg.get("growth_department"):
        parts.append(f"Equipe {cfg['growth_department']} en croissance")
    return " + ".join(parts) or "Compte cible"


def company_size(summary: dict) -> str:
    """Extrait une taille lisible depuis company.summary.staff (forme variable)."""
    staff = summary.get("staff")
    if isinstance(staff, dict):
        for k in ("total", "count", "employees", "range"):
            if staff.get(k):
                return str(staff[k])
    elif staff:
        return str(staff)
    return ""


def map_row(r: dict, sig: str) -> dict:
    """Mappe une ligne /leads-finder (imbriquee : profile / company.summary / link)."""
    prof = r.get("profile") or {}
    comp = (r.get("company") or {}).get("summary") or {}
    link = r.get("link") or {}
    return {
        "company": comp.get("name", ""),
        "industry": r.get("industry") or comp.get("industry", ""),
        "companySize": company_size(comp),
        "signal": sig,
        "firstname": prof.get("first_name", ""),
        "lastname": prof.get("last_name", ""),
        "jobTitle": prof.get("headline") or prof.get("title", ""),
        "profileUrl": link.get("linkedin", ""),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Signaux d'achat Airscale")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    filters = build_filters(cfg)
    if not filters:
        sys.exit("config: renseigne au moins un filtre (job, industry, funding...).")
    count = int(cfg.get("count", 10))
    sig = signal_label(cfg)

    print("[preview] preflight gratuit /leads-finder/preview", file=sys.stderr)
    total = preview_leads(filters)
    if total is not None:
        print(f"[preview] ~{total} resultats estimes. Recuperation de {count}.", file=sys.stderr)

    print("[search] /leads-finder", file=sys.stderr)
    resp = post("leads-finder", {"filters": filters, "page": 0, "size": count})
    rows_raw = resp.get("rows") or unwrap(resp).get("rows") or []
    if not rows_raw:
        sys.exit("Aucun resultat. Assouplis les filtres ou le signal.")

    rows = [map_row(r, sig) for r in rows_raw]

    dest = Path(args.out or cfg.get("output_path") or DEFAULT_OUT)
    path = write_csv(rows, COLS, dest)
    print(f"[ok] {len(rows)} comptes chauds -> {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
