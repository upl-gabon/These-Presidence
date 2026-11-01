# -*- coding: utf-8 -*-
"""Canevas Valax au format Word (.docx) — Thèse DBA S. P. MINANG.

Déclinaison DOCX de `CANEVAS_VALAX.md` (même contenu, même traçabilité).
Structure imposée par les consignes du Professeur Valax transmises par
l'auteur (20/09/2026) : 10 rubriques, revue sur 2 slides.

Garde-fous (D9) : chapitres 5–6 préparatoires (aucun résultat inventé) ;
codes EPES-A à EPES-E ; date de soutenance : 15/12/2026 (fournie par l'auteur) ; statut « proposition
IA — à valider par l'auteur ». Charte : encre #232B33 / bronze #6E4F0E.

Sortie : presentation/CANEVAS_VALAX.docx
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

INK = RGBColor(0x23, 0x2B, 0x33)
INKD = RGBColor(0x14, 0x1B, 0x22)
BRONZE = RGBColor(0x8A, 0x64, 0x14)
BRONZE_D = RGBColor(0x6E, 0x4F, 0x0E)
MUTED = RGBColor(0x5E, 0x6A, 0x76)
BRONZE_FILL = "F1E8D0"
BRONZE_HEAD = "6E4F0E"

SERIF = "Georgia"
SANS = "Segoe UI"


def shade(cell, fill):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), fill)
    cell._tc.get_or_add_tcPr().append(shd)


def set_font(run, name=SANS, size=10.5, color=INK, bold=False, italic=False):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    rfonts.set(qn("w:ascii"), name)
    rfonts.set(qn("w:hAnsi"), name)


def para(doc, before=0, after=6, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    if align is not None:
        p.alignment = align
    return p


def hrule(doc, color="8A6414", size="12"):
    p = para(doc, before=2, after=10)
    ppr = p._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), size)
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    bdr.append(bottom)
    ppr.append(bdr)
    return p


def heading(doc, text, level=1):
    p = para(doc, before=14 if level == 1 else 10, after=5)
    r = p.add_run(text)
    set_font(r, SERIF, 15 if level == 1 else 12.5,
             BRONZE_D if level == 1 else INKD, bold=True)
    return p


def bullet(doc, lead, rest, size=10.5):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(3)
    if lead:
        set_font(p.add_run(lead + " "), SANS, size, BRONZE_D, bold=True)
    set_font(p.add_run(rest), SANS, size, INK)
    return p


doc = Document()
sec = doc.sections[0]
sec.top_margin = sec.bottom_margin = Cm(2)
sec.left_margin = sec.right_margin = Cm(2)

normal = doc.styles["Normal"]
normal.font.name = SANS
normal.font.size = Pt(10.5)
normal.font.color.rgb = INK

# ---- En-tête ----
p = para(doc, after=2)
set_font(p.add_run("PROPOSITION IA — À VALIDER PAR L'AUTEUR"), SANS, 9,
         BRONZE, bold=True)

p = para(doc, after=2)
set_font(p.add_run("Canevas synthétique de soutenance"), SERIF, 22, INKD,
         bold=True)

p = para(doc, after=4)
set_font(p.add_run("Consignes du Professeur Valax — dix rubriques, onze "
                   "slides (≈ 24 minutes)"), SERIF, 12.5, MUTED, italic=True)

p = para(doc, after=8)
set_font(p.add_run("Serge Patrick MINANG — Thèse de Doctorate of Business "
                   "Administration (DBA) · « La gouvernance augmentée des "
                   "établissements privés d'enseignement supérieur au Gabon "
                   "en situation de polycrise »"), SANS, 9.5, MUTED)
hrule(doc)

p = para(doc, after=12)
set_font(p.add_run("Sources du contenu : document de thèse fourni par "
                   "l'auteur (20/09/2026) et dépôt These-Presidence. "
                   "Garde-fous : aucun résultat de terrain inventé — les "
                   "rubriques 6 et 7 présentent l'architecture de restitution "
                   "(chapitres 5–6 préparatoires) ; terrain codé EPES-A à "
                   "EPES-E ; date de soutenance : 15 décembre 2026 (fournie par "
                   "l'auteur)."),
         SANS, 9, MUTED, italic=True)

# ---- Tableau de correspondance ----
heading(doc, "Vue d'ensemble — 10 rubriques, 11 slides")
cols = ["Rubrique (Valax)", "Slide", "Titre proposé", "Message clé",
        "Durée · statut"]
widths = [Cm(3.2), Cm(1.3), Cm(3.6), Cm(5.4), Cm(3.5)]
rows = [
    ("1. Titre", "1", "Page de titre",
     "Le sujet en une phrase : articuler IA et IE pour gouverner les EPES "
     "en polycrise", "0,5 min · établi"),
    ("2. Intérêt actuel", "2", "Pourquoi ce sujet, maintenant ?",
     "Un croisement à documenter — polycrise × IA × EPES gabonais — pas "
     "une mode à suivre", "2 min · établi"),
    ("3. Revue (1/2)", "3", "Gouverner une organisation académique",
     "Aucune théorie seule n'explique la décision : lectures plurielles "
     "et limites", "2,5 min · établi"),
    ("3. Revue (2/2)", "4", "IA, IE et finalités : la lacune instruite",
     "L'articulation IA–IE dans la gouvernance des EPES n'est documentée "
     "nulle part", "2,5 min · établi"),
    ("4. Cadre théorique", "5",
     "La gouvernance augmentée : cadre et propositions",
     "GA = orchestration IA–IE sous responsabilité humaine, définie "
     "indépendamment de ses effets", "3 min · établi"),
    ("5. Design de recherche", "6",
     "Étude qualitative multi-cas, abductive",
     "5 cas (EPES-A…E), 45 participants cible, Q1–Q14, N1–N8, NVivo, "
     "triangulation", "3 min · établi"),
    ("6. Résultats", "7",
     "Résultats — architecture de restitution",
     "Ce que le chapitre 5 établira : corpus, monographies, configurations, "
     "effets", "3 min · préparatoire"),
    ("7. Analyse des résultats", "8",
     "Confronter les propositions aux données",
     "Statuts argumentés de P1–P7, cas négatifs, explications rivales, "
     "révision du modèle", "2,5 min · préparatoire"),
    ("8. Implications managériales", "9",
     "Des options proportionnées, encadrées",
     "R1–R6, feuille de route en 6 phases, garde-fous NIST/UNESCO — ne pas "
     "déployer reste légitime", "2,5 min · établi (indicatif)"),
    ("9. Limites, perspectives", "10",
     "Limites assumées, perspectives ouvertes",
     "Généralisation analytique prudente ; quatre prolongements de "
     "recherche", "2 min · établi"),
    ("10. Conclusion", "11", "Conclusion",
     "La GA : des décisions dont les raisons, les conséquences et les "
     "limites sont examinables", "1 min · établi"),
]
table = doc.add_table(rows=1, cols=5)
table.style = "Table Grid"
for i, c in enumerate(table.rows[0].cells):
    c.width = widths[i]
    shade(c, BRONZE_HEAD)
    p = c.paragraphs[0]
    set_font(p.add_run(cols[i]), SANS, 9, RGBColor(0xFF, 0xFF, 0xFF),
             bold=True)
for row in rows:
    cells = table.add_row().cells
    for i, val in enumerate(row):
        cells[i].width = widths[i]
        p = cells[i].paragraphs[0]
        set_font(p.add_run(val), SANS, 8.5, INK,
                 bold=(i == 0))

p = para(doc, before=6, after=12)
set_font(p.add_run("Durées indicatives : à ajuster au format imposé par "
                   "l'école doctorale (compressible à ≈ 15 minutes en "
                   "traitant ensemble les slides 3–4)."), SANS, 8.5, MUTED,
         italic=True)

# ---- Détail slide par slide ----
heading(doc, "Détail slide par slide")

details = [
    ("Slide 1 — Titre (rubrique 1)", [
        "Titre intégral de la thèse ; auteur ; mention du directeur de thèse "
        "(reprise des remerciements fournis — à confirmer par l'auteur).",
        "Mention sobre : « Support de soutenance — document de travail ».",
        "Date de soutenance : 15 décembre 2026 (fournie par l'auteur) ; lieu non communiqué.",
    ]),
    ("Slide 2 — Intérêt actuel du sujet (rubrique 2)", [
        "Un contexte sous tension — contraintes financières, académiques et "
        "institutionnelles interconnectées : configuration de « polycrise » "
        "(résumé ; chapitre 1, § 1.10).",
        "Une technologie qui change la décision — l'IA se diffuse dans le "
        "pilotage ; ses effets réels restent à établir, sans "
        "techno-solutionnisme (chapitre 2, § 2.5).",
        "Un angle mort de la littérature — l'articulation IA–IE dans la "
        "gouvernance des EPES n'est pas documentée (chapitre 2, "
        "§ 2.10.2–2.10.3).",
        "Une utilité managériale (DBA) — les conditions de décisions rapides "
        "qui préservent qualité académique, équilibre humain, RSE et "
        "développement durable (chapitre 3, § 3.1).",
        "Bandeau de position : « ni promesse technologique, ni rejet de "
        "principe — un objet à construire et à examiner ».",
    ]),
    ("Slide 3 — Revue de la littérature (1/2) : gouverner une organisation "
     "académique", [
        "Lectures plurielles de la gouvernance — agence (Jensen et Meckling, "
        "1976), intendance (Davis et al., 1997), parties prenantes (Freeman, "
        "1984 ; Mitchell et al., 1997), dépendance aux ressources (Pfeffer et "
        "Salancik, 2003 [1978]).",
        "Légitimité et spécificités universitaires — institutionnel (Meyer et "
        "Rowan, 1977 ; DiMaggio et Powell, 1983) ; autorités multiples "
        "(Clark, 1983), couplage lâche (Weick, 1976), transformations "
        "managériales (Bleiklie et Kogan, 2007).",
        "Limites des modèles classiques — structure formelle ≠ pouvoir "
        "effectif ; rationalité limitée (Simon, 1955) ; réactivité aux "
        "indicateurs (Espeland et Sauder, 2007) ; tensions persistantes "
        "(Smith et Lewis, 2011).",
        "Transition : aucune approche seule n'éclaire la décision en "
        "polycrise.",
    ]),
    ("Slide 4 — Revue de la littérature (2/2) : IA, IE et finalités", [
        "IA et décision — paradoxe automatisation–augmentation (Raisch et "
        "Krakowski, 2021) ; combinaisons humain–IA non systématiquement "
        "supérieures (Vaccaro et al., 2024) ; gestion des risques (NIST, "
        "2023, 2024 ; Miao et Holmes, 2023).",
        "Intelligence émotionnelle — modèles distincts (Mayer et al., 2004 ; "
        "Petrides et Furnham, 2001 ; Goleman, 2001 ; Bar-On, 2006) ; apports "
        "dépendants des mesures (Joseph et al., 2015) ; usages ambivalents "
        "(Côté et al., 2011).",
        "Polycrise et finalités — crises interdépendantes (Lawrence et al., "
        "2024) ; performance globale, RSE et développement durable : "
        "registres liés, non interchangeables (ISO 26000 ; Vallaeys, 2014 ; "
        "Nations Unies, 2015).",
        "Lacune instruite (encadré) — l'articulation IA–IE dans la "
        "gouvernance des EPES : ni cadre non circulaire, ni données "
        "contextuelles (Gabon).",
    ]),
    ("Slide 5 — Cadre théorique (rubrique 4)", [
        "Définition opérationnelle de la gouvernance augmentée (chapitre 3, "
        "§ 3.2.4, citation).",
        "Architecture : contexte de polycrise → capacités (IA · IE · jugement "
        "professionnel) → orchestration sous responsabilité humaine → effets "
        "(performance globale · RSE · développement durable), conditions "
        "transversales (P7).",
        "Sept propositions P1–P7 (chapitre 3, § 3.6) ; proposition centrale "
        "P4.",
        "Garde-fou conceptuel : la gouvernance augmentée est définie "
        "indépendamment de ses effets (anti-tautologie).",
    ]),
    ("Slide 6 — Design de recherche (rubrique 5)", [
        "Positionnement interprétativiste à sensibilité constructiviste ; "
        "logique abductive (Dubois et Gadde, 2002).",
        "Terrain : 5 EPES (codes EPES-A à EPES-E), critères C1–C5, variation "
        "maximale ; usage d'IA non exigé.",
        "Participants : cible de 45 personnes distinctes (15 direction · "
        "20 académiques · 10 fonctions d'appui) ; consentement individuel.",
        "Collecte : entretiens semi-directifs (Q1–Q14), observations "
        "autorisées, analyse documentaire, journal de terrain.",
        "Analyse : thématique hybride (N1–N8 + codes émergents), épisodes "
        "décisionnels, NVivo ; rigueur et éthique (triangulation, "
        "pseudonymisation, réflexivité du praticien-chercheur).",
    ]),
    ("Slide 7 — Résultats (rubrique 6) — PRÉPARATOIRE", [
        "Bandeau visible : « Aucun résultat acquis avant la collecte — "
        "structure de restitution du chapitre 5, à compléter avec le corpus "
        "réel ».",
        "Corpus réel — cas confirmés, participants distincts, écarts "
        "justifiés au protocole, suffisance informationnelle (chapitre 5, "
        "§ 5.1).",
        "Monographies intra-cas — configurations de gouvernance, épisodes "
        "décisionnels, sources et restrictions (§ 5.2).",
        "Comparaison inter-cas — contrastes et conditions ; établissements "
        "décrits, non classés (§ 5.8).",
        "Effets par registre — performance globale, RSE, développement "
        "durable : effets perçus / documentés / contributions plausibles "
        "(§ 5.7). Règle : aucun chiffre ni verbatim anticipé.",
    ]),
    ("Slide 8 — Analyse des résultats (rubrique 7) — PRÉPARATOIRE", [
        "Confrontation de P1 à P7 — statuts argumentés : étayée dans "
        "certaines configurations · partiellement étayée · mise en tension · "
        "non documentée (chapitre 5, § 5.9).",
        "Cas négatifs et explications rivales (Maxwell, 2004) — les éléments "
        "contraires sont conservés ; aucune attribution causale nette.",
        "Triangulation — entretiens × observations × documents ; "
        "convergences et divergences expliquées.",
        "Révision du modèle — conserver, restreindre, scinder, reformuler, "
        "suspendre, retirer ou ajouter ; chaque décision tracée (chapitre 6, "
        "§ 6.4).",
    ]),
    ("Slide 9 — Implications managériales (rubrique 8)", [
        "Six options R1–R6 (chapitre 6, § 6.6) : clarifier l'arbitrage · "
        "fiabiliser les informations · encadrer un usage d'IA · organiser le "
        "désaccord · suivre les effets distincts · examiner impacts et "
        "recours.",
        "Feuille de route conditionnelle en 6 phases (§ 6.8) : diagnostic, "
        "préparation, essai limité, évaluation, arbitrage, réexamen.",
        "Garde-fous : NIST AI RMF (2023) et profil IA générative (2024) ; "
        "orientation UNESCO (Miao et Holmes, 2023) ; fiche de traçabilité des "
        "arbitrages.",
        "Mention de statut : « options indicatives — à rattacher aux constats "
        "réels » ; ne pas déployer reste une décision de gouvernance "
        "légitime.",
    ]),
    ("Slide 10 — Limites et perspectives (rubrique 9)", [
        "Limites (chapitre 6, § 6.9) : pas de représentativité statistique ; "
        "IE étudiée par pratiques situées (aucune mesure psychométrique) ; "
        "étude transversale (effets durables non établis d'avance) ; accès "
        "inégal aux sources ; praticien-chercheur (réflexivité outillée).",
        "Perspectives (§ 6.10) : suivi longitudinal ; voix des étudiants, "
        "familles, partenaires ; comparaisons élargies (frontières de "
        "transfert, sans classement) ; évaluation des outils d'action en "
        "usage réel.",
    ]),
    ("Slide 11 — Conclusion (rubrique 10)", [
        "Rappel bref de la question centrale ; ce que la thèse apportera : "
        "un cadre discipliné (capacités · processus · effets), des mécanismes "
        "et conditions documentés, une aide au discernement du dirigeant "
        "(finalité DBA).",
        "Clôture sobre : « des décisions dont les raisons, les conséquences "
        "et les limites peuvent être examinées » ; remerciement au jury.",
        "Issue ouverte assumée : une gouvernance augmentée non documentée "
        "dans le périmètre resterait une conclusion recevable.",
    ]),
]
for title, items in details:
    heading(doc, title, level=2)
    for it in items:
        bullet(doc, "", it)

# ---- Points de vigilance ----
heading(doc, "Points de vigilance (cohérence avec le dépôt)")
vigilances = [
    "Statuts explicites partout (échange jury n° 3) : slides 7–8 marquées "
    "« préparatoire » ; slide 9 « options indicatives » ; contributions "
    "« attendues » à l'oral.",
    "Dédicace et remerciements : absentes du canevas Valax. Les slides 2–3 "
    "de la version 15 slides restent disponibles — à trancher avec le "
    "directeur (remerciement oral en ouverture ou slides optionnelles).",
    "Revue sur 2 slides équilibrées : (1/2) gouvernance et universités ; "
    "(2/2) IA–IE–finalités ; la lacune n'apparaît qu'en fin de slide 4 pour "
    "préparer le cadre théorique.",
    "Après la collecte : slides 7–8 à réécrire à partir des résultats réels "
    "(tableau 5.17) et retrait des mentions « préparatoire ».",
]
for i, v in enumerate(vigilances, 1):
    p = doc.add_paragraph(style="List Number")
    p.paragraph_format.space_after = Pt(3)
    set_font(p.add_run(v), SANS, 10.5, INK)

# ---- Fichiers ----
heading(doc, "Fichiers du dossier presentation/")
t2 = doc.add_table(rows=1, cols=2)
t2.style = "Table Grid"
for i, h in enumerate(["Fichier", "Rôle"]):
    t2.rows[0].cells[i].width = Cm(7 if i == 0 else 10)
    shade(t2.rows[0].cells[i], BRONZE_HEAD)
    set_font(t2.rows[0].cells[i].paragraphs[0].add_run(h), SANS, 9,
             RGBColor(0xFF, 0xFF, 0xFF), bold=True)
for f, role in [
    ("CANEVAS_VALAX.docx", "Ce document (canevas Word, 10 rubriques)"),
    ("CANEVAS_VALAX.md", "Canevas source (même contenu, format Markdown)"),
    ("CANEVAS_VALAX_DEVELOPPE.md", "Version développée : script oral par slide"),
    ("CANEVAS_VALAX_DEVELOPPE.docx", "Version développée Word (annotable)"),
    ("CANEVAS_VALAX_DEVELOPPE.pdf", "Version développée PDF (14 pages)"),
    ("generer_canevas_valax_developpe_docx.py", "Régénération du Word développé"),
    ("generer_canevas_valax_developpe_pdf.py", "Régénération du PDF développé"),
    ("Soutenance_DBA_MINANG_canevas_Valax_11_slides.pptx",
     "Déclinaison PowerPoint du canevas (11 slides 16:9)"),
    ("generer_canevas_valax_docx.py", "Régénération de ce document"),
    ("generer_canevas_valax_pptx.py", "Régénération du PowerPoint"),
    ("Soutenance_DBA_MINANG_15_slides.pptx",
     "Version 15 slides (contient dédicace et remerciements)"),
]:
    cells = t2.add_row().cells
    cells[0].width = Cm(7)
    cells[1].width = Cm(10)
    set_font(cells[0].paragraphs[0].add_run(f), "Consolas", 9, BRONZE_D,
             bold=True)
    set_font(cells[1].paragraphs[0].add_run(role), SANS, 9, INK)

p = para(doc, before=10, after=0)
set_font(p.add_run("Proposition IA — à valider par l'auteur. Ce document ne "
                   "contient aucune donnée de terrain : les rubriques "
                   "« Résultats » et « Analyse » seront complétées après la "
                   "collecte, à partir du corpus réel."), SANS, 8.5, MUTED,
         italic=True)

# ---- Pied de page ----
fp = sec.footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
set_font(fp.add_run("S. P. MINANG — Thèse DBA · Gouvernance augmentée des "
                    "EPES gabonais · canevas Valax — proposition IA"),
         SANS, 8, MUTED)

cp = doc.core_properties
cp.title = "Canevas de soutenance — consignes Valax (10 rubriques)"
cp.author = "Serge Patrick MINANG"
cp.subject = "Thèse DBA — gouvernance augmentée des EPES gabonais"
cp.comments = ("Proposition IA — à valider par l'auteur. Sources : document "
               "de thèse fourni (20/09/2026) et dépôt. Rubriques résultats/"
               "analyse préparatoires ; rien d'inventé.")

OUT = "presentation/CANEVAS_VALAX.docx"
doc.save(OUT)
print("OK —", OUT)
