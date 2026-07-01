# forward-airscale

Des **skills prets a l'emploi** pour transformer [Airscale](https://www.airscale.io) (sourcing et enrichissement de leads par API, facon Clay) en resultats metier concrets : listes ICP, signaux d'achat, emails et telephones verifies, fiches enrichies, reverse lookup.

Chaque skill est un **template** que tu adaptes a ta cible (ton ICP, ton fichier, tes signaux) en remplissant un `config.yaml`. Tu le lances depuis ton agent (Claude Code, Codex...) ou directement en ligne de commande, et tu obtiens un livrable mis en forme (CSV, fiche markdown).

> Guides cote business (cas d'usage, exemples, comment s'en servir) : **[les guides Forward](https://www.forward-ai.fr/cas-d-usage/airscale)**.

## Ce que ce repo n'est pas

On ne reconstruit pas l'API Airscale et on ne duplique pas le serveur MCP officiel. Ici, ce sont des **workflows metier** (une liste ICP, un fichier enrichi, une fiche entreprise) qui orchestrent les endpoints Airscale via une couche `requests` minimale.

## Installation

```bash
git clone https://github.com/iamachilles/forward-airscale.git
cd forward-airscale
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # puis colle ta cle AIRSCALE_API_KEY
```

Cle API : onglet API sur [app.airscale.io](https://app.airscale.io). Airscale est facture **a l'usage** (pas d'abonnement) : ~0,1 credit par lead retourne ou enrichi, ~1 a 2 credits par recherche IA. Le compteur de credits et les comptages (`/count`, `/preview`) sont gratuits.

## Les skills (9, en 4 familles)

### Sourcing
| Skill | Ce qu'il produit |
|---|---|
| `airscale-liste-icp` | Liste de cibles correspondant a ton ICP (decideurs + entreprise + LinkedIn) |
| `airscale-signaux-achat` | Comptes en signal d'achat (levee de fonds recente, equipe qui grossit) |

### Coordonnees
| Skill | Ce qu'il produit |
|---|---|
| `airscale-emails-fichier` | CSV enrichi en emails professionnels verifies |
| `airscale-telephones` | Mobiles d'une liste de decideurs (cold calling) |
| `airscale-multicanal` | Email pro + email perso + mobile pour une sequence multicanal |

### Enrichissement
| Skill | Ce qu'il produit |
|---|---|
| `airscale-fiche-entreprise` | Fiche entreprise enrichie + ses decideurs |
| `airscale-trouver-linkedin` | Backfill des URLs LinkedIn manquantes d'un fichier |

### Identification
| Skill | Ce qu'il produit |
|---|---|
| `airscale-reverse-lookup` | Profil enrichi a partir d'un email ou d'un numero |
| `airscale-recherche-ia` | Reponse data structuree a la demande (agent de recherche Airscale) |

## Comment s'en servir

Trois manieres, de la plus rapide a la plus industrielle :

1. **Avec un agent + le MCP Airscale (ad hoc, zero installation)** : Airscale fournit un [serveur MCP](https://docs.airscale.io/mcp/airscale-mcp-server) (outils `airscale_find_people`, `airscale_find_companies`, `airscale_airsearch`, enrichissement email/telephone/profil, exports). Branche-le dans ton Claude et demande-lui de suivre le `SKILL.md` du cas voulu. Parfait pour une recherche ponctuelle.
2. **Avec un agent + les skills de ce repo** : ouvre le repo dans ton agent, remplis le `config.yaml` du skill voulu, demande a l'agent de lancer le skill. L'agent suit la `Procedure` du `SKILL.md`.
3. **En ligne de commande (volume, cron, zero token)** : chaque skill a un `scripts/run.py` autonome. C'est le bon choix pour traiter un fichier ou rafraichir une liste en boucle.
   ```bash
   python .claude/skills/airscale-liste-icp/scripts/run.py \
     --config .claude/skills/airscale-liste-icp/config.yaml
   ```

> Pour du volume (enrichir des centaines de lignes), prefere le mode 3 (un script qui boucle) plutot que de mettre un LLM dans la boucle ligne a ligne : c'est deterministe et ca ne consomme pas de tokens.

## Adapter un skill

Chaque skill est un template. Copie son `config.example.yaml` en `config.yaml`, renseigne ta cible/tes filtres, et lance. La section "Adapter a ton cas" de chaque `SKILL.md` explique les variantes (ex : la liste ICP se decline en sourcing de partenaires ou de fournisseurs en changeant les filtres).

## Structure

```
.claude/skills/airscale-*/   un dossier par skill : SKILL.md + config.example.yaml + scripts/
lib/airscale_helpers.py      couche partagee (auth, POST + backoff, preflights gratuits, ecriture)
examples/                    une sortie reelle par skill
guides/                      les guides cote business (un par cas + index)
docs/skill-template.md       la convention d'un skill (pour en ajouter)
```

## Licence

MIT. Construit par [Forward](https://www.forward-ai.fr).
