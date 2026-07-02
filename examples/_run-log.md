# Journal des runs d'exemples

Les fichiers de ce dossier sont des **sorties réelles** des skills, générées une fois
pour servir d'illustration (cibles publiques). Ils ne se régénèrent pas à chaque usage.

| Skill | Exemple | Endpoints réels appelés | Résultat |
|---|---|---|---|
| airscale-liste-icp | liste-icp.csv | find-people/count + find-people (10) | 10 Head of Sales FR |
| airscale-decideurs-comptes | decideurs-comptes.csv | find-people x3 (un par domaine) | 9 décideurs sur 3 comptes (Qonto, PayFit, Spendesk) |
| airscale-emails-fichier | emails-fichier.csv | email x3 | 2/3 emails pro vérifiés |
| airscale-telephones | telephones.csv | phone x2 | 1/2 mobiles |
| airscale-multicanal | multicanal.csv | email + personal-email + phone | email perso + mobile trouvés |
| airscale-fiche-entreprise | fiche-entreprise.md | company + find-people | firmographie + 2 décideurs |
| airscale-trouver-linkedin | trouver-linkedin.csv | url-search-people x3 | 3/3 URLs |
| airscale-reverse-lookup | reverse-lookup.md | reverse-email | profil complet |
| airscale-recherche-ia | recherche-ia.md | airsearch | CEO + année de création, source citée |
| airscale-pipeline-outbound | pipeline-outbound.csv | find-people/count + find-people (2) + waterfall email/phone/personal-email | 2 leads prêts à séquencer, coordonnées complètes |
| airscale-hygiene-crm | hygiene-crm.csv | profile + email (x2) | 1 changement d'entreprise détecté (Fishtown Analytics -> dbt Labs), email vérifié |

**Coût** : ~15 crédits pour les 9 premiers skills, puis ~100 crédits pour les 2 skills
composites (les enrichissements premium profile/téléphone/email perso coûtent plus cher
que le sourcing, d'où les avertissements "Coût estimé" dans ces skills). Compteur de
crédits et preflights (/count, /preview) gratuits.

> Pour régénérer un exemple : `python .claude/skills/<skill>/scripts/run.py --config <skill>/config.example.yaml`.
> Pense au coût : chaque run consomme des crédits réels.
