---
name: airscale-recherche-ia
description: Use when you need a structured data answer to a natural-language question (airsearch agent). Input = a prompt + optional field schema in config.yaml, output = a structured answer with sources.
---

# Recherche IA structuree a la demande

## Objectif & quand

Poser une **question en langage naturel** et recevoir une reponse **structuree** (champs typés) avec un score de confiance et ses sources, via l'agent de recherche d'Airscale (airsearch). A lancer pour une donnee ponctuelle difficile a trouver (ex : "qui est le CEO et l'annee de creation de telle societe", "le CRM utilise par telle entreprise").

> Pour construire une liste a partir de filtres, utilise plutot `airscale-liste-icp`. Ici on repond a une question precise, eventuellement champ par champ.

## Prerequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (`airscale_airsearch`).

## Config

| Champ | Role | Exemple |
|---|---|---|
| `prompt` | La question en langage naturel | `"Qui est le CEO d'Airscale ?"` |
| `schema_file` | JSON champ -> type (optionnel) | `"schema.example.json"` |
| `output_path` | Markdown de sortie | `null` |

Types de schema acceptes : `string, url, email, number, int, float, boolean, date, phone`.

## Adapter a ton cas

- **Donnee unique** : laisse `schema_file` vide, formule juste `prompt` (reponse en texte source).
- **Extraction multi-champs** : decris les champs voulus dans le JSON (`schema.example.json`) pour une sortie exploitable directement.
- **En masse** : pour poser la meme question sur N entites, ecris une boucle qui appelle `run.py` (ou la fonction) par entite plutot qu'un LLM par ligne.

## Procedure

Un `/airsearch` avec `prompt` (+ `schema` charge depuis `schema_file` si fourni). La reponse contient les champs du schema, plus `response`, `confidence_score`, `certainty_tag`, `sources`, `reasoning`. Tout est rendu en markdown.

> Mapping MCP : `/airsearch` -> `airscale_airsearch`.

## Livrable

Un markdown `examples/recherche-ia.md` : champs structures + reponse + confiance + sources.

## Cout estime

Facture a l'usage par Airscale (~1 a 2 credits par requete airsearch ; le cout exact via le MCP est a confirmer).

## Exemple

Voir `examples/recherche-ia.md`.
