---
title: "Rafraîchir et nettoyer votre CRM"
tool: airscale
famille: "Enrichissement"
slug: airscale-hygiene-crm
skill: airscale-hygiene-crm
description: "Repassez sur un export CRM : postes et entreprises à jour, contacts qui ont changé de boîte détectés, emails périmés repérés."
reading_time: 3
---

# Rafraîchir et nettoyer votre CRM

## En bref

Vous partez d'un export CRM et vous le remettez à jour : le poste et l'entreprise actuels de chaque contact, un marqueur pour ceux qui ont changé de boîte, et un email pro frais pour repérer les adresses périmées.

## Le problème

Un CRM se périme tout seul. Les gens changent de poste, quittent leur entreprise, et leurs emails finissent par renvoyer des bounces. Une base non entretenue, c'est des campagnes qui tapent dans le vide et des signaux manqués.

## Ce que vous obtenez

Votre CSV d'origine, plus cinq colonnes : `current_title`, `current_company`, `changed_company`, `email`, `email_status`. Le marqueur `changed_company` est un signal fort : un contact qui a bougé, c'est un lead de départ ou un champion à suivre dans sa nouvelle boîte.

## Comment vous en servir

1. Clonez le repo [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez-le.
2. Copiez le `config.example.yaml` du skill `airscale-hygiene-crm` en `config.yaml`.
3. Pointez `input_csv` vers votre export et indiquez la colonne LinkedIn et la colonne entreprise connue.
4. Lancez le skill (ou via le MCP Airscale).

## Coût

Facturé à l'usage : un enrichissement profil plus un enrichissement email par ligne. Ciblez les segments à réactiver pour maîtriser le volume.

## Adapter à votre cas

- Détection de départ uniquement : filtrez sur `changed_company = yes`.
- Vérification d'emails uniquement : lisez `email_status` pour remplacer les adresses non vérifiées.
- Colonnes nommées autrement : pointez la configuration vers les noms réels de votre export.

> Exemple de sortie réelle : `examples/hygiene-crm.csv` dans le repo.
