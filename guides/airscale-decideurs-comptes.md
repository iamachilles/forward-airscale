---
title: "Les décideurs de vos comptes cibles"
tool: airscale
famille: "Sourcing"
slug: airscale-decideurs-comptes
skill: airscale-decideurs-comptes
description: "Vous avez votre liste de comptes ABM, mais pas les bons interlocuteurs dedans. Trouvez les décideurs de chaque compte, avec leur LinkedIn."
reading_time: 2
---

# Les décideurs de vos comptes cibles

## En bref

Vous partez de vos comptes cibles (leurs domaines) et vous obtenez, pour chacun, les décideurs à contacter avec leur poste et leur LinkedIn.

## Le problème

Vous avez votre liste de comptes ABM. Mais une liste d'entreprises ne se démarche pas : il faut le bon interlocuteur dans chacune. Le trouver compte par compte, à la main, c'est ce qui bloque le passage à l'action.

## Ce que vous obtenez

Un CSV, une ligne par décideur : `domain, firstname, lastname, jobTitle, companyName, profileUrl`. Vous choisissez les fonctions visées et le nombre de contacts par compte.

## Comment vous en servir

Tout est prêt dans un *repo* (dossier de code public, gratuit) :

1. **Récupérez le dossier** (bouton ci-dessous).
2. **Installez-le** (instructions fournies).
3. **Pointez vers votre liste de comptes** (colonne de domaines) et indiquez les fonctions visées.
4. **Lancez le cas d'usage**, vous-même ou via votre assistant IA.

## Coût

Facturé à l'usage par Airscale (~0,1 crédit par décideur retourné). Le nombre de comptes multiplié par le nombre de contacts par compte vous donne l'ordre de grandeur avant de lancer.

## Adapter à votre cas

- **Fonctions larges** : visez des tokens de séniorité (Head, VP, Chief, Director) plutôt qu'un intitulé exact qui varie d'une entreprise à l'autre.
- **Un département précis** : ajoutez un mot métier (Marketing, Finance, Data).
- **Domaines de plateforme** : évitez les domaines partagés par beaucoup d'entités (ils remontent des gens hors de l'entreprise) ; utilisez le domaine corporate du compte.

> Exemple de sortie réelle : `examples/decideurs-comptes.csv` dans le repo.
