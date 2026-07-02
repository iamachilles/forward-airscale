---
name: airscale-reverse-lookup
description: Use when you have an email or a phone number and want to know who it belongs to (enriched profile). Input = an email or phone in config.yaml, output = a markdown contact sheet.
---

# Reverse lookup : qui se cache derrière un email ou un numéro

## Objectif & quand

Partir d'un **email** ou d'un **numéro de téléphone** et retrouver le profil complet de la personne (nom, poste, entreprise, LinkedIn). À lancer pour qualifier un lead entrant (formulaire avec juste un email), identifier un appelant, ou dédupliquer un contact.

## Prérequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (outils reverse email / reverse phone).

## Config

| Champ | Role | Exemple |
|---|---|---|
| `email` | Email à résoudre (prioritaire si rempli) | `"victor@airscale.io"` |
| `phone` | Numéro à résoudre (format international) | `"+33610607076"` |
| `output_path` | Markdown de sortie | `null` |

Renseigne `email` **ou** `phone`. Si les deux sont remplis, `email` est utilisé.

## Adapter à ton cas

- **Qualif de formulaire** : branche ce skill sur les emails entrants pour enrichir avant routage commercial.
- **Identification d'appel** : pars du `phone` pour retrouver le contact avant de rappeler.

## Procédure

- Si `email` : `/reverse-email` avec `email`.
- Sinon : `/reverse-phone` avec `mobile_phone` (attention : le bon champ est `mobile_phone`, pas `phone`).

La réponse (profil enrichi, sous `body`) est rendue en fiche markdown.

> Mapping MCP : outils reverse email / reverse phone du serveur MCP Airscale.

## Livrable

Un markdown `examples/reverse-lookup.md` : fiche contact (nom, poste, entreprise, localisation, LinkedIn, et autres champs retournés).

## Coût estimé

Facturé à l'usage par Airscale (par reverse lookup).

## Exemple

Voir `examples/reverse-lookup.md`.
