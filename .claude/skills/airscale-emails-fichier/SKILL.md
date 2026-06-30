---
name: airscale-emails-fichier
description: Use when you have a CSV of people (name+company or LinkedIn URL) to enrich with verified professional emails. Input = a CSV in config.yaml, output = the same CSV + email columns.
---

# Enrichir un fichier en emails pro verifies

## Objectif & quand

Partir d'un **fichier existant** de contacts et trouver l'email professionnel verifie de chacun. A lancer pour rendre une liste actionnable avant une campagne, ou nettoyer un export CRM.

> Deux facons d'identifier un contact : (1) URL LinkedIn seule, ou (2) prenom + nom + domaine de l'entreprise. Le script gere les deux par ligne.

## Prerequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (outils d'enrichissement email).
- Un CSV d'entree (voir `input.example.csv`).

## Config

| Champ | Role | Exemple |
|---|---|---|
| `input_csv` | Chemin du CSV d'entree | `"input.example.csv"` |
| `linkedin_column` | Colonne URL LinkedIn (si dispo) | `"linkedin_url"` |
| `firstname_column` | Colonne prenom | `"first_name"` |
| `lastname_column` | Colonne nom | `"last_name"` |
| `domain_column` | Colonne domaine entreprise | `"domain"` |
| `output_path` | CSV de sortie | `null` |

## Adapter a ton cas

- **Fichier 100% LinkedIn** : remplis seulement `linkedin_column`, laisse les autres vides.
- **Fichier nom + societe** : remplis `firstname/lastname/domain` (le domaine fiabilise le matching).
- **Volume > 100** : Airscale expose `/email-bulk` (async via webhook, jusqu'a 100 inputs/appel) ; ce script boucle en synchrone, suffisant jusqu'a quelques centaines de lignes.

## Procedure

Pour chaque ligne : un `/email`. Corps = `linkedin_profile_url` si la colonne LinkedIn est remplie, sinon `first_name` + `last_name` + `domain`. Les colonnes `email`, `email_status`, `provider` sont ajoutees aux colonnes d'origine. Une ligne en echec n'arrete pas le batch.

> Mapping MCP : enrichissement email du serveur MCP Airscale (nom d'outil exact a confirmer cote MCP).

## Livrable

Un CSV `examples/emails-fichier.csv` : colonnes d'origine + `email, email_status, provider`.

## Cout estime

Facture a l'usage par Airscale (enrichissement email par contact). Voir le [pricing Airscale](https://app.airscale.io).

## Exemple

Voir `examples/emails-fichier.csv`.
