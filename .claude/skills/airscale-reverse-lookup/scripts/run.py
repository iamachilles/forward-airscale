#!/usr/bin/env python3
"""Reverse lookup via Airscale : email ou telephone -> profil enrichi.

/reverse-email (si email) ou /reverse-phone (si phone, champ mobile_phone).
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

DEFAULT_OUT = ROOT / "examples" / "reverse-lookup.md"
# Champs candidats a afficher en premier (on rend ceux qui existent).
PREFERRED = [
    ("firstname", "Prenom"), ("lastname", "Nom"), ("fullName", "Nom complet"),
    ("headline", "Headline"), ("jobTitle", "Poste"), ("companyName", "Entreprise"),
    ("company", "Entreprise"), ("industry", "Secteur"), ("location", "Localisation"),
    ("profileUrl", "LinkedIn"), ("linkedin_url", "LinkedIn"), ("url", "LinkedIn"),
    ("email", "Email"), ("phone_numbers", "Telephone"),
]
# Cles techniques a ne pas afficher (urns, images, identifiants internes).
NOISE = {"picture", "background", "entityUrn", "objectUrn", "identifier",
         "profilePictureUrl", "premium", "creator"}


def fmt(val) -> str:
    """Rend une valeur lisible (deballe les dicts type localisation)."""
    if isinstance(val, dict):
        for k in ("defaultValue", "default", "shortValue", "full_name", "name"):
            if val.get(k):
                return str(val[k])
        parts = [str(val[k]) for k in ("city", "state", "country") if val.get(k)]
        return ", ".join(parts) if parts else ""
    return str(val)


def render(body: dict) -> str:
    lines = []
    shown_labels = set()
    for key, label in PREFERRED:
        val = body.get(key)
        if val and label not in shown_labels:
            text = fmt(val)
            if text:
                lines.append(f"- **{label}** : {text}")
                shown_labels.add(label)
    # Champs restants non couverts (scalaires uniquement, hors bruit technique)
    covered = {k for k, _ in PREFERRED}
    extra = [
        f"- **{k}** : {v}"
        for k, v in body.items()
        if k not in covered and k not in NOISE and isinstance(v, (str, int, float)) and v
    ]
    return "\n".join(lines + extra) or "- (aucun champ retourne)"


def main() -> None:
    ap = argparse.ArgumentParser(description="Reverse lookup Airscale")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    email = (cfg.get("email") or "").strip()
    phone = (cfg.get("phone") or "").strip() if cfg.get("phone") else ""
    if not email and not phone:
        sys.exit("config: renseigne 'email' ou 'phone'.")

    if email:
        print(f"[reverse-email] {email}", file=sys.stderr)
        body = unwrap(post("reverse-email", {"email": email}))
        source = email
    else:
        print(f"[reverse-phone] {phone}", file=sys.stderr)
        body = unwrap(post("reverse-phone", {"mobile_phone": phone}))
        source = phone

    out_text = (
        f"# Reverse lookup - {source}\n\n"
        f"_Genere le {date.today().isoformat()} via Airscale._\n\n"
        f"{render(body)}\n"
    )
    dest = args.out or cfg.get("output_path") or str(DEFAULT_OUT)
    path = write_output(out_text, dest)
    print(f"[ok] fiche -> {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
