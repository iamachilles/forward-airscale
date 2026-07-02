---
title: "Les mobiles pour le cold calling"
tool: airscale
famille: "Coordonnées"
slug: airscale-telephones
skill: airscale-telephones
description: "Récupérez le numéro de mobile d'une liste de décideurs à partir de leurs profils LinkedIn."
reading_time: 2
---

# Les mobiles pour le cold calling

## En bref

Vous avez une liste de profils LinkedIn et vous voulez ajouter le canal téléphone. Le skill récupère le mobile de chacun.

## Le problème

L'email seul ne suffit pas toujours. Mais trouver des mobiles fiables, profil par profil, est lent et la qualité des numéros varie énormément d'une source à l'autre.

## Ce que vous obtenez

Votre CSV d'origine, plus les colonnes `phone` et `provider`. Une ligne en échec n'arrête pas le reste du fichier.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-telephones` en `config.yaml`.
3. Pointez `input_csv` vers votre fichier et indiquez la colonne LinkedIn.
4. Lancez le skill (ou via le MCP Airscale).

## Coût

Facturé à l'usage (enrichissement téléphone par contact, en général plus cher que l'email). Réservez-le aux contacts déjà qualifiés.

## Adapter à votre cas

- Enchaînez-le après une liste ICP (colonne `profileUrl`).
- Priorisez les comptes chauds avant de consommer des crédits téléphone.

> Exemple de sortie réelle : `examples/telephones.csv` dans le repo.
