# -*- coding: utf-8 -*-
"""Déclinaison PowerPoint du canevas Valax (11 slides) — Thèse DBA S. P. MINANG.

Structure imposée par les consignes transmises par l'auteur (Professeur VALAX,
Directeur du DBA) : 1 titre · 2 intérêt actuel · 3 revue de littérature
(2 slides) · 4 cadre théorique · 5 design de recherche · 6 résultats ·
7 analyse des résultats · 8 implications managériales · 9 limites et
perspectives · 10 conclusion.

Sources : document de thèse fourni par l'auteur (20/09/2026) + dépôt.
Garde-fous (D9) : chapitres 5–6 préparatoires → slides 6–7 = architecture de
restitution explicite, aucun résultat inventé ; codes EPES-A à EPES-E ;
aucune date de soutenance ; charte encre/bronze/papier.

Sortie : presentation/Soutenance_DBA_MINANG_canevas_Valax_11_slides.pptx
Statut : proposition IA — à valider par l'auteur. Trame détaillée :
presentation/CANEVAS_VALAX.md
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

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
GREY = RGBColor.from_string("9AA5B0")

SERIF = "Georgia"
SANS = "Segoe UI"
FOOTER_TXT = ("S. P. MINANG — Thèse DBA · Gouvernance augmentée des EPES "
              "gabonais · canevas Valax")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
GX = [0.6, 6.78]
GY = [1.78, 3.44, 5.10]


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
    c_txt = GREY if light else MUTED
    rect(s, 0.6, 7.06, 12.13, 0.012, fill=c_line)
    tf = tbox(s, 0.6, 7.14, 9.9, 0.28)
    run(para(tf, True), FOOTER_TXT, 8.5, c_txt)
    tf = tbox(s, 11.53, 7.14, 1.2, 0.28)
    run(para(tf, True, align=PP_ALIGN.RIGHT), "%d / 11" % n, 8.5, c_txt)


def card(s, x, y, w, h, accent=False):
    if accent:
        rect(s, x, y, 0.07, h, fill=BRONZE)
    return rect(s, x, y, w, h, fill=CARD, line=LINE, line_w=1.0,
                shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)


def bullet(tf, lead, rest, size=11.5, first=False, after=6):
    p = para(tf, first, after=after, line=1.1)
    run(p, "—  ", size, BRONZE, bold=True)
    if lead:
        run(p, lead, size, BRONZE_D, bold=True)
    run(p, rest, size, INK)
    return p


def bandeau(s, y, h, label, text, size=11.5):
    b = rect(s, 0.6, y, 12.13, h, fill=BRONZE_S, line=BRONZE, line_w=1.0,
             shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
    tf = tbox(s, 0.9, y + 0.1, 11.55, h - 0.2, anchor=MSO_ANCHOR.MIDDLE)
    p = para(tf, True, line=1.12)
    if label:
        run(p, label + " ", size, BRONZE_D, bold=True)
    run(p, text, size, INKD)
    return b


# =====================================================================
# S1 — Titre (rubrique 1)
# =====================================================================
s = new_slide()
mono = rect(s, 6.39, 0.62, 0.56, 0.56, fill=INKD, line=BRONZE, line_w=1.75,
            shape=MSO_SHAPE.OVAL)
mtf = mono.text_frame
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
    "Support de soutenance — canevas Valax — document de travail", 10.5,
    BRONZE_S, spc=120)

# =====================================================================
# S2 — Intérêt actuel du sujet (rubrique 2)
# =====================================================================
s = new_slide()
header(s, "Rubrique 2 — Intérêt actuel du sujet",
       "Pourquoi ce sujet, maintenant ?")

cards = [
    ("Un contexte sous tension",
     "Les EPES gabonais cumulent des contraintes financières, académiques et "
     "institutionnelles interconnectées — une configuration de « polycrise » "
     "à documenter, cas par cas."),
    ("Une technologie qui change la décision",
     "L'IA se diffuse dans le pilotage des organisations ; ses effets réels "
     "sur la gouvernance restent à établir — sans techno-solutionnisme."),
    ("Un angle mort de la littérature",
     "L'articulation entre IA et intelligence émotionnelle dans la gouvernance "
     "des établissements privés d'enseignement supérieur n'est pas documentée."),
    ("Une utilité managériale (DBA)",
     "Identifier les conditions de décisions rapides qui préservent la qualité "
     "académique, l'équilibre humain, la RSE et le développement durable."),
]
for i, (t_, d_) in enumerate(cards):
    x = GX[i % 2]
    y = GY[i // 2]
    card(s, x, y, 5.95, 1.52, accent=True)
    tf = tbox(s, x + 0.24, y + 0.13, 5.5, 1.3)
    p = para(tf, True, after=3)
    run(p, t_, 12.5, BRONZE_D, bold=True)
    p = para(tf, line=1.08)
    run(p, d_, 10.8, INK)

bandeau(s, 5.32, 1.32, "Position de la thèse :",
        "ni promesse technologique, ni rejet de principe — un objet à "
        "construire et à examiner sur le terrain.")
footer(s, 2)

# =====================================================================
# S3 — Revue de la littérature (1/2) (rubrique 3)
# =====================================================================
s = new_slide()
header(s, "Rubrique 3 — Revue de la littérature (1/2)",
       "Gouverner une organisation académique")

cols = [
    ("Lectures plurielles de la gouvernance", [
        "Agence : contrôle et asymétries d'information (Jensen et Meckling).",
        "Intendance : confiance et engagement (Davis et al.).",
        "Parties prenantes : attentes concurrentes (Freeman ; Mitchell et al.).",
        "Dépendance aux ressources : contraintes externes (Pfeffer et "
        "Salancik).",
    ]),
    ("Légitimité et spécificités universitaires", [
        "Conformité, mythes et découplage (Meyer et Rowan ; DiMaggio et "
        "Powell).",
        "Autorités multiples et coordination (Clark).",
        "Couplage lâche des organisations éducatives (Weick).",
        "Transformations managériales (Bleiklie et Kogan).",
    ]),
    ("Limites des modèles classiques", [
        "Structure formelle ≠ pouvoir effectif.",
        "Rationalité limitée : décider sous incertitude (Simon).",
        "Indicateurs réactifs : ce qui est mesuré change (Espeland et Sauder).",
        "Tensions persistantes entre exigences légitimes (Smith et Lewis).",
    ]),
]
CX = [0.6, 4.71, 8.82]
for i, (ct, cb) in enumerate(cols):
    card(s, CX[i], 1.78, 3.91, 3.95)
    rect(s, CX[i], 1.78, 3.91, 0.07, fill=BRONZE)
    tf = tbox(s, CX[i] + 0.2, 1.98, 3.51, 3.65)
    p = para(tf, True, after=6, line=1.08)
    run(p, ct, 12.5, BRONZE_D, bold=True)
    for b in cb:
        bullet(tf, "", b, size=10.3, after=5)

bandeau(s, 5.95, 0.82, "Constat :",
        "aucune approche seule n'éclaire la décision en contexte de "
        "polycrise — d'où un cadre intégré.")
footer(s, 3)

# =====================================================================
# S4 — Revue de la littérature (2/2) (rubrique 3)
# =====================================================================
s = new_slide()
header(s, "Rubrique 3 — Revue de la littérature (2/2)",
       "IA, IE et finalités : la lacune instruite")

cols = [
    ("Intelligence artificielle et décision", [
        "Automatisation vs augmentation : un paradoxe (Raisch et Krakowski, "
        "2021).",
        "Combinaisons humain–IA : gains non automatiques (Vaccaro et al., "
        "2024).",
        "Gestion des risques : NIST (2023, 2024) ; orientation UNESCO "
        "(Miao et Holmes, 2023).",
    ]),
    ("Intelligence émotionnelle", [
        "Modèles distincts : habiletés, trait, compétences, émotionnel-social "
        "(Mayer et al. ; Petrides et Furnham ; Goleman ; Bar-On).",
        "Apports réels mais dépendants des mesures (Joseph et al., 2015).",
        "Usages ambivalents possibles (Côté et al., 2011).",
    ]),
    ("Polycrise et finalités", [
        "Crises interdépendantes : stress communs, effets de propagation, "
        "rétroactions (Lawrence et al., 2024).",
        "Performance globale, RSE, développement durable : registres liés, "
        "non interchangeables (ISO 26000 ; Vallaeys ; ONU, 2015).",
    ]),
]
for i, (ct, cb) in enumerate(cols):
    card(s, CX[i], 1.78, 3.91, 3.3)
    rect(s, CX[i], 1.78, 3.91, 0.07, fill=BRONZE)
    tf = tbox(s, CX[i] + 0.2, 1.98, 3.51, 3.0)
    p = para(tf, True, after=6, line=1.08)
    run(p, ct, 12.5, BRONZE_D, bold=True)
    for b in cb:
        bullet(tf, "", b, size=10.3, after=5)

card(s, 0.6, 5.32, 12.13, 1.42, accent=True)
tf = tbox(s, 0.95, 5.5, 11.55, 1.15)
p = para(tf, True, after=3)
run(p, "Lacune instruite par la thèse", 12, BRONZE_D, bold=True)
p = para(tf, line=1.1)
run(p, "L'articulation IA–IE dans la gouvernance des EPES n'est documentée "
       "nulle part : ni cadre non circulaire, ni données contextuelles sur "
       "l'enseignement supérieur privé africain.", 12, INK, italic=True)
footer(s, 4)

# =====================================================================
# S5 — Cadre théorique (rubrique 4)
# =====================================================================
s = new_slide()
header(s, "Rubrique 4 — Cadre théorique",
       "La gouvernance augmentée : cadre et propositions")

card(s, 0.6, 1.78, 12.13, 1.32, accent=True)
tf = tbox(s, 0.95, 1.93, 11.55, 1.1)
p = para(tf, True, after=2)
run(p, "Définition opérationnelle (chap. 3, § 3.2.4)", 11, BRONZE_D, bold=True)
p = para(tf, line=1.12)
run(p, "« Configuration décisionnelle où des fonctions d'IA et des pratiques "
       "relevant de l'intelligence émotionnelle sont articulées, avec des "
       "modalités repérables d'interprétation, d'arbitrage, de mise en œuvre "
       "ou de révision — sous une responsabilité humaine identifiable. »",
    12.5, INKD, italic=True, font=SERIF)

boxes = [
    ("Contexte", "Polycrise : interdépendances à documenter (P1)"),
    ("Capacités", "IA (P2) · IE (P3) · jugement professionnel"),
    ("Gouvernance augmentée", "Orchestration sous responsabilité humaine (P4)"),
    ("Effets", "Performance globale (P5) · RSE et DD (P6)"),
]
bx = 0.6
bw = 2.79
for i, (bt, bb) in enumerate(boxes):
    card(s, bx, 3.32, bw, 1.18)
    rect(s, bx, 3.32, bw, 0.07, fill=BRONZE)
    tf = tbox(s, bx + 0.14, 3.46, bw - 0.28, 0.98)
    p = para(tf, True, after=2, align=PP_ALIGN.CENTER)
    run(p, bt, 11.5, INKD, bold=True)
    p = para(tf, align=PP_ALIGN.CENTER, line=1.02)
    run(p, bb, 9.3, MUTED)
    if i < 3:
        ar = rect(s, bx + bw + 0.06, 3.74, 0.32, 0.32, fill=BRONZE,
                  shape=MSO_SHAPE.RIGHT_ARROW)
        ar.line.fill.background()
    bx += bw + 0.46

bandeau(s, 4.68, 0.6, "Conditions (P7) :",
        "ressources, compétences, règles, culture du dialogue, contrôle, "
        "parties prenantes.", size=11)

tf = tbox(s, 0.6, 5.52, 12.13, 1.35)
p = para(tf, True, after=4, line=1.15)
run(p, "Sept propositions (P1–P7) : ", 11.5, BRONZE_D, bold=True)
run(p, "polycrise→pratiques · contribution conditionnelle de l'IA · IE et "
       "action collective · orchestration IA–IE (proposition centrale) · "
       "performance globale · RSE et DD · conditions organisationnelles et "
       "institutionnelles.", 11.5, INK)
p = para(tf, line=1.15)
run(p, "Garde-fou conceptuel : ", 11.5, BRONZE_D, bold=True)
run(p, "la gouvernance augmentée est définie indépendamment de ses effets — "
       "les bénéfices sont des questions empiriques, pas des définitions.",
    11.5, INK)
footer(s, 5)

# =====================================================================
# S6 — Design de recherche (rubrique 5)
# =====================================================================
s = new_slide()
header(s, "Rubrique 5 — Design de recherche",
       "Étude qualitative multi-cas, abductive et outillée")

meth = [
    ("Positionnement",
     "Interprétativisme à sensibilité constructiviste ; logique abductive "
     "(Dubois et Gadde, 2002)."),
    ("Terrain",
     "5 EPES gabonais (EPES-A à EPES-E), variation maximale, critères C1–C5 ; "
     "usage d'IA non exigé."),
    ("Participants",
     "Cible : 45 personnes distinctes — 15 DIR · 20 ACA · 10 fonctions d'appui "
     "(ADM, RH, NUM-QRSE)."),
    ("Collecte",
     "Entretiens semi-directifs (Q1–Q14), observations autorisées, documents, "
     "journal de terrain."),
    ("Analyse",
     "Thématique hybride (N1–N8 + codes émergents), épisodes décisionnels, "
     "NVivo — matrices exploratoires."),
    ("Rigueur et éthique",
     "Triangulation, pseudonymisation, audit trail, réflexivité du "
     "praticien-chercheur."),
]
for i, (mt, mb) in enumerate(meth):
    x = GX[i % 2]
    y = GY[i // 2]
    card(s, x, y, 5.95, 1.52, accent=True)
    tf = tbox(s, x + 0.24, y + 0.13, 5.5, 1.3)
    p = para(tf, True, after=3)
    run(p, mt, 12.5, BRONZE_D, bold=True)
    p = para(tf, line=1.08)
    run(p, mb, 10.6, INK)
footer(s, 6)

# =====================================================================
# S7 — Résultats (rubrique 6) — préparatoire
# =====================================================================
s = new_slide()
header(s, "Rubrique 6 — Résultats",
       "Architecture de restitution (préparatoire)")

bandeau(s, 1.78, 0.62, "Aucun résultat acquis avant la collecte :",
        "structure du chapitre 5, à compléter avec le corpus réel — aucun "
        "chiffre ni verbatim anticipé.")

steps = [
    ("1", "Corpus réel",
     "Cas confirmés, participants distincts, écarts justifiés au protocole, "
     "bilan de suffisance informationnelle."),
    ("2", "Monographies intra-cas",
     "Configurations de gouvernance et épisodes décisionnels ; sources et "
     "restrictions explicites."),
    ("3", "Comparaison inter-cas",
     "Contrastes et conditions ; établissements décrits, jamais classés sur "
     "une échelle unique."),
    ("4", "Effets par registre",
     "Performance globale, RSE, DD : effets perçus / documentés / "
     "contributions plausibles, séparés."),
]
y = 2.66
for n_, st_, sd_ in steps:
    circ = rect(s, 0.78, y + 0.05, 0.5, 0.5, fill=INKD, line=BRONZE,
                line_w=1.25, shape=MSO_SHAPE.OVAL)
    ctf = circ.text_frame
    cp = para(ctf, True, align=PP_ALIGN.CENTER)
    run(cp, n_, 14, BRONZE_S, bold=True, font=SERIF)
    tf = tbox(s, 1.52, y, 11.2, 0.68)
    p = para(tf, True, line=1.08)
    run(p, st_ + " — ", 12.5, BRONZE_D, bold=True)
    run(p, sd_, 12, INK)
    y += 0.83

bandeau(s, 6.1, 0.68, "Après le terrain :",
        "les slides 7 et 8 seront réécrites à partir des résultats réels "
        "(tableau 5.17) et la mention « préparatoire » retirée.")
footer(s, 7)

# =====================================================================
# S8 — Analyse des résultats (rubrique 7) — préparatoire
# =====================================================================
s = new_slide()
header(s, "Rubrique 7 — Analyse des résultats",
       "Confronter les propositions aux données (préparatoire)")

items = [
    ("Confrontation de P1 à P7",
     "Statuts argumentés : étayée dans certaines configurations · "
     "partiellement étayée · mise en tension · non documentée."),
    ("Cas négatifs et explications rivales",
     "Les éléments contraires sont conservés (Maxwell, 2004) : aucune "
     "attribution causale nette n'est annoncée."),
    ("Triangulation des sources",
     "Entretiens × observations × documents : convergences et divergences "
     "expliquées, indépendance vérifiée."),
    ("Révision du modèle",
     "Conserver, restreindre, scinder, reformuler, suspendre, retirer ou "
     "ajouter — chaque décision tracée et argumentée."),
]
for i, (t_, d_) in enumerate(items):
    x = GX[i % 2]
    y = GY[i // 2]
    card(s, x, y, 5.95, 1.52, accent=True)
    tf = tbox(s, x + 0.24, y + 0.13, 5.5, 1.3)
    p = para(tf, True, after=3)
    run(p, t_, 12.5, BRONZE_D, bold=True)
    p = para(tf, line=1.08)
    run(p, d_, 10.8, INK)

bandeau(s, 5.32, 1.32, "Issue ouverte assumée :",
        "une gouvernance augmentée non documentée dans le périmètre étudié "
        "resterait une conclusion recevable de la recherche.")
footer(s, 8)

# =====================================================================
# S9 — Implications managériales (rubrique 8)
# =====================================================================
s = new_slide()
header(s, "Rubrique 8 — Implications managériales",
       "Des options proportionnées, encadrées par des garde-fous")

card(s, 0.6, 1.78, 6.6, 4.2)
tf = tbox(s, 0.85, 1.95, 6.1, 3.9)
p = para(tf, True, after=5)
run(p, "Six options (R1–R6)", 12.5, BRONZE_D, bold=True)
opts = [
    ("R1", "Clarifier l'arbitrage : registre des décisions importantes."),
    ("R2", "Fiabiliser les informations : définitions, sources, corrections."),
    ("R3", "Encadrer un usage d'IA : périmètre, contrôle, solution de repli."),
    ("R4", "Organiser le désaccord : objections exprimables et traitées."),
    ("R5", "Suivre les effets distincts : bénéficiaires, coûts, charges."),
    ("R6", "Examiner impacts et recours : en vérifiant l'effectivité."),
]
for r_, o_ in opts:
    bullet(tf, r_ + " — ", o_, size=10.8, after=5)

card(s, 7.5, 1.78, 5.23, 4.2)
tf = tbox(s, 7.74, 1.95, 4.78, 3.9)
p = para(tf, True, after=5)
run(p, "Garde-fous et feuille de route", 12.5, BRONZE_D, bold=True)
bullet(tf, "", "Références : NIST AI RMF (2023) et profil IA générative "
       "(2024) ; UNESCO (Miao et Holmes, 2023).", size=10.8, after=5)
bullet(tf, "", "Fiche de traçabilité : information → vérification → objection "
       "→ décideur → suivi.", size=10.8, after=5)
bullet(tf, "", "Feuille de route en 6 phases : diagnostic, préparation, essai "
       "limité, évaluation, arbitrage, réexamen.", size=10.8, after=5)
bullet(tf, "", "Ne pas déployer, réduire ou arrêter un usage d'IA reste une "
       "décision de gouvernance légitime.", size=10.8, after=0)

bandeau(s, 6.2, 0.6, "Statut :",
        "options indicatives — à rattacher aux constats réels issus du "
        "terrain, coût complet et alternative sans IA compris.")
footer(s, 9)

# =====================================================================
# S10 — Limites et perspectives (rubrique 9)
# =====================================================================
s = new_slide()
header(s, "Rubrique 9 — Limites et perspectives",
       "Limites assumées, perspectives ouvertes")

card(s, 0.6, 1.78, 6.2, 4.55)
tf = tbox(s, 0.85, 1.95, 5.7, 4.25)
p = para(tf, True, after=5)
run(p, "Limites assumées", 12.5, BRONZE_D, bold=True)
for b in [
    "Pas de représentativité statistique : généralisation analytique "
    "prudente, cinq cas contrastés.",
    "IE étudiée par des pratiques situées — aucune mesure psychométrique des "
    "personnes.",
    "Étude transversale : les effets durables ne sont pas établis d'avance.",
    "Accès inégal aux sources : qualité des preuves intégrée à "
    "l'interprétation.",
    "Praticien-chercheur : réflexivité outillée (journal, mémos, cas "
    "négatifs, audit trail).",
]:
    bullet(tf, "", b, size=10.8, after=5)

card(s, 7.1, 1.78, 5.63, 4.55)
tf = tbox(s, 7.34, 1.95, 5.15, 4.25)
p = para(tf, True, after=5)
run(p, "Perspectives", 12.5, BRONZE_D, bold=True)
for b in [
    "Suivi longitudinal : les pratiques se maintiennent-elles après "
    "l'urgence ou un changement d'équipe ?",
    "Voix des parties prenantes : étudiants, familles, partenaires — "
    "aujourd'hui indirectes.",
    "Comparaisons élargies : frontières de transfert des mécanismes, sans "
    "classement sectoriel.",
    "Évaluation des outils d'action (fiches, feuilles de route) en usage "
    "réel.",
    "Voie quantitative éventuelle : opérationnalisation distincte des "
    "concepts, sans échelle improvisée.",
]:
    bullet(tf, "", b, size=10.8, after=5)
footer(s, 10)

# =====================================================================
# S11 — Conclusion (rubrique 10)
# =====================================================================
s = new_slide(bg=INKD)
rect(s, 0, 0, 13.333, 0.06, fill=BRONZE)
rect(s, 6.585, 0.85, 0.16, 0.16, fill=BRONZE, shape=MSO_SHAPE.DIAMOND)

tf = tbox(s, 1.0, 1.2, 11.33, 1.15)
p = para(tf, True, align=PP_ALIGN.CENTER)
run(p, "Conclusion", 34, BRONZE_S, bold=True, font=SERIF)

tf = tbox(s, 1.6, 2.35, 10.13, 1.6)
p = para(tf, True, align=PP_ALIGN.CENTER, after=8, line=1.15)
run(p, "Question centrale", 12, BRONZE, bold=True, spc=120)
p = para(tf, align=PP_ALIGN.CENTER, line=1.15)
run(p, "Comment, et sous quelles conditions, l'articulation éventuelle de "
       "l'IA et de l'IE intervient-elle dans la gouvernance des EPES "
       "gabonais en polycrise — et avec quels effets documentés ?",
    13.5, WHITE, italic=True, font=SERIF)

rect(s, 4.47, 4.15, 0.16, 0.16, fill=BRONZE, shape=MSO_SHAPE.DIAMOND)

tf = tbox(s, 1.5, 4.45, 10.33, 1.35)
p = para(tf, True, align=PP_ALIGN.CENTER, after=5, line=1.15)
run(p, "Ce que la thèse apportera : ", 12.5, BRONZE_S, bold=True)
run(p, "un cadre discipliné (capacités · processus · effets), des mécanismes "
       "et conditions documentés, une aide au discernement du dirigeant.",
    12.5, WHITE)
p = para(tf, align=PP_ALIGN.CENTER, line=1.15)
run(p, "Des décisions dont les raisons, les conséquences et les limites "
       "peuvent être examinées.", 12.5, GREY, italic=True)

tf = tbox(s, 2.0, 6.05, 9.33, 0.85)
p = para(tf, True, align=PP_ALIGN.CENTER, after=3)
run(p, "Merci de votre attention", 16, BRONZE_S, bold=True, font=SERIF)
p = para(tf, align=PP_ALIGN.CENTER)
run(p, "Serge Patrick MINANG — Thèse de Doctorate of Business "
       "Administration (DBA)", 11, GREY)

footer(s, 11, light=True)

# ---- Métadonnées ----
cp = prs.core_properties
cp.title = ("Soutenance DBA — canevas Valax (11 slides) — gouvernance "
            "augmentée des EPES gabonais")
cp.author = "Serge Patrick MINANG"
cp.subject = ("Thèse DBA — IA, IE, performance globale, RSE, développement "
              "durable — structure Valax en 10 rubriques")
cp.comments = ("Proposition IA — à valider par l'auteur. Structure selon les "
               "consignes du Professeur Valax. Sources : thèse fournie "
               "(20/09/2026) + dépôt. Slides 7-8 préparatoires ; rien "
               "d'inventé ; pas de date de soutenance.")

OUT = "presentation/Soutenance_DBA_MINANG_canevas_Valax_11_slides.pptx"
prs.save(OUT)
print("OK —", OUT, "—", len(prs.slides._sldIdLst), "slides")
