---
title: "Le kit Airscale"
tool: airscale
type: famille
slug: airscale
description: "11 cas d'usage prêts à l'emploi pour transformer Airscale en résultats commerciaux : listes ICP, décideurs de comptes, emails et téléphones vérifiés, fiches enrichies, hygiène de CRM."
---

# Le kit Airscale (11 cas)

Airscale est une plateforme de **sourcing et d'enrichissement de leads** (façon Clay) branchée sur 50+ fournisseurs de données. On a packagé nos cas d'usage préférés : pour chacun, un guide côté business et un skill côté technique que vous (ou votre IA) branchez en quelques minutes.

> Le guide explique le quoi et le pourquoi. Le repo ([forward-airscale](https://github.com/iamachilles/forward-airscale)) contient le skill, le script et un exemple réel.

## Pourquoi un outil dédié plutôt que des exports manuels

- **Plus complet** : 50+ fournisseurs interrogés en cascade, pour maximiser la couverture email et téléphone.
- **Plus rapide** : une liste ICP ou un fichier enrichi en une commande, pas en une après-midi.
- **Facturé à l'usage** : vous payez les leads retournés ou enrichis, pas un abonnement de plus. Le comptage est gratuit (vous savez le volume avant de payer).
- **Pilotable par votre IA** : via le serveur MCP Airscale, votre assistant interroge l'outil tout seul.

## Les 11 cas, en 4 familles

### Sourcing
- **[Une liste de prospects ICP à la demande](airscale-liste-icp.md)** : vos cibles (fonctions, zone, mots-clés) avec entreprise et LinkedIn.
- **[Les décideurs de tes comptes cibles](airscale-decideurs-comptes.md)** : à partir de ta liste de comptes, les bons interlocuteurs dans chacun.
- **[Une liste prête à séquencer, de bout en bout](airscale-pipeline-outbound.md)** : sourcing ICP et coordonnées complètes en une seule commande.

### Coordonnées
- **[Enrichir un fichier en emails pro vérifiés](airscale-emails-fichier.md)** : votre liste rendue actionnable.
- **[Les mobiles pour le cold calling](airscale-telephones.md)** : les numéros de vos décideurs.
- **[Coordonnées complètes pour une séquence multicanal](airscale-multicanal.md)** : email pro + email perso + mobile.

### Enrichissement
- **[Une fiche entreprise enrichie](airscale-fiche-entreprise.md)** : firmographie + décideurs clés d'un compte.
- **[Retrouver les URLs LinkedIn manquantes](airscale-trouver-linkedin.md)** : réconcilier un fichier avant de l'enrichir.
- **[Rafraîchir et nettoyer votre CRM](airscale-hygiene-crm.md)** : postes et entreprises à jour, changements de boîte détectés, emails périmés repérés.

### Identification
- **[Qui se cache derrière un email ou un numéro](airscale-reverse-lookup.md)** : le profil complet, pour qualifier un entrant.
- **[Une réponse data structurée à la demande](airscale-recherche-ia.md)** : l'agent de recherche IA d'Airscale.

## Comment démarrer

1. Récupérez votre clé API sur [app.airscale.io](https://app.airscale.io) (onglet API).
2. Clonez [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez (voir le README).
3. Choisissez un cas, remplissez son `config.yaml`, lancez.
4. Ou, sans rien installer : branchez le [serveur MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) dans votre Claude et demandez-lui de suivre le skill.

> Besoin qu'on le branche sur vos vraies données ? [Prenons rendez-vous](https://www.forward-ai.fr).
