---
title: "Enrichir un fichier en emails pro vérifiés"
tool: airscale
famille: "Coordonnées"
slug: airscale-emails-fichier
skill: airscale-emails-fichier
description: "Partez d'une liste de contacts (nom + société ou LinkedIn) et récupérez l'email professionnel vérifié de chacun."
reading_time: 3
---

# Enrichir un fichier en emails pro vérifiés

## En bref

Vous avez une liste de contacts sans email. Vous la passez au skill et vous récupérez l'email professionnel vérifié de chacun, prête pour la campagne.

## Le problème

Un fichier de prospects sans email n'est pas actionnable. Chercher les adresses une par une est interminable, et beaucoup d'outils renvoient des emails non vérifiés qui plombent la délivrabilité.

## Ce que vous obtenez

Votre CSV d'origine, plus trois colonnes : `email`, `email_status` (vérifié ou non), `provider`. Chaque contact est identifié par son URL LinkedIn ou par prénom + nom + domaine.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-emails-fichier` en `config.yaml`.
3. Pointez `input_csv` vers votre fichier et indiquez les colonnes (LinkedIn, ou prénom/nom/domaine).
4. Lancez le skill (ou via le MCP Airscale).

## Coût

Facturé à l'usage par Airscale (un enrichissement email par contact). La logique en cascade interroge plusieurs fournisseurs pour maximiser le taux de réussite.

## Adapter à votre cas

- Fichier 100% LinkedIn : remplissez seulement la colonne URL.
- Fichier nom + société : le domaine fiabilise le matching.
- Volume important : Airscale propose un mode bulk asynchrone pour les gros fichiers.

> Exemple de sortie réelle : `examples/emails-fichier.csv` dans le repo.
