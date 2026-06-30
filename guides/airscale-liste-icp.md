---
title: "Une liste de prospects ICP a la demande"
tool: airscale
famille: "Sourcing"
slug: airscale-liste-icp
skill: airscale-liste-icp
description: "Generez une liste de prospects correspondant a votre client ideal, avec leur entreprise et leur LinkedIn, en une commande."
reading_time: 3
---

# Une liste de prospects ICP a la demande

## En bref

Vous decrivez votre client ideal (fonctions, zone, mots-cles) et vous obtenez une liste de prospects prete a importer : nom, poste, entreprise, taille, secteur, URL LinkedIn.

## Le probleme

Construire une liste de cibles a la main, c'est des heures sur LinkedIn et des exports a recoller, avant meme d'avoir parle a qui que ce soit. Et la liste est perimee le mois suivant.

## Ce que vous obtenez

Un CSV importable dans votre CRM, une ligne par decideur : `firstname, lastname, jobTitle, companyName, companySize, companyIndustry, profileUrl`. Le volume disponible est affiche avant que vous ne payiez quoi que ce soit.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/ColinDargent/forward-airscale) et installez-le (voir le README).
2. Copiez `config.example.yaml` du skill `airscale-liste-icp` en `config.yaml`.
3. Renseignez vos filtres : `job_titles`, `locations`, `keywords`, `size`.
4. Lancez le skill (ou demandez a votre IA branchee sur le MCP Airscale de le faire).

## Cout

Facture a l'usage par Airscale (~0,1 credit par prospect retourne). Le comptage prealable est gratuit : vous connaissez le volume avant de lancer.

## Adapter a votre cas

- Sourcing de partenaires ou revendeurs : visez les fonctions "partenariats".
- Sourcing par techno ou secteur : ajoutez des mots-cles (ex : un CRM, un secteur).
- Zone fine : pays, region ou ville.

> Exemple de sortie reelle : `examples/liste-icp.csv` dans le repo.
