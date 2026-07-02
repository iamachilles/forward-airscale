---
name: airscale-hygiene-crm
description: Use when a CRM export has gone stale and you want to refresh it: for each person, re-fetch current job title and company, flag who changed companies, and re-find a fresh professional email. Input = a CSV export in config.yaml, output = the same CSV + refresh columns.
---

# Rafraîchir et nettoyer un CRM

## Objectif & quand

Partir d'un **export CRM** (CSV) et le remettre à jour. Avec le temps, un CRM se périme : les gens changent de poste, quittent leur boîte, et les emails tombent en panne. Ce skill repasse sur chaque ligne, récupère le poste et l'entreprise actuels depuis LinkedIn, détecte qui a changé d'entreprise (signal fort : lead de départ, champion à suivre dans sa nouvelle boîte), et re-trouve un email pro frais pour repérer les adresses périmées.

> À lancer avant une réactivation de base, un nettoyage trimestriel, ou quand un taux de bounce anormal signale des emails périmés.

## Prérequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (outils d'enrichissement profil et email).
- Un export CRM en CSV, avec au minimum une colonne URL LinkedIn et une colonne entreprise connue (voir `input.example.csv`).

## Config

| Champ | Rôle | Exemple |
|---|---|---|
| `input_csv` | Chemin de l'export CRM | `"input.example.csv"` |
| `linkedin_column` | Colonne URL LinkedIn (identifie chaque ligne) | `"linkedin_url"` |
| `company_column` | Colonne entreprise connue dans le CRM (base de comparaison) | `"company"` |
| `output_path` | CSV de sortie | `null` |

## Adapter à ton cas

- **Colonnes nommées autrement** : pointe `linkedin_column` et `company_column` vers les noms réels de ton export (ex `Profil LinkedIn`, `Societe`). Les colonnes d'origine sont conservées telles quelles.
- **Détection de départ uniquement** : concentre-toi sur `changed_company = yes` pour lister les gens qui ont bougé (à re-séquencer ou à re-qualifier).
- **Vérification d'emails uniquement** : lis `email_status` pour repérer les adresses non vérifiées à remplacer.
- **Lignes sans URL LinkedIn** : elles sont conservées mais laissées vides sur les colonnes de rafraîchissement (l'URL est la clé d'identification).

## Procédure

Pour chaque ligne, identifiée par la colonne URL LinkedIn :

1. `/profile` avec `{"linkedin_profile_url": url}` -> profil actuel. On extrait le poste (`current_title`) et l'entreprise (`current_company`) en parse défensif : le body peut porter `jobTitle` / `headline` / `companyName` au top-level, ou une entreprise imbriquée dans une liste `positions` / `experience`. On prend la première valeur non vide.
2. Comparaison de l'entreprise actuelle à l'entreprise connue du CRM (`company_column`), après normalisation (casse, ponctuation, suffixes juridiques type Inc/SAS/Labs). Si différente : `changed_company = yes`. Si identique : `no`. Si l'une des deux manque : vide.
3. `/email` avec `{"linkedin_profile_url": url}` -> `email` + `email_status` (détecte les emails périmés).

Une ligne en échec (profile ou email) n'arrête pas le batch. Un `time.sleep(0.2)` espace les appels.

> Mapping MCP : enrichissement profil et email du serveur MCP Airscale (noms d'outils exacts à confirmer côté MCP).

## Livrable

Un CSV `examples/hygiene-crm.csv` : colonnes d'origine + `current_title`, `current_company`, `changed_company`, `email`, `email_status`.

## Coût estimé

Facturé à l'usage par Airscale : un enrichissement profil + un enrichissement email par ligne. Voir le [pricing Airscale](https://app.airscale.io).

## Exemple

Voir `examples/hygiene-crm.csv`.
