# forward-airscale - rapport de build (Jalon 1)

Construit le 2026-06-30 par Claude, en autonomie, calqué sur le repo [`forward-linkup`](https://github.com/ColinDargent/forward-linkup) de Colin. Tout est local dans le vault, **rien n'a été poussé ni publié**.

## Ce qui est fait

| Livrable | Etat | Ou |
|---|---|---|
| Repo technique (9 skills + lib + scripts) | OK | `.claude/skills/airscale-*`, `lib/airscale_helpers.py` |
| Couche partagee `requests` (auth, backoff 429, preflights gratuits) | OK | `lib/airscale_helpers.py` |
| README + template + LICENSE + .env.example + .gitignore + requirements | OK | racine |
| Exemples reels (1 run par skill) | OK | `examples/` (+ `_run-log.md`) |
| Guides business (9 + index) | OK | `guides/` |
| Note de portage site | OK | `site/README.md` |
| Post LinkedIn d'annonce (draft FR) | OK | `shared/content/linkedin/achille/2026-06-30-kit-airscale-9-skills.md` |
| Deck partageable (HTML + PDF, charte Forward) | OK | `deck/kit-airscale.html` + `.pdf` (6 pages) |

## Les 11 skills (4 familles)

Sourcing : `airscale-liste-icp`, `airscale-decideurs-comptes`, `airscale-pipeline-outbound`.
Coordonnées : `airscale-emails-fichier`, `airscale-telephones`, `airscale-multicanal`.
Enrichissement : `airscale-fiche-entreprise`, `airscale-trouver-linkedin`, `airscale-hygiene-crm`.
Identification : `airscale-reverse-lookup`, `airscale-recherche-ia`.

Chaque skill : `SKILL.md` (8 sections, mode script + mode MCP) + `config.example.yaml` + `scripts/run.py` (+ input/schema d'exemple). Les 14 endpoints REST Airscale sont couverts.

## Validation

- Tous les scripts compilent (`py_compile`).
- Smoke test offline (post mocké, zéro réseau) : 9/9 OK.
- Préflights gratuits sur la vraie clé : solde + `/find-people/count` + `/leads-finder/preview` confirmés.
- Exemples réels générés : 9/9, vraies données (emails valides, mobiles, fiches, reverse, airsearch sourcé).

## Cout

**~15 credits Airscale** au total (solde 6354 -> 6339), bien sous le cap de 25 fixé. Aucun run de test à vide. Détail dans `examples/_run-log.md`.

## Decisions notables

- **Scripts en REST `requests`**, pas via le MCP : pas de SDK Python Airscale, et surtout le volume doit rester déterministe (cron, zéro token), comme le choix de Colin pour Linkup. Le MCP Airscale est intégré comme **chemin agent / ad hoc** (mapping endpoint -> outil MCP dans chaque SKILL.md).
- **Pas de duplication MDX** : la source de contenu reste `guides/` (frontmatter Astro-ready) ; le mapping vers le schema de collection du site se fait cote `site-forward`.

## Fait depuis (2026-06-30, après le build local)

1. **Push GitHub** : repo poussé en **privé** sur `github.com/iamachilles/forward-airscale` (le token n'a pas les droits sur l'org ColinDargent ; gh CLI = compte iamachilles). 64 fichiers, branche `main`.
2. **Integration site** : faite et poussée en **PR** sur `site-forward` -> [ColinDargent/site-forward#13](https://github.com/ColinDargent/site-forward/pull/13). Famille `airscale` + 4 thèmes dans `families.ts`, 9 cas en MDX, générateur de pages `/cas-d-usage/airscale/[slug]`. `npm run build` + `validate-schema` OK (9 pages cas + page famille + carte sur le hub). **Non mergée** (le merge déploie sur Vercel).

## Décision : le repo vit sous iamachilles

Pas d'org Forward, donc le kit reste sous **`github.com/iamachilles/forward-airscale`** (public, 2026-07-01). Les liens du repo et du site pointent tous dessus. `forward-linkup`/`forward-unipile` restent chez ColinDargent, airscale est chez Achille : assumé.

## Fait depuis (2026-07-01)

- **Accents FR** posés dans tout le repo (README, SKILL.md, guides, lib, run.py, configs, deck) : demande d'Achille, divergence assumée avec `forward-linkup` (ASCII). Fait via 4 sous-agents + relecture.
- **2 skills composites ajoutés** (portant le kit de 9 à 11), suite à l'analyse "endpoint-shaped vs job-shaped" : `airscale-pipeline-outbound` (sourcing ICP + waterfall coordonnées en un job -> liste prête à séquencer) et `airscale-hygiene-crm` (ré-enrichit un export CRM : postes/entreprises à jour, changement de boîte, emails périmés). Exemples réels générés (pipeline : 2 leads complets ; hygiène : changement Fishtown Analytics -> dbt Labs détecté). `/profile` a un shape imbriqué (`positionGroups.contents[0].company.name`), extraction corrigée en conséquence.
- Guides + `guides/index.md` + README + `site/README.md` mis à jour à 11 cas. Smoke test offline 11/11 OK.
- **`signaux-achat` retiré, remplacé par `airscale-decideurs-comptes`.** Audit API : le filtre `funding`/`growth`/`industry` du leads-finder est **ignoré par Airscale** (mêmes totaux avec/sans ; seuls `job` et `peopleLocation` filtrent) et le champ `financial` ne porte qu'une fourchette de CA, aucune donnée de levée. Le cas signaux-achat fabriquait donc un signal non vérifié. Remplacé par un vrai job ABM : les décideurs de tes comptes cibles via `/find-people` + `companyDomain` (filtre vérifié : Qonto/PayFit/Spendesk renvoient les bons décideurs). Le kit reste à 11 cas. Site : PR #14 met à jour (+3 nouveaux, -signaux).

## Reste a faire

1. **Débloquer le déploiement Vercel** : la PR #13 est **mergée sur `main`** (commit `6c9207b`), mais Vercel a **bloqué le déploiement de prod** ("Deployment was blocked", car le commit vient de `iamachilles` et pas de Colin). Les pages airscale sont en 404 sur le site tant que Colin ne relance pas le déploiement (bouton "Redeploy" sur `main`, ou autoriser iamachilles comme auteur de déploiement dans les réglages Vercel du projet). Seul point qui dépend vraiment de Colin (pas d'accès Vercel côté Achille : ni token `.env`, ni CLI).
2. **Confirmer les noms d'outils MCP** d'enrichissement/export + le cout airsearch via MCP (annoncé 2 crédits vs 1 en REST). Non bloquant. Mettre à jour les SKILL.md ensuite.
3. **Publier le post LinkedIn** (`status: draft` -> `scheduled` -> `published`).
4. **Partager le deck** (`deck/kit-airscale.pdf`).

## Rollback

Tout est nouveau et local : `rm -rf shared/repos/forward-airscale` + `git checkout shared/repos/CLAUDE.md` + supprimer le draft LinkedIn et le message `shared/claude/pour-colin/`. Rien hors du vault n'a été touché (aucun push, aucune publication).
