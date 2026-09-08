# Thèse DBA — Serge Patrick MINANG (dépôt autonome)

**Recherche doctorale : gouvernance augmentée des EPES gabonais**,
articulation IA × intelligence émotionnelle en situation de polycrise.
Travail en cours (septembre 2026).

> Dépôt autonome extrait de `upl-gabon/UPL-Gabon` le 08/09/2026, hébergé sur
> `github.com/upl-gabon/These-Presidence` (**privé exigé** — documents de travail internes).
> **Zéro dépendance locale** : les seuls liens vers l'UPL sont absolus
> (`https://upl-gabon.com/`). Ce dépôt vit seul : site + jury + reprise.

**Lire dans l'ordre :** `REPRISE.md` → `README.md` (ce fichier) → `docs/JURY_SIMULE.md`
→ `docs/GARDE_FOUS_IA.md` (la mémoire des conversations vit dans `docs/ARCHIVES.md`).

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
   Garde-fous anti-hallucination IA verrouillés dans `docs/GARDE_FOUS_IA.md` (décision D9).

## Structure

```
├── index.html       Accueil : titre, question centrale, QR1–QR4, P1–P7, méthode, auteur
├── plan.html        Plan général harmonisé (3 parties, 6 chapitres, conclusion, annexes A–K)
├── supports.html    27 tableaux + 13 figures (intitulés provisoires, septembre 2026)
├── documents.html   Documents de travail, confidentialité, demande d'accès
├── style.css        Styles propres (aucune dépendance externe)
├── app.js           Nav mobile, année, bandeau d'échanges indépendant
├── tests/site.test.mjs  12 tests de stabilité (Node ≥ 18)
├── docs/JURY_SIMULE.md  Jury accompagnant (Chabanne-Rive · Valax · Loufrani) :
│                    question/conseil à chaque conversation + critiques + exigences + journaux
├── docs/GARDE_FOUS_IA.md  Garde-fous anti-hallucination IA — dix règles + checklist (D9)
├── docs/ARCHIVES.md     Archives des conversations — mémoire intégrale (systématique)
├── docs/FICHE_CONCEPT_GA.md  Fiche concept « gouvernance augmentée » (T1) —
│                    proposition IA — à valider par l'auteur avant intégration au manuscrit
├── REPRISE.md       ★ Reprise instantanée — lire et maintenir en premier
├── robots.txt       Zone privée (voir règle 2)
└── package.json
```

## Commandes

```bash
npm test     # 12 tests — OBLIGATOIRE avant toute livraison
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

Le jury est un **comité d'accompagnement exigeant**, pas une instance distante : à
**chaque conversation**, un membre pose une question ou donne un conseil (rotation
Chabanne-Rive → Valax → Loufrani, avec sa voix propre : « Serge », « Monsieur
MINANG », la parole demandée) ; la discussion est dynamique puis **toujours
clôturée** — résolue ou explicitement reportée. Une conversation ne s'arrête
jamais net.

La priorité du jury est le **fond scientifique** : question, concepts, contribution,
contexte, preuves, interprétation et limites. La mise en page, le site, Git, les tests et
l'archivage ne sont pas jugés pour eux-mêmes ; la forme n'entre en discussion que lorsqu'elle
conditionne la validité ou la traçabilité scientifique.

Chaque conversation est **archivée systématiquement** dans `docs/ARCHIVES.md`,
sans solliciter l'utilisateur (l'auteur ne connaît pas GitHub : l'IA décide seule
des questions techniques, l'auteur valide le fond scientifique) — **on ne perd
rien** des échanges et des décisions.

L'IA travaille sous **garde-fous anti-hallucination** verrouillés
(`docs/GARDE_FOUS_IA.md`, décision D9) : rien de neuf sans source tracée,
références bibliographiques jamais générées, données de terrain et citations
jamais inventées, productions non sourcées marquées `proposition IA — à valider`,
aucun comblement d'inconnue, relecture du `git diff` ligne à ligne. Un garde-fou
violé = livraison refusée.

Dépôt **privé exigé** (discrétion, documents internes — voir `REPRISE.md` § 1) ;
jamais de push direct sur `main` (branche → PR → merge).
