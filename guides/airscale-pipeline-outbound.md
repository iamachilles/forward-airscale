---
title: "Une liste prête à séquencer, de bout en bout"
tool: airscale
famille: "Sourcing"
slug: airscale-pipeline-outbound
skill: airscale-pipeline-outbound
description: "D'un ICP à une liste importable dans votre outil de séquençage, coordonnées comprises, en une seule commande."
reading_time: 3
---

# Une liste prête à séquencer, de bout en bout

## En bref

Vous décrivez votre client idéal et vous récupérez une liste de prospects déjà enrichie de leurs coordonnées (email pro, mobile, email perso). Importable directement dans votre outil de séquençage, sans étape intermédiaire.

## Le problème

Sourcer une liste, c'est une étape. Trouver les coordonnées de chacun, c'en est une autre. Les enchaîner à la main sur plusieurs outils, fichier après fichier, c'est ce qui transforme une bonne intention de prospection en après-midi perdue.

## Ce que vous obtenez

Un CSV prêt à séquencer, une ligne par prospect : `firstname, lastname, jobTitle, companyName, profileUrl, email, phone, personal_email`. Un seul job compose le sourcing ICP et le waterfall de coordonnées.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-pipeline-outbound` en `config.yaml`.
3. Renseignez vos filtres ICP (`job_titles`, `locations`, `keywords`, `size`) et les `channels` voulus.
4. Lancez le skill (ou via le MCP Airscale).

## Coût

Facturé à l'usage : un sourcing (~0,1 crédit par lead) plus les canaux d'enrichissement demandés par lead. Le comptage est gratuit : vérifiez le volume avant de lancer, et réduisez `channels` pour maîtriser la facture.

## Adapter à votre cas

- Coordonnées légères : gardez seulement `email` dans `channels`.
- Sourcing par techno ou secteur : ajoutez des mots-clés.
- Volume : `size` pilote le nombre de leads sourcés, donc de waterfalls lancés.

> Exemple de sortie réelle : `examples/pipeline-outbound.csv` dans le repo.
