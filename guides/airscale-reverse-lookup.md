---
title: "Qui se cache derriere un email ou un numero"
tool: airscale
famille: "Identification"
slug: airscale-reverse-lookup
skill: airscale-reverse-lookup
description: "Partez d'un email ou d'un telephone et retrouvez le profil complet de la personne : nom, poste, entreprise, LinkedIn."
reading_time: 2
---

# Qui se cache derriere un email ou un numero

## En bref

Vous avez juste un email (ou un numero) et vous voulez savoir qui c'est. Le skill remonte le profil complet.

## Le probleme

Un formulaire entrant ne laisse souvent qu'un email. Un appel manque ne laisse qu'un numero. Sans contexte, impossible de prioriser ou de personnaliser la reponse.

## Ce que vous obtenez

Une fiche markdown : nom, poste, entreprise, secteur, localisation, LinkedIn, et les autres champs retournes par Airscale.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/ColinDargent/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-reverse-lookup` en `config.yaml`.
3. Renseignez l'`email` ou le `phone` a resoudre.
4. Lancez le skill (ou via le MCP Airscale).

## Cout

Facture a l'usage par Airscale (par reverse lookup).

## Adapter a votre cas

- Qualification de formulaire : enrichissez les emails entrants avant le routage commercial.
- Identification d'appel : retrouvez le contact avant de rappeler.

> Exemple de sortie reelle : `examples/reverse-lookup.md` dans le repo.
