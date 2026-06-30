---
title: "Enrichir un fichier en emails pro verifies"
tool: airscale
famille: "Coordonnees"
slug: airscale-emails-fichier
skill: airscale-emails-fichier
description: "Partez d'une liste de contacts (nom + societe ou LinkedIn) et recuperez l'email professionnel verifie de chacun."
reading_time: 3
---

# Enrichir un fichier en emails pro verifies

## En bref

Vous avez une liste de contacts sans email. Vous la passez au skill et vous recuperez l'email professionnel verifie de chacun, prete pour la campagne.

## Le probleme

Un fichier de prospects sans email n'est pas actionnable. Chercher les adresses une par une est interminable, et beaucoup d'outils renvoient des emails non verifies qui plombent la delivrabilite.

## Ce que vous obtenez

Votre CSV d'origine, plus trois colonnes : `email`, `email_status` (verifie ou non), `provider`. Chaque contact est identifie par son URL LinkedIn ou par prenom + nom + domaine.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/ColinDargent/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-emails-fichier` en `config.yaml`.
3. Pointez `input_csv` vers votre fichier et indiquez les colonnes (LinkedIn, ou prenom/nom/domaine).
4. Lancez le skill (ou via le MCP Airscale).

## Cout

Facture a l'usage par Airscale (un enrichissement email par contact). La logique en cascade interroge plusieurs fournisseurs pour maximiser le taux de reussite.

## Adapter a votre cas

- Fichier 100% LinkedIn : remplissez seulement la colonne URL.
- Fichier nom + societe : le domaine fiabilise le matching.
- Volume important : Airscale propose un mode bulk asynchrone pour les gros fichiers.

> Exemple de sortie reelle : `examples/emails-fichier.csv` dans le repo.
