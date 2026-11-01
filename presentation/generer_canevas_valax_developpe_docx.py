# -*- coding: utf-8 -*-
"""Version WORD du canevas Valax DÉVELOPPÉ — Thèse DBA S. P. MINANG.

Convertit presentation/CANEVAS_VALAX_DEVELOPPE.md (source unique) en document
Word annotable : titres, tableaux, scripts oraux en retrait avec filet bronze.
Charte encre/bronze/papier du dépôt. Régénération :
    python3 presentation/generer_canevas_valax_developpe_docx.py

Sortie : presentation/CANEVAS_VALAX_DEVELOPPE.docx
Statut : proposition IA — à valider par l'auteur. Date de soutenance :
15 décembre 2026 (fournie par l'auteur).
"""

import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "presentation" / "CANEVAS_VALAX_DEVELOPPE.md"
OUT = ROOT / "presentation" / "CANEVAS_VALAX_DEVELOPPE.docx"

INK = RGBColor(0x23, 0x2B, 0x33)
INKD = RGBColor(0x14, 0x1B, 0x22)
BRONZE = RGBColor(0x8A, 0x64, 0x14)
BRONZE_D = RGBColor(0x6E, 0x4F, 0x0E)
MUTED = RGBColor(0x5E, 0x6A, 0x76)
SERIF, SANS = "Georgia", "Segoe UI"

INLINE = re.compile(r"(\*\*.+?\*\*|`[^`]+`)")


def set_font(run, name=SANS, size=10.5, color=INK, bold=False, italic=False):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    rpr = run._r.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    rfonts.set(qn("w:ascii"), name)
    rfonts.set(qn("w:hAnsi"), name)
    return run


def add_runs(p, text, size=10.5, color=INK, base_bold=False, italic=False,
             font=SANS):
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            set_font(p.add_run(part[2:-2]), font, size, BRONZE_D,
                     bold=True, italic=italic)
        elif part.startswith("`") and part.endswith("`"):
            set_font(p.add_run(part[1:-1]), "Consolas", size - 1, INKD,
                     bold=base_bold, italic=italic)
        else:
            set_font(p.add_run(part), font, size, color,
                     bold=base_bold, italic=italic)


def left_bronze_border(p):
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), "18")
    left.set(qn("w:space"), "8")
    left.set(qn("w:color"), "8A6414")
    pbdr.append(left)
    pPr.append(pbdr)


def shade(cell, hexcolor):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), hexcolor)
    cell._tc.get_or_add_tcPr().append(shd)


def main():
    lines = SRC.read_text(encoding="utf-8").splitlines()
    doc = Document()
    for section in doc.sections:
        section.left_margin = section.right_margin = Cm(2.2)
        section.top_margin = section.bottom_margin = Cm(1.8)

    # En-tête du document
    p = doc.add_paragraph()
    set_font(p.add_run("PROPOSITION IA — À VALIDER PAR L'AUTEUR"), SANS, 9,
             BRONZE, bold=True)
    p = doc.add_paragraph()
    set_font(p.add_run("Canevas Valax DÉVELOPPÉ — script oral par slide"),
             SERIF, 19, INKD, bold=True)
    p = doc.add_paragraph()
    set_font(p.add_run("Serge Patrick MINANG — Thèse DBA · Soutenance du "
                       "15 décembre 2026 (date fournie par l'auteur)"),
             SANS, 10, MUTED, italic=True)
    p = doc.add_paragraph()
    set_font(p.add_run("Développé depuis CANEVAS_VALAX_DEVELOPPE.md (source "
                       "unique) : contenu à l'écran, script oral chronométré, "
                       "transition, sources, vigilance — par slide. Le "
                       "PowerPoint 11 slides porte une version condensée de "
                       "ce script dans ses notes. Garde-fous : chapitres 5–6 "
                       "préparatoires ; codes EPES-A à EPES-E ; aucun "
                       "résultat de terrain inventé."),
             SANS, 9, MUTED, italic=True)
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "12")
    bottom.set(qn("w:space"), "6")
    bottom.set(qn("w:color"), "8A6414")
    pbdr.append(bottom)
    pPr.append(pbdr)

    i, first_h1 = 0, True
    while i < len(lines):
        ln = lines[i]

        if ln.startswith("# ") and first_h1:      # titre principal → déjà en tête
            first_h1 = False
            i += 1
            continue
        if ln.startswith("## "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(16)
            p.paragraph_format.space_after = Pt(4)
            add_runs(p, ln[3:], size=13.5, color=BRONZE_D, base_bold=True,
                     font=SERIF)
            i += 1
            continue
        if ln.startswith("### "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(3)
            add_runs(p, ln[4:], size=11.5, color=INKD, base_bold=True,
                     font=SERIF)
            i += 1
            continue
        if ln.startswith(">"):                    # bloc script / note
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.6)
            p.paragraph_format.space_after = Pt(4)
            left_bronze_border(p)
            add_runs(p, ln.lstrip("> ").strip(), size=10.5, color=INK,
                     italic=True)
            i += 1
            continue
        if ln.startswith("|"):                    # tableau
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            table = doc.add_table(rows=len(rows), cols=len(rows[0]))
            table.style = "Table Grid"
            for r, row in enumerate(rows):
                for c, txt in enumerate(row):
                    cell = table.cell(r, c)
                    cell.text = ""
                    cp = cell.paragraphs[0]
                    add_runs(cp, txt, size=9,
                             color=INKD if r else BRONZE_D,
                             base_bold=(r == 0))
                    if r == 0:
                        shade(cell, "F1E8D0")
            doc.add_paragraph()
            continue
        if re.match(r"^\s*- ", ln):               # puce
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            p.paragraph_format.space_after = Pt(2)
            set_font(p.add_run("—  "), SANS, 10.5, BRONZE, bold=True)
            add_runs(p, re.sub(r"^\s*- ", "", ln))
            i += 1
            continue
        if re.match(r"^\s*\d+\. ", ln):           # liste numérotée (texte gardé)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            p.paragraph_format.space_after = Pt(2)
            add_runs(p, ln.strip())
            i += 1
            continue
        if ln.strip() in ("", "---"):
            i += 1
            continue
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        add_runs(p, ln)
        i += 1

    # Pied de page
    foot = doc.sections[0].footer.paragraphs[0]
    foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_font(foot.add_run("S. P. MINANG — Thèse DBA · canevas Valax développé · "
                          "soutenance du 15 décembre 2026 — proposition IA"),
             SANS, 8, MUTED, italic=True)

    cp = doc.core_properties
    cp.title = "Canevas Valax développé — script oral par slide (soutenance DBA)"
    cp.author = "Serge Patrick MINANG"
    cp.subject = ("Thèse DBA — gouvernance augmentée des EPES gabonais — "
                  "script oral du canevas Valax (10 rubriques, 11 slides)")
    cp.comments = ("Proposition IA — à valider par l'auteur. Soutenance du "
                   "15 décembre 2026 (date fournie par l'auteur). Slides 7-8 "
                   "préparatoires ; rien d'inventé.")

    doc.save(OUT)
    print("OK —", OUT.relative_to(ROOT), "—",
          len(doc.paragraphs), "paragraphes,", len(doc.tables), "tableaux")


if __name__ == "__main__":
    main()
