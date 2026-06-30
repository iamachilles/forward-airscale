---
name: airscale-telephones
description: Use when you have a list of LinkedIn profile URLs and need their mobile numbers for cold calling. Input = a CSV of LinkedIn URLs, output = the same CSV + phone column.
---

# Mobiles pour le cold calling

## Objectif & quand

Recuperer le **numero de mobile** d'une liste de decideurs (a partir de leurs URLs LinkedIn) pour alimenter une sequence d'appels. A lancer quand l'email seul ne suffit pas et que tu veux ajouter le canal telephone.

## Prerequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (outil d'enrichissement telephone).
- Un CSV d'entree avec une colonne URL LinkedIn.

## Config

| Champ | Role | Exemple |
|---|---|---|
| `input_csv` | Chemin du CSV d'entree | `"input.example.csv"` |
| `linkedin_column` | Colonne contenant l'URL LinkedIn | `"linkedin_url"` |
| `output_path` | CSV de sortie | `null` |

## Adapter a ton cas

- **Enchainer apres une liste ICP** : passe le CSV de `airscale-liste-icp` (colonne `profileUrl`) en entree, en reglant `linkedin_column: "profileUrl"`.
- **Prioriser** : ne garde que les comptes chauds (`airscale-signaux-achat`) avant de consommer des credits telephone (plus chers que l'email).

## Procedure

Pour chaque ligne : un `/phone` avec `linkedin_profile_url`. Synchrone. La colonne `phone` (et `provider`) est ajoutee. Une ligne en echec n'arrete pas le batch.

> Mapping MCP : enrichissement telephone du serveur MCP Airscale (nom d'outil exact a confirmer cote MCP).

## Livrable

Un CSV `examples/telephones.csv` : colonnes d'origine + `phone, provider`.

## Cout estime

Facture a l'usage par Airscale (enrichissement telephone par contact ; en general plus cher que l'email). Cible des contacts deja qualifies pour maitriser le cout.

## Exemple

Voir `examples/telephones.csv`.
