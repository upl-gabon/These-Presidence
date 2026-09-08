# Thèse DBA — Serge Patrick MINANG (dépôt autonome)

**Recherche doctorale : gouvernance augmentée des EPES gabonais**,
articulation IA × intelligence émotionnelle en situation de polycrise.
Travail en cours (septembre 2026).

> Dépôt autonome extrait de `upl-gabon/UPL-Gabon` le 08/09/2026, hébergé sur
> `github.com/upl-gabon/These-Presidence` (**privé exigé** — documents de travail internes).
> **Zéro dépendance locale** : les seuls liens vers l'UPL sont absolus
> (`https://upl-gabon.com/`). Ce dépôt vit seul : site + jury + reprise.

**Lire dans l'ordre :** `REPRISE.md` → `README.md` (ce fichier) → `docs/JURY_SIMULE.md`.

## Règles non négociables

1. **Autonomie** — aucun fichier hors de ce dépôt ; chartes et scripts propres
   (encre/bronze/papier) ; ni bleu `#0B2A5B` ni or `#C9A227` de l'UPL.
2. **Discrétion** — `noindex` sur chaque page + `robots.txt` restrictif, hors sitemap.
   Pour rendre public un jour : supprimer `robots.txt` + retirer les `noindex` (décision auteur).
3. **Ponts autorisés UNIQUEMENT** (verrouillés par les tests) :
   `https://upl-gabon.com/`, `https://upl-gabon.com/contact.html`,
   `mailto:contact@upl-gabon.com?subject=Recherche doctorale` — **aucun mail inventé**.
4. **Confidentialité du terrain** — codes **EPES-A à EPES-E** en public.
   Noms pressentis, correspondances, consentements, enregistrements : **jamais dans Git**.
5. **Rien d'inventé** — tout contenu vient des documents de l'auteur (plan harmonisé,
   liste des supports). Pas d'université d'inscription, directeur, date de soutenance supposés.

## Structure

```
├── index.html       Accueil : titre, question centrale, QR1–QR4, P1–P7, méthode, auteur
├── plan.html        Plan général harmonisé (3 parties, 6 chapitres, conclusion, annexes A–K)
├── supports.html    27 tableaux + 13 figures (intitulés provisoires, septembre 2026)
├── documents.html   Documents de travail, confidentialité, demande d'accès
├── style.css        Styles propres (aucune dépendance externe)
├── app.js           Nav mobile, année, bandeau d'échanges indépendant
├── tests/site.test.mjs  9 tests de stabilité (Node ≥ 18)
├── docs/JURY_SIMULE.md  Jury simulé (Chabanne-Rive · Valax · Loufrani) + exigences
├── REPRISE.md       ★ Reprise instantanée — lire et maintenir en premier
├── robots.txt       Zone privée (voir règle 2)
└── package.json
```

## Commandes

```bash
npm test     # 9 tests — OBLIGATOIRE avant toute livraison
npm run serve  # aperçu local → http://127.0.0.1:5173/
```

Aucun `npm install` nécessaire (aucune dépendance).

## Ajouter une page (checklist)

1. Copier le header/footer/nav d'une page existante.
2. `<meta name="robots" content="noindex, nofollow">` obligatoire.
3. `<div data-action-band></div>` avant `</main>` (rendu par `app.js`).
4. `<script src="app.js"></script>` + `<link rel="stylesheet" href="style.css">` uniquement.
5. Ajouter le lien dans la nav de toutes les pages + `npm test` vert.

## Validation

Tout livrable passe le **jury simulé** (`docs/JURY_SIMULE.md`) :
un seul ❌ = reprise exigée. Puis validation finale de l'auteur (Serge Patrick MINANG).
Dépôt **privé exigé** (discrétion, documents internes — voir `REPRISE.md` § 1) ;
jamais de push direct sur `main` (branche → PR → merge).
