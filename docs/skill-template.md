# Convention d'un skill forward-airscale

Tous les skills suivent le même moule. Pour en ajouter un, copie cette structure.

## Arborescence

```
.claude/skills/airscale-{cas}/
  SKILL.md             le playbook (frontmatter + sections imposées)
  config.example.yaml  config pré-remplie (cible fictive) -> l'utilisateur la copie en config.yaml
  scripts/
    run.py             lit config.yaml + .env, appelle Airscale via lib/, ecrit le livrable
  (input.example.csv / schema.example.json si le skill en a besoin)
```

## Frontmatter SKILL.md

```yaml
---
name: airscale-{cas}
description: Use when [condition de declenchement]. [1 phrase sur l'input -> output].
---
```

Seuls `name` et `description` sont requis (format Claude Code natif).

## Sections imposées du SKILL.md

1. `## Objectif & quand` - à quoi sert le skill, pour qui, quand le déclencher.
2. `## Prérequis` - les deux modes : (A) clé AIRSCALE_API_KEY dans `.env` + `pip install -r requirements.txt` pour `run.py` ; (B) serveur MCP Airscale branché dans l'agent pour l'ad hoc.
3. `## Config` - tableau des champs du `config.yaml` (nom, rôle, exemple).
4. `## Adapter à ton cas` - comment instancier le template (variantes, cibles, filtres).
5. `## Procédure` - endpoints REST Airscale utilisés + paramètres exacts, ET le mapping vers l'outil MCP équivalent quand on le connaît. C'est la logique que l'agent suit / que run.py exécute.
6. `## Livrable` - format de sortie + où il est écrit.
7. `## Coût estimé` - ordre de grandeur en crédits Airscale (transparence pour le dirigeant).
8. `## Exemple` - pointe vers `examples/{cas}.*`.

## Contrat de `scripts/run.py`

- Invocation : `python scripts/run.py --config <chemin config.yaml> [--out <chemin sortie>]`.
- Lit la config via `lib.airscale_helpers.load_config`.
- Appelle Airscale via `lib.airscale_helpers.post` (et `count_people` / `preview_leads` pour les preflights gratuits avant tout sourcing payant).
- Écrit le livrable via `write_output` / `write_csv` (défaut : `examples/{cas}.md` ou `.csv`).
- N'imprime jamais la clé. Loggue les étapes (endpoint appelé, statut) sur stderr.
- Une ligne qui échoue ne casse pas le batch (try/except par item).
- Cibles d'exemple : publiques/fictives uniquement (le repo est public).

## Mapping endpoint REST -> outil MCP Airscale

| REST (`run.py`) | Outil MCP (mode agent ad hoc) |
|---|---|
| `/find-people`, `/find-people/count` | `airscale_find_people`, `airscale_count_find_people` |
| `/leads-finder`, `/leads-finder/preview` | `airscale_find_companies` (+ valeurs de filtres : `airscale_find_companies_filter_values`) |
| `/airsearch` | `airscale_airsearch` |
| `/credits` | `airscale_check_credits` |
| `/email`, `/phone`, `/personal-email`, `/profile`, `/company`, `/reverse-*` | outils d'enrichissement du MCP (noms exacts à confirmer depuis le serveur MCP) |

## Helpers disponibles (`lib/airscale_helpers.py`)

- `get_key()` -> str (clé depuis .env)
- `load_config(path)` -> dict
- `post(endpoint, body, timeout=, max_retries=)` -> dict (auth + backoff 429)
- `unwrap(resp)` -> dict (déballe `response`/`body`)
- `credits()` -> int (gratuit)
- `count_people(query)` / `preview_leads(filters)` -> int (preflight gratuit)
- `write_output(text, path)` / `write_csv(rows, fieldnames, path)` -> Path
