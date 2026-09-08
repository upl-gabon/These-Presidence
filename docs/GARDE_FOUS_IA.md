# Garde-fous IA anti-hallucination — protéger la thèse de l'« abracadabra »

> **Objet.** L'IA est autorisée à travailler sur ce dépôt (rédiger, structurer,
> critiquer, archiver). Elle n'est **jamais autorisée à inventer**. Ce document fixe
> les garde-fous qu'**aucune IA ne peut contourner** — décision D9
> (`REPRISE.md` § 3), exigée par l'auteur le 08/09/2026. Un seul garde-fou violé =
> livraison refusée, contenu retiré, reprise exigée.

**Principe zéro :** tout ce qui n'est pas traçable à une source existante
(documents de l'auteur, fichiers du dépôt, littérature réellement vérifiée)
est une **proposition à vérifier** — jamais un fait. Un trou reste un trou :
on le nomme, on ne le comble pas avec du plausible.

## Les dix garde-fous (verrouillés)

1. **Rien de neuf sans source.** Aucun fait, chiffre, date, nom propre, institution,
   loi, tarif ou citation ne peut apparaître sans source écrite traçable. « Je me
   souviens », « c'est connu », « c'est probable » ne sont pas des sources.
2. **Références bibliographiques : jamais générées.** Aucune référence (auteur,
   année, titre, revue, éditeur) inventée, « reconstituée de mémoire » ou complétée
   par vraisemblance. Toute référence doit exister et être vérifiable ; sinon on
   écrit explicitement `[référence à vérifier par l'auteur]`.
3. **Données de terrain interdites d'invention.** Aucun entretien, verbatim,
   statistique, résultat d'enquête ou observation fabriqué — même « à titre
   d'illustration » sans l'être. Les cas restent codés **EPES-A à EPES-E** (D2) ;
   noms pressentis, correspondances, consentements : jamais dans Git.
4. **Citations : mot pour mot ou rien.** Aucune citation attribuée à quiconque —
   y compris les membres du jury simulé — sans trace écrite dans le dépôt. Le jury
   simulé ne « parle » que dans `docs/JURY_SIMULE.md`, dans le cadre de la
   simulation déclarée ; aucun propos ne doit être présenté comme venant des
   personnes réelles.
5. **Proposition ≠ fait.** Toute production IA utile mais non sourcée est marquée
   `proposition IA — à valider par l'auteur`. Elle ne se noie jamais dans du
   contenu établi, ne se formule jamais au présent de vérité.
6. **Pas de comblement.** Ne jamais remplir une inconnue (université
   d'inscription, directeur de thèse, date de soutenance, partenaire, budget,
   effectif) par une valeur plausible : l'inconnue reste écrite comme inconnue
   (règle D4 : rien d'inventé).
7. **Valeurs canoniques intouchables sans GO.** 27 tableaux, 13 figures, 5 cas,
   45 participants (cible), QR1–QR4, P1–P7, 3 parties, 6 chapitres, annexes A–K :
   les valeurs du dépôt ne changent que sur GO explicite de l'auteur, jamais
   « pour être cohérent ».
8. **Relecture du diff, ligne à ligne.** Avant toute livraison : relire
   `git diff` et se demander pour chaque ligne ajoutée : « d'où vient cette
   information ? » Toute ligne non traçable est retirée ou marquée
   `proposition IA`.
9. **Ton sans amplification.** Pas de superlatifs, pas de promesses, pas de
   résultats annoncés d'avance, pas d'anglicisme creux. Ton factuel, sobre
   (`REPRISE.md` § 4). L'IA ne parle jamais au nom de l'auteur : elle propose,
   l'auteur valide.
10. **Traçabilité finale.** `npm test` vert ; `REPRISE.md`, journaux du jury et
    `docs/ARCHIVES.md` à jour. Ce qui n'est pas écrit n'existe pas ; ce qui est
    écrit doit être sourcé.

## Checklist de fin de conversation (l'IA la déroule avant d'archiver)

- [ ] Aucune référence bibliographique ajoutée sans vérification réelle.
- [ ] Aucun chiffre, date, nom, institution modifié ou créé sans GO de l'auteur.
- [ ] Aucune donnée de terrain ou citation fabriquée ; codes EPES respectés.
- [ ] Toute production non sourcée est marquée `proposition IA — à valider`.
- [ ] `git diff` relu ligne à ligne (« d'où vient cette information ? »).
- [ ] `npm test` vert ; REPRISE, journaux jury et archives à jour.
- [ ] Conversation clôturée et archivée (`docs/ARCHIVES.md`, D8) — rien de perdu.

## Ce que ces garde-fous ne visent PAS

Ils ne visent pas l'effort intellectuel (proposer une reformulation, un plan, une
objection critique, un angle d'analyse) : c'est le travail attendu de l'IA,
notamment via le jury accompagnant (D7). Ils visent uniquement l'introduction
**d'éléments factuels non traçables**. L'IA peut douter, proposer, critiquer ;
elle ne peut pas affirmer sans source.

---

*Rattachements : `README.md` règle 5 (« Rien d'inventé ») ; `REPRISE.md` § 3
(D4, D9) ; `docs/JURY_SIMULE.md` exigences conjointes n° 2 et règles de
fonctionnement n° 6 ; verrouillé par `tests/site.test.mjs`.*
