# Contenu site-ready (à porter sur site-forward)

Les guides business du dossier `../guides/` sont la **source de contenu** pour la page
cas d'usage Airscale du site Forward. Ils sont écrits avec un frontmatter compatible Astro
(`title`, `description`, `tool`, `famille`, `slug`, `reading_time`).

## Arborescence d'URL cible (calquée sur Linkup)

Colin a déjà la page Linkup en ligne sous cette logique :

```
/cas-d-usage/famille/airscale        <- hub du kit (depuis guides/index.md)
/cas-d-usage/airscale/{slug}         <- une page par cas (depuis guides/airscale-{slug}.md)
```

| Slug | Guide source | Famille |
|---|---|---|
| airscale-liste-icp | guides/airscale-liste-icp.md | Sourcing |
| airscale-decideurs-comptes | guides/airscale-decideurs-comptes.md | Sourcing |
| airscale-pipeline-outbound | guides/airscale-pipeline-outbound.md | Sourcing |
| airscale-emails-fichier | guides/airscale-emails-fichier.md | Coordonnées |
| airscale-telephones | guides/airscale-telephones.md | Coordonnées |
| airscale-multicanal | guides/airscale-multicanal.md | Coordonnées |
| airscale-fiche-entreprise | guides/airscale-fiche-entreprise.md | Enrichissement |
| airscale-trouver-linkedin | guides/airscale-trouver-linkedin.md | Enrichissement |
| airscale-hygiene-crm | guides/airscale-hygiene-crm.md | Enrichissement |
| airscale-reverse-lookup | guides/airscale-reverse-lookup.md | Identification |
| airscale-recherche-ia | guides/airscale-recherche-ia.md | Identification |

## Intégration (faite)

L'intégration au site `site-forward` (Astro) a été réalisée en MDX (les guides ci-dessus sont la source de vérité éditoriale ; le MDX du site en est le portage) :
- famille `airscale` + 4 thèmes ajoutés dans `src/lib/cas-usage/families.ts` ;
- un fichier `src/content/casUsages/{slug}.mdx` par cas ;
- générateur de pages `src/pages/cas-d-usage/airscale/[slug].astro`.

Les 9 premiers cas sont partis dans la PR #13 (mergée), les 2 composites (`pipeline-outbound`, `hygiene-crm`) dans une PR de suivi. Reste le déploiement Vercel (côté Colin) pour la mise en ligne.
