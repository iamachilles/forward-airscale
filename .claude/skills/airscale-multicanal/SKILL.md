---
name: airscale-multicanal
description: Use when you need full contact details (pro email + personal email + mobile) for a list of LinkedIn profiles to run a multichannel sequence. Input = a CSV of LinkedIn URLs, output = the same CSV + 3 contact columns.
---

# Coordonnées complètes pour séquence multicanal

## Objectif & quand

Récupérer en un passage **l'email pro, l'email perso et le mobile** d'une liste de contacts (par URL LinkedIn), pour lancer une séquence qui combine email pro, email perso et appel. À lancer sur une liste déjà qualifiée.

## Prérequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (outils d'enrichissement email / email perso / téléphone).
- Un CSV d'entrée avec une colonne URL LinkedIn.

## Config

| Champ | Role | Exemple |
|---|---|---|
| `input_csv` | Chemin du CSV d'entrée | `"input.example.csv"` |
| `linkedin_column` | Colonne URL LinkedIn | `"linkedin_url"` |
| `channels` | Canaux à récupérer | `["email", "personal_email", "phone"]` |
| `output_path` | CSV de sortie | `null` |

## Adapter à ton cas

- **Budget serré** : limite `channels` à `["email"]` puis n'ajoute `phone` que sur les contacts prioritaires (le téléphone coûte plus cher).
- **Séquence "perso d'abord"** : garde `["personal_email", "phone"]` pour une approche moins corporate.

## Procédure

Pour chaque ligne (par `linkedin_profile_url`) : `/email`, `/personal-email`, `/phone` selon `channels`. Les colonnes `email`, `personal_email`, `phone` sont ajoutées. Chaque canal en échec laisse sa cellule vide sans casser le reste.

> Mapping MCP : les trois outils d'enrichissement correspondants du serveur MCP Airscale.

## Livrable

Un CSV `examples/multicanal.csv` : colonnes d'origine + `email, personal_email, phone`.

## Coût estimé

Facturé à l'usage : la somme des canaux demandés par contact. Le téléphone est en général le plus cher : réserve-le aux contacts à forte valeur.

## Exemple

Voir `examples/multicanal.csv`.
