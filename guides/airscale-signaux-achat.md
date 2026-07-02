---
title: "Les comptes en signal d'achat"
tool: airscale
famille: "Sourcing"
slug: airscale-signaux-achat
skill: airscale-signaux-achat
description: "Sortez la liste des entreprises qui viennent de lever des fonds ou dont une équipe grossit, avec les décideurs à contacter."
reading_time: 3
---

# Les comptes en signal d'achat

## En bref

Vous ciblez des entreprises avec un déclencheur récent (levée de fonds, équipe qui recrute) et vous obtenez la liste des comptes chauds plus leurs décideurs.

## Le problème

Démarcher tout le monde au même moment, c'est gaspiller son énergie. Les comptes qui viennent de lever ou qui structurent une équipe sont ceux qui achètent, mais repérer ce signal à la main est impossible à l'échelle.

## Ce que vous obtenez

Un CSV : `company, industry, companySize, signal, firstname, lastname, jobTitle, profileUrl`. La colonne `signal` indique ce qui a déclenché l'inclusion (ex : "Levée de fonds < 6 mois").

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-signaux-achat` en `config.yaml`.
3. Réglez le signal : `funding` + `funding_date_months`, ou `growth_department`, plus vos filtres (secteur, taille, zone).
4. Lancez le skill (ou via le MCP Airscale).

## Coût

Facturé à l'usage (~0,1 crédit par lead). La prévisualisation du volume est gratuite.

## Adapter à votre cas

- Pur intent "levée" : `funding: true`, `funding_date_months: 3`.
- Pur intent "ça recrute" : `growth_department: "Sales"`.
- Comptes ABM : combinez secteur + taille + signal pour resserrer.

> Exemple de sortie réelle : `examples/signaux-achat.csv` dans le repo.
