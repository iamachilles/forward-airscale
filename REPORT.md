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

## Les 9 skills (4 familles)

Sourcing : `airscale-liste-icp`, `airscale-signaux-achat`.
Coordonnees : `airscale-emails-fichier`, `airscale-telephones`, `airscale-multicanal`.
Enrichissement : `airscale-fiche-entreprise`, `airscale-trouver-linkedin`.
Identification : `airscale-reverse-lookup`, `airscale-recherche-ia`.

Chaque skill : `SKILL.md` (8 sections, mode script + mode MCP) + `config.example.yaml` + `scripts/run.py` (+ input/schema d'exemple). Les 14 endpoints REST Airscale sont couverts.

## Validation

- Tous les scripts compilent (`py_compile`).
- Smoke test offline (post mocké, zéro réseau) : 9/9 OK.
- Préflights gratuits sur la vraie clé : solde + `/find-people/count` + `/leads-finder/preview` confirmés.
- Exemples reels generes : 9/9, vraies donnees (emails valides, mobiles, fiches, reverse, airsearch sourcé).

## Cout

**~15 credits Airscale** au total (solde 6354 -> 6339), bien sous le cap de 25 fixé. Aucun run de test à vide. Détail dans `examples/_run-log.md`.

## Decisions notables

- **Scripts en REST `requests`**, pas via le MCP : pas de SDK Python Airscale, et surtout le volume doit rester déterministe (cron, zéro token), comme le choix de Colin pour Linkup. Le MCP Airscale est intégré comme **chemin agent / ad hoc** (mapping endpoint -> outil MCP dans chaque SKILL.md).
- **Pas de duplication MDX** : la source de contenu reste `guides/` (frontmatter Astro-ready) ; le mapping vers le schema de collection du site se fait cote `site-forward`.

## Fait depuis (2026-06-30, après le build local)

1. **Push GitHub** : repo poussé en **privé** sur `github.com/iamachilles/forward-airscale` (le token n'a pas les droits sur l'org ColinDargent ; gh CLI = compte iamachilles). 64 fichiers, branche `main`.
2. **Integration site** : faite et poussée en **PR** sur `site-forward` -> [ColinDargent/site-forward#13](https://github.com/ColinDargent/site-forward/pull/13). Famille `airscale` + 4 thèmes dans `families.ts`, 9 cas en MDX, générateur de pages `/cas-d-usage/airscale/[slug]`. `npm run build` + `validate-schema` OK (9 pages cas + page famille + carte sur le hub). **Non mergée** (le merge déploie sur Vercel).

## Reste a faire (Jalon 2, avec Colin)

1. **Rendre `forward-airscale` public sous ColinDargent** (transfert depuis iamachilles, ou recréation) : les liens du site (`repoUrl`/`repo_url`) pointent déjà vers `iamachilles/forward-airscale`. **Prérequis au merge de la PR #13**, sinon les boutons "récupérer le dossier" donnent un 404.
2. **Merger la PR #13** une fois le repo public (déploie le kit sur le site).
3. **Confirmer les noms d'outils MCP** d'enrichissement/export depuis le serveur MCP live, et le cout exact d'airsearch via MCP (annoncé 2 crédits vs 1 en REST). Mettre à jour les SKILL.md.
4. **Publier le post LinkedIn** (passer `status: draft` -> `scheduled` -> `published`).
5. **Partager le deck** (`deck/kit-airscale.pdf`).

## Rollback

Tout est nouveau et local : `rm -rf shared/repos/forward-airscale` + `git checkout shared/repos/CLAUDE.md` + supprimer le draft LinkedIn et le message `shared/claude/pour-colin/`. Rien hors du vault n'a été touché (aucun push, aucune publication).
