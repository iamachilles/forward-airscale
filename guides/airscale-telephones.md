---
title: "Les mobiles pour le cold calling"
tool: airscale
famille: "Coordonnees"
slug: airscale-telephones
skill: airscale-telephones
description: "Recuperez le numero de mobile d'une liste de decideurs a partir de leurs profils LinkedIn."
reading_time: 2
---

# Les mobiles pour le cold calling

## En bref

Vous avez une liste de profils LinkedIn et vous voulez ajouter le canal telephone. Le skill recupere le mobile de chacun.

## Le probleme

L'email seul ne suffit pas toujours. Mais trouver des mobiles fiables, profil par profil, est lent et la qualite des numeros varie enormement d'une source a l'autre.

## Ce que vous obtenez

Votre CSV d'origine, plus les colonnes `phone` et `provider`. Une ligne en echec n'arrete pas le reste du fichier.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/ColinDargent/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-telephones` en `config.yaml`.
3. Pointez `input_csv` vers votre fichier et indiquez la colonne LinkedIn.
4. Lancez le skill (ou via le MCP Airscale).

## Cout

Facture a l'usage (enrichissement telephone par contact, en general plus cher que l'email). Reservez-le aux contacts deja qualifies.

## Adapter a votre cas

- Enchainez-le apres une liste ICP (colonne `profileUrl`).
- Priorisez les comptes chauds avant de consommer des credits telephone.

> Exemple de sortie reelle : `examples/telephones.csv` dans le repo.
