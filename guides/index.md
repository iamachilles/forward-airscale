---
title: "Le kit Airscale"
tool: airscale
type: famille
slug: airscale
description: "9 cas d'usage prets a l'emploi pour transformer Airscale en resultats commerciaux : listes ICP, signaux d'achat, emails et telephones verifies, fiches enrichies."
---

# Le kit Airscale (9 cas)

Airscale est une plateforme de **sourcing et d'enrichissement de leads** (facon Clay) branchee sur 50+ fournisseurs de donnees. On a packagé nos 9 cas d'usage preferes : pour chacun, un guide cote business et un skill cote technique que vous (ou votre IA) branchez en quelques minutes.

> Le guide explique le quoi et le pourquoi. Le repo ([forward-airscale](https://github.com/iamachilles/forward-airscale)) contient le skill, le script et un exemple reel.

## Pourquoi un outil dedie plutot que des exports manuels

- **Plus complet** : 50+ fournisseurs interroges en cascade, pour maximiser la couverture email et telephone.
- **Plus rapide** : une liste ICP ou un fichier enrichi en une commande, pas en une apres-midi.
- **Facture a l'usage** : vous payez les leads retournes ou enrichis, pas un abonnement de plus. Le comptage est gratuit (vous savez le volume avant de payer).
- **Pilotable par votre IA** : via le serveur MCP Airscale, votre assistant interroge l'outil tout seul.

## Les 9 cas, en 4 familles

### Sourcing
- **[Une liste de prospects ICP a la demande](airscale-liste-icp.md)** : vos cibles (fonctions, zone, mots-cles) avec entreprise et LinkedIn.
- **[Les comptes en signal d'achat](airscale-signaux-achat.md)** : entreprises qui viennent de lever des fonds ou dont une equipe grossit.

### Coordonnees
- **[Enrichir un fichier en emails pro verifies](airscale-emails-fichier.md)** : votre liste rendue actionnable.
- **[Les mobiles pour le cold calling](airscale-telephones.md)** : les numeros de vos decideurs.
- **[Coordonnees completes pour une sequence multicanal](airscale-multicanal.md)** : email pro + email perso + mobile.

### Enrichissement
- **[Une fiche entreprise enrichie](airscale-fiche-entreprise.md)** : firmographie + decideurs cles d'un compte.
- **[Retrouver les URLs LinkedIn manquantes](airscale-trouver-linkedin.md)** : reconcilier un fichier avant de l'enrichir.

### Identification
- **[Qui se cache derriere un email ou un numero](airscale-reverse-lookup.md)** : le profil complet, pour qualifier un entrant.
- **[Une reponse data structuree a la demande](airscale-recherche-ia.md)** : l'agent de recherche IA d'Airscale.

## Comment demarrer

1. Recuperez votre cle API sur [app.airscale.io](https://app.airscale.io) (onglet API).
2. Clonez [forward-airscale](https://github.com/iamachilles/forward-airscale) et installez (voir le README).
3. Choisissez un cas, remplissez son `config.yaml`, lancez.
4. Ou, sans rien installer : branchez le [serveur MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) dans votre Claude et demandez-lui de suivre le skill.

> Besoin qu'on le branche sur vos vraies donnees ? [Prenons rendez-vous](https://www.forward-ai.fr).
