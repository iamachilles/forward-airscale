#!/usr/bin/env python3
"""Rafraîchir et nettoyer un export CRM via Airscale : /profile + /email.

Pour chaque ligne (identifiée par URL LinkedIn) :
  1) /profile -> poste actuel + entreprise actuelle (parse défensif du body)
  2) compare l'entreprise actuelle à l'entreprise connue du CRM -> changed_company
  3) /email -> email pro re-trouvé + email_status (détecte les emails périmés)
Écrit le CSV d'origine + current_title, current_company, changed_company,
email, email_status.

Usage:
    python scripts/run.py --config config.yaml [--out chemin.csv]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from lib.airscale_helpers import load_config, post, unwrap  # noqa: E402

DEFAULT_OUT = ROOT / "examples" / "hygiene-crm.csv"
ENRICH = ["current_title", "current_company", "changed_company", "email", "email_status"]

# Clés candidates pour le poste actuel, par ordre de préférence.
TITLE_KEYS = ["jobTitle", "job_title", "headline", "title", "position", "occupation"]
# Clés candidates pour l'entreprise actuelle, par ordre de préférence.
COMPANY_KEYS = ["companyName", "company_name", "company", "currentCompany",
                "organization", "employer"]


def _flat(val) -> str:
    """Rend une valeur scalaire ou déballe un dict (nom d'entreprise imbriqué)."""
    if isinstance(val, dict):
        for k in ("name", "companyName", "company_name", "defaultValue", "default", "title"):
            inner = val.get(k)
            if isinstance(inner, str) and inner.strip():
                return inner.strip()
        return ""
    if isinstance(val, (str, int, float)):
        return str(val).strip()
    return ""


def _pick(body: dict, keys: list[str]) -> str:
    """Première valeur non vide parmi `keys` au top-level du body."""
    for k in keys:
        text = _flat(body.get(k))
        if text:
            return text
    return ""


def _current_group(body: dict) -> dict:
    """Premier bloc d'expérience (poste courant) de la réponse /profile Airscale.

    Le shape réel : `positionGroups.contents[0]` = { company:{name,...},
    profilePositions:[{title,...}] }. On tombe en secours sur d'autres formes
    (`positions`/`experience`) si un autre fournisseur renvoie un shape différent.
    """
    pg = body.get("positionGroups")
    if isinstance(pg, dict):
        contents = pg.get("contents")
        if isinstance(contents, list) and contents and isinstance(contents[0], dict):
            return contents[0]
    for key in ("positions", "experience", "experiences", "jobs"):
        seq = body.get(key)
        if isinstance(seq, list) and seq and isinstance(seq[0], dict):
            return seq[0]
    return {}


def extract_company_from_positions(body: dict) -> str:
    """Nom de l'entreprise actuelle depuis le bloc d'expérience courant."""
    group = _current_group(body)
    company = group.get("company")
    if isinstance(company, dict) and company.get("name"):
        return str(company["name"]).strip()
    return _pick(group, COMPANY_KEYS)


def extract_title_from_positions(body: dict) -> str:
    """Titre du poste actuel depuis le bloc d'expérience courant."""
    group = _current_group(body)
    for key in ("profilePositions", "positions"):
        seq = group.get(key)
        if isinstance(seq, list) and seq and isinstance(seq[0], dict):
            t = _pick(seq[0], TITLE_KEYS)
            if t:
                return t
    return _pick(group, TITLE_KEYS)


def _norm(s: str) -> str:
    """Normalise un nom d'entreprise pour comparaison (casse, espaces, suffixes)."""
    s = (s or "").lower().strip()
    s = re.sub(r"[.,]", " ", s)
    s = re.sub(r"\b(inc|llc|ltd|sa|sas|sasu|sarl|gmbh|corp|co|labs?)\b", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def main() -> None:
    ap = argparse.ArgumentParser(description="Hygiène CRM Airscale (profile + email)")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    li_col = cfg.get("linkedin_column", "linkedin_url")
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
        for k in ENRICH:
            enriched[k] = ""
        url = (row.get(li_col) or "").strip()
        if not url:
            print("  ! ligne ignorée (pas d'URL LinkedIn)", file=sys.stderr)
            out_rows.append(enriched)
            continue

        print(f"[profile] {url}", file=sys.stderr)
        try:
            profile = unwrap(post("profile", {"linkedin_profile_url": url}))
        except Exception as e:  # une ligne qui échoue ne casse pas le batch
            print(f"  ! échec /profile : {e}", file=sys.stderr)
            profile = {}

        cur_title = extract_title_from_positions(profile) or _pick(profile, TITLE_KEYS)
        cur_company = extract_company_from_positions(profile) or _pick(profile, COMPANY_KEYS)
        enriched["current_title"] = cur_title
        enriched["current_company"] = cur_company

        known_company = (row.get(co_col) or "").strip()
        if cur_company and known_company:
            enriched["changed_company"] = "yes" if _norm(cur_company) != _norm(known_company) else "no"
        else:
            enriched["changed_company"] = ""

        time.sleep(0.2)  # courtoisie rate limit

        print(f"[email] {url}", file=sys.stderr)
        try:
            email_resp = unwrap(post("email", {"linkedin_profile_url": url}))
        except Exception as e:
            print(f"  ! échec /email : {e}", file=sys.stderr)
            email_resp = {}
        enriched["email"] = email_resp.get("email", "")
        enriched["email_status"] = email_resp.get("email_status", "")

        out_rows.append(enriched)
        time.sleep(0.2)  # courtoisie rate limit

    out_cols = list(in_cols) + [c for c in ENRICH if c not in in_cols]
    dest = Path(args.out or cfg.get("output_path") or DEFAULT_OUT)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_cols)
        w.writeheader()
        w.writerows(out_rows)
    changed = sum(1 for r in out_rows if r.get("changed_company") == "yes")
    print(f"[ok] {len(out_rows)} lignes, {changed} changement(s) d'entreprise -> {dest}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
