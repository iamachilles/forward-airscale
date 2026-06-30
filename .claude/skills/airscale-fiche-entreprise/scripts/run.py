#!/usr/bin/env python3
"""Fiche entreprise enrichie via Airscale : /company + /find-people.

1) /company -> firmographie depuis l'URL LinkedIn entreprise
2) /find-people (companyLinkedinUrl + JobTitle) -> decideurs cles
Ecrit une fiche markdown.

Usage:
    python scripts/run.py --config config.yaml [--out chemin.md]
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from lib.airscale_helpers import load_config, post, unwrap, write_output  # noqa: E402

DEFAULT_OUT = ROOT / "examples" / "fiche-entreprise.md"
# Champs firmographiques candidats (on affiche ceux qui existent).
FIRMO = [
    ("name", "Nom"), ("industry", "Secteur"), ("companySize", "Taille"),
    ("size", "Taille"), ("website", "Site"), ("companyWebsite", "Site"),
    ("headquarters", "Siege"), ("location", "Localisation"), ("founded", "Creation"),
]


def main() -> None:
    ap = argparse.ArgumentParser(description="Fiche entreprise Airscale")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    url = cfg.get("company_linkedin_url")
    if not url:
        sys.exit("config: 'company_linkedin_url' est requis.")
    titles = cfg.get("decision_maker_titles") or []
    max_contacts = int(cfg.get("max_contacts", 3))

    print(f"[company] /company {url}", file=sys.stderr)
    company = unwrap(post("company", {"linkedin_profile_url": url}))
    name = company.get("name") or url

    query: dict = {"companyLinkedinUrl": {"include": [url]}}
    if titles:
        query["JobTitle"] = {"include": titles}
    print("[people] /find-people (decideurs)", file=sys.stderr)
    people_resp = post("find-people", {"query": query, "size": max_contacts})
    leads = people_resp.get("leads") or unwrap(people_resp).get("leads") or []

    # Section firmographie
    seen = set()
    firmo_lines = []
    for key, label in FIRMO:
        if label in seen:
            continue
        val = company.get(key)
        if val:
            firmo_lines.append(f"- **{label}** : {val}")
            seen.add(label)
    desc = company.get("description") or company.get("about") or ""

    # Tableau decideurs
    if leads:
        rows = ["| Nom | Poste | LinkedIn |", "|---|---|---|"]
        for ld in leads:
            fn = ld.get("firstname", "")
            ln = ld.get("lastname", "")
            jt = ld.get("jobTitle", ld.get("headline", ""))
            pu = ld.get("profileUrl", "")
            link = f"[profil]({pu})" if pu else ""
            rows.append(f"| {fn} {ln} | {jt} | {link} |")
        people_block = "\n".join(rows)
    else:
        people_block = "_(aucun decideur retourne pour ces fonctions)_"

    out_text = (
        f"# Fiche entreprise - {name}\n\n"
        f"_Genere le {date.today().isoformat()} via Airscale._\n\n"
        f"## Firmographie\n\n"
        + ("\n".join(firmo_lines) if firmo_lines else "- (firmographie non retournee)")
        + "\n\n"
        + (f"## Description\n\n{desc}\n\n" if desc else "")
        + f"## Decideurs cles\n\n{people_block}\n"
    )
    dest = args.out or cfg.get("output_path") or str(DEFAULT_OUT)
    path = write_output(out_text, dest)
    print(f"[ok] fiche -> {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
