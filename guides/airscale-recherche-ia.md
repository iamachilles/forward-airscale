---
title: "Une reponse data structuree a la demande"
tool: airscale
famille: "Identification"
slug: airscale-recherche-ia
skill: airscale-recherche-ia
description: "Posez une question en langage naturel et recevez une reponse structuree (champs typés) avec son score de confiance et ses sources."
reading_time: 3
---

# Une reponse data structuree a la demande

## En bref

Vous posez une question precise ("qui est le CEO et l'annee de creation de telle societe ?") et l'agent de recherche d'Airscale renvoie une reponse structuree, avec sa confiance et ses sources.

## Le probleme

Certaines donnees ne tiennent pas dans un filtre de recherche : il faut aller chercher une information precise, la verifier, la sourcer. Fait a la main, c'est une recherche web par entite.

## Ce que vous obtenez

Une fiche markdown : les champs que vous avez demandes (selon votre schema), la reponse en clair, un score de confiance et les sources citees.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/ColinDargent/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-recherche-ia` en `config.yaml`.
3. Ecrivez votre `prompt` et, si vous voulez une sortie exploitable, decrivez les champs voulus dans un schema JSON.
4. Lancez le skill (ou via le MCP Airscale, outil `airscale_airsearch`).

## Cout

Facture a l'usage par Airscale (~1 a 2 credits par requete).

## Adapter a votre cas

- Donnee unique : laissez le schema vide, vous recevez la reponse en texte source.
- Extraction multi-champs : decrivez les champs pour une sortie directement exploitable.
- En masse : bouclez sur une liste d'entites plutot que de poser la question une par une a la main.

> Exemple de sortie reelle : `examples/recherche-ia.md` dans le repo.
