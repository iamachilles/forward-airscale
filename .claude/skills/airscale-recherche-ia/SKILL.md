---
name: airscale-recherche-ia
description: Use when you need a structured data answer to a natural-language question (airsearch agent). Input = a prompt + optional field schema in config.yaml, output = a structured answer with sources.
---

# Recherche IA structurée à la demande

## Objectif & quand

Poser une **question en langage naturel** et recevoir une réponse **structurée** (champs typés) avec un score de confiance et ses sources, via l'agent de recherche d'Airscale (airsearch). À lancer pour une donnée ponctuelle difficile à trouver (ex : "qui est le CEO et l'année de création de telle société", "le CRM utilisé par telle entreprise").

> Pour construire une liste à partir de filtres, utilise plutôt `airscale-liste-icp`. Ici on répond à une question précise, éventuellement champ par champ.

## Prérequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (`airscale_airsearch`).

## Config

| Champ | Role | Exemple |
|---|---|---|
| `prompt` | La question en langage naturel | `"Qui est le CEO d'Airscale ?"` |
| `schema_file` | JSON champ -> type (optionnel) | `"schema.example.json"` |
| `output_path` | Markdown de sortie | `null` |

Types de schéma acceptés : `string, url, email, number, int, float, boolean, date, phone`.

## Adapter à ton cas

- **Donnée unique** : laisse `schema_file` vide, formule juste `prompt` (réponse en texte source).
- **Extraction multi-champs** : décris les champs voulus dans le JSON (`schema.example.json`) pour une sortie exploitable directement.
- **En masse** : pour poser la même question sur N entités, écris une boucle qui appelle `run.py` (ou la fonction) par entité plutôt qu'un LLM par ligne.

## Procédure

Un `/airsearch` avec `prompt` (+ `schema` chargé depuis `schema_file` si fourni). La réponse contient les champs du schéma, plus `response`, `confidence_score`, `certainty_tag`, `sources`, `reasoning`. Tout est rendu en markdown.

> Mapping MCP : `/airsearch` -> `airscale_airsearch`.

## Livrable

Un markdown `examples/recherche-ia.md` : champs structurés + réponse + confiance + sources.

## Coût estimé

Facturé à l'usage par Airscale (~1 à 2 crédits par requête airsearch ; le coût exact via le MCP est à confirmer).

## Exemple

Voir `examples/recherche-ia.md`.
