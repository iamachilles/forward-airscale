# Journal des runs d'exemples

Les fichiers de ce dossier sont des **sorties reelles** des skills, generees une fois
pour servir d'illustration (cibles publiques). Ils ne se regenerent pas a chaque usage.

| Skill | Exemple | Endpoints reels appeles | Resultat |
|---|---|---|---|
| airscale-liste-icp | liste-icp.csv | find-people/count + find-people (10) | 10 Head of Sales FR |
| airscale-signaux-achat | signaux-achat.csv | leads-finder/preview + leads-finder (10) | 10 CEO de boites ayant leve < 6 mois |
| airscale-emails-fichier | emails-fichier.csv | email x3 | 2/3 emails pro verifies |
| airscale-telephones | telephones.csv | phone x2 | 1/2 mobiles |
| airscale-multicanal | multicanal.csv | email + personal-email + phone | email perso + mobile trouves |
| airscale-fiche-entreprise | fiche-entreprise.md | company + find-people | firmographie + 2 decideurs |
| airscale-trouver-linkedin | trouver-linkedin.csv | url-search-people x3 | 3/3 URLs |
| airscale-reverse-lookup | reverse-lookup.md | reverse-email | profil complet |
| airscale-recherche-ia | recherche-ia.md | airsearch | CEO + annee de creation, source citee |

**Cout total : ~15 credits Airscale** (solde 6354 -> 6339), tres en dessous du cap de 25
fixe pour cette generation. Compteur de credits et preflights (/count, /preview) gratuits.

> Pour regenerer un exemple : `python .claude/skills/<skill>/scripts/run.py --config <skill>/config.example.yaml`.
> Pense au cout : chaque run consomme des credits reels.
