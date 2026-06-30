---
name: airscale-signaux-achat
description: Use when you want accounts showing buying signals (recent funding, team growth in a department) plus their decision-makers. Input = signal filters in config.yaml, output = a CSV of hot accounts + contacts.
---

# Comptes en signal d'achat

## Objectif & quand

Sortir une liste de **comptes chauds** : entreprises qui viennent de lever des fonds ou dont une equipe (sales, marketing, tech...) grossit, avec les decideurs a contacter. A lancer pour prioriser l'outbound sur des comptes qui ont un declencheur recent.

## Prerequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (`airscale_find_companies`).

## Config

| Champ | Role | Exemple |
|---|---|---|
| `job` | Fonctions des decideurs a remonter | `["Head of Sales", "CEO"]` |
| `people_location` | Zones | `["France"]` |
| `industry` | Secteurs cibles | `["Software"]` |
| `company_size` | Taille d'entreprise | `"11-50"` |
| `funding` | Filtrer sur une levee de fonds | `true` |
| `funding_date_months` | Anciennete max de la levee (3/6/12/24) | `6` |
| `growth_department` | Departement en croissance d'effectif | `"Sales"` |
| `count` | Nombre de lignes | `10` |
| `output_path` | CSV de sortie | `null` |

## Adapter a ton cas

- **Pur intent "levee"** : `funding: true`, `funding_date_months: 3`, laisse `growth_department` vide.
- **Pur intent "ca recrute"** : `growth_department: "Sales"` (ou "Engineering"), `funding: false`.
- **Comptes ABM** : combine `industry` + `company_size` + un signal pour resserrer la liste.

## Procedure

1. **Preflight gratuit** : `/leads-finder/preview` sur les `filters` construits (total estime).
2. `/leads-finder` avec `filters` (job, peopleLocation, industry, size, funding, fundingDateMonths, growth/department) et `size`. (5 req/s.)
3. Composition d'une colonne `signal` (ce qui a declenche l'inclusion) + ecriture CSV.

> Mapping MCP : `/leads-finder` -> `airscale_find_companies`, valeurs de filtres -> `airscale_find_companies_filter_values`.

## Livrable

Un CSV `examples/signaux-achat.csv` : `company, industry, companySize, signal, firstname, lastname, jobTitle, profileUrl`.

## Cout estime

Facture a l'usage (~0,1 credit / lead). Le `/leads-finder/preview` est **gratuit** : previsualise le volume avant de payer.

## Exemple

Voir `examples/signaux-achat.csv`.
