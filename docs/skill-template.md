# Convention d'un skill forward-airscale

Tous les skills suivent le meme moule. Pour en ajouter un, copie cette structure.

## Arborescence

```
.claude/skills/airscale-{cas}/
  SKILL.md             le playbook (frontmatter + sections imposees)
  config.example.yaml  config pre-remplie (cible fictive) -> l'utilisateur la copie en config.yaml
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

## Sections imposees du SKILL.md

1. `## Objectif & quand` - a quoi sert le skill, pour qui, quand le declencher.
2. `## Prerequis` - les deux modes : (A) cle AIRSCALE_API_KEY dans `.env` + `pip install -r requirements.txt` pour `run.py` ; (B) serveur MCP Airscale branche dans l'agent pour l'ad hoc.
3. `## Config` - tableau des champs du `config.yaml` (nom, role, exemple).
4. `## Adapter a ton cas` - comment instancier le template (variantes, cibles, filtres).
5. `## Procedure` - endpoints REST Airscale utilises + parametres exacts, ET le mapping vers l'outil MCP equivalent quand on le connait. C'est la logique que l'agent suit / que run.py execute.
6. `## Livrable` - format de sortie + ou il est ecrit.
7. `## Cout estime` - ordre de grandeur en credits Airscale (transparence pour le dirigeant).
8. `## Exemple` - pointe vers `examples/{cas}.*`.

## Contrat de `scripts/run.py`

- Invocation : `python scripts/run.py --config <chemin config.yaml> [--out <chemin sortie>]`.
- Lit la config via `lib.airscale_helpers.load_config`.
- Appelle Airscale via `lib.airscale_helpers.post` (et `count_people` / `preview_leads` pour les preflights gratuits avant tout sourcing payant).
- Ecrit le livrable via `write_output` / `write_csv` (defaut : `examples/{cas}.md` ou `.csv`).
- N'imprime jamais la cle. Loggue les etapes (endpoint appele, statut) sur stderr.
- Une ligne qui echoue ne casse pas le batch (try/except par item).
- Cibles d'exemple : publiques/fictives uniquement (le repo est public).

## Mapping endpoint REST -> outil MCP Airscale

| REST (`run.py`) | Outil MCP (mode agent ad hoc) |
|---|---|
| `/find-people`, `/find-people/count` | `airscale_find_people`, `airscale_count_find_people` |
| `/leads-finder`, `/leads-finder/preview` | `airscale_find_companies` (+ valeurs de filtres : `airscale_find_companies_filter_values`) |
| `/airsearch` | `airscale_airsearch` |
| `/credits` | `airscale_check_credits` |
| `/email`, `/phone`, `/personal-email`, `/profile`, `/company`, `/reverse-*` | outils d'enrichissement du MCP (noms exacts a confirmer depuis le serveur MCP) |

## Helpers disponibles (`lib/airscale_helpers.py`)

- `get_key()` -> str (cle depuis .env)
- `load_config(path)` -> dict
- `post(endpoint, body, timeout=, max_retries=)` -> dict (auth + backoff 429)
- `unwrap(resp)` -> dict (deballe `response`/`body`)
- `credits()` -> int (gratuit)
- `count_people(query)` / `preview_leads(filters)` -> int (preflight gratuit)
- `write_output(text, path)` / `write_csv(rows, fieldnames, path)` -> Path
