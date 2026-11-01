# -*- coding: utf-8 -*-
"""Canevas Valax au format PDF — Thèse DBA S. P. MINANG.

Déclinaison PDF de `CANEVAS_VALAX.md` / `CANEVAS_VALAX.docx` (même contenu).
Version lisible partout : ouverture sans Word ni PowerPoint.

Garde-fous (D9) : chapitres 5–6 préparatoires (aucun résultat inventé) ;
codes EPES-A à EPES-E ; date de soutenance : 15/12/2026 (fournie par l'auteur) ; statut « proposition
IA — à valider par l'auteur ».

Sortie : presentation/CANEVAS_VALAX.pdf
"""

from fpdf import FPDF

INK = (35, 43, 51)
INKD = (20, 27, 34)
BRONZE = (138, 100, 20)
BRONZE_D = (110, 79, 14)
MUTED = (94, 106, 118)
BRONZE_S = (241, 232, 208)
WHITE = (255, 255, 255)
LINE = (227, 218, 198)

DEJA = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DEJA_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
DEJAS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

ROWS = [
    ("1. Titre", "1", "Page de titre",
     "Le sujet en une phrase : articuler IA et IE pour gouverner les EPES en polycrise",
     "0,5 min · établi"),
    ("2. Intérêt actuel", "2", "Pourquoi ce sujet, maintenant ?",
     "Un croisement à documenter — polycrise × IA × EPES gabonais — pas une mode à suivre",
     "2 min · établi"),
    ("3. Revue (1/2)", "3", "Gouverner une organisation académique",
     "Aucune théorie seule n'explique la décision : lectures plurielles et limites",
     "2,5 min · établi"),
    ("3. Revue (2/2)", "4", "IA, IE et finalités : la lacune instruite",
     "L'articulation IA–IE dans la gouvernance des EPES n'est documentée nulle part",
     "2,5 min · établi"),
    ("4. Cadre théorique", "5", "La gouvernance augmentée : cadre et propositions",
     "GA = orchestration IA–IE sous responsabilité humaine, définie indépendamment de ses effets",
     "3 min · établi"),
    ("5. Design de recherche", "6", "Étude qualitative multi-cas, abductive",
     "5 cas (EPES-A…E), 45 participants cible, Q1–Q14, N1–N8, NVivo, triangulation",
     "3 min · établi"),
    ("6. Résultats", "7", "Résultats — architecture de restitution",
     "Ce que le chapitre 5 établira : corpus, monographies, configurations, effets",
     "3 min · PRÉPARATOIRE"),
    ("7. Analyse des résultats", "8", "Confronter les propositions aux données",
     "Statuts argumentés de P1–P7, cas négatifs, explications rivales, révision du modèle",
     "2,5 min · PRÉPARATOIRE"),
    ("8. Implications managériales", "9", "Des options proportionnées, encadrées",
     "R1–R6, feuille de route en 6 phases, garde-fous NIST/UNESCO — ne pas déployer reste légitime",
     "2,5 min · indicatif"),
    ("9. Limites, perspectives", "10", "Limites assumées, perspectives ouvertes",
     "Généralisation analytique prudente ; quatre prolongements de recherche",
     "2 min · établi"),
    ("10. Conclusion", "11", "Conclusion",
     "La GA : des décisions dont les raisons, les conséquences et les limites sont examinables",
     "1 min · établi"),
]

DETAILS = [
    ("Slide 1 — Titre (rubrique 1)", [
        "Titre intégral de la thèse ; auteur ; mention du directeur de thèse (reprise des remerciements fournis — à confirmer par l'auteur).",
        "Mention sobre : « Support de soutenance — document de travail ».",
        "Date de soutenance : 15 décembre 2026 (fournie par l'auteur) ; lieu non communiqué.",
    ]),
    ("Slide 2 — Intérêt actuel du sujet (rubrique 2)", [
        "Un contexte sous tension — contraintes financières, académiques et institutionnelles interconnectées : configuration de « polycrise » (résumé ; chapitre 1, § 1.10).",
        "Une technologie qui change la décision — l'IA se diffuse dans le pilotage ; ses effets réels restent à établir, sans techno-solutionnisme (chapitre 2, § 2.5).",
        "Un angle mort de la littérature — l'articulation IA–IE dans la gouvernance des EPES n'est pas documentée (chapitre 2, § 2.10.2–2.10.3).",
        "Une utilité managériale (DBA) — les conditions de décisions rapides qui préservent qualité académique, équilibre humain, RSE et développement durable (chapitre 3, § 3.1).",
        "Bandeau de position : « ni promesse technologique, ni rejet de principe — un objet à construire et à examiner ».",
    ]),
    ("Slide 3 — Revue de la littérature (1/2) : gouverner une organisation académique", [
        "Lectures plurielles de la gouvernance — agence (Jensen et Meckling, 1976), intendance (Davis et al., 1997), parties prenantes (Freeman, 1984 ; Mitchell et al., 1997), dépendance aux ressources (Pfeffer et Salancik, 2003 [1978]).",
        "Légitimité et spécificités universitaires — institutionnel (Meyer et Rowan, 1977 ; DiMaggio et Powell, 1983) ; autorités multiples (Clark, 1983), couplage lâche (Weick, 1976), transformations managériales (Bleiklie et Kogan, 2007).",
        "Limites des modèles classiques — structure formelle ≠ pouvoir effectif ; rationalité limitée (Simon, 1955) ; réactivité aux indicateurs (Espeland et Sauder, 2007) ; tensions persistantes (Smith et Lewis, 2011).",
        "Transition : aucune approche seule n'éclaire la décision en polycrise.",
    ]),
    ("Slide 4 — Revue de la littérature (2/2) : IA, IE et finalités", [
        "IA et décision — paradoxe automatisation–augmentation (Raisch et Krakowski, 2021) ; combinaisons humain–IA non systématiquement supérieures (Vaccaro et al., 2024) ; gestion des risques (NIST, 2023, 2024 ; Miao et Holmes, 2023).",
        "Intelligence émotionnelle — modèles distincts (Mayer et al., 2004 ; Petrides et Furnham, 2001 ; Goleman, 2001 ; Bar-On, 2006) ; apports dépendants des mesures (Joseph et al., 2015) ; usages ambivalents (Côté et al., 2011).",
        "Polycrise et finalités — crises interdépendantes (Lawrence et al., 2024) ; performance globale, RSE et développement durable : registres liés, non interchangeables (ISO 26000 ; Vallaeys, 2014 ; Nations Unies, 2015).",
        "Lacune instruite (encadré) — l'articulation IA–IE dans la gouvernance des EPES : ni cadre non circulaire, ni données contextuelles (Gabon).",
    ]),
    ("Slide 5 — Cadre théorique (rubrique 4)", [
        "Définition opérationnelle de la gouvernance augmentée (chapitre 3, § 3.2.4, citation).",
        "Architecture : contexte de polycrise → capacités (IA · IE · jugement professionnel) → orchestration sous responsabilité humaine → effets (performance globale · RSE · développement durable), conditions transversales (P7).",
        "Sept propositions P1–P7 (chapitre 3, § 3.6) ; proposition centrale P4.",
        "Garde-fou conceptuel : la gouvernance augmentée est définie indépendamment de ses effets (anti-tautologie).",
    ]),
    ("Slide 6 — Design de recherche (rubrique 5)", [
        "Positionnement interprétativiste à sensibilité constructiviste ; logique abductive (Dubois et Gadde, 2002).",
        "Terrain : 5 EPES (codes EPES-A à EPES-E), critères C1–C5, variation maximale ; usage d'IA non exigé.",
        "Participants : cible de 45 personnes distinctes (15 direction · 20 académiques · 10 fonctions d'appui) ; consentement individuel.",
        "Collecte : entretiens semi-directifs (Q1–Q14), observations autorisées, analyse documentaire, journal de terrain.",
        "Analyse : thématique hybride (N1–N8 + codes émergents), épisodes décisionnels, NVivo ; rigueur et éthique (triangulation, pseudonymisation, réflexivité du praticien-chercheur).",
    ]),
    ("Slide 7 — Résultats (rubrique 6) — PRÉPARATOIRE", [
        "Bandeau visible : « Aucun résultat acquis avant la collecte — structure de restitution du chapitre 5, à compléter avec le corpus réel ».",
        "Corpus réel — cas confirmés, participants distincts, écarts justifiés au protocole, suffisance informationnelle (chapitre 5, § 5.1).",
        "Monographies intra-cas — configurations de gouvernance, épisodes décisionnels, sources et restrictions (§ 5.2).",
        "Comparaison inter-cas — contrastes et conditions ; établissements décrits, non classés (§ 5.8).",
        "Effets par registre — performance globale, RSE, développement durable : effets perçus / documentés / contributions plausibles (§ 5.7). Règle : aucun chiffre ni verbatim anticipé.",
    ]),
    ("Slide 8 — Analyse des résultats (rubrique 7) — PRÉPARATOIRE", [
        "Confrontation de P1 à P7 — statuts argumentés : étayée dans certaines configurations · partiellement étayée · mise en tension · non documentée (chapitre 5, § 5.9).",
        "Cas négatifs et explications rivales (Maxwell, 2004) — les éléments contraires sont conservés ; aucune attribution causale nette.",
        "Triangulation — entretiens × observations × documents ; convergences et divergences expliquées.",
        "Révision du modèle — conserver, restreindre, scinder, reformuler, suspendre, retirer ou ajouter ; chaque décision tracée (chapitre 6, § 6.4).",
    ]),
    ("Slide 9 — Implications managériales (rubrique 8)", [
        "Six options R1–R6 (chapitre 6, § 6.6) : clarifier l'arbitrage · fiabiliser les informations · encadrer un usage d'IA · organiser le désaccord · suivre les effets distincts · examiner impacts et recours.",
        "Feuille de route conditionnelle en 6 phases (§ 6.8) : diagnostic, préparation, essai limité, évaluation, arbitrage, réexamen.",
        "Garde-fous : NIST AI RMF (2023) et profil IA générative (2024) ; orientation UNESCO (Miao et Holmes, 2023) ; fiche de traçabilité des arbitrages.",
        "Mention de statut : « options indicatives — à rattacher aux constats réels » ; ne pas déployer reste une décision de gouvernance légitime.",
    ]),
    ("Slide 10 — Limites et perspectives (rubrique 9)", [
        "Limites (chapitre 6, § 6.9) : pas de représentativité statistique ; IE étudiée par pratiques situées (aucune mesure psychométrique) ; étude transversale (effets durables non établis d'avance) ; accès inégal aux sources ; praticien-chercheur (réflexivité outillée).",
        "Perspectives (§ 6.10) : suivi longitudinal ; voix des étudiants, familles, partenaires ; comparaisons élargies (frontières de transfert, sans classement) ; évaluation des outils d'action en usage réel.",
    ]),
    ("Slide 11 — Conclusion (rubrique 10)", [
        "Rappel bref de la question centrale ; ce que la thèse apportera : un cadre discipliné (capacités · processus · effets), des mécanismes et conditions documentés, une aide au discernement du dirigeant (finalité DBA).",
        "Clôture sobre : « des décisions dont les raisons, les conséquences et les limites peuvent être examinées » ; remerciement au jury.",
        "Issue ouverte assumée : une gouvernance augmentée non documentée dans le périmètre resterait une conclusion recevable.",
    ]),
]

VIGILANCES = [
    "Statuts explicites partout (échange jury n° 3) : slides 7–8 marquées « préparatoire » ; slide 9 « options indicatives » ; contributions « attendues » à l'oral.",
    "Dédicace et remerciements : absentes du canevas Valax. Les slides 2–3 de la version 15 slides restent disponibles — à trancher avec le directeur (remerciement oral en ouverture ou slides optionnelles).",
    "Revue sur 2 slides équilibrées : (1/2) gouvernance et universités ; (2/2) IA–IE–finalités ; la lacune n'apparaît qu'en fin de slide 4 pour préparer le cadre théorique.",
    "Après la collecte : slides 7–8 à réécrire à partir des résultats réels (tableau 5.17) et retrait des mentions « préparatoire ».",
]

FILES = [
    ("CANEVAS_VALAX.docx", "Canevas Word (imprimable, annotable)"),
    ("CANEVAS_VALAX.html", "Version lisible dans tout navigateur"),
    ("CANEVAS_VALAX.pdf", "Ce document (partage et impression)"),
    ("CANEVAS_VALAX.md", "Canevas source (même contenu, format Markdown)"),
    ("CANEVAS_VALAX_DEVELOPPE.md", "Version développée : script oral par slide"),
    ("CANEVAS_VALAX_DEVELOPPE.docx", "Version développée Word (annotable)"),
    ("CANEVAS_VALAX_DEVELOPPE.pdf", "Version développée PDF (14 pages)"),
    ("generer_canevas_valax_developpe_docx.py", "Régénération du Word développé"),
    ("generer_canevas_valax_developpe_pdf.py", "Régénération du PDF développé"),
    ("Soutenance_DBA_MINANG_canevas_Valax_11_slides.pptx",
     "Déclinaison PowerPoint du canevas (11 slides 16:9)"),
    ("Soutenance_DBA_MINANG_15_slides.pptx",
     "Version 15 slides (contient dédicace et remerciements)"),
]


class PDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("DejaVu", "", 7.5)
        self.set_text_color(*MUTED)
        self.cell(0, 6, "S. P. MINANG — Thèse DBA · Canevas Valax — proposition IA — à valider par l'auteur",
                  align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*BRONZE)
        self.set_line_width(0.4)
        self.line(15, 16, 195, 16)
        self.ln(4)

    def footer(self):
        self.set_y(-14)
        self.set_font("DejaVu", "", 7.5)
        self.set_text_color(*MUTED)
        self.cell(0, 8, f"Page {self.page_no()}/{{nb}}", align="C")


pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_font("DejaVu", "", DEJA)
pdf.add_font("DejaVu", "B", DEJA_B)
pdf.add_font("SerifB", "B", DEJAS_B)
pdf.set_margins(15, 15, 15)
pdf.set_auto_page_break(True, margin=18)
pdf.add_page()

# ---- En-tête ----
pdf.set_font("DejaVu", "B", 8)
pdf.set_text_color(*BRONZE)
pdf.cell(0, 5, "PROPOSITION IA — À VALIDER PAR L'AUTEUR", new_x="LMARGIN", new_y="NEXT")
pdf.ln(1)
pdf.set_font("SerifB", "B", 20)
pdf.set_text_color(*INKD)
pdf.cell(0, 10, "Canevas synthétique de soutenance", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("DejaVu", "", 11)
pdf.set_text_color(*MUTED)
pdf.multi_cell(0, 6, "Consignes du Professeur Valax — dix rubriques, onze slides (≈ 24 minutes)",
               new_x="LMARGIN", new_y="NEXT")
pdf.set_font("DejaVu", "", 8.5)
pdf.multi_cell(0, 5,
               "Serge Patrick MINANG — Thèse de Doctorate of Business Administration (DBA) · "
               "« La gouvernance augmentée des établissements privés d'enseignement supérieur "
               "au Gabon en situation de polycrise »", new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
pdf.set_draw_color(*BRONZE)
pdf.set_line_width(0.8)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(3)
pdf.set_font("DejaVu", "", 7.8)
pdf.set_text_color(*MUTED)
pdf.multi_cell(0, 4.6,
               "Sources du contenu : document de thèse fourni par l'auteur (20/09/2026) et dépôt "
               "These-Presidence. Aucun résultat de terrain inventé : les rubriques 6 et 7 sont "
               "préparatoires (chapitres 5–6) ; terrain codé EPES-A à EPES-E ; date de "
               "soutenance : 15 décembre 2026 (fournie par l'auteur).", new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)


def h1(pdf, text):
    pdf.ln(2)
    pdf.set_font("SerifB", "B", 13)
    pdf.set_text_color(*BRONZE_D)
    pdf.cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(*LINE)
    pdf.set_line_width(0.3)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(2.5)


def h2(pdf, text):
    pdf.ln(1.5)
    pdf.set_font("DejaVu", "B", 10)
    pdf.set_text_color(*INKD)
    pdf.multi_cell(0, 5.5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.8)


def bullets(pdf, items, size=9):
    pdf.set_font("DejaVu", "", size)
    pdf.set_text_color(*INK)
    for it in items:
        y0 = pdf.get_y()
        pdf.set_xy(19, y0)
        pdf.set_text_color(*BRONZE)
        pdf.cell(4, 5, "–")
        pdf.set_xy(23, y0)
        pdf.set_text_color(*INK)
        pdf.multi_cell(172 - 8, 5, it, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(0.8)


# ---- Vue d'ensemble ----
h1(pdf, "Vue d'ensemble — 10 rubriques, 11 slides")
from fpdf.fonts import FontFace

pdf.set_font("DejaVu", "", 7.6)
with pdf.table(
        col_widths=(32, 8, 42, 82, 26),
        text_align=("LEFT", "CENTER", "LEFT", "LEFT", "LEFT"),
        line_height=4.1,
        padding=1.4,
        headings_style=FontFace(emphasis="BOLD", color=WHITE,
                                fill_color=BRONZE_D),
) as table:
    hr_ = table.row()
    for htxt in ["Rubrique (Valax)", "Sl.", "Titre proposé", "Message clé",
                 "Durée · statut"]:
        hr_.cell(htxt)
    for row in ROWS:
        r = table.row()
        r.cell(str(row[0]))
        r.cell(str(row[1]))
        r.cell(str(row[2]))
        r.cell(str(row[3]))
        r.cell(str(row[4]))
pdf.ln(2)
pdf.set_font("DejaVu", "", 7.8)
pdf.set_text_color(*MUTED)
pdf.multi_cell(0, 4.6,
               "Durées indicatives : à ajuster au format imposé par l'école doctorale "
               "(compressible à ≈ 15 minutes en traitant ensemble les slides 3–4).",
               new_x="LMARGIN", new_y="NEXT")

# ---- Détail ----
h1(pdf, "Détail slide par slide")
for title, items in DETAILS:
    h2(pdf, title)
    bullets(pdf, items)

# ---- Vigilances ----
h1(pdf, "Points de vigilance (cohérence avec le dépôt)")
bullets(pdf, VIGILANCES)

# ---- Fichiers ----
h1(pdf, "Fichiers du dossier presentation/")
pdf.set_font("DejaVu", "B", 7.8)
pdf.set_fill_color(*BRONZE_D)
pdf.set_text_color(*WHITE)
pdf.cell(80, 6, " Fichier", fill=True, border=1)
pdf.cell(105, 6, " Rôle", fill=True, border=1, new_x="LMARGIN", new_y="NEXT")
pdf.set_font("DejaVu", "", 7.8)
for f, role in FILES:
    if pdf.get_y() > 272:
        pdf.add_page()
    pdf.set_text_color(*BRONZE_D)
    pdf.cell(80, 6, " " + f, border=1)
    pdf.set_text_color(*INK)
    pdf.cell(105, 6, " " + role, border=1, new_x="LMARGIN", new_y="NEXT")

pdf.ln(4)
pdf.set_font("DejaVu", "", 7.8)
pdf.set_text_color(*MUTED)
pdf.multi_cell(0, 4.6,
               "Proposition IA — à valider par l'auteur. Ce document ne contient aucune donnée "
               "de terrain : les rubriques « Résultats » et « Analyse » seront complétées après "
               "la collecte, à partir du corpus réel.", new_x="LMARGIN", new_y="NEXT")

pdf.set_title("Canevas de soutenance — consignes Valax (10 rubriques)")
pdf.set_author("Serge Patrick MINANG")
pdf.set_subject("Thèse DBA — gouvernance augmentée des EPES gabonais")
OUT = "presentation/CANEVAS_VALAX.pdf"
pdf.output(OUT)
print("OK —", OUT, "—", pdf.page_no(), "pages")
