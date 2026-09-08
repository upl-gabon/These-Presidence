# Archives des conversations — mémoire intégrale du chantier

> **Règle (décision D8, `REPRISE.md` § 3).** Chaque conversation de travail sur ce
> dépôt est **archivée systématiquement à sa clôture** par l'IA qui l'a menée —
> **sans solliciter l'avis de l'utilisateur**. L'auteur ne connaît pas GitHub :
> l'IA prend seule les décisions techniques et documentaires (branches, PR, merge
> après tests verts, fichiers, tests) ; l'auteur valide le **fond scientifique**.
> On ne perd rien : livrables, échanges jury, décisions, suites. Ce qui n'est pas
> écrit ici est considéré perdu — donc tout s'écrit, au moment de la clôture,
> avant le commit final.

**Format d'une entrée** (une par conversation, numérotation continue, la plus
récente en haut) : objet · réalisé (fichiers) · échange jury complet · décisions ·
prochaine étape. L'historique antérieur à la conversation n° 1 reste tracé dans le
journal de `REPRISE.md` § 5 et dans l'historique Git.

---


## Conversation n° 1 — 08/09/2026 — Nouveau cycle : résumé du travail et prise de parole du jury

**Objet.** À l'ouverture de cette nouvelle arena, l'auteur demande un résumé du travail
accompli et la prise de parole du jury. Les conversations n° 1 et n° 2 de l'ancien cycle
restent conservées ci-dessous comme historique opposable ; la numérotation de ce cycle
repart à n° 1, conformément à l'annonce de l'auteur.

**Résumé transmis.**

- La recherche porte sur la **gouvernance augmentée des EPES gabonais**, et sur
  l'articulation IA × intelligence émotionnelle en situation de polycrise.
- Le dépôt est autonome : site en quatre pages, pages discrètes, documents de travail,
  tests et mémoire du chantier. `npm test` reste vert : **12/12**.
- Le premier chantier, T1, est livré dans `docs/FICHE_CONCEPT_GA.md` (v1.1). La fiche
  propose une définition opérationnelle, cinq attributs observables A1–A5, trois exclusions,
  deux cas-limites, un glossaire et des règles d'inférence ; elle est explicitement marquée
  `proposition IA — à valider par l'auteur`.
- Le passage jury n° 1 de la fiche GA est favorable pour sa fonction d'outillage :
  Chabanne-Rive ✅, Valax ✅, Loufrani ✅, aucun ❌. Les réserves restent suivies :
  littérature réelle au chapitre 2, branchement sur le guide et les grilles en T2, pilote
  de codage avant le terrain.
- Le travail suivant est T2 : protocole de cas, annexes C–D, branchement des indicateurs
  A1–A5 sur les annexes A/D/F, pilote de codage et saturation informationnelle. Les 45
  participants restent une cible de travail, non un quota.
- Restent à l'auteur la validation du **fond scientifique** de la fiche GA et, côté dépôt,
  le passage en privé dans les réglages GitHub. Rien de nouveau n'est ajouté à la thèse
  par ce résumé.

**Réalisé (fichiers).**

- `docs/JURY_SIMULE.md` — échange n° 3 ajouté au Journal des échanges ; prise de parole de
  Loufrani consignée ; prochain intervenant passé à Rive.
- `REPRISE.md` — état du nouveau cycle, journal et prochain chantier synchronisés.
- `docs/ARCHIVES.md` — présente entrée d'archive.

**Échange jury n° 3 — Sabrina Loufrani (temps jury, dialogue complet).**

> **Loufrani — parole demandée :** Monsieur MINANG, si vous me permettez d'intervenir,
> le prochain verrou est méthodologique. Avant tout entretien, le protocole doit être daté
> et versionné. Comment allez-vous relier concrètement les indicateurs A1–A5 aux questions
> d'entretien, aux observations, aux documents et au dictionnaire de codes, sans traiter la
> cible de 45 participants comme un quota obligatoire ?
>
> **Réponse de travail (auteur/IA) :** Le chantier T2 commencera par une matrice de
> branchement des indicateurs A1–A5 sur le guide d'entretien (annexe A), les grilles
> d'observation et documentaire (annexe D), puis le dictionnaire de codes (annexe F).
> Le protocole sera daté et versionné avant le terrain ; le pilote de codage testera les
> règles sur des documents réels. Les 45 participants restent une cible de travail : l'arrêt
> dépendra de la saturation informationnelle, et chaque écart au protocole sera journalisé.
>
> **Loufrani :** C'est la bonne séquence. Je vous demande de ne pas confondre une matrice
> remplie avec une preuve de saturation : la première prépare l'enquête, la seconde se
> démontre au fil des données. Le passage au terrain reste donc conditionné par le protocole
> versionné et le pilote de codage.

**Clôture.** Échange résolu comme cadrage du T2 : les raccordements A1–A5, le protocole
préalable, le pilote de codage et la saturation informationnelle sont confirmés comme
prochaines actions. Aucun résultat de terrain, aucune référence nouvelle et aucune donnée
nouvelle n'ont été ajoutés.

**Décisions.** Le résumé ne remplace pas la validation du fond par l'auteur. Le prochain
intervenant du temps jury est **Chabanne-Rive** ; le prochain chantier est **T2**.


**Addendum — orientation de l'auteur : fond avant forme.** L'auteur précise que le jury doit
s'exprimer sur le fond scientifique plutôt que sur la forme. Cette orientation est intégrée
à `docs/JURY_SIMULE.md`, `REPRISE.md` et `README.md` : la question, le concept, le mécanisme,
le contexte gabonais, les preuves, l'interprétation et les limites sont prioritaires ; la
forme n'est retenue que si elle conditionne la validité ou la traçabilité scientifique.
Le test de stabilité a été complété pour maintenir cette règle.

**Échange jury n° 4 — Jérôme Chabanne-Rive (temps jury, dialogue complet).**

> **Rive :** Serge, je te le dis franchement : le jury doit d'abord savoir ce que ta thèse
> apporte. La question n'est pas de savoir si le dépôt est bien rangé ni si le protocole est
> joliment présenté. La question est : qu'est-ce que la **gouvernance augmentée** change
> réellement dans la gouvernance d'un EPES gabonais ? Quel mécanisme relie l'usage réel de
> l'IA, l'intelligence émotionnelle, le jugement humain et la responsabilité ? Qu'est-ce qui
> permet de la distinguer d'un simple pilotage instrumenté ou d'un discours sur l'IA ?
>
> **Réponse de travail (auteur/IA) :** La fiche T1 propose de traiter la gouvernance
> augmentée comme une propriété de processus, graduelle et observable dans des scènes de
> décision, et non comme le nom d'un outil ou d'une intention déclarée. Les attributs A1–A5,
> les exclusions et les cas-limites donnent une première frontière. Le terrain devra ensuite
> montrer si cette articulation existe, sous quelles conditions, et avec quelles limites ; si
> aucun cas ne la documente, la thèse devra le conclure. Le chapitre 2 devra positionner cette
> proposition dans la littérature réelle sur la gouvernance des établissements.
>
> **Rive :** Voilà le bon centre de gravité. Ne confonds jamais définition et démonstration :
> la fiche rend l'objet discutable, elle ne prouve pas encore sa contribution. Au prochain
> passage, je regarderai les scènes, les différences avec les alternatives et ce que le
> contexte gabonais apprend que l'on ne pourrait pas déduire d'un discours général sur l'IA.

**Clôture de l'addendum.** Résolu comme orientation scientifique : les prochains échanges et
livrables du jury porteront sur le fond de la contribution ; les éléments de forme ne seront
retenus que s'ils compromettent la validité, la traçabilité ou l'interprétation scientifique.
Le prochain intervenant est **Marc Valax**.


**Addendum 2 — état empirique clarifié par l'auteur.** L'auteur précise que le terrain n'a
pas encore été réalisé : il a conçu la méthodologie et ses outils. Le dépôt ne contient donc
pas d'entretiens, d'observations, de données de terrain ni de résultats empiriques acquis.
Cette distinction est désormais verrouillée dans `REPRISE.md` (D12) et dans le périmètre du
jury : dispositif prévu, données à recueillir et résultats à établir ne doivent pas être
confondus.

**Échange jury n° 5 — Marc Valax (temps jury, dialogue complet).**

> **Valax :** Monsieur MINANG, c'est une distinction décisive. Vous n'avez pas encore fait
> le terrain : vous avez conçu la méthodologie. Je ne peux donc pas évaluer des résultats,
> des effets ou des configurations observées. Je peux évaluer la promesse de savoir
> actionnable du dispositif prévu, ses conditions de test et la séparation entre ce qui est
> conçu, ce qui sera observé et ce qui restera peut-être absent.
>
> **Réponse de travail (auteur/IA) :** C'est acté. À ce stade, la fiche GA, le protocole à
> construire et les outils associés sont des propositions de conception méthodologique. Aucun
> entretien, aucune observation, aucun document de terrain et aucun résultat empirique ne sont
> présentés comme acquis. Le terrain devra produire — ou ne pas produire — les éléments qui
> permettront ensuite de discuter les propositions.
>
> **Valax :** Très bien, Monsieur MINANG. Maintenez cette discipline dans chaque chapitre :
> un dispositif prévu n'est pas une donnée, une hypothèse n'est pas un résultat et une
> possibilité d'action n'est pas encore une recommandation validée. Le jury jugera d'abord la
> qualité du raisonnement et du dispositif ; les résultats ne pourront être discutés qu'après
> leur production et leur traçabilité.

**Clôture de l'addendum 2.** Résolu : la distinction entre méthodologie conçue, terrain à
venir et résultats empiriques est verrouillée. Le prochain intervenant est **Sabrina Loufrani**.


**Addendum 3 — support de soutenance préparatoire reçu.** Le fichier
`docs/DEPOT_AUTEUR/Soutenance_DBA_MINANG_version_revisee_Phoenix.pdf` a été téléversé dans la
zone prévue. Il s'agit d'une version préparatoire révisée, explicitement « sous réserve du
terrain », comprenant 23 diapositives d'exposé et les annexes scientifiques A1–A6. Le support
couvre le problème managérial, la question centrale, les ancrages théoriques, les critères
d'observation, le modèle exploratoire, le protocole qualitatif prévu, P1–P7, la chaîne de
preuves, les résultats à établir, la discussion, les limites et les perspectives.

**Lecture de fond.** Le support respecte la distinction méthodologie / résultats : les
emplacements `[Résultat]`, `[À établir]`, les matrices à compléter et la mention « sous réserve
du terrain » ne présentent pas de données fabriquées. Il est recevable comme architecture de
soutenance préparatoire. Les verrous restent : protocole T2 daté et versionné, branchement
A1–A5 sur guide/grilles/codebook, pilote, saturation, vérification des références et future
démonstration de P4 par des matériaux authentiques.

**Échange jury n° 6 — Sabrina Loufrani (temps jury, dialogue complet).**

> **Loufrani — parole demandée :** Monsieur MINANG, votre support a un mérite important :
> il ne maquille pas l'inconnu. Les mentions `[Résultat]`, `[À établir]`, les matrices à
> renseigner et la formule « sous réserve du terrain » signalent que les diapositives 11 à
> 22 décrivent des emplacements de résultats, non des conclusions. Mais un emplacement vide
> ne constitue pas encore une méthode suffisante. Avant le terrain, il faut verrouiller le
> guide, les grilles, le dictionnaire de codes, le pilote et la règle de saturation.
>
> **Réponse de travail (auteur/IA) :** Le PDF est bien un support de soutenance préparatoire.
> Il expose le problème managérial, la question centrale, les ancrages théoriques, les
> critères d'observation, le modèle exploratoire, le protocole qualitatif prévu, la chaîne de
> preuves et les conditions de discussion. P4 reste une proposition à éprouver : l'articulation
> IA–IE sera recherchée dans des scènes de décision, pas présupposée. Le chantier T2 doit
> maintenant transformer cette architecture en protocole daté et testable.
>
> **Loufrani :** C'est recevable comme architecture de recherche, pas comme soutenance de
> résultats. Je maintiens trois exigences de fond : chaque futur résultat devra renvoyer à un
> matériau sourcé ; « non documenté » ne devra pas être confondu avec « absent » ; et la
> comparaison inter-cas devra conserver les différences au lieu de les lisser. Le support est
> prêt pour cette étape préparatoire, mais pas pour conclure à la place du terrain.

**Clôture de l'addendum 3.** Résolu comme lecture préparatoire : le document est accepté comme
architecture à éprouver ; aucun résultat empirique n'est validé. Le prochain intervenant est
**Jérôme Chabanne-Rive**.


**Addendum 4 — proposition d'un support plus explicite avant le terrain.** À la suite de la
lecture du PDF, une trame de 20 diapositives a été proposée dans
`docs/DEPOT_AUTEUR/PROPOSITION_SUPPORT_SOUTENANCE_PRE_TERRAIN.md`. Elle sépare explicitement
quatre statuts : travail préparatoire, propositions à éprouver, matériaux à recueillir et
résultats à établir. Elle recentre la présentation sur la contribution, la scène
décisionnelle, la chaîne de preuves, le codage, la saturation, les limites et les conditions
de recommandations. Elle est marquée `proposition IA — à valider par l'auteur` et ne remplace
pas le PDF reçu sans validation de fond.

**Échange jury n° 7 — Jérôme Chabanne-Rive (temps jury, dialogue complet).**

> **Rive :** Serge, une meilleure soutenance préparatoire n'est pas une soutenance qui
> remplit les cases vides avec des phrases plus élégantes. C'est une soutenance qui permet
> au jury de distinguer, dès la première minute, ce qui est déjà établi, ce qui est proposé,
> ce qui sera recueilli et ce qui ne pourra être établi qu'après le terrain. Le centre doit
> rester votre contribution : qu'est-ce que P4 cherche à expliquer, et quelle observation
> pourrait la mettre en difficulté ?
>
> **Réponse de travail (auteur/IA) :** La proposition sépare ces quatre statuts, place la
> question et le périmètre avant les résultats futurs, décrit la scène décisionnelle, la
> chaîne de preuves, le codage, la saturation et un gabarit de résultat. Elle conserve P1–P7
> comme propositions à confronter et réserve toute réponse finale à l'enquête.
>
> **Rive :** C'est la bonne correction. Ne faites pas de la prudence une faiblesse : dire
> « résultat à établir » est plus scientifique que d'annoncer un résultat sans matériau. La
> prochaine version devra toutefois rester courte à l'oral et laisser la place aux cas, quand
> ils existeront. Pour l'instant, la trame est recevable comme support pré-terrain.

**Clôture de l'addendum 4.** Résolu comme proposition de travail : trame améliorée, aucun
résultat ajouté ; validation du fond par l'auteur encore requise. Le prochain intervenant est
**Marc Valax**.

**Addendum 5 — livrables visuels.** La trame proposée a été rendue sous deux formats :
`PROPOSITION_SUPPORT_SOUTENANCE_PRE_TERRAIN.pptx` (20 diapositives, format 16:9) et
`PROPOSITION_SUPPORT_PRE_TERRAIN_VISUEL.png` (visuel de couverture). Il s'agit d'une mise en
forme de la proposition précédente, pas d'un nouveau contenu empirique ni d'un verdict
scientifique. Le PDF initial reste conservé séparément.


---

## Conversation n° 2 — 08/09/2026 — GO de l'auteur : fiche concept GA rédigée, passage jury n° 1 rendu (T1 livré)

**Objet.** L'auteur donne son GO (« on continue, on fusionne sans demander, rien de
technique à demander à l'utilisateur — la conversation et la reprise comptent, les détails
techniques se règlent en autonomie »). L'IA exécute donc seule : rédaction du livrable T1
(**fiche concept « gouvernance augmentée »**, § 3.2–3.3), passage jury n° 1 sur ce
livrable, temps jury (Valax, échange n° 2), mise à jour des journaux, des archives, de la
reprise, tests, branche → PR → merge — sans aucune question technique à l'auteur.

**Réalisé (fichiers).**

- `docs/FICHE_CONCEPT_GA.md` — **création** : fiche concept GA v1.1 (T1). Contenu :
  positionnement dans l'existant de la gouvernance des établissements d'enseignement
  (consigne Rive, échange n° 1) ; définition opérationnelle en un paragraphe (propriété de
  processus, émergente et graduelle, espace de jugement préservé) ; **5 attributs
  observables** A1–A5 (usage effectif de l'IA, dernier mot humain, dimension émotionnelle
  mobilisée dans les scènes instrumentées, orchestration et apprentissage, garde-fous et
  responsabilité) — chacun avec indicateurs, sources d'évidence (E/O/D) et **marqueur
  longitudinal** ; **3 exclusions** E1–E3 (pilotage instrumenté, automatisation/
  numérisation isolées, usage déclaratif ou occasionnel) avec tests de classement ;
  **2 cas-limites tranchés** CL1 (dirigeant seul assisté par IA générative) et CL2 (comité
  outillé qui délibère) — codage par scène ; glossaire discipliné (GA vs pilotage
  instrumenté, management algorithmique, e-gouvernance, numérisation/automatisation, usage
  personnel d'IA générative) ; règles d'inférence pour l'enquête (jamais de code « GA »
  direct — anti-tautologie ; GA présente/absente/partielle ; testabilité de P4 ; issue
  possible sans GA ; branchement sur les annexes A/D/F en T2 ; pilote de codage avant le
  terrain). Marquée `proposition IA — à valider par l'auteur` ; aucun fait ni référence
  inventé (placeholders `[référence à vérifier par l'auteur]` pour la littérature).
- `docs/JURY_SIMULE.md` — **échange n° 2 ajouté au Journal des échanges (Valax)** ;
  « Prochain intervenant » passé à Loufrani ; **passage jury n° 1 consigné** (journal des
  passages + section détaillée « Passage jury n° 1 — Fiche concept GA ») : Rive ✅ solide
  (réserve : littérature réelle à mobiliser au chap. 2), Valax ✅ solide (réserve :
  branchement guide/grilles en T2), Loufrani ✅ solide (réserve : pilote de codage avant
  terrain) — aucun ❌.
- `docs/ARCHIVES.md` — la présente entrée (conversation n° 2).
- `REPRISE.md` — état § 1, chantiers § 2 (T1 ✅ livré), décisions § 3 (D10 ajoutée),
  journal § 5 (entrée 08/09/2026).
- `tests/site.test.mjs` — fiche concept ajoutée aux fichiers requis (toujours 12 tests).
- `README.md` — arborescence `docs/` à jour (fiche concept GA).

**Échange jury n° 2 — Marc Valax (temps jury, dialogue complet).**

> **Valax :** Monsieur MINANG, cette fiche concept doit faire tenir debout votre
> « gouvernance augmentée » — c'est le passage jury n° 1, et c'est la pièce maîtresse de
> P4. Avant que vous ne la figiez, deux exigences de ma part. Premièrement, la
> **reconnaissabilité** : votre lecteur dirigeant d'EPES doit pouvoir dire, lundi matin
> dans son établissement, s'il fait ou non de la gouvernance augmentée — sinon le concept
> restera un mot de séminaire. Deuxièmement, le **temps** : la polycrise est un processus,
> la gouvernance se joue dans la durée. Un cliché instantané ne prouve rien. Où voyez-vous,
> dans la fiche, la profondeur temporelle ? Et si aucun cas ne documente l'articulation —
> que dira la thèse ?
>
> **Réponse (auteur/IA) :** Monsieur le Professeur, la fiche prend la **scène décisionnelle**
> pour unité d'observation et de codage, jamais l'outil ni l'individu : chaque attribut
> (A1–A5) est décrit par des indicateurs qu'un dirigeant peut observer en réunion, en
> arbitrage, en régulation de crise — et par un **marqueur longitudinal** (traces datées,
> trajectoire 2022–2026, retours dans les cas). Quant à l'absence : la fiche écrit noir sur
> blanc que si aucun cas ne documente la GA, la thèse le conclura explicitement — une
> configuration absente des terrains est un résultat, pas un échec (renvoi au plan § 6.4).
>
> **Valax :** C'est l'esprit d'un DBA, Monsieur MINANG. La fiche doit rester un outil et
> non devenir une doctrine : veillez à ce que chaque indicateur soit branché, en temps
> utile, sur votre guide d'entretien et vos grilles d'observation — sinon elle flottera
> au-dessus de l'enquête. Je vous reverrai sur le protocole.
>
> **Réponse :** C'est acté : le branchement sur le guide (annexe A, 14 questions) et les
> grilles (annexe D) est le premier objet du chantier T2, inscrit dans la fiche (§ 7.6)
> et dans REPRISE.md.

**Clôture de l'échange :** résolu — marqueurs longitudinaux, scène comme unité
d'observation et issue possible sans GA intégrés à la fiche v1.1 ; branchement guide/
grilles programmé en T2. Consigné au Journal des échanges (`docs/JURY_SIMULE.md`, n° 2).

**Passage jury n° 1 (résumé) — fiche concept GA v1.1 :** Rive **✅ solide** (réserve
mineure : littérature réelle au chap. 2) ; Valax **✅ solide** (réserve mineure :
branchement A/D en T2) ; Loufrani **✅ solide** (réserve mineure : pilote de codage avant
terrain). **Aucun ❌.** Décision : validée pour fonction d'outillage (concept opérationnel,
codage NVivo, testabilité de P4) ; **en attente de la validation du fond par l'auteur** —
étape qui ne peut être simulée. Détail dans `docs/JURY_SIMULE.md`.

**Décisions.** D10 — les fiches concept (dont la fiche GA) sont des **documents de travail
internes** rangés dans `docs/`, hors pages publiques du site ; elles sont marquées
`proposition IA — à valider par l'auteur` et ne rejoignent le manuscrit (§ 3.2–3.3) qu'après
validation du fond par l'auteur (détail `REPRISE.md` § 3). Rappel exécuté : autonomie
technique totale (aucune question posée à l'auteur — D8), branche → PR → merge (D6),
12/12 tests verts avant merge.

**Prochaine étape.** T1 ✅ livré (attente : validation du fond par l'auteur, à la lecture
de `docs/FICHE_CONCEPT_GA.md`). **Annonce de l'auteur** : il ouvrira, dans une nouvelle
arena, une nouvelle « conversation n° 1 » où le jury prend connaissance de la thèse
(« bonjour…, on a pris connaissance… ») — les chantiers reprendront ensuite (T2 d'abord :
brancher les indicateurs A1–A5 de la fiche GA sur le guide (annexe A), les grilles
d'observation et documentaire (annexe D), le dictionnaire de codes (annexe F) ; pilote de
codage ; règle de saturation). La numérotation des archives repart de « Conversation n° 1 »
avec la mention du nouveau cycle (les entrées n° 1–2 du 08/09/2026 restent opposables).
Prochain intervenant du temps jury : **Loufrani**.

---

## Conversation n° 1 — 08/09/2026 — Le jury devient accompagnant ; garde-fous IA ; le dépôt gagne une mémoire

**Objet.** Décisions de l'auteur (Serge Patrick MINANG), exécutées par l'IA de bout
en bout : (1) le jury simulé devient un **comité d'accompagnement exigeant** — à
chaque conversation, un membre pose **une question ou donne un conseil**, en
**discussion dynamique** et toujours **clôturée** (« on arrête la conversation » =
clôture propre, jamais d'arrêt net) ; (2) chaque membre a **sa voix** : Rive dit
« **Serge** » (ils se connaissent), Valax dit « **Monsieur MINANG** », Loufrani
**demande la parole** et n'interrompt jamais ; (3) **archivage systématique** de
chaque conversation **sans avis de l'utilisateur** — l'IA prend seule les décisions
(l'auteur ne connaît pas GitHub) et **ne perd rien** des conversations ; (4)
**garde-fous anti-hallucination IA** pour empêcher tout contenu inventé
(« abracadabrantesque ») : références fantômes, données fabriquées, comblement
d'inconnues.

**Réalisé (fichiers).**

- `docs/JURY_SIMULE.md` — titre et rôle repositionnés (« comité d'accompagnement
  exigeant ») ; nouvelle section « Le temps du jury dans chaque conversation »
  (5 règles du dialogue) ; bloc « Les trois voix » ; **journal des échanges** créé
  (échange n° 1 : Rive) ; règles de fonctionnement remaniées (deux temps :
  dialogue à chaque conversation / passage à chaque livrable ; les deux journaux
  tenus).
- `docs/ARCHIVES.md` — création (ce fichier) : mémoire intégrale (décision D8).
- `docs/GARDE_FOUS_IA.md` — création : **dix garde-fous anti-hallucination IA** +
  checklist de fin de conversation (décision D9). L'IA rédige et critique, elle
  n'invente jamais ; un garde-fou violé = livraison refusée.
- `REPRISE.md` — protocole § 0 enrichi (étapes 4–8 : temps jury, garde-fous
  anti-hallucination, clôture + archivage systématique, autonomie décisionnelle de
  l'IA) ; état § 1, chantiers § 2 (T1 enrichi de la consigne Rive), décisions § 3
  (D7, D8, D9), règles § 4, journal § 5 à jour.
- `README.md` — jury décrit comme comité d'accompagnement ; garde-fous ajoutés
  (règle 5 + validation) ; archives ajoutées à la structure et à la lecture ;
  section Validation réécrite ; 12 tests.
- `tests/site.test.mjs` — 3 tests ajoutés (« jury accompagnant », « archives »,
  « garde-fous anti-hallucination IA ») ; `docs/GARDE_FOUS_IA.md` et
  `docs/ARCHIVES.md` ajoutés aux fichiers requis. 12/12 verts.

**Échange jury n° 1 — Chabanne-Rive (temps jury, dialogue complet).**

> **Rive :** Serge, je te parle franchement, comme d'habitude. Ta fiche concept
> « gouvernance augmentée » — notre passage jury n° 1, en attente de ton feu vert —
> ne doit pas être écrite dans le vide. Définis-la **dans** ce qu'on sait de la
> gouvernance des établissements d'enseignement : collégiale contre managériale,
> dirigeant-fondateur, tutelles, accréditations. Si « augmentée » n'est pas
> positionnée dans cet existant, ce sera un slogan plaqué — exactement le soupçon
> d'oxymore que ton annexe cherche à lever.
>
> **Réponse (auteur/IA) :** Consigne intégrée au cahier des charges de T1 : la fiche
> GA comportera (i) le positionnement explicite dans l'existant de la gouvernance
> des EPES, (ii) le glossaire discipliné déjà prévu (GA vs pilotage instrumenté vs
> management algorithmique vs e-gouvernance), (iii) les contre-exemples et
> cas-limites exigés par l'annexe.
>
> **Rive :** C'est cela, Serge. Et retiens : ton apport se mesurera à l'écart avec
> cet existant — c'est là que ta thèse gagnera sa légitimité, pas dans la
> novation verbale. Bonne rédaction ; je relirai au passage n° 1.

**Clôture de l'échange :** résolu — consigne intégrée à T1 (rédaction en attente du
GO de l'auteur). Consigné au Journal des échanges (`docs/JURY_SIMULE.md`).

**Décisions.** D7 (jury = comité d'accompagnement exigeant : temps jury à chaque
conversation, rotation, trois voix, clôture obligatoire) ; D8 (archivage
systématique dans ce fichier, sans avis utilisateur, autonomie décisionnelle IA,
perte zéro) ; D9 (garde-fous anti-hallucination IA : dix règles + checklist,
livraison refusée si un seul garde-fou est violé). Détail dans `REPRISE.md` § 3.

**Prochaine étape.** T1 — fiche concept GA (§ 3.2–3.3), en attente du GO de
l'auteur, cahier des charges enrichi. Prochain intervenant du temps jury :
**Valax**.
