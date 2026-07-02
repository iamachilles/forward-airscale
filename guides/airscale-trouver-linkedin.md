---
title: "Retrouver les URLs LinkedIn manquantes"
tool: airscale
famille: "Enrichissement"
slug: airscale-trouver-linkedin
skill: airscale-trouver-linkedin
description: "Complétez un fichier où il manque les profils LinkedIn, à partir du prénom, du nom et de l'entreprise."
reading_time: 2
---

# Retrouver les URLs LinkedIn manquantes

## En bref

Vous avez des contacts (prénom, nom, entreprise) mais pas leurs profils LinkedIn. Le skill les retrouve, ligne par ligne.

## Le problème

Beaucoup d'enrichissements (email, téléphone) partent de l'URL LinkedIn. Un fichier qui ne l'a pas est bloqué à l'entrée. Et un export de salon ou de webinaire arrive rarement avec le LinkedIn.

## Ce que vous obtenez

Votre CSV d'origine, plus une colonne `linkedin_url`. C'est souvent le prérequis des autres skills "coordonnées".

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-trouver-linkedin` en `config.yaml`.
3. Pointez `input_csv` vers votre fichier et indiquez les colonnes prénom, nom, entreprise.
4. Lancez le skill (ou via le MCP Airscale).

## Coût

Facturé à l'usage par Airscale (par recherche d'URL).

## Adapter à votre cas

- Avant un enrichissement : enchaînez ce skill puis l'enrichissement email ou téléphone.
- Liste événement : transformez un fichier nom + société en profils exploitables.

> Exemple de sortie réelle : `examples/trouver-linkedin.csv` dans le repo.
