---
name: airscale-liste-icp
description: Use when you need a list of target prospects matching an ICP (job titles, location, keywords). Input = ICP filters in config.yaml, output = a CSV of contacts + their company + LinkedIn.
---

# Liste de prospects ICP a la demande

## Objectif & quand

**Generer** une liste de prospects correspondant a ton profil de client ideal (fonctions, zone, mots-cles) avec, pour chacun, son entreprise et son URL LinkedIn. A lancer pour amorcer une campagne commerciale ou nourrir ton CRM.

> Different de l'enrichissement : ici on *cree* la liste a partir de filtres. L'enrichissement (`airscale-emails-fichier`) part d'une liste existante.

## Prerequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) branche dans ton IA (outil `airscale_find_people`).

## Config

| Champ | Role | Exemple |
|---|---|---|
| `job_titles` | Fonctions ciblees (include) | `["Head of Sales", "VP Sales"]` |
| `exclude_titles` | Fonctions a exclure | `["Assistant"]` |
| `locations` | Zones geographiques | `["France"]` |
| `keywords` | Mots-cles cherches dans tout le profil | `["SaaS"]` |
| `size` | Nombre de cibles (1-100) | `10` |
| `output_path` | CSV de sortie | `null` |

## Adapter a ton cas

- **Sourcing partenaires / revendeurs** : `job_titles` = `["responsable partenariats"]`.
- **Sourcing par techno / secteur** : ajoute des `keywords` (ex `["Salesforce"]`, `["fintech"]`).
- **Zone fine** : `locations` accepte pays, region ou ville (ex `["Lyon"]`).

## Procedure

1. **Preflight gratuit** : `/find-people/count` sur le `query` construit, pour connaitre le volume avant de payer.
2. `/find-people` avec `query` = `{ JobTitle:{include,exclude}, location:{include}, keyword:{include} }` et `size`. (6 req/s, ~0,1 credit / lead.)
3. Ecriture d'un CSV.

> Mapping MCP : `/find-people` -> `airscale_find_people`, `/find-people/count` -> `airscale_count_find_people`.

## Livrable

Un CSV `examples/liste-icp.csv` : `firstname, lastname, jobTitle, companyName, companySize, companyIndustry, profileUrl`.

## Cout estime

Facture a l'usage par Airscale (~0,1 credit / lead retourne). Le comptage `/find-people/count` est **gratuit** : compte toujours avant de lancer. Voir le [pricing Airscale](https://app.airscale.io).

## Exemple

Voir `examples/liste-icp.csv`.
