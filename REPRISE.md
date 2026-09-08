# REPRISE — reprise instantanée (LIRE EN PREMIER)

> **Toute IA ouvrant une conversation sur ce dépôt commence ici.**
> Hypothèse par défaut : **la conversation précédente s'est arrêtée net** —
> ce fichier dit exactement où, et comment continuer.

## 0. Protocole obligatoire (chaque message, sans exception)

1. **Lire dans l'ordre** : ce fichier → `README.md` → `docs/JURY_SIMULE.md`.
   Vérifier `git log --oneline -5` et `git status`.
2. **Ouvrir ta réponse en disant EXACTEMENT où on s'est arrêté** (section 1).
3. **Continuer directement** le chantier, avec par défaut la lentille jury :
   critique, améliorations, réflexion, rigueur, **exigence DBA**
   (savoir actionnable, preuves tracées, rien d'inventé).
4. **À LA FIN DE CHAQUE MESSAGE : mettre à jour ce fichier**
   (État § 1, Chantiers § 2, Décisions § 3 si besoin, Journal § 5).
   Puis commiter + pusher si des fichiers ont changé.
5. Règle d'or : **un fait n'existe que s'il est écrit ici ou dans `docs/JURY_SIMULE.md`**.
   En cas de conflit entre ta mémoire de conversation et ce fichier, **ce fichier gagne**.

## 1. ÉTAT — où on s'est arrêté (màj : 08/09/2026, mise en propre du dépôt GitHub)

- **Dépôt GitHub propre et prêt : `upl-gabon/These-Presidence`**, branche `main`
  (site 4 pages FR + CSS/JS autonomes, jury simulé, tests ; extraction du 08/09/2026
  depuis `upl-gabon/UPL-Gabon`, liens UPL absolus `https://upl-gabon.com/`).
  Nettoyage 08/09/2026 : `these-SPM.zip` (doublon de l'upload) et `CREER-LE-REPO.md`
  (obsolète — son étape 5) retirés ; contenu mis sur `main` via PR (D6 respecté).
  Tests **9/9 verts**.
- **⚠️ Reste à faire par l'auteur (onglet Settings du dépôt GitHub)** : le dépôt est
  encore **public** — le passer en **privé** (règle de discrétion n° 2 ; impossible au
  jeton IA : droits admin requis). Dans la foulée : désactiver Wiki et Projects,
  ajouter une description. GitHub Pages : non activé (incompatible privé gratuit ;
  rendre le site public un jour = décision auteur, règle 2 du README).
- **Composition verrouillée** : jury simulé = Chabanne-Rive (Lyon) · Valax (Nice) ·
  Loufrani (Nice) — passage n° 0 journalisé (3 × ⚠️).
- **Question en suspens** : GO de l'auteur pour lancer le **passage jury n° 1 —
  fiche concept « gouvernance augmentée » (§ 3.2–3.3)** : définition 1 §, 4–6 attributs
  observables, 3 exclusions, 2 cas-limites tranchés, glossaire discipliné.

## 2. Chantiers ouverts (jury — ordre = bloquants d'abord)

| # | Chantier | Statut | Verdicts R/V/L | Prochaine action |
|---|---|---|---|---|
| T1 | Fiche concept GA (§ 3.2–3.3) | ⏳ en attente GO | — | Rédiger + passage jury n° 1 |
| T2 | Protocole de cas (annexes C–D) + règle de saturation | 🔴 non démarré | Loufrani ❌ potentiel | Cadrer après T1 |
| T3 | Typologie des usages IA (tab. 5.3) + grille d'observation | 🔴 non démarré | Exigence permanente n° 3 | Cadrer après T1 |
| T4 | 4e regard expert IA (chap. 5) | 📌 rappel | — | Identifier un nom le moment venu |

## 3. Décisions verrouillées (ne pas rouvrir sans GO explicite)

- D1. Autonomie totale : aucun fichier hors dépôt, charte propre, `noindex` + `robots.txt`,
  hors sitemap. Ponts autorisés UNIQUEMENT : `https://upl-gabon.com/`,
  `https://upl-gabon.com/contact.html`, `mailto:contact@upl-gabon.com?subject=Recherche doctorale`.
- D2. Confidentialité terrain : codes **EPES-A à EPES-E** en public ; noms pressentis,
  correspondances, consentements, enregistrements : **jamais dans Git**.
- D3. Jury simulé = Chabanne-Rive · Valax · Loufrani (simulation interne, non-implication
  explicite). 1 × ❌ = reprise exigée. 10 exigences conjointes (`docs/JURY_SIMULE.md`).
- D4. Rien d'inventé : pas d'université d'inscription, directeur, date de soutenance,
  mail, tarif ou partenaire supposés. Tout contenu vient des documents de l'auteur.
- D5. Dossier Matrix Group R+2 (bâtiment UPL) : hors périmètre thèse.
- D6. Jamais de push direct sur `main` (branche → PR → merge). `npm test` vert avant merge.

## 4. Règles express (rappel sec)

- Parler français. Ton : factuel, sobre ; jamais défensif, jamais de promesse.
- Tests : `npm test` (9 tests) — Node ≥ 18. Aperçu : `npm run serve` → `/`.
- Termes bannis dans le HTML : voir `tests/site.test.mjs`.
- Validation : auteur (tout contenu). Dépôt privé recommandé.

## 5. Journal (bref — derniers en haut)

- **08/09/2026 (mise en propre GitHub)** : contenu du zip commité sur `main` via
  PR n° 1 (branche → PR → merge, D6) ; `these-SPM.zip` et `CREER-LE-REPO.md`
  supprimés ; README/REPRISE actualisés. Reste à l'auteur : passer le dépôt en
  privé (Settings — le jeton IA n'a pas les droits admin). 9/9 verts.
  T1 (fiche concept GA) inchangé.
- **08/09/2026** : création du dépôt par extraction (`these/` → racine, liens absolus,
  jury + reprise + tests adaptés). 9/9 verts. En attente GO passage n° 1 (fiche concept GA).
- **Antériorité (dépôt UPL-Gabon)** : zone `these/` créée depuis le Drive « Thèse president
  privé » (plan harmonisé + 27 tab./13 fig.) ; double piste outillée ; jury recomposé
  Rive/Valax/Loufrani + annexe « oxymore ou slogan / § 3.3 ».
