# REPRISE — reprise instantanée (LIRE EN PREMIER)

> **Toute IA ouvrant une conversation sur ce dépôt commence ici.**
> Hypothèse par défaut : **la conversation précédente s'est arrêtée net** —
> ce fichier dit exactement où, et comment continuer.

## 0. Protocole obligatoire (chaque message, sans exception)

1. **Lire dans l'ordre** : ce fichier → `README.md` → `docs/JURY_SIMULE.md`
   → `docs/GARDE_FOUS_IA.md` (+ la dernière entrée de `docs/ARCHIVES.md`).
   Vérifier `git log --oneline -5` et `git status`.
2. **Ouvrir ta réponse en disant EXACTEMENT où on s'est arrêté** (section 1).
3. **Continuer directement** le chantier, avec par défaut la lentille jury :
   critique, améliorations, réflexion, rigueur, **exigence DBA**
   (savoir actionnable, preuves tracées, rien d'inventé).
4. **Temps jury — une question ou un conseil à CHAQUE conversation** : le membre
   dont c'est le tour (rotation Rive → Valax → Loufrani ; prochain intervenant =
   celui qui suit le dernier inscrit au journal des échanges de
   `docs/JURY_SIMULE.md`) intervient **avec sa voix** (Rive : « Serge » ;
   Valax : « Monsieur MINANG » ; Loufrani : demande la parole, n'interrompt
   jamais). Discussion **dynamique** : 1 à 3 passes (question ou conseil →
   réponse → réaction), puis **clôture** — résolu, ou explicitement reporté.
   Consigner dans le journal des échanges.
5. **Garde-fous anti-hallucination (D9) — AUCUNE exception** : appliquer
   `docs/GARDE_FOUS_IA.md` (dix garde-fous + checklist) à tout ce que tu produis.
   Rien de neuf sans source ; références jamais générées ; données terrain jamais
   inventées ; propositions marquées `proposition IA — à valider` ; un trou reste
   un trou. Relecture du `git diff` ligne à ligne avant livraison.
6. **Clôture et archivage systématiques — on ne s'arrête jamais net, on ne perd
   rien** : à la fin de la conversation, **archive-toi** dans `docs/ARCHIVES.md`
   (numéro suivant : objet, réalisé, échange jury complet, décisions, prochaine
   étape), mets à jour ce fichier (§ 1, § 2, § 3, § 5), puis **commit + push** —
   **sans solliciter l'avis de l'utilisateur** : c'est systématique, pas optionnel.
7. **Autonomie décisionnelle** : l'auteur ne connaît pas GitHub — tu prends **seul**
   les décisions techniques et documentaires (branches, PR, merge après tests
   verts, fichiers, tests) ; l'auteur valide le **fond scientifique**. Ne bloque
   jamais une livraison en attendant une décision technique.
8. Règle d'or : **un fait n'existe que s'il est écrit ici, dans
   `docs/JURY_SIMULE.md`, dans `docs/GARDE_FOUS_IA.md` ou dans
   `docs/ARCHIVES.md`**. En cas de conflit entre ta mémoire de conversation et
   ces fichiers, **ces fichiers gagnent**.

## 1. ÉTAT — où on s'est arrêté (màj : 08/09/2026, jury accompagnant + garde-fous + archives)

- **Dépôt GitHub propre et prêt : `upl-gabon/These-Presidence`**, branche `main`
  (site 4 pages FR + CSS/JS autonomes, jury simulé, tests ; extraction du 08/09/2026
  depuis `upl-gabon/UPL-Gabon`, liens UPL absolus `https://upl-gabon.com/`).
  Nettoyage 08/09/2026 : `these-SPM.zip` (doublon de l'upload) et `CREER-LE-REPO.md`
  (obsolète — son étape 5) retirés ; contenu mis sur `main` via PR (D6 respecté).
  Tests **12/12 verts**.
- **Temps jury actif (D7)** : à CHAQUE conversation, un membre du jury pose une
  question ou donne un conseil — dialogue dynamique (1–3 passes), puis clôture
  (résolu ou explicitement reporté), tout consigné dans le Journal des échanges
  (`docs/JURY_SIMULE.md`). Échange n° 1 : Rive (08/09/2026, fiche concept GA).
  **Prochain intervenant : Valax.**
- **Garde-fous anti-hallucination actifs (D9)** : `docs/GARDE_FOUS_IA.md` — dix
  garde-fous + checklist de fin de conversation. L'IA rédige et critique, elle
  n'invente jamais ; un seul garde-fou violé = livraison refusée.
- **Archives actives (D8)** : chaque conversation est archivée systématiquement à
  sa clôture dans `docs/ARCHIVES.md` — par l'IA, **sans solliciter l'utilisateur**
  (conversation n° 1 : 08/09/2026). On ne perd rien.
- **⚠️ Reste à faire par l'auteur (onglet Settings du dépôt GitHub)** : le dépôt est
  encore **public** — le passer en **privé** (règle de discrétion n° 2 ; impossible au
  jeton IA : droits admin requis). Dans la foulée : désactiver Wiki et Projects,
  ajouter une description. GitHub Pages : non activé (incompatible privé gratuit ;
  rendre le site public un jour = décision auteur, règle 2 du README).
- **Composition verrouillée** : jury simulé = Chabanne-Rive (Lyon) · Valax (Nice) ·
  Loufrani (Nice) — passage n° 0 journalisé (3 × ⚠️).
- **Question en suspens** : GO de l'auteur pour lancer le **passage jury n° 1 —
  fiche concept « gouvernance augmentée » (§ 3.2–3.3)** : définition 1 §, 4–6 attributs
  observables, 3 exclusions, 2 cas-limites tranchés, glossaire discipliné — et, depuis
  l'échange n° 1 (Rive), **positionnement explicite dans l'existant de la gouvernance
  des établissements d'enseignement** (collégiale vs managériale, dirigeant-fondateur,
  tutelles, accréditations).

## 2. Chantiers ouverts (jury — ordre = bloquants d'abord)

| # | Chantier | Statut | Verdicts R/V/L | Prochaine action |
|---|---|---|---|---|
| T1 | Fiche concept GA (§ 3.2–3.3) | ⏳ en attente GO | — | Rédiger (avec consigne Rive, échange n° 1 : positionner GA dans l'existant) + passage jury n° 1 |
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
- D7. Jury = **comité d'accompagnement exigeant**, pas instance distante : à CHAQUE
  conversation, un membre pose une question ou donne un conseil (rotation
  Rive → Valax → Loufrani, journal des échanges en témoignage) ; dialogue dynamique
  (1–3 passes) avec les trois voix (Rive : « Serge » ; Valax : « Monsieur MINANG » ;
  Loufrani : demande la parole, n'interrompt jamais) ; clôture systématique (résolu
  ou explicitement reporté). Une conversation ne s'arrête jamais net.
- D8. **Archivage systématique** : chaque conversation est archivée à sa clôture dans
  `docs/ARCHIVES.md` — par l'IA, **sans solliciter l'avis de l'utilisateur**. L'auteur
  ne connaît pas GitHub : l'IA prend seule les décisions techniques et documentaires
  (branches, PR, merge après tests verts, fichiers, tests) ; l'auteur valide le fond
  scientifique. On ne perd rien de ce qui s'est dit ou décidé.
- D9. **Garde-fous anti-hallucination IA** (`docs/GARDE_FOUS_IA.md`) : rien de neuf
  sans source tracée ; références bibliographiques jamais générées ni complétées ;
  données de terrain et citations jamais inventées ; productions non sourcées
  marquées `proposition IA — à valider` ; aucun comblement d'inconnue ; valeurs
  canoniques intouchables sans GO ; relecture du `git diff` ligne à ligne avant
  livraison. Un seul garde-fou violé = livraison refusée.

## 4. Règles express (rappel sec)

- Parler français. Ton : factuel, sobre ; jamais défensif, jamais de promesse.
- Tests : `npm test` (12 tests) — Node ≥ 18. Aperçu : `npm run serve` → `/`.
- Termes bannis dans le HTML : voir `tests/site.test.mjs`.
- Anti-hallucination : `docs/GARDE_FOUS_IA.md` — dix garde-fous + checklist,
  relecture du `git diff` ligne à ligne avant toute livraison (D9).
- Temps jury : une question ou un conseil par conversation (rotation, trois voix),
  clôture obligatoire, Journal des échanges à jour (`docs/JURY_SIMULE.md`).
- Archivage : chaque conversation archivée dans `docs/ARCHIVES.md`, sans avis
  utilisateur — on ne perd rien.
- Validation : auteur (tout contenu). Dépôt privé recommandé.

## 5. Journal (bref — derniers en haut)

- **08/09/2026 (jury accompagnant + archives + garde-fous, D7–D9)** : jury
  repositionné en **comité d'accompagnement exigeant** — une question ou un conseil
  d'un membre à CHAQUE conversation (rotation Rive → Valax → Loufrani), dialogue
  dynamique en 1–3 passes, clôture obligatoire (résolu ou reporté) ; trois voix
  (Rive : « Serge » ; Valax : « Monsieur MINANG » ; Loufrani : demande la parole,
  n'interrompt jamais). Journal des échanges créé dans `docs/JURY_SIMULE.md`
  (échange n° 1 : Rive — fiche GA à positionner dans l'existant ; consigne intégrée
  à T1). `docs/ARCHIVES.md` créé : archivage systématique de chaque conversation,
  sans solliciter l'utilisateur (l'auteur n'est pas sur GitHub — l'IA décide seule).
  `docs/GARDE_FOUS_IA.md` créé : dix garde-fous anti-hallucination IA + checklist
  (D9). Protocole (`REPRISE.md` § 0, étapes 4–8), README et tests synchronisés
  (12 tests). 12/12 verts. T1 inchangé (attente GO) ; prochain intervenant :
  **Valax**.
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
