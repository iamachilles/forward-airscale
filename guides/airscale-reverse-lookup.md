---
title: "Qui se cache derrière un email ou un numéro"
tool: airscale
famille: "Identification"
slug: airscale-reverse-lookup
skill: airscale-reverse-lookup
description: "Partez d'un email ou d'un téléphone et retrouvez le profil complet de la personne : nom, poste, entreprise, LinkedIn."
reading_time: 2
---

# Qui se cache derrière un email ou un numéro

## En bref

Vous avez juste un email (ou un numéro) et vous voulez savoir qui c'est. Le skill remonte le profil complet.

## Le problème

Un formulaire entrant ne laisse souvent qu'un email. Un appel manqué ne laisse qu'un numéro. Sans contexte, impossible de prioriser ou de personnaliser la réponse.

## Ce que vous obtenez

Une fiche markdown : nom, poste, entreprise, secteur, localisation, LinkedIn, et les autres champs retournés par Airscale.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-reverse-lookup` en `config.yaml`.
3. Renseignez l'`email` ou le `phone` à résoudre.
4. Lancez le skill (ou via le MCP Airscale).

## Coût

Facturé à l'usage par Airscale (par reverse lookup).

## Adapter à votre cas

- Qualification de formulaire : enrichissez les emails entrants avant le routage commercial.
- Identification d'appel : retrouvez le contact avant de rappeler.

> Exemple de sortie réelle : `examples/reverse-lookup.md` dans le repo.
