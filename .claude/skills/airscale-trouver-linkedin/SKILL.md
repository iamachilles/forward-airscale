---
name: airscale-trouver-linkedin
description: Use when you have a list of people (first name + last name + company) missing their LinkedIn URL. Input = a CSV in config.yaml, output = the same CSV + linkedin_url column.
---

# Retrouver les URLs LinkedIn manquantes

## Objectif & quand

Completer un fichier ou il manque les **URLs LinkedIn** : a partir du prenom, du nom et de l'entreprise, retrouver le profil. A lancer pour reconcilier un export sans LinkedIn avant de l'enrichir (email, telephone) ou de le pousser dans une campagne.

> C'est souvent le prerequis des autres skills "coordonnees" : beaucoup d'enrichissements partent de l'URL LinkedIn.

## Prerequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (outil de recherche d'URL profil).
- Un CSV d'entree avec prenom, nom et entreprise.

## Config

| Champ | Role | Exemple |
|---|---|---|
| `input_csv` | Chemin du CSV d'entree | `"input.example.csv"` |
| `firstname_column` | Colonne prenom | `"first_name"` |
| `lastname_column` | Colonne nom | `"last_name"` |
| `company_column` | Colonne entreprise | `"company"` |
| `output_path` | CSV de sortie | `null` |

## Adapter a ton cas

- **Avant un enrichissement** : enchaine ce skill puis `airscale-emails-fichier` / `airscale-telephones` en reglant leur `linkedin_column: "linkedin_url"`.
- **Liste evenement / salon** : badge scanne (nom + societe) -> profils LinkedIn pour le suivi.

## Procedure

Pour chaque ligne : un `/url-search-people` avec `first_name` + `last_name` + `company_name` (les trois requis). La colonne `linkedin_url` est ajoutee. Une ligne en echec n'arrete pas le batch.

> Mapping MCP : outil de recherche d'URL profil du serveur MCP Airscale.

## Livrable

Un CSV `examples/trouver-linkedin.csv` : colonnes d'origine + `linkedin_url`.

## Cout estime

Facture a l'usage par Airscale (par recherche d'URL).

## Exemple

Voir `examples/trouver-linkedin.csv`.
