---
name: airscale-fiche-entreprise
description: Use when you want an enriched company sheet (firmographics + key decision-makers) from a company LinkedIn URL. Input = a company URL in config.yaml, output = a markdown sheet.
---

# Fiche entreprise enrichie

## Objectif & quand

Produire une **fiche** sur une entreprise à partir de son URL LinkedIn : firmographie (secteur, taille, site, description) plus ses décideurs clés. À lancer avant une prise de contact ABM, ou pour qualifier un compte entrant.

## Prérequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (`airscale_find_people` + enrichissement entreprise).

## Config

| Champ | Role | Exemple |
|---|---|---|
| `company_linkedin_url` | URL LinkedIn de l'entreprise | `"https://linkedin.com/company/airscale-io"` |
| `decision_maker_titles` | Fonctions des décideurs à remonter | `["CEO", "Head of Sales"]` |
| `max_contacts` | Nombre de décideurs | `3` |
| `output_path` | Markdown de sortie | `null` |

## Adapter à ton cas

- **Qualification entrante** : colle l'URL LinkedIn de la société d'un lead entrant pour décider vite s'il est dans l'ICP.
- **Cartographie de compte** : monte `max_contacts` et élargis `decision_maker_titles` pour mapper le comité d'achat.

## Procédure

1. `/company` avec `linkedin_profile_url` (URL d'entreprise) -> firmographie.
2. `/find-people` avec `query.companyLinkedinUrl.include = [url]` + `JobTitle.include = decision_maker_titles`, `size = max_contacts` -> décideurs.
3. Assemblage d'une fiche markdown (section entreprise + tableau décideurs).

> Mapping MCP : `/find-people` -> `airscale_find_people` ; enrichissement entreprise via l'outil correspondant du MCP.

## Livrable

Un markdown `examples/fiche-entreprise.md` : en-tête entreprise (firmographie) + tableau des décideurs (nom, poste, LinkedIn).

## Coût estimé

Facturé à l'usage : un enrichissement entreprise + ~0,1 crédit par décideur retourné.

## Exemple

Voir `examples/fiche-entreprise.md`.
