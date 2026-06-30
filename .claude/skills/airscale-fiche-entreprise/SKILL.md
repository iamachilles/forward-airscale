---
name: airscale-fiche-entreprise
description: Use when you want an enriched company sheet (firmographics + key decision-makers) from a company LinkedIn URL. Input = a company URL in config.yaml, output = a markdown sheet.
---

# Fiche entreprise enrichie

## Objectif & quand

Produire une **fiche** sur une entreprise a partir de son URL LinkedIn : firmographie (secteur, taille, site, description) plus ses decideurs cles. A lancer avant une prise de contact ABM, ou pour qualifier un compte entrant.

## Prerequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (`airscale_find_people` + enrichissement entreprise).

## Config

| Champ | Role | Exemple |
|---|---|---|
| `company_linkedin_url` | URL LinkedIn de l'entreprise | `"https://linkedin.com/company/airscale-io"` |
| `decision_maker_titles` | Fonctions des decideurs a remonter | `["CEO", "Head of Sales"]` |
| `max_contacts` | Nombre de decideurs | `3` |
| `output_path` | Markdown de sortie | `null` |

## Adapter a ton cas

- **Qualification entrante** : colle l'URL LinkedIn de la societe d'un lead entrant pour decider vite s'il est dans l'ICP.
- **Cartographie de compte** : monte `max_contacts` et elargis `decision_maker_titles` pour mapper le comite d'achat.

## Procedure

1. `/company` avec `linkedin_profile_url` (URL d'entreprise) -> firmographie.
2. `/find-people` avec `query.companyLinkedinUrl.include = [url]` + `JobTitle.include = decision_maker_titles`, `size = max_contacts` -> decideurs.
3. Assemblage d'une fiche markdown (section entreprise + tableau decideurs).

> Mapping MCP : `/find-people` -> `airscale_find_people` ; enrichissement entreprise via l'outil correspondant du MCP.

## Livrable

Un markdown `examples/fiche-entreprise.md` : en-tete entreprise (firmographie) + tableau des decideurs (nom, poste, LinkedIn).

## Cout estime

Facture a l'usage : un enrichissement entreprise + ~0,1 credit par decideur retourne.

## Exemple

Voir `examples/fiche-entreprise.md`.
