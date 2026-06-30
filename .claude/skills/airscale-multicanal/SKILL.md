---
name: airscale-multicanal
description: Use when you need full contact details (pro email + personal email + mobile) for a list of LinkedIn profiles to run a multichannel sequence. Input = a CSV of LinkedIn URLs, output = the same CSV + 3 contact columns.
---

# Coordonnees completes pour sequence multicanal

## Objectif & quand

Recuperer en un passage **l'email pro, l'email perso et le mobile** d'une liste de contacts (par URL LinkedIn), pour lancer une sequence qui combine email pro, email perso et appel. A lancer sur une liste deja qualifiee.

## Prerequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (outils d'enrichissement email / email perso / telephone).
- Un CSV d'entree avec une colonne URL LinkedIn.

## Config

| Champ | Role | Exemple |
|---|---|---|
| `input_csv` | Chemin du CSV d'entree | `"input.example.csv"` |
| `linkedin_column` | Colonne URL LinkedIn | `"linkedin_url"` |
| `channels` | Canaux a recuperer | `["email", "personal_email", "phone"]` |
| `output_path` | CSV de sortie | `null` |

## Adapter a ton cas

- **Budget serre** : limite `channels` a `["email"]` puis n'ajoute `phone` que sur les contacts prioritaires (le telephone coute plus cher).
- **Sequence "perso d'abord"** : garde `["personal_email", "phone"]` pour une approche moins corporate.

## Procedure

Pour chaque ligne (par `linkedin_profile_url`) : `/email`, `/personal-email`, `/phone` selon `channels`. Les colonnes `email`, `personal_email`, `phone` sont ajoutees. Chaque canal en echec laisse sa cellule vide sans casser le reste.

> Mapping MCP : les trois outils d'enrichissement correspondants du serveur MCP Airscale.

## Livrable

Un CSV `examples/multicanal.csv` : colonnes d'origine + `email, personal_email, phone`.

## Cout estime

Facture a l'usage : la somme des canaux demandes par contact. Le telephone est en general le plus cher : reserve-le aux contacts a forte valeur.

## Exemple

Voir `examples/multicanal.csv`.
