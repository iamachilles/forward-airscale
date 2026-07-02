---
title: "Une liste de prospects ICP à la demande"
tool: airscale
famille: "Sourcing"
slug: airscale-liste-icp
skill: airscale-liste-icp
description: "Générez une liste de prospects correspondant à votre client idéal, avec leur entreprise et leur LinkedIn, en une commande."
reading_time: 3
---

# Une liste de prospects ICP à la demande

## En bref

Vous décrivez votre client idéal (fonctions, zone, mots-clés) et vous obtenez une liste de prospects prête à importer : nom, poste, entreprise, taille, secteur, URL LinkedIn.

## Le problème

Construire une liste de cibles à la main, c'est des heures sur LinkedIn et des exports à recoller, avant même d'avoir parlé à qui que ce soit. Et la liste est périmée le mois suivant.

## Ce que vous obtenez

Un CSV importable dans votre CRM, une ligne par décideur : `firstname, lastname, jobTitle, companyName, companySize, companyIndustry, profileUrl`. Le volume disponible est affiché avant que vous ne payiez quoi que ce soit.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le (voir le README).
2. Copiez `config.example.yaml` du skill `airscale-liste-icp` en `config.yaml`.
3. Renseignez vos filtres : `job_titles`, `locations`, `keywords`, `size`.
4. Lancez le skill (ou demandez à votre IA branchée sur le MCP Airscale de le faire).

## Coût

Facturé à l'usage par Airscale (~0,1 crédit par prospect retourné). Le comptage préalable est gratuit : vous connaissez le volume avant de lancer.

## Adapter à votre cas

- Sourcing de partenaires ou revendeurs : visez les fonctions "partenariats".
- Sourcing par techno ou secteur : ajoutez des mots-clés (ex : un CRM, un secteur).
- Zone fine : pays, région ou ville.

> Exemple de sortie réelle : `examples/liste-icp.csv` dans le repo.
