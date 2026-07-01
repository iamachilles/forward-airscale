---
title: "Coordonnees completes pour une sequence multicanal"
tool: airscale
famille: "Coordonnees"
slug: airscale-multicanal
skill: airscale-multicanal
description: "Recuperez en un passage l'email pro, l'email perso et le mobile d'une liste de contacts, pour une sequence qui combine les canaux."
reading_time: 2
---

# Coordonnees completes pour une sequence multicanal

## En bref

Pour chaque contact (par URL LinkedIn), le skill recupere d'un coup l'email pro, l'email perso et le mobile. De quoi lancer une sequence qui alterne les canaux.

## Le probleme

Une bonne sequence touche le prospect sur plusieurs canaux. Mais reunir les trois coordonnees demande d'habitude trois outils differents et trois passages.

## Ce que vous obtenez

Votre CSV d'origine, plus les colonnes `email`, `personal_email`, `phone`. Vous choisissez les canaux a recuperer.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-multicanal` en `config.yaml`.
3. Pointez `input_csv` vers vos profils LinkedIn et choisissez les `channels`.
4. Lancez le skill (ou via le MCP Airscale).

## Cout

Facture a l'usage : la somme des canaux demandes par contact. Le telephone est le plus cher : reservez-le aux contacts a forte valeur.

## Adapter a votre cas

- Budget serre : limitez aux emails, ajoutez le mobile seulement sur les prioritaires.
- Approche moins corporate : email perso + mobile.

> Exemple de sortie reelle : `examples/multicanal.csv` dans le repo.
