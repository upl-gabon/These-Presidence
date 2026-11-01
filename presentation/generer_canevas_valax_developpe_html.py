# -*- coding: utf-8 -*-
"""Version HTML lisible du canevas Valax DÉVELOPPÉ — Thèse DBA S. P. MINANG.

Convertit presentation/CANEVAS_VALAX_DEVELOPPE.md en page HTML autonome
(charte encre/bronze/papier du dépôt — jamais de bleu/gold UPL).
Le MD reste la source ; régénérer après toute modification :
    python3 presentation/generer_canevas_valax_developpe_html.py

Sortie : presentation/CANEVAS_VALAX_DEVELOPPE.html
Statut : proposition IA — à valider par l'auteur.
"""

import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "presentation" / "CANEVAS_VALAX_DEVELOPPE.md"
OUT = ROOT / "presentation" / "CANEVAS_VALAX_DEVELOPPE.html"

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Canevas Valax DÉVELOPPÉ — script oral par slide (soutenance DBA)</title>
<style>
  :root{
    --paper:#FAF8F2; --card:#FFFFFF; --ink:#232B33; --inkd:#141B22;
    --bronze:#8A6414; --bronzeD:#6E4F0E; --bronzeS:#F1E8D0;
    --line:#E3DAC6; --muted:#5E6A76;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--paper);color:var(--ink);
    font:16px/1.6 "Segoe UI",system-ui,-apple-system,sans-serif}
  .wrap{max-width:980px;margin:0 auto;padding:2rem 1.25rem 4rem}
  .top{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;
    color:var(--bronze);font-weight:700}
  h1{font-family:Georgia,serif;color:var(--inkd);font-size:1.9rem;margin:.3rem 0 .2rem}
  .sub{font-family:Georgia,serif;font-style:italic;color:var(--muted);margin:0 0 .4rem}
  hr{border:0;border-top:2px solid var(--bronze);margin:.6rem 0 1.2rem}
  h2{font-family:Georgia,serif;color:var(--bronzeD);font-size:1.3rem;
    margin:2.2rem 0 .5rem;border-bottom:1px solid var(--line);padding-bottom:.25rem}
  h3{font-family:Georgia,serif;color:var(--inkd);font-size:1.05rem;margin:1.6rem 0 .4rem}
  table{width:100%;border-collapse:collapse;background:var(--card);
    border:1px solid var(--line);font-size:.85rem;margin:.6rem 0 1rem}
  th{background:var(--bronzeD);color:#fff;text-align:left;padding:.45rem .55rem;
    font-size:.72rem;text-transform:uppercase;letter-spacing:.04em}
  td{border:1px solid var(--line);padding:.42rem .55rem;vertical-align:top}
  ul,ol{margin:.3rem 0 .8rem;padding-left:1.4rem}
  li{margin:.28rem 0}
  li b,td b,p b{color:var(--bronzeD)}
  p{margin:.45rem 0}
  blockquote{margin:.6rem 0 1rem;padding:.75rem 1.05rem;background:var(--card);
    border:1px solid var(--line);border-left:4px solid var(--bronze);
    border-radius:0 8px 8px 0;font-size:1.02rem}
  blockquote p{margin:.35rem 0}
  code{background:var(--bronzeS);border:1px solid var(--line);border-radius:4px;
    padding:.05rem .3rem;font-size:.85em;color:var(--inkd)}
  .foot{margin-top:2.4rem;font-size:.78rem;color:var(--muted);font-style:italic;
    border-top:1px solid var(--line);padding-top:.8rem}
</style>
</head>
<body>
<div class="wrap">
  <div class="top">Proposition IA — à valider par l'auteur</div>
__BODY__
  <p class="foot">Document généré depuis CANEVAS_VALAX_DEVELOPPE.md — une version condensée
  du script figure dans le volet de notes du PowerPoint
  « Soutenance_DBA_MINANG_canevas_Valax_11_slides.pptx ».
  Garde-fous : chapitres 5–6 préparatoires ; codes EPES-A à EPES-E ; date de
  soutenance : 15 décembre 2026 (fournie par l'auteur) ; aucun résultat de terrain inventé.</p>
</div>
</body>
</html>
"""


def build_body(md_text: str) -> str:
    body = markdown.markdown(
        md_text,
        extensions=["tables", "sane_lists"],
        output_format="html5",
    )
    # Le titre H1 du MD devient l'en-tête de la page : on le retire du corps.
    body = re.sub(r"<h1>.*?</h1>\s*", "", body, count=1)
    return body


def main() -> None:
    md_text = SRC.read_text(encoding="utf-8")
    # Sous-titre = première ligne « > » de bloc du MD (statut), déjà dans le bandeau.
    body = build_body(md_text)
    page = TEMPLATE.replace("__BODY__", body)
    OUT.write_text(page, encoding="utf-8")
    print("OK —", OUT.relative_to(ROOT),
          "(", len(page), "caractères )")


if __name__ == "__main__":
    main()
