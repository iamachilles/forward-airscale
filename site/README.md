# Contenu site-ready (a porter sur site-forward)

Les guides business du dossier `../guides/` sont la **source de contenu** pour la page
cas d'usage Airscale du site Forward. Ils sont ecrits avec un frontmatter compatible Astro
(`title`, `description`, `tool`, `famille`, `slug`, `reading_time`).

## Arborescence d'URL cible (calquee sur Linkup)

Colin a deja la page Linkup en ligne sous cette logique :

```
/cas-d-usage/famille/airscale        <- hub du kit (depuis guides/index.md)
/cas-d-usage/airscale/{slug}         <- une page par cas (depuis guides/airscale-{slug}.md)
```

| Slug | Guide source | Famille |
|---|---|---|
| airscale-liste-icp | guides/airscale-liste-icp.md | Sourcing |
| airscale-signaux-achat | guides/airscale-signaux-achat.md | Sourcing |
| airscale-emails-fichier | guides/airscale-emails-fichier.md | Coordonnees |
| airscale-telephones | guides/airscale-telephones.md | Coordonnees |
| airscale-multicanal | guides/airscale-multicanal.md | Coordonnees |
| airscale-fiche-entreprise | guides/airscale-fiche-entreprise.md | Enrichissement |
| airscale-trouver-linkedin | guides/airscale-trouver-linkedin.md | Enrichissement |
| airscale-reverse-lookup | guides/airscale-reverse-lookup.md | Identification |
| airscale-recherche-ia | guides/airscale-recherche-ia.md | Identification |

## Integration

Le repo public du site (`site-forward`, Astro) appartient a Colin. L'integration consiste a :
1. Creer la famille `airscale` (a cote de `linkup` et `unipile`) dans la collection de contenu du site.
2. Importer chaque guide comme une entree de la collection cas-d-usage, en mappant le frontmatter sur le schema de la collection existante.
3. Ajouter le kit Airscale a la page d'accueil `/cas-d-usage`.

> On ne duplique pas le contenu en MDX ici : la source de verite est `guides/`. Le mapping vers le schema exact de la collection Astro se fait au moment de l'integration, cote `site-forward` (la ou le schema est visible).
