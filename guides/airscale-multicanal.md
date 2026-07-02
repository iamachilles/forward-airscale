---
title: "Coordonnées complètes pour une séquence multicanal"
tool: airscale
famille: "Coordonnées"
slug: airscale-multicanal
skill: airscale-multicanal
description: "Récupérez en un passage l'email pro, l'email perso et le mobile d'une liste de contacts, pour une séquence qui combine les canaux."
reading_time: 2
---

# Coordonnées complètes pour une séquence multicanal

## En bref

Pour chaque contact (par URL LinkedIn), le skill récupère d'un coup l'email pro, l'email perso et le mobile. De quoi lancer une séquence qui alterne les canaux.

## Le problème

Une bonne séquence touche le prospect sur plusieurs canaux. Mais réunir les trois coordonnées demande d'habitude trois outils différents et trois passages.

## Ce que vous obtenez

Votre CSV d'origine, plus les colonnes `email`, `personal_email`, `phone`. Vous choisissez les canaux à récupérer.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-multicanal` en `config.yaml`.
3. Pointez `input_csv` vers vos profils LinkedIn et choisissez les `channels`.
4. Lancez le skill (ou via le MCP Airscale).

## Coût

Facturé à l'usage : la somme des canaux demandés par contact. Le téléphone est le plus cher : réservez-le aux contacts à forte valeur.

## Adapter à votre cas

- Budget serré : limitez aux emails, ajoutez le mobile seulement sur les prioritaires.
- Approche moins corporate : email perso + mobile.

> Exemple de sortie réelle : `examples/multicanal.csv` dans le repo.
