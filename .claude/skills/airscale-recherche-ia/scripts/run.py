#!/usr/bin/env python3
"""Recherche IA structuree via Airscale /airsearch.

Pose `prompt` (+ `schema` optionnel) -> reponse structuree + sources.
Ecrit un markdown.

Usage:
    python scripts/run.py --config config.yaml [--out chemin.md]
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from lib.airscale_helpers import load_config, post, write_output  # noqa: E402

DEFAULT_OUT = ROOT / "examples" / "recherche-ia.md"
META = {"status", "response", "confidence_score", "certainty_tag",
        "sources", "reasoning", "duration_ms"}


def main() -> None:
    ap = argparse.ArgumentParser(description="Recherche IA Airscale (airsearch)")
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    cfg = load_config(args.config)
    prompt = cfg.get("prompt")
    if not prompt:
        sys.exit("config: 'prompt' est requis.")

    body: dict = {"prompt": prompt}
    schema_file = cfg.get("schema_file")
    if schema_file:
        schema_path = Path(schema_file)
        if not schema_path.is_absolute():
            # cherche relativement au dossier du skill puis a la racine
            cand = Path(args.config).resolve().parent / schema_file
            schema_path = cand if cand.exists() else ROOT / schema_file
        if schema_path.exists():
            body["schema"] = json.loads(schema_path.read_text(encoding="utf-8"))
        else:
            print(f"  ! schema_file introuvable ({schema_path}), recherche sans schema", file=sys.stderr)

    print("[airsearch] /airsearch", file=sys.stderr)
    resp = post("airsearch", body)

    # Champs structures = tout ce qui n'est pas meta
    fields = {k: v for k, v in resp.items() if k not in META}
    field_lines = "\n".join(f"- **{k}** : {v}" for k, v in fields.items()) or "- (aucun champ structure)"
    sources = resp.get("sources") or []
    src_lines = "\n".join(
        f"- {s.get('url', s) if isinstance(s, dict) else s}" for s in sources[:8]
    ) or "- (aucune source)"

    out_text = (
        f"# Recherche IA - airsearch\n\n"
        f"_Genere le {date.today().isoformat()} via Airscale._\n\n"
        f"**Question** : {prompt}\n\n"
        f"## Reponse structuree\n\n{field_lines}\n\n"
        f"## Reponse\n\n{resp.get('response', '')}\n\n"
        f"**Confiance** : {resp.get('confidence_score', 'n/a')} "
        f"({resp.get('certainty_tag', 'n/a')})\n\n"
        f"## Sources\n{src_lines}\n"
    )
    dest = args.out or cfg.get("output_path") or str(DEFAULT_OUT)
    path = write_output(out_text, dest)
    print(f"[ok] resultat -> {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
