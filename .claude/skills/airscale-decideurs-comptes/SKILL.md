---
name: airscale-decideurs-comptes
description: Use when you already have a list of target accounts (company domains) and need the right decision-makers at each. Input = a CSV of domains in config.yaml, output = a CSV of contacts per account.
---

# Les décideurs de tes comptes cibles

## Objectif & quand

Tu as déjà ta **liste de comptes cibles** (une liste ABM, un territoire, des comptes sortis d'un salon) mais pas les bons interlocuteurs dedans. Ce skill part des domaines des entreprises et remonte, pour chacune, les décideurs à contacter avec leur LinkedIn.

> Différent de `airscale-liste-icp` (qui *crée* une liste à partir de critères ICP) : ici tu pars de comptes que tu as déjà choisis et tu cherches qui contacter dans chacun.

## Prérequis

Deux modes :
- **Script (`run.py`)** : `AIRSCALE_API_KEY` dans `.env` + `pip install -r requirements.txt`.
- **Agent ad hoc** : serveur [MCP Airscale](https://docs.airscale.io/mcp/airscale-mcp-server) (`airscale_find_people`).
- Un CSV d'entrée avec une colonne de domaines d'entreprise.

## Config

| Champ | Rôle | Exemple |
|---|---|---|
| `input_csv` | Chemin du CSV de comptes | `"input.example.csv"` |
| `domain_column` | Colonne des domaines | `"domain"` |
| `job_titles` | Fonctions visées (tokens larges) | `["Head", "VP", "Chief", "Director", "CEO", "Founder"]` |
| `per_company` | Nombre de décideurs par compte | `3` |
| `output_path` | CSV de sortie | `null` |

## Adapter à ton cas

- **Titres larges** : Airscale fait un matching par mot sur le titre. Vise des tokens de séniorité (`Head`, `VP`, `Chief`, `Director`) plutôt qu'un intitulé exact (`Head of Sales` peut rater si l'entreprise nomme le poste autrement).
- **Cibler une fonction précise** : mets des tokens métier (`Marketing`, `Finance`, `Data`) pour ne remonter que ce département.
- **Comptes identifiés par leur page LinkedIn** : la même logique marche avec `companyLinkedinUrl` à la place du domaine (cf `airscale-fiche-entreprise`).
- **Attention aux domaines de plateforme** : un domaine partagé par beaucoup d'entités (ex `doctolib.fr`, utilisé par des milliers de cabinets) remonte des gens qui ne travaillent pas dans l'entreprise. Utilise le domaine corporate propre du compte.

## Procédure

Pour chaque domaine du CSV : un `/find-people` avec `query = { companyDomain:{include:[domaine]}, JobTitle:{include:job_titles} }` et `size = per_company`. Les contacts trouvés sont ajoutés au CSV de sortie, avec le domaine d'origine. `/find-people/count` (gratuit) peut être utilisé en amont pour jauger le volume par compte.

> Mapping MCP : `/find-people` -> `airscale_find_people`.

## Livrable

Un CSV `examples/decideurs-comptes.csv` : `domain, firstname, lastname, jobTitle, companyName, profileUrl`.

## Coût estimé

Facturé à l'usage par Airscale (~0,1 crédit par décideur retourné). Le comptage est gratuit : le nombre de comptes x `per_company` te donne l'ordre de grandeur avant de lancer.

## Exemple

Voir `examples/decideurs-comptes.csv`.
