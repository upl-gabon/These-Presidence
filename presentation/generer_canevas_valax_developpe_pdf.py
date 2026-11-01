# -*- coding: utf-8 -*-
"""Version PDF du canevas Valax DÉVELOPPÉ — Thèse DBA S. P. MINANG.

Convertit presentation/CANEVAS_VALAX_DEVELOPPE.md (source unique) en PDF A4
partageable/imprimable (fpdf2 + DejaVu). Tableau via l'API native pdf.table().
Charte encre/bronze/papier du dépôt. Régénération :
    python3 presentation/generer_canevas_valax_developpe_pdf.py

Sortie : presentation/CANEVAS_VALAX_DEVELOPPE.pdf
Statut : proposition IA — à valider par l'auteur. Date de soutenance :
15 décembre 2026 (fournie par l'auteur).
"""

import re
from pathlib import Path

from fpdf import FPDF
from fpdf.fonts import FontFace

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "presentation" / "CANEVAS_VALAX_DEVELOPPE.md"
OUT = ROOT / "presentation" / "CANEVAS_VALAX_DEVELOPPE.pdf"

PAPER = (250, 248, 242)
INK = (35, 43, 51)
INKD = (20, 27, 34)
BRONZE = (138, 100, 20)
BRONZE_D = (110, 79, 14)
BRONZE_S = (241, 232, 208)
MUTED = (94, 106, 118)
LINE = (227, 218, 198)

FD = "/usr/share/fonts/truetype/dejavu/"
INLINE = re.compile(r"\*\*(.+?)\*\*|`([^`]+)`")


def plain(text):
    """Markdown inline → texte brut (le PDF garde la mise en forme structurelle)."""
    return INLINE.sub(lambda m: m.group(1) or m.group(2), text)


class PDF(FPDF):
    def footer(self):
        self.set_y(-14)
        self.set_draw_color(*LINE)
        self.set_line_width(0.3)
        self.line(15, self.get_y(), 195, self.get_y())
        self.set_font("DejaVu", "", 7.2)
        self.set_text_color(*MUTED)
        self.cell(0, 4.5,
                  "S. P. MINANG — Thèse DBA · canevas Valax développé · "
                  "soutenance du 15 décembre 2026 — proposition IA",
                  align="L")
        self.cell(0, 4.5, "%d / {nb}" % self.page_no(), align="R")


def h2(pdf, text):
    pdf.ln(2)
    pdf.set_font("DejaVu", "B", 12.5)
    pdf.set_text_color(*BRONZE_D)
    pdf.multi_cell(0, 6, plain(text), new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(*LINE)
    pdf.set_line_width(0.3)
    pdf.line(15, pdf.get_y() + 0.5, 195, pdf.get_y() + 0.5)
    pdf.ln(2.5)


def h3(pdf, text):
    pdf.ln(1.5)
    pdf.set_font("DejaVu", "B", 10.5)
    pdf.set_text_color(*INKD)
    pdf.multi_cell(0, 5.2, plain(text), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.8)


def body(pdf, text, size=9.2, color=INK, style="", italic=False, indent=0):
    pdf.set_x(15 + indent)
    pdf.set_font("DejaVu", style, size)
    pdf.set_text_color(*color)
    pdf.multi_cell(180 - indent, 4.7, plain(text), new_x="LMARGIN",
                   new_y="NEXT")
    pdf.ln(0.6)


def script(pdf, text):
    """Bloc « > » : script oral — retrait, italique, filet bronze à gauche."""
    y0 = pdf.get_y()
    pdf.set_x(21)
    pdf.set_font("DejaVu", "I", 9.2)
    pdf.set_text_color(*INK)
    pdf.multi_cell(174, 4.7, plain(text), new_x="LMARGIN", new_y="NEXT")
    y1 = pdf.get_y()
    pdf.set_fill_color(*BRONZE)
    pdf.rect(15.5, y0, 1.1, max(y1 - y0 - 1.2, 2), "F")
    pdf.ln(1.2)


def bullet(pdf, text):
    pdf.set_font("DejaVu", "", 9.2)
    pdf.set_text_color(*BRONZE)
    pdf.set_x(19)
    pdf.cell(5, 4.7, "—")
    pdf.set_text_color(*INK)
    pdf.multi_cell(171, 4.7, plain(text), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.4)


def table(pdf, rows):
    pdf.set_font("DejaVu", "", 7.8)
    pdf.set_text_color(*INK)
    head = FontFace(family="DejaVu", emphasis="BOLD", size_pt=7.8,
                    color=BRONZE_D, fill_color=BRONZE_S)
    with pdf.table(col_widths=(34, 12, 42, 66, 26), text_align="LEFT",
                   headings_style=head, line_height=4.6,
                   borders_layout="ALL") as t:
        for r, row in enumerate(rows):
            tr = t.row()
            for cell in row:
                tr.cell(plain(cell))
    pdf.ln(3)


def main():
    lines = SRC.read_text(encoding="utf-8").splitlines()

    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=16)
    pdf.set_margins(15, 14, 15)
    pdf.add_font("DejaVu", "", FD + "DejaVuSans.ttf")
    pdf.add_font("DejaVu", "B", FD + "DejaVuSans-Bold.ttf")
    for style, base in (("I", "DejaVuSans.ttf"), ("BI", "DejaVuSans-Bold.ttf")):
        oblique = base.replace(".ttf", "Oblique.ttf").replace(
            "SansBold", "Sans-Bold")
        try:
            pdf.add_font("DejaVu", style, FD + oblique)
        except FileNotFoundError:
            pdf.add_font("DejaVu", style, FD + base)  # sandbox sans oblique
    pdf.add_page()
    pdf.set_fill_color(*PAPER)
    pdf.rect(0, 0, 210, 297, "F")

    pdf.set_font("DejaVu", "B", 8)
    pdf.set_text_color(*BRONZE)
    pdf.cell(0, 4.5, "PROPOSITION IA — À VALIDER PAR L'AUTEUR",
             new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    pdf.set_font("DejaVu", "B", 16)
    pdf.set_text_color(*INKD)
    pdf.multi_cell(0, 7.2, "Canevas Valax DÉVELOPPÉ — script oral par slide",
                   new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DejaVu", "I", 9)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(0, 4.8,
                   "Serge Patrick MINANG — Thèse DBA · Soutenance du "
                   "15 décembre 2026 (date fournie par l'auteur)",
                   new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1.5)
    pdf.set_draw_color(*BRONZE)
    pdf.set_line_width(0.6)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(3)
    pdf.set_font("DejaVu", "", 7.8)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(0, 4.4,
                   "Développé depuis CANEVAS_VALAX_DEVELOPPE.md (source unique) : "
                   "contenu à l'écran, script oral chronométré (≈ 140 mots/min), "
                   "transition, sources, vigilance — par slide. Le PowerPoint 11 "
                   "slides porte une version condensée de ce script dans ses notes. "
                   "Garde-fous : chapitres 5–6 préparatoires ; codes EPES-A à "
                   "EPES-E ; aucun résultat de terrain inventé.",
                   new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("# "):
            i += 1
            continue
        if ln.startswith("## "):
            h2(pdf, ln[3:])
        elif ln.startswith("### "):
            h3(pdf, ln[4:])
        elif ln.startswith(">"):
            script(pdf, ln.lstrip("> ").strip())
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            table(pdf, rows)
            continue
        elif re.match(r"^\s*- ", ln):
            bullet(pdf, re.sub(r"^\s*- ", "", ln))
        elif re.match(r"^\s*\d+\. ", ln):
            body(pdf, ln.strip(), indent=4)
        elif ln.strip() in ("", "---"):
            pdf.ln(0.8)
        else:
            body(pdf, ln)
        i += 1

    pdf.output(OUT)
    print("OK —", OUT.relative_to(ROOT), "—", pdf.page_no(), "pages")


if __name__ == "__main__":
    main()
