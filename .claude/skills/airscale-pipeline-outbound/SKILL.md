---
name: airscale-pipeline-outbound
description: Use when you want a ready-to-sequence prospect list end-to-end. Input = ICP filters + channels in config.yaml, output = a CSV of contacts with email, phone and personal email already enriched.
---

# Une liste prête à séquencer, de bout en bout

## Objectif & quand

**Produire** en une seule commande une liste directement actionnable : on source les prospects qui correspondent à ton client idéal (fonctions, zone, mots-clés), puis on récupère leurs coordonnées (email pro, mobile, email perso) dans la foulée. À lancer quand tu veux passer d'un ICP à une liste importable dans ton outil de séquençage sans enchaîner plusieurs étapes.

> C'est la valeur de ce skill : au lieu de lancer `airscale-liste-icp` puis `airscale-multicanal` à la suite, un seul job compose le sourcing et le waterfall de coordonnées et écrit un CSV prêt à séquencer.

## Prérequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) branché dans ton IA (outils `airscale_find_people` + outils d'enrichissement).

## Config

| Champ | Rôle | Exemple |
|---|---|---|
| `job_titles` | Fonctions ciblées (include) | `["Head of Sales", "VP Sales"]` |
| `exclude_titles` | Fonctions à exclure | `["Assistant"]` |
| `locations` | Zones géographiques | `["France"]` |
| `keywords` | Mots-clés cherchés dans tout le profil | `["SaaS"]` |
| `size` | Nombre de cibles à sourcer (1-100) | `10` |
| `channels` | Canaux à récupérer (parmi `email`, `phone`, `personal_email`) | `["email", "phone", "personal_email"]` |
| `output_path` | CSV de sortie | `null` |

## Adapter à ton cas

- **Coordonnées légères** : ne garde que `email` dans `channels` pour limiter les crédits (une seule requête d'enrichissement par lead au lieu de trois).
- **Sourcing par techno ou secteur** : ajoute des `keywords` (ex `["Salesforce"]`, `["fintech"]`).
- **Zone fine** : `locations` accepte pays, région ou ville (ex `["Lyon"]`).
- **Volume** : `size` pilote combien de leads sont sourcés (donc combien de waterfalls seront lancés ensuite).

## Procédure

1. **Preflight gratuit** : `/find-people/count` sur le `query` construit, pour connaître le volume avant de payer.
2. `/find-people` avec `query` = `{ JobTitle:{include,exclude}, location:{include}, keyword:{include} }` et `size`. Récupère `resp.leads`.
3. **Waterfall par lead** : pour chaque lead sourcé, sur son `profileUrl`, appelle les `channels` demandés : `/email`, `/phone`, `/personal-email` (corps `{ "linkedin_profile_url": profileUrl }`). Un canal qui échoue laisse le champ vide sans casser le batch.
4. Écriture d'un CSV prêt à séquencer.

> Mapping MCP : `/find-people` -> `airscale_find_people`, `/find-people/count` -> `airscale_count_find_people`. Les endpoints d'enrichissement `/email`, `/phone`, `/personal-email` correspondent aux outils d'enrichissement du MCP (noms exacts à confirmer depuis le serveur MCP).

## Livrable

Un CSV `examples/pipeline-outbound.csv`, une ligne par prospect prêt à importer : `firstname, lastname, jobTitle, companyName, profileUrl, email, phone, personal_email`.

## Coût estimé

Facturé à l'usage par Airscale. Ce skill combine **1 sourcing** (~0,1 crédit / lead retourné) **+ N x canaux enrichissements** (une requête par canal et par lead), donc il coûte plus cher qu'un sourcing seul. Le comptage `/find-people/count` est **gratuit** : compte toujours le volume avant de lancer, et réduis `channels` si tu veux limiter la facture. Voir le [pricing Airscale](https://app.airscale.io).

## Exemple

Voir `examples/pipeline-outbound.csv`.
