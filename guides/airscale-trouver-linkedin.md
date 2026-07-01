---
title: "Retrouver les URLs LinkedIn manquantes"
tool: airscale
famille: "Enrichissement"
slug: airscale-trouver-linkedin
skill: airscale-trouver-linkedin
description: "Completez un fichier ou il manque les profils LinkedIn, a partir du prenom, du nom et de l'entreprise."
reading_time: 2
---

# Retrouver les URLs LinkedIn manquantes

## En bref

Vous avez des contacts (prenom, nom, entreprise) mais pas leurs profils LinkedIn. Le skill les retrouve, ligne par ligne.

## Le probleme

Beaucoup d'enrichissements (email, telephone) partent de l'URL LinkedIn. Un fichier qui ne l'a pas est bloque a l'entree. Et un export de salon ou de webinaire arrive rarement avec le LinkedIn.

## Ce que vous obtenez

Votre CSV d'origine, plus une colonne `linkedin_url`. C'est souvent le prerequis des autres skills "coordonnees".

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-trouver-linkedin` en `config.yaml`.
3. Pointez `input_csv` vers votre fichier et indiquez les colonnes prenom, nom, entreprise.
4. Lancez le skill (ou via le MCP Airscale).

## Cout

Facture a l'usage par Airscale (par recherche d'URL).

## Adapter a votre cas

- Avant un enrichissement : enchainez ce skill puis l'enrichissement email ou telephone.
- Liste evenement : transformez un fichier nom + societe en profils exploitables.

> Exemple de sortie reelle : `examples/trouver-linkedin.csv` dans le repo.
