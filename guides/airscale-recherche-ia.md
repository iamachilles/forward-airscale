---
title: "Une réponse data structurée à la demande"
tool: airscale
famille: "Identification"
slug: airscale-recherche-ia
skill: airscale-recherche-ia
description: "Posez une question en langage naturel et recevez une réponse structurée (champs typés) avec son score de confiance et ses sources."
reading_time: 3
---

# Une réponse data structurée à la demande

## En bref

Vous posez une question précise ("qui est le CEO et l'année de création de telle société ?") et l'agent de recherche d'Airscale renvoie une réponse structurée, avec sa confiance et ses sources.

## Le problème

Certaines données ne tiennent pas dans un filtre de recherche : il faut aller chercher une information précise, la vérifier, la sourcer. Fait à la main, c'est une recherche web par entité.

## Ce que vous obtenez

Une fiche markdown : les champs que vous avez demandés (selon votre schéma), la réponse en clair, un score de confiance et les sources citées.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-recherche-ia` en `config.yaml`.
3. Écrivez votre `prompt` et, si vous voulez une sortie exploitable, décrivez les champs voulus dans un schéma JSON.
4. Lancez le skill (ou via le MCP Airscale, outil `airscale_airsearch`).

## Coût

Facturé à l'usage par Airscale (~1 à 2 crédits par requête).

## Adapter à votre cas

- Donnée unique : laissez le schéma vide, vous recevez la réponse en texte source.
- Extraction multi-champs : décrivez les champs pour une sortie directement exploitable.
- En masse : bouclez sur une liste d'entités plutôt que de poser la question une par une à la main.

> Exemple de sortie réelle : `examples/recherche-ia.md` dans le repo.
