# -*- coding: utf-8 -*-
"""Génère la présentation de soutenance (15 slides) — Thèse DBA S. P. MINANG.

Sources du contenu (fournies par l'auteur, 20/09/2026) : document de thèse
(dédicace, remerciements, résumé, plan général, chapitres 1–6, conclusion) et
dépôt (REPRISE.md, style.css : palette encre/bronze/papier).

Garde-fous appliqués (docs/GARDE_FOUS_IA.md, D9) :
- rien d'inventé : pas de date de soutenance, pas d'université supposée,
  pas de résultat de terrain (chap. 5–6 = architecture préparatoire) ;
- terrain codé EPES-A à EPES-E (aucun nom pressenti) ;
- ton sobre, valeurs canoniques du dépôt (5 cas, 45 participants cible,
  QR1–QR4, P1–P7, N1–N8, 3 parties, 6 chapitres).

Sortie : presentation/Soutenance_DBA_MINANG_15_slides.pptx
Statut : proposition IA — à valider par l'auteur.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ---- Charte du dépôt (style.css — encre / bronze / papier) ----
PAPER = RGBColor.from_string("FAF8F2")
CARD = RGBColor.from_string("FFFFFF")
INK = RGBColor.from_string("232B33")
INKD = RGBColor.from_string("141B22")
BRONZE = RGBColor.from_string("8A6414")
BRONZE_D = RGBColor.from_string("6E4F0E")
BRONZE_S = RGBColor.from_string("F1E8D0")
LINE = RGBColor.from_string("E3DAC6")
MUTED = RGBColor.from_string("5E6A76")
WHITE = RGBColor.from_string("FFFFFF")

SERIF = "Georgia"
SANS = "Segoe UI"

FOOTER_TXT = "S. P. MINANG — Thèse DBA · Gouvernance augmentée des EPES gabonais"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]


def new_slide(bg=PAPER):
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = bg
    return s


def rect(s, x, y, w, h, fill=None, line=None, line_w=1.0,
         shape=MSO_SHAPE.RECTANGLE, radius=None):
    sp = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    sp.shadow.inherit = False
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid()
        sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line
        sp.line.width = Pt(line_w)
    if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        try:
            sp.adjustments[0] = radius
        except Exception:
            pass
    return sp


def tbox(s, x, y, w, h, anchor=None):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    if anchor is not None:
        tf.vertical_anchor = anchor
    return tf


def para(tf, first=False, align=PP_ALIGN.LEFT, before=0, after=0, line=None):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_before = Pt(before)
    p.space_after = Pt(after)
    if line is not None:
        p.line_spacing = line
    return p


def run(p, t, size=13, color=INK, bold=False, italic=False, font=SANS, spc=None):
    r = p.add_run()
    r.text = t
    f = r.font
    f.name = font
    f.size = Pt(size)
    f.bold = bold
    f.italic = italic
    f.color.rgb = color
    if spc:
        r._r.get_or_add_rPr().set("spc", str(spc))
    return r


def header(s, kicker, title):
    tf = tbox(s, 0.6, 0.42, 12.13, 0.32)
    run(para(tf, True), kicker.upper(), 11, BRONZE, bold=True, spc=260)
    tf = tbox(s, 0.6, 0.74, 12.13, 0.72)
    run(para(tf, True), title, 26, INKD, bold=True, font=SERIF)
    rect(s, 0.62, 1.55, 12.11, 0.012, fill=LINE)
    rect(s, 0.62, 1.53, 0.95, 0.045, fill=BRONZE)


def footer(s, n, light=False):
    c_line = RGBColor.from_string("3A4550") if light else LINE
    c_txt = RGBColor.from_string("9AA5B0") if light else MUTED
    rect(s, 0.6, 7.06, 12.13, 0.012, fill=c_line)
    tf = tbox(s, 0.6, 7.14, 9.5, 0.28)
    run(para(tf, True), FOOTER_TXT, 8.5, c_txt)
    tf = tbox(s, 11.53, 7.14, 1.2, 0.28)
    run(para(tf, True, align=PP_ALIGN.RIGHT), "%d / 15" % n, 8.5, c_txt)


def card(s, x, y, w, h):
    return rect(s, x, y, w, h, fill=CARD, line=LINE, line_w=1.0,
                shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)


def bullet(tf, lead, rest, size=12.5, first=False, after=7, lead_color=BRONZE_D):
    p = para(tf, first, after=after, line=1.12)
    run(p, "—  ", size, BRONZE, bold=True)
    if lead:
        run(p, lead, size, lead_color, bold=True)
    run(p, rest, size, INK)
    return p


# =====================================================================
# SLIDE 1 — Titre
# =====================================================================
s = new_slide()
mono = rect(s, 6.39, 0.62, 0.56, 0.56, fill=INKD, line=BRONZE, line_w=1.75,
            shape=MSO_SHAPE.OVAL)
mtf = mono.text_frame
mtf.word_wrap = False
mp = para(mtf, True, align=PP_ALIGN.CENTER)
run(mp, "SM", 13, BRONZE_S, bold=True, font=SERIF)

tf = tbox(s, 1.2, 1.42, 10.93, 0.34)
run(para(tf, True, align=PP_ALIGN.CENTER),
    "THÈSE PRÉSENTÉE EN VUE DE L'OBTENTION DU DOCTORATE OF BUSINESS "
    "ADMINISTRATION (DBA)", 11.5, BRONZE, bold=True, spc=200)

tf = tbox(s, 0.9, 1.86, 11.53, 1.55)
p = para(tf, True, align=PP_ALIGN.CENTER, line=1.08)
run(p, "La gouvernance augmentée des établissements privés "
       "d'enseignement supérieur au Gabon en situation de polycrise",
    29, INKD, bold=True, font=SERIF)

rect(s, 6.58, 3.52, 0.16, 0.16, fill=BRONZE, shape=MSO_SHAPE.DIAMOND)

tf = tbox(s, 1.5, 3.84, 10.33, 0.95)
p = para(tf, True, align=PP_ALIGN.CENTER, line=1.15)
run(p, "Articulation entre intelligence artificielle et intelligence "
       "émotionnelle au service de la performance globale, de la "
       "responsabilité sociétale et du développement durable",
    15, MUTED, italic=True, font=SERIF)

tf = tbox(s, 2.5, 5.05, 8.33, 1.3)
p = para(tf, True, align=PP_ALIGN.CENTER, after=4)
run(p, "Serge Patrick MINANG", 19, INKD, bold=True)
p = para(tf, align=PP_ALIGN.CENTER, after=2)
run(p, "Directeur de thèse : Professeur Jérôme CHABANE RIVE", 12, MUTED)

rect(s, 0, 6.84, 13.333, 0.03, fill=BRONZE)
rect(s, 0, 6.87, 13.333, 0.63, fill=INKD)
tf = tbox(s, 2.0, 7.02, 9.33, 0.34)
run(para(tf, True, align=PP_ALIGN.CENTER),
    "Support de soutenance — document de travail", 10.5, BRONZE_S, spc=120)

# =====================================================================
# SLIDE 2 — Dédicace
# =====================================================================
s = new_slide()
header(s, "Dédicace", "À celles et à ceux qui ont rendu ce parcours possible")

blocks = [
    "À la mémoire de mes parents, MINANG Jean Baptiste et MINANG Jeanne, "
    "enseignants, qui ont consacré leur vie à l'éducation, à la formation "
    "des jeunes générations et à la transmission du savoir.",
    "À mon épouse, MINANG Blandine, pour son soutien indéfectible, sa "
    "patience, sa compréhension et son accompagnement constant tout au long "
    "de ce parcours exigeant.",
    "À mes enfants — Stan, Aldrin, Calvin, Cleanne et Diamant — pour leur "
    "affection, leur compréhension et leur soutien silencieux.",
    "Au Professeur Franck IDIATA, Président de l'EM Gabon, et au Professeur "
    "Khadija IDRISSI, de l'Université Mundiapolis du Maroc, pour la "
    "confiance qui a profondément marqué mon parcours académique.",
    "À toutes les personnes qui, de près ou de loin, ont contribué à la "
    "réalisation de ce projet : qu'elles trouvent ici l'expression de ma "
    "profonde reconnaissance et de mon sincère respect.",
]
y = 1.82
for i, b in enumerate(blocks):
    tf = tbox(s, 1.35, y, 10.63, 0.72)
    p = para(tf, True, align=PP_ALIGN.CENTER, line=1.1)
    run(p, b, 13.5, INK, italic=True, font=SERIF)
    y += 0.72
    if i < len(blocks) - 1:
        rect(s, 6.61, y + 0.04, 0.12, 0.12, fill=BRONZE, shape=MSO_SHAPE.DIAMOND)
        y += 0.26
footer(s, 2)

# =====================================================================
# SLIDE 3 — Remerciements
# =====================================================================
s = new_slide()
header(s, "Remerciements", "Ce travail porte la marque de nombreux soutiens")

thanks = [
    ("Professeur VALAX — Directeur du DBA",
     "Pour la qualité du programme, sa vision académique et son engagement "
     "dans la formation doctorale."),
    ("Professeur Jérôme CHABANE RIVE — Directeur de thèse",
     "Pour son accompagnement rigoureux, ses conseils avisés, sa "
     "disponibilité et la pertinence de ses orientations scientifiques."),
    ("Corps professoral — Université Mundiapolis (Maroc) et "
     "Université Nice Côte d'Azur",
     "Pour la richesse des enseignements dispensés et la qualité des "
     "échanges académiques."),
    ("Membres du jury",
     "Pour le temps consacré à l'évaluation de ce travail : leurs "
     "observations et recommandations sont une contribution précieuse."),
    ("Collègues du DBA de Mundiapolis à Casablanca",
     "« Bien que seul étranger de la promotion, je ne me suis jamais senti "
     "étranger au Maroc, que je considère aujourd'hui comme ma deuxième "
     "patrie. »"),
    ("Toutes celles et ceux qui ont contribué, de près ou de loin",
     "Chercheurs, personnels, proches et partenaires : à l'aboutissement de "
     "ce projet doctoral."),
]
gx = [0.6, 6.78]
gy = [1.78, 3.44, 5.10]
for i, (name, desc) in enumerate(thanks):
    x = gx[i % 2]
    y = gy[i // 2]
    card(s, x, y, 5.95, 1.52)
    tf = tbox(s, x + 0.22, y + 0.13, 5.51, 1.28)
    p = para(tf, True, after=3, line=1.05)
    run(p, name, 12, BRONZE_D, bold=True)
    p = para(tf, line=1.08)
    run(p, desc, 10.8, INK)
footer(s, 3)

# =====================================================================
# SLIDE 4 — Plan de la présentation
# =====================================================================
s = new_slide()
header(s, "Plan de la présentation", "Quinze slides, du contexte aux enseignements")

items = [
    "Contexte — les EPES gabonais face à la polycrise",
    "Problématique et questions de recherche (QR1–QR4)",
    "Revue critique de la littérature",
    "Cadre conceptuel — la gouvernance augmentée",
    "Modèle exploratoire et propositions (P1–P7)",
    "Méthodologie qualitative multi-cas",
    "Architecture d'analyse des résultats (préparatoire)",
    "Effets examinés : performance globale, RSE, développement durable",
    "Recommandations indicatives et garde-fous",
    "Contributions, limites et perspectives",
]
gx = [0.85, 6.98]
y0 = 1.95
for i, it in enumerate(items):
    x = gx[i // 5]
    y = y0 + (i % 5) * 0.97
    num = rect(s, x, y, 0.52, 0.52, fill=BRONZE_S, line=BRONZE, line_w=1.0,
               shape=MSO_SHAPE.OVAL)
    ntf = num.text_frame
    np_ = para(ntf, True, align=PP_ALIGN.CENTER)
    run(np_, str(i + 1), 15, BRONZE_D, bold=True, font=SERIF)
    tf = tbox(s, x + 0.75, y + 0.02, 4.85, 0.85)
    p = para(tf, True, line=1.05)
    run(p, it, 13, INK, bold=True)

footer(s, 4)

# =====================================================================
# SLIDE 5 — Contexte
# =====================================================================
s = new_slide()
header(s, "Chapitre 1 — Contextualisation", "Les EPES gabonais face à la polycrise")

tf = tbox(s, 0.7, 1.82, 11.93, 3.1)
bullet(tf, "Des organisations académiques, économiques et sociales. ",
       "Universités, grandes écoles et instituts complètent l'offre publique "
       "(repère CAMES) ; leurs missions et leurs contraintes diffèrent.",
       first=True)
bullet(tf, "Un encadrement institutionnel spécifique. ",
       "Habilitation à fonder et autorisation d'ouverture distinctes "
       "(décret n° 0446/PR/MESRS du 5 septembre 2016) ; la conformité est "
       "une activité continue de gouvernance.")
bullet(tf, "Quatre fonctions à articuler. ",
       "Orienter, exécuter, garantir la qualité académique, contrôler — "
       "avec des tensions : ambition et capacités, attractivité et exigence "
       "scientifique, continuité et dépendance aux personnes clés.")
bullet(tf, "Un pilotage financier sous tension. ",
       "Dépendance aux scolarités, décalages d'encaissements, obligations "
       "fiscales et sociales, arbitrages entre équilibre économique et "
       "accessibilité des études.")
bullet(tf, "La polycrise : une hypothèse de lecture, non un constat. ",
       "Des perturbations qui peuvent se combiner et amplifier les "
       "vulnérabilités (Lawrence et al., 2024) — leurs interdépendances "
       "restent à documenter, cas par cas.", after=0)

card(s, 0.6, 5.28, 12.13, 1.42)
rect(s, 0.6, 5.28, 0.09, 1.42, fill=BRONZE)
tf = tbox(s, 0.95, 5.46, 11.55, 1.1)
p = para(tf, True, after=3)
run(p, "Question de gouvernance", 12, BRONZE_D, bold=True)
p = para(tf, line=1.12)
run(p, "Comment décider lorsque les contraintes financières, académiques, "
       "humaines et institutionnelles peuvent se renforcer mutuellement ? "
       "La gouvernance y est traitée comme une activité d'arbitrage "
       "explicite — et non comme un organigramme.", 12.5, INK, italic=True)
footer(s, 5)

# =====================================================================
# SLIDE 6 — Problématique et questions de recherche
# =====================================================================
s = new_slide()
header(s, "Problématique", "Une question centrale, quatre questions de recherche")

card(s, 0.6, 1.78, 12.13, 1.12)
rect(s, 0.6, 1.78, 0.09, 1.12, fill=BRONZE)
tf = tbox(s, 0.95, 1.92, 11.55, 0.9)
p = para(tf, True, line=1.12)
run(p, "Comment, et sous quelles conditions organisationnelles et "
       "institutionnelles, l'articulation éventuelle de l'IA et de l'IE "
       "intervient-elle dans les pratiques de gouvernance des EPES gabonais "
       "confrontés à la polycrise, et quels effets lui sont attribués ou "
       "peuvent être documentés sur la performance globale, la responsabilité "
       "sociétale et les contributions au développement durable ?",
    13, INKD, italic=True, font=SERIF)

qrs = [
    ("QR1 — Polycrise et gouvernance",
     "Comment les difficultés et leurs interdépendances reconfigurent-elles, "
     "ou non, les pratiques de gouvernance ?"),
    ("QR2 — Intelligence artificielle",
     "Quelles fonctions réelles, quels usages, quelle contribution "
     "conditionnelle à l'information et à l'anticipation ?"),
    ("QR3 — Intelligence émotionnelle",
     "Quelle place des pratiques émotionnelles et relationnelles dans le "
     "jugement, la délibération et l'action collective ?"),
    ("QR4 — Effets et conditions",
     "Performance globale, RSE, développement durable : quels effets, pour "
     "qui, selon quelles conditions et quels horizons ?"),
]
gy = [3.08, 4.68]
for i, (qt, qb) in enumerate(qrs):
    x = gx[i % 2]
    y = gy[i // 2]
    card(s, x, y, 5.95, 1.46)
    tf = tbox(s, x + 0.22, y + 0.14, 5.51, 1.22)
    p = para(tf, True, after=3)
    run(p, qt, 12.5, BRONZE_D, bold=True)
    p = para(tf, line=1.08)
    run(p, qb, 11, INK)

tf = tbox(s, 0.6, 6.32, 12.13, 0.55)
p = para(tf, True, line=1.1)
run(p, "Statuts des effets distingués dans toute la thèse : ", 10.5, MUTED)
run(p, "perçu · documenté · contribution plausible", 10.5, BRONZE_D, bold=True)
run(p, " — aucune attribution causale nette n'est annoncée.", 10.5, MUTED)
footer(s, 6)

# =====================================================================
# SLIDE 7 — Revue critique de la littérature
# =====================================================================
s = new_slide()
header(s, "Chapitre 2 — Revue critique", "Ce que la littérature éclaire — et ce qu'elle laisse ouvert")

cols = [
    ("Gouvernance des organisations et des universités", [
        "Agence, intendance, parties prenantes, dépendance aux ressources, "
        "perspectives institutionnelles et cognitives.",
        "Spécificités universitaires : autorités multiples, couplages "
        "lâches (Clark ; Weick ; Bleiklie et Kogan).",
        "Des structures formelles qui ne disent pas le pouvoir effectif "
        "(Meyer et Rowan ; DiMaggio et Powell).",
    ]),
    ("Intelligence artificielle et décision", [
        "Paradoxe automatisation–augmentation (Raisch et Krakowski, 2021).",
        "Collaboration humain–IA : résultats hétérogènes selon les tâches "
        "(Vaccaro, Almaatouq et Malone, 2024).",
        "Cadres de gestion des risques : NIST (2023, 2024) ; orientation "
        "UNESCO (Miao et Holmes, 2023).",
    ]),
    ("Intelligence émotionnelle et leadership", [
        "Modèles distincts : habiletés (Mayer et al.), trait (Petrides et "
        "Furnham), compétences (Goleman), émotionnel-social (Bar-On).",
        "Apports réels mais dépendants des mesures et des situations "
        "(Joseph et Newman, 2010 ; Joseph et al., 2015).",
        "L'IE n'est ni la bienveillance, ni le charisme, ni le jugement "
        "tout entier ; ses usages peuvent être ambivalents.",
    ]),
]
cx = [0.6, 4.71, 8.82]
for i, (ct, cb) in enumerate(cols):
    card(s, cx[i], 1.78, 3.91, 3.62)
    tf = tbox(s, cx[i] + 0.2, 1.94, 3.51, 3.35)
    p = para(tf, True, after=6, line=1.08)
    run(p, ct, 12.5, BRONZE_D, bold=True)
    for b in cb:
        bullet(tf, "", b, size=10.3, after=5)

card(s, 0.6, 5.62, 12.13, 1.12)
rect(s, 0.6, 5.62, 0.09, 1.12, fill=BRONZE)
tf = tbox(s, 0.95, 5.76, 11.55, 0.9)
p = para(tf, True, after=2)
run(p, "Lacune travaillée par la thèse", 12, BRONZE_D, bold=True)
p = para(tf, line=1.1)
run(p, "L'articulation entre IA et IE dans la gouvernance des EPES reste à "
       "construire : sans circularité (le concept ne présuppose pas ses "
       "effets) et sans techno-solutionnisme.", 12, INK)
footer(s, 7)

# =====================================================================
# SLIDE 8 — Cadre conceptuel : la gouvernance augmentée
# =====================================================================
s = new_slide()
header(s, "Chapitre 3 — Cadre conceptuel", "La gouvernance augmentée : un construit de travail")

card(s, 0.6, 1.78, 12.13, 1.95)
rect(s, 0.6, 1.78, 0.09, 1.95, fill=BRONZE)
tf = tbox(s, 0.95, 1.96, 11.55, 1.65)
p = para(tf, True, after=4)
run(p, "Définition opérationnelle (section 3.2.4)", 11.5, BRONZE_D, bold=True,
    spc=60)
p = para(tf, line=1.18)
run(p, "« Configuration décisionnelle dans laquelle des fonctions "
       "d'intelligence artificielle et des pratiques humaines relevant de "
       "l'intelligence émotionnelle sont articulées, au sein d'une même "
       "séquence ou de séquences reliées, avec des modalités repérables "
       "d'interprétation, d'arbitrage, de mise en œuvre ou de révision — "
       "sous une responsabilité humaine identifiable. »",
    14, INKD, italic=True, font=SERIF)

tf = tbox(s, 0.7, 4.0, 12.0, 1.35)
bullet(tf, "Définie indépendamment de ses résultats. ",
       "« Augmentée » ne signifie pas supérieure : les effets sont des "
       "questions empiriques distinctes (anti-tautologie).", first=True)
bullet(tf, "Des frontières disciplinées. ",
       "Numérisation ≠ automatisation ≠ IA ; l'IE ≠ bienveillance, charisme "
       "ou jugement professionnel tout entier.")

tf = tbox(s, 0.7, 5.42, 12.0, 0.35)
p = para(tf, True)
run(p, "Configurations comparées — sans échelle de progrès :", 11.5, MUTED,
    bold=True)
chips = ["Non-usage", "Assistance", "Coexistence", "Orchestration"]
cxp = 0.7
for cpt in chips:
    ch = rect(s, cxp, 5.85, 2.62, 0.52, fill=BRONZE_S, line=BRONZE, line_w=1.0,
              shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
    ctf = ch.text_frame
    cp = para(ctf, True, align=PP_ALIGN.CENTER)
    run(cp, cpt, 12, BRONZE_D, bold=True)
    cxp += 2.87
footer(s, 8)

# =====================================================================
# SLIDE 9 — Modèle conceptuel et propositions
# =====================================================================
s = new_slide()
header(s, "Chapitre 3 — Modèle exploratoire", "Architecture du modèle et sept propositions de recherche")

boxes = [
    ("Contexte — polycrise", "Interdépendances de crises à documenter (P1)"),
    ("Capacités mobilisées", "Fonctions d'IA (P2) · pratiques d'IE (P3)"),
    ("Gouvernance augmentée", "Orchestration IA–IE sous responsabilité "
     "humaine (P4)"),
    ("Effets examinés", "Performance globale (P5) · RSE et DD (P6)"),
]
bx = 0.6
bw = 2.79
for i, (bt, bb) in enumerate(boxes):
    card(s, bx, 1.82, bw, 1.28)
    rect(s, bx, 1.82, bw, 0.07, fill=BRONZE)
    tf = tbox(s, bx + 0.15, 1.98, bw - 0.3, 1.05)
    p = para(tf, True, after=2, align=PP_ALIGN.CENTER)
    run(p, bt, 12, INKD, bold=True)
    p = para(tf, align=PP_ALIGN.CENTER, line=1.05)
    run(p, bb, 9.8, MUTED)
    if i < 3:
        ar = rect(s, bx + bw + 0.06, 2.29, 0.34, 0.34, fill=BRONZE,
                  shape=MSO_SHAPE.RIGHT_ARROW)
        ar.line.fill.background()
    bx += bw + 0.46

cond = rect(s, 0.6, 3.32, 12.13, 0.55, fill=BRONZE_S, line=BRONZE, line_w=1.0,
            shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.25)
ctf = cond.text_frame
cp = para(ctf, True, align=PP_ALIGN.CENTER)
run(cp, "Conditions organisationnelles et institutionnelles (P7) : "
        "ressources, compétences, règles, culture du dialogue, contrôle, "
        "parties prenantes", 11, BRONZE_D, bold=True)

props = [
    ("P1", "Polycrise → reconfiguration des pratiques (adaptation ou "
     "centralisation)."),
    ("P2", "Contribution conditionnelle de l'IA : fonction adaptée, sorties "
     "vérifiées, supervision effective."),
    ("P3", "Contribution de l'IE au jugement et à l'action collective, sans "
     "supprimer la contestation."),
    ("P4", "Orchestration IA–IE : arbitrages plus explicites et révisables — "
     "proposition centrale."),
    ("P5", "Contribution différenciée, différée, à certaines dimensions de la "
     "performance globale."),
    ("P6", "Soutien à la RSE et au DD si impacts et long terme influencent "
     "réellement les arbitrages."),
    ("P7", "Les conditions expliquent la forme, la continuité et les "
     "conséquences de l'articulation."),
]
gy = 4.14
for i, (pn, pt_) in enumerate(props[:4]):
    tf = tbox(s, 0.6, gy + i * 0.67, 6.0, 0.62)
    p = para(tf, True, line=1.05)
    run(p, pn + "  ", 11.5, BRONZE, bold=True)
    run(p, pt_, 10.8, INK)
for i, (pn, pt_) in enumerate(props[4:]):
    tf = tbox(s, 6.9, gy + i * 0.67, 5.85, 0.62)
    p = para(tf, True, line=1.05)
    run(p, pn + "  ", 11.5, BRONZE, bold=True)
    run(p, pt_, 10.8, INK)

tf = tbox(s, 6.9, gy + 3 * 0.67, 5.85, 0.55)
p = para(tf, True, line=1.05)
run(p, "Statuts possibles : ", 10.5, MUTED)
run(p, "étayée · partiellement étayée · mise en tension · non documentée",
    10.5, BRONZE_D, bold=True)
footer(s, 9)

# =====================================================================
# SLIDE 10 — Méthodologie
# =====================================================================
s = new_slide()
header(s, "Chapitre 4 — Méthodologie", "Étude qualitative multi-cas, abductive et outillée")

meth = [
    ("Positionnement",
     "Interprétativisme à sensibilité constructiviste ; logique abductive "
     "(Dubois et Gadde, 2002) : allers-retours cadre ↔ terrain."),
    ("Terrain",
     "5 EPES gabonais (EPES-A à EPES-E), sélection raisonnée à variation "
     "maximale — critères C1 à C5 ; usage d'IA non exigé."),
    ("Participants",
     "Cible : 45 personnes distinctes — 15 DIR · 20 ACA · 10 fonctions "
     "d'appui (ADM, RH, NUM-QRSE) ; consentement individuel."),
    ("Collecte",
     "Entretiens semi-directifs (14 questions, Q1–Q14), observations "
     "autorisées, analyse documentaire, journal de terrain — triangulation."),
    ("Analyse",
     "Thématique hybride : 8 nœuds N1–N8 + codes émergents ; épisodes "
     "décisionnels reconstitués ; NVivo (matrices exploratoires)."),
    ("Rigueur et éthique",
     "Crédibilité, transférabilité, traçabilité (audit trail) ; "
     "pseudonymisation, cas codés, réflexivité du praticien-chercheur."),
]
gy = [1.78, 3.44, 5.10]
for i, (mt, mb) in enumerate(meth):
    x = gx[i % 2]
    y = gy[i // 2]
    card(s, x, y, 5.95, 1.52)
    rect(s, x, y, 0.07, 1.52, fill=BRONZE)
    tf = tbox(s, x + 0.24, y + 0.13, 5.5, 1.3)
    p = para(tf, True, after=3)
    run(p, mt, 12.5, BRONZE_D, bold=True)
    p = para(tf, line=1.08)
    run(p, mb, 10.6, INK)
footer(s, 10)

# =====================================================================
# SLIDE 11 — Architecture d'analyse des résultats (préparatoire)
# =====================================================================
s = new_slide()
header(s, "Chapitre 5 — Présentation et analyse des résultats",
       "Architecture d'analyse des résultats (préparatoire)")

note = rect(s, 0.6, 1.78, 12.13, 0.62, fill=BRONZE_S, line=BRONZE, line_w=1.0,
            shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.25)
ntf = note.text_frame
np_ = para(ntf, True, align=PP_ALIGN.CENTER)
run(np_, "Version préparatoire : le protocole définit ce qui sera établi ; "
         "les exemples illustratifs du manuscrit sont fictifs et à remplacer "
         "par le corpus réel.", 11.5, BRONZE_D, bold=True)

steps = [
    ("1", "Corpus réel",
     "Cas confirmés, participants distincts, écarts justifiés au protocole, "
     "bilan de suffisance informationnelle."),
    ("2", "Monographies intra-cas",
     "Configurations de gouvernance et épisodes décisionnels, sources et "
     "restrictions explicites."),
    ("3", "Comparaison inter-cas",
     "Contrastes et conditions — configurations comparées, établissements "
     "non classés."),
    ("4", "Confrontation de P1 à P7",
     "Statuts argumentés, cas négatifs, explications rivales (Maxwell, "
     "2004), triangulation."),
    ("5", "Révision du modèle",
     "Conserver, restreindre, scinder, reformuler, suspendre ou retirer — "
     "chaque décision tracée."),
]
y = 2.62
for n_, st_, sd_ in steps:
    circ = rect(s, 0.75, y + 0.06, 0.5, 0.5, fill=INKD, line=BRONZE,
                line_w=1.25, shape=MSO_SHAPE.OVAL)
    ctf = circ.text_frame
    cp = para(ctf, True, align=PP_ALIGN.CENTER)
    run(cp, n_, 14, BRONZE_S, bold=True, font=SERIF)
    tf = tbox(s, 1.5, y, 11.2, 0.68)
    p = para(tf, True, line=1.08)
    run(p, st_ + " — ", 12.5, BRONZE_D, bold=True)
    run(p, sd_, 12, INK)
    y += 0.83
footer(s, 11)

# =====================================================================
# SLIDE 12 — Effets : performance globale, RSE, DD
# =====================================================================
s = new_slide()
header(s, "Chapitres 2, 5 et 6 — Évaluation des effets",
       "Trois registres liés, mais non interchangeables")

cols = [
    ("Performance globale", [
        "Cinq dimensions : économique, académique, humaine, sociale, "
        "environnementale.",
        "Pas de score unique ni de compensation automatique entre "
        "dimensions.",
        "Indicateurs datés, périmètres explicites, explications rivales "
        "examinées.",
    ]),
    ("Responsabilité sociétale", [
        "Répondre des impacts, au-delà de la philanthropie (Carroll ; "
        "Wood ; ISO 26000).",
        "Lecture universitaire : impacts organisationnels, éducatifs, "
        "cognitifs et sociaux (Vallaeys).",
        "Engagement ≠ pratique ≠ effet suivi ; les voix absentes sont "
        "signalées.",
    ]),
    ("Développement durable", [
        "Horizon collectif de long terme (Nations Unies, 2015 — Programme "
        "2030).",
        "Durabilité ≠ survie de l'établissement ; dématérialisation ≠ "
        "baisse d'impact démontrée.",
        "Contributions situées et plausibles ; le recul temporel manque "
        "alors qu'il est dit.",
    ]),
]
cx = [0.6, 4.71, 8.82]
for i, (ct, cb) in enumerate(cols):
    card(s, cx[i], 1.78, 3.91, 3.85)
    rect(s, cx[i], 1.78, 3.91, 0.07, fill=BRONZE)
    tf = tbox(s, cx[i] + 0.2, 1.98, 3.51, 3.55)
    p = para(tf, True, after=6)
    run(p, ct, 13, BRONZE_D, bold=True)
    for b in cb:
        bullet(tf, "", b, size=10.5, after=6)

card(s, 0.6, 5.85, 12.13, 0.95)
tf = tbox(s, 0.85, 6.0, 11.6, 0.7)
p = para(tf, True, line=1.12)
run(p, "Exigence de lecture : ", 11.5, BRONZE_D, bold=True)
run(p, "la performance rend visibles des résultats ; la RSE, la manière de "
       "répondre des impacts ; le développement durable, l'inscription dans "
       "la durée. Un gain local ne vaut pas amélioration globale — et "
       "réciproquement.", 11.5, INK, italic=True)
footer(s, 12)

# =====================================================================
# SLIDE 13 — Recommandations et garde-fous
# =====================================================================
s = new_slide()
header(s, "Chapitre 6 — Recommandations",
       "Des options proportionnées, encadrées par des garde-fous")

card(s, 0.6, 1.78, 6.6, 4.6)
tf = tbox(s, 0.85, 1.95, 6.1, 4.3)
p = para(tf, True, after=5)
run(p, "Six options managériales (R1–R6)", 12.5, BRONZE_D, bold=True)
opts = [
    ("R1", "Clarifier l'arbitrage : registre des décisions importantes "
     "(objet, options, décideur, suivi)."),
    ("R2", "Fiabiliser les informations : définitions, sources, corrections "
     "habilitées."),
    ("R3", "Encadrer un usage d'IA : périmètre, contrôle, solution de "
     "repli, réversibilité."),
    ("R4", "Organiser le désaccord : objections exprimables, consignées et "
     "traitées."),
    ("R5", "Suivre les effets distincts : bénéficiaires, coûts et charges "
     "identifiés."),
    ("R6", "Examiner impacts et recours : en vérifiant l'effectivité, pas "
     "seulement le texte."),
]
for r_, o_ in opts:
    bullet(tf, r_ + " — ", o_, size=10.8, after=5)

card(s, 7.5, 1.78, 5.23, 4.6)
tf = tbox(s, 7.74, 1.95, 4.78, 4.3)
p = para(tf, True, after=5)
run(p, "Garde-fous et feuille de route", 12.5, BRONZE_D, bold=True)
bullet(tf, "", "Cadres de référence : NIST AI RMF (2023) et profil IA "
       "générative (2024) ; orientation UNESCO (Miao et Holmes, 2023).",
       size=10.8, after=5)
bullet(tf, "", "Fiche de traçabilité des arbitrages : information produite "
       "→ vérification → objection → décideur → suivi.", size=10.8, after=5)
bullet(tf, "", "Feuille de route conditionnelle en six phases : diagnostic, "
       "préparation, essai limité, évaluation, arbitrage, réexamen.",
       size=10.8, after=5)
bullet(tf, "", "Ne pas utiliser, réduire ou arrêter un usage d'IA demeure "
       "une décision de gouvernance légitime et argumentable.",
       size=10.8, after=0)

tf = tbox(s, 0.6, 6.5, 12.13, 0.4)
p = para(tf, True)
run(p, "Options indicatives — à rattacher à des constats réels issus du "
       "terrain, avec leur coût complet et leur alternative sans IA.",
    10.5, MUTED, italic=True)
footer(s, 13)

# =====================================================================
# SLIDE 14 — Contributions, limites, perspectives
# =====================================================================
s = new_slide()
header(s, "Discussion et conclusion",
       "Contributions attendues, limites assumées, perspectives")

cols = [
    ("Contributions attendues", [
        "Conceptuelle : frontières entre capacités, processus et effets "
        "(anti-circularité).",
        "Processuelle : mécanismes d'articulation reconstitués par "
        "épisodes décisionnels.",
        "Contextuelle : conditions spécifiques aux EPES gabonais en "
        "situation de polycrise.",
        "Managériale (DBA) : une aide au discernement des dirigeants et "
        "des instances.",
    ]),
    ("Limites assumées", [
        "Pas de représentativité statistique : généralisation analytique "
        "prudente.",
        "IE étudiée par des pratiques situées — aucune mesure "
        "psychométrique.",
        "Étude transversale : les effets durables ne sont pas établis "
        "d'avance.",
        "Praticien-chercheur : réflexivité outillée (journal, mémos, cas "
        "négatifs, audit trail).",
    ]),
    ("Perspectives", [
        "Suivi longitudinal des pratiques et des apprentissages "
        "organisationnels.",
        "Voix des étudiants, des familles et des partenaires, aujourd'hui "
        "indirectes.",
        "Comparaisons élargies : frontières de transfert des mécanismes, "
        "sans classement.",
        "Évaluation des outils d'action (fiches, feuilles de route) en "
        "usage réel.",
    ]),
]
cx = [0.6, 4.71, 8.82]
for i, (ct, cb) in enumerate(cols):
    card(s, cx[i], 1.78, 3.91, 4.72)
    rect(s, cx[i], 1.78, 3.91, 0.07, fill=BRONZE)
    tf = tbox(s, cx[i] + 0.2, 1.98, 3.51, 4.4)
    p = para(tf, True, after=6)
    run(p, ct, 13, BRONZE_D, bold=True)
    for b in cb:
        bullet(tf, "", b, size=10.3, after=5)
footer(s, 14)

# =====================================================================
# SLIDE 15 — Merci
# =====================================================================
s = new_slide(bg=INKD)
rect(s, 0, 0, 13.333, 0.06, fill=BRONZE)
rect(s, 6.585, 1.7, 0.16, 0.16, fill=BRONZE, shape=MSO_SHAPE.DIAMOND)

tf = tbox(s, 1.5, 2.15, 10.33, 1.1)
p = para(tf, True, align=PP_ALIGN.CENTER)
run(p, "Merci de votre attention", 40, BRONZE_S, bold=True, font=SERIF)

tf = tbox(s, 2.0, 3.5, 9.33, 1.2)
p = para(tf, True, align=PP_ALIGN.CENTER, line=1.25)
run(p, "La gouvernance augmentée : des capacités techniques et humaines "
       "articulées, examinées et révisables — au service de décisions dont "
       "les raisons peuvent être discutées.", 14.5, WHITE, italic=True,
    font=SERIF)

rect(s, 6.585, 4.95, 0.16, 0.16, fill=BRONZE, shape=MSO_SHAPE.DIAMOND)

tf = tbox(s, 2.0, 5.3, 9.33, 1.0)
p = para(tf, True, align=PP_ALIGN.CENTER, after=3)
run(p, "Serge Patrick MINANG", 15, BRONZE_S, bold=True)
p = para(tf, align=PP_ALIGN.CENTER)
run(p, "La gouvernance augmentée des EPES gabonais — thèse de Doctorate of "
       "Business Administration (DBA)", 11, RGBColor.from_string("9AA5B0"))

footer(s, 15, light=True)

# ---- Métadonnées ----
cp = prs.core_properties
cp.title = ("Soutenance DBA — La gouvernance augmentée des EPES gabonais "
            "(15 slides)")
cp.author = "Serge Patrick MINANG"
cp.subject = ("Thèse DBA — IA, IE, performance globale, RSE, développement "
              "durable")
cp.comments = ("Proposition IA — à valider par l'auteur. Contenu sourcé : "
               "document de thèse fourni par l'auteur (20/09/2026) et dépôt "
               "These-Presidence (REPRISE.md, style.css). Aucune donnée de "
               "terrain inventée ; aucun résultat acquis ; pas de date de "
               "soutenance.")

OUT = "presentation/Soutenance_DBA_MINANG_15_slides.pptx"
prs.save(OUT)
print("OK —", OUT, "—", len(prs.slides._sldIdLst), "slides")
