---
title: "Une fiche entreprise enrichie"
tool: airscale
famille: "Enrichissement"
slug: airscale-fiche-entreprise
skill: airscale-fiche-entreprise
description: "A partir de l'URL LinkedIn d'une entreprise, obtenez sa firmographie et ses decideurs cles dans une fiche prete a lire."
reading_time: 3
---

# Une fiche entreprise enrichie

## En bref

Vous collez l'URL LinkedIn d'une entreprise et vous recevez une fiche : secteur, taille, site, description, plus ses decideurs cles avec leur LinkedIn.

## Le probleme

Avant une approche ABM ou pour qualifier un compte entrant, il faut rassembler la firmographie et identifier les bons interlocuteurs. Fait a la main, c'est dix onglets ouverts par compte.

## Ce que vous obtenez

Une fiche markdown : un bloc firmographie (secteur, taille, site, description) et un tableau des decideurs (nom, poste, LinkedIn).

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-fiche-entreprise` en `config.yaml`.
3. Renseignez l'URL LinkedIn de l'entreprise et les fonctions des decideurs voulus.
4. Lancez le skill (ou via le MCP Airscale).

## Cout

Facture a l'usage : un enrichissement entreprise plus ~0,1 credit par decideur retourne.

## Adapter a votre cas

- Qualification entrante : decidez vite si un lead est dans votre ICP.
- Cartographie de compte : montez le nombre de contacts et elargissez les fonctions pour mapper le comite d'achat.

> Exemple de sortie reelle : `examples/fiche-entreprise.md` dans le repo.
