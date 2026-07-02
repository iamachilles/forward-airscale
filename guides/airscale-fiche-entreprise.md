---
title: "Une fiche entreprise enrichie"
tool: airscale
famille: "Enrichissement"
slug: airscale-fiche-entreprise
skill: airscale-fiche-entreprise
description: "À partir de l'URL LinkedIn d'une entreprise, obtenez sa firmographie et ses décideurs clés dans une fiche prête à lire."
reading_time: 3
---

# Une fiche entreprise enrichie

## En bref

Vous collez l'URL LinkedIn d'une entreprise et vous recevez une fiche : secteur, taille, site, description, plus ses décideurs clés avec leur LinkedIn.

## Le problème

Avant une approche ABM ou pour qualifier un compte entrant, il faut rassembler la firmographie et identifier les bons interlocuteurs. Fait à la main, c'est dix onglets ouverts par compte.

## Ce que vous obtenez

Une fiche markdown : un bloc firmographie (secteur, taille, site, description) et un tableau des décideurs (nom, poste, LinkedIn).

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-fiche-entreprise` en `config.yaml`.
3. Renseignez l'URL LinkedIn de l'entreprise et les fonctions des décideurs voulus.
4. Lancez le skill (ou via le MCP Airscale).

## Coût

Facturé à l'usage : un enrichissement entreprise plus ~0,1 crédit par décideur retourné.

## Adapter à votre cas

- Qualification entrante : décidez vite si un lead est dans votre ICP.
- Cartographie de compte : montez le nombre de contacts et élargissez les fonctions pour mapper le comité d'achat.

> Exemple de sortie réelle : `examples/fiche-entreprise.md` dans le repo.
