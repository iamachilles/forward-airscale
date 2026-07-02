---
name: airscale-trouver-linkedin
description: Use when you have a list of people (first name + last name + company) missing their LinkedIn URL. Input = a CSV in config.yaml, output = the same CSV + linkedin_url column.
---

# Retrouver les URLs LinkedIn manquantes

## Objectif & quand

Compléter un fichier où il manque les **URLs LinkedIn** : à partir du prénom, du nom et de l'entreprise, retrouver le profil. À lancer pour réconcilier un export sans LinkedIn avant de l'enrichir (email, téléphone) ou de le pousser dans une campagne.

> C'est souvent le prérequis des autres skills "coordonnées" : beaucoup d'enrichissements partent de l'URL LinkedIn.

## Prérequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (outil de recherche d'URL profil).
- Un CSV d'entrée avec prénom, nom et entreprise.

## Config

| Champ | Role | Exemple |
|---|---|---|
| `input_csv` | Chemin du CSV d'entrée | `"input.example.csv"` |
| `firstname_column` | Colonne prénom | `"first_name"` |
| `lastname_column` | Colonne nom | `"last_name"` |
| `company_column` | Colonne entreprise | `"company"` |
| `output_path` | CSV de sortie | `null` |

## Adapter à ton cas

- **Avant un enrichissement** : enchaîne ce skill puis `airscale-emails-fichier` / `airscale-telephones` en réglant leur `linkedin_column: "linkedin_url"`.
- **Liste événement / salon** : badge scanné (nom + société) -> profils LinkedIn pour le suivi.

## Procédure

Pour chaque ligne : un `/url-search-people` avec `first_name` + `last_name` + `company_name` (les trois requis). La colonne `linkedin_url` est ajoutée. Une ligne en échec n'arrête pas le batch.

> Mapping MCP : outil de recherche d'URL profil du serveur MCP Airscale.

## Livrable

Un CSV `examples/trouver-linkedin.csv` : colonnes d'origine + `linkedin_url`.

## Coût estimé

Facturé à l'usage par Airscale (par recherche d'URL).

## Exemple

Voir `examples/trouver-linkedin.csv`.
