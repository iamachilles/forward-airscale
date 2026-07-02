---
name: airscale-telephones
description: Use when you have a list of LinkedIn profile URLs and need their mobile numbers for cold calling. Input = a CSV of LinkedIn URLs, output = the same CSV + phone column.
---

# Mobiles pour le cold calling

## Objectif & quand

Récupérer le **numéro de mobile** d'une liste de décideurs (à partir de leurs URLs LinkedIn) pour alimenter une séquence d'appels. À lancer quand l'email seul ne suffit pas et que tu veux ajouter le canal téléphone.

## Prérequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (outil d'enrichissement téléphone).
- Un CSV d'entrée avec une colonne URL LinkedIn.

## Config

| Champ | Role | Exemple |
|---|---|---|
| `input_csv` | Chemin du CSV d'entrée | `"input.example.csv"` |
| `linkedin_column` | Colonne contenant l'URL LinkedIn | `"linkedin_url"` |
| `output_path` | CSV de sortie | `null` |

## Adapter à ton cas

- **Enchaîner après une liste ICP** : passe le CSV de `airscale-liste-icp` (colonne `profileUrl`) en entrée, en réglant `linkedin_column: "profileUrl"`.
- **Prioriser** : ne garde que les contacts qualifiés avant de consommer des crédits téléphone (plus chers que l'email).

## Procédure

Pour chaque ligne : un `/phone` avec `linkedin_profile_url`. Synchrone. La colonne `phone` (et `provider`) est ajoutée. Une ligne en échec n'arrête pas le batch.

> Mapping MCP : enrichissement téléphone du serveur MCP Airscale (nom d'outil exact à confirmer côté MCP).

## Livrable

Un CSV `examples/telephones.csv` : colonnes d'origine + `phone, provider`.

## Coût estimé

Facturé à l'usage par Airscale (enrichissement téléphone par contact ; en général plus cher que l'email). Cible des contacts déjà qualifiés pour maîtriser le coût.

## Exemple

Voir `examples/telephones.csv`.
