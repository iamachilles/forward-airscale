---
title: "Les comptes en signal d'achat"
tool: airscale
famille: "Sourcing"
slug: airscale-signaux-achat
skill: airscale-signaux-achat
description: "Sortez la liste des entreprises qui viennent de lever des fonds ou dont une equipe grossit, avec les decideurs a contacter."
reading_time: 3
---

# Les comptes en signal d'achat

## En bref

Vous ciblez des entreprises avec un declencheur recent (levee de fonds, equipe qui recrute) et vous obtenez la liste des comptes chauds plus leurs decideurs.

## Le probleme

Demarcher tout le monde au meme moment, c'est gaspiller son energie. Les comptes qui viennent de lever ou qui structurent une equipe sont ceux qui achetent, mais reperer ce signal a la main est impossible a l'echelle.

## Ce que vous obtenez

Un CSV : `company, industry, companySize, signal, firstname, lastname, jobTitle, profileUrl`. La colonne `signal` indique ce qui a declenche l'inclusion (ex : "Levee de fonds < 6 mois").

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-signaux-achat` en `config.yaml`.
3. Reglez le signal : `funding` + `funding_date_months`, ou `growth_department`, plus vos filtres (secteur, taille, zone).
4. Lancez le skill (ou via le MCP Airscale).

## Cout

Facture a l'usage (~0,1 credit par lead). La previsualisation du volume est gratuite.

## Adapter a votre cas

- Pur intent "levee" : `funding: true`, `funding_date_months: 3`.
- Pur intent "ca recrute" : `growth_department: "Sales"`.
- Comptes ABM : combinez secteur + taille + signal pour resserrer.

> Exemple de sortie reelle : `examples/signaux-achat.csv` dans le repo.
