"""Helpers partagés pour les skills Airscale de forward-airscale.

Couche mince au-dessus de l'API REST Airscale (https://api.airscale.io/v1).
Airscale n'a pas de SDK Python officiel : on enveloppe les appels en `requests`.
On NE reconstruit PAS l'API : chaque skill orchestre quelques endpoints pour
produire un livrable métier (liste, CSV enrichi, fiche).

- get_key()        : lit AIRSCALE_API_KEY (.env), exit clair si absente
- load_config()    : lit un config.yaml
- post()           : POST authentifié + gestion d'erreurs + backoff sur 429
- unwrap()         : déballe les réponses enveloppées sous "response"/"body"
- credits()        : solde de crédits (gratuit)
- count_people()   : preflight gratuit /find-people/count
- preview_leads()  : preflight gratuit /leads-finder/preview
- write_output()   : écrit un livrable texte sur disque
- write_csv()      : écrit une liste de dicts en CSV

Toutes les fonctions sont synchrones et sans dépendance aux skills (réutilisables).

Conventions Airscale (vérifiées, cf. .claude/skills/airscale du vault) :
- Base URL https://api.airscale.io/v1, tous les endpoints en POST (même les lectures).
- Auth : header Authorization: Bearer <AIRSCALE_API_KEY>.
- Crédits : recherches ~0,1 crédit / lead ; airsearch ~1-2 crédits / requête ;
  compteur de crédits et endpoints /count|/preview gratuits.
- Erreurs : 401 clé, 400 requête, 403 crédits insuffisants, 429 rate limit,
  502/504 échec/timeout côté Airscale.
- Certaines réponses sont enveloppées sous "response" (ex credits) ou "body"
  (ex profile/company/reverse) : utiliser unwrap() / lire le shape réel.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path
from typing import Any

import requests
import yaml
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.airscale.io/v1"


def get_key() -> str:
    """Retourne la clé AIRSCALE_API_KEY depuis l'environnement (.env)."""
    key = os.environ.get("AIRSCALE_API_KEY")
    if not key:
        sys.exit(
            "AIRSCALE_API_KEY manquante. Copie .env.example en .env et renseigne ta clé "
            "(onglet API sur https://app.airscale.io)."
        )
    return key


def load_config(path: str | Path) -> dict[str, Any]:
    """Charge un config.yaml en dict."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def post(
    endpoint: str,
    body: dict[str, Any] | None = None,
    *,
    timeout: int = 60,
    max_retries: int = 4,
) -> dict[str, Any]:
    """POST authentifié sur /v1/<endpoint>. Retourne le JSON désérialisé.

    Gère le backoff exponentiel sur 429 (rate limit). Lève RuntimeError sur les
    autres erreurs (401/400/403/5xx) avec un message lisible (sans la clé).
    """
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    headers = {
        "Authorization": f"Bearer {get_key()}",
        "Content-Type": "application/json",
    }
    delay = 2.0
    last_exc: Exception | None = None
    for attempt in range(max_retries):
        try:
            r = requests.post(url, headers=headers, json=body or {}, timeout=timeout)
        except requests.RequestException as e:  # réseau : on retente
            last_exc = e
            time.sleep(delay)
            delay *= 2
            continue
        if r.status_code == 429:  # rate limit : backoff puis retry
            time.sleep(delay)
            delay *= 2
            continue
        if r.status_code == 401:
            raise RuntimeError("401 Airscale : clé absente ou invalide.")
        if r.status_code == 403:
            raise RuntimeError("403 Airscale : crédits insuffisants.")
        if not r.ok:
            raise RuntimeError(f"{r.status_code} Airscale sur /{endpoint} : {r.text[:300]}")
        try:
            return r.json()
        except ValueError:
            raise RuntimeError(f"Réponse non-JSON sur /{endpoint} : {r.text[:200]}")
    raise RuntimeError(
        f"/{endpoint} : échec après {max_retries} tentatives"
        + (f" ({last_exc})" if last_exc else " (429 persistant)")
    )


def unwrap(resp: dict[str, Any]) -> dict[str, Any]:
    """Déballe une réponse Airscale enveloppée sous 'response' ou 'body'.

    Plusieurs endpoints renvoient l'utile sous une clé d'enveloppe ; les autres
    le mettent au top-level. On vérifie et on renvoie le contenu pertinent.
    """
    if not isinstance(resp, dict):
        return {}
    for key in ("response", "body"):
        inner = resp.get(key)
        if isinstance(inner, dict):
            return inner
    return resp


def credits() -> int | None:
    """Solde de crédits (gratuit). Lit .response.credits (vérité terrain)."""
    resp = post("credits", {})
    inner = unwrap(resp)
    val = inner.get("credits", resp.get("credits"))
    try:
        return int(val)
    except (TypeError, ValueError):
        return None


def count_people(query: dict[str, Any]) -> int | None:
    """Preflight gratuit : nombre de personnes pour un `query` /find-people."""
    resp = post("find-people/count", {"query": query})
    inner = unwrap(resp)
    for k in ("total", "count"):
        if k in inner:
            return inner[k]
        if k in resp:
            return resp[k]
    return None


def preview_leads(filters: dict[str, Any]) -> int | None:
    """Preflight gratuit : total estimé pour un `filters` /leads-finder."""
    resp = post("leads-finder/preview", {"filters": filters, "page": 0, "size": 1})
    inner = unwrap(resp)
    return inner.get("total", resp.get("total"))


def write_output(text: str, path: str | Path) -> Path:
    """Écrit `text` dans `path` (crée les dossiers parents). Retourne le Path."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def write_csv(rows: list[dict[str, Any]], fieldnames: list[str], path: str | Path) -> Path:
    """Écrit `rows` en CSV avec l'en-tête `fieldnames`. Retourne le Path."""
    import csv

    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return p
