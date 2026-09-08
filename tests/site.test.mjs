/**
 * Tests du dépôt autonome THÈSE (site personnel de recherche)
 * Exécution : npm test
 */
import { readFileSync, existsSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import assert from "assert";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, "..");

function read(rel) {
  return readFileSync(join(ROOT, rel), "utf8");
}

const PAGES = ["index.html", "plan.html", "supports.html", "documents.html"];

let failed = 0;
function test(title, fn) {
  try {
    fn();
    console.log("  ✓", title);
  } catch (e) {
    failed++;
    console.error("  ✗", title);
    console.error("   ", e.message);
  }
}

console.log("\nTHÈSE (dépôt autonome) — tests\n");

test("pages, styles, script et docs existent", () => {
  for (const f of [
    ...PAGES,
    "style.css",
    "app.js",
    "README.md",
    "REPRISE.md",
    "docs/JURY_SIMULE.md",
    "docs/GARDE_FOUS_IA.md",
    "docs/ARCHIVES.md",
    "docs/FICHE_CONCEPT_GA.md",
    "docs/DEPOT_AUTEUR/README.md",
    "docs/DEPOT_AUTEUR/Soutenance_DBA_MINANG_version_revisee_Phoenix.pdf",
    "package.json",
    "robots.txt",
  ]) {
    assert.ok(existsSync(join(ROOT, f)), `manque ${f}`);
  }
});

test("noindex sur toutes les pages (zone discrète)", () => {
  for (const f of PAGES) {
    assert.ok(read(f).includes("noindex"), `${f} sans noindex`);
  }
  assert.ok(read("robots.txt").includes("Disallow"), "robots.txt sans Disallow");
});

test("autonomie — aucune dépendance locale externe", () => {
  const banned = [
    "../",
    "assets/",
    "config.js",
    "include.js",
    "main.js",
    "effects.js",
    "logo-upl",
    "window.UPL",
    "UPL.config",
  ];
  for (const f of [...PAGES, "app.js", "style.css"]) {
    const content = read(f);
    for (const b of banned) {
      assert.ok(!content.includes(b), `"${b}" trouvé dans ${f}`);
    }
  }
});

test("charte propre — ni bleu ni or UPL", () => {
  for (const f of [...PAGES, "style.css"]) {
    const content = read(f).toLowerCase();
    assert.ok(!content.includes("#0b2a5b"), `bleu UPL trouvé dans ${f}`);
    assert.ok(!content.includes("#c9a227"), `or UPL trouvé dans ${f}`);
  }
});

test("ponts autorisés uniquement (pas de mail inventé, pas de lien sauvage)", () => {
  const allowedHosts = ["https://upl-gabon.com/", "https://upl-gabon.com/contact.html"];
  for (const f of PAGES) {
    const html = read(f);
    for (const m of html.matchAll(/mailto:([^"?\s>]+)/g)) {
      assert.equal(m[1], "contact@upl-gabon.com", `mailto non autorisé dans ${f} : ${m[1]}`);
    }
    for (const m of html.matchAll(/href="(https:\/\/upl-gabon\.com[^"]*)"/g)) {
      assert.ok(allowedHosts.includes(m[1]), `lien sortant non autorisé dans ${f} : ${m[1]}`);
    }
  }
});

test("confidentialité — codes EPES-A..E, jamais de noms pressentis ni Matrix", () => {
  const banned = [
    "Saint-Exupéry",
    "Saint-Exupery",
    "BGFI",
    "SUP de COM",
    "EM Gabon",
    "Techniques Avancées",
    "Matrix",
  ];
  for (const f of PAGES) {
    const html = read(f);
    for (const b of banned) {
      assert.ok(!html.includes(b), `"${b}" trouvé dans ${f} (régime de confidentialité)`);
    }
  }
  assert.ok(read("plan.html").includes("EPES-A"), "codes EPES-A..E manquants");
});

test("contenu — question centrale, QR, P, méthode, supports", () => {
  const index = read("index.html");
  assert.ok(index.includes("sous quelles conditions l'articulation"), "question centrale manquante");
  for (const q of ["QR1", "QR2", "QR3", "QR4"]) {
    assert.ok(index.includes(q), `${q} manquant`);
  }
  for (let i = 1; i <= 7; i++) {
    assert.ok(new RegExp(`\\bP${i}\\b`).test(index), `P${i} manquant`);
  }
  const plan = read("plan.html");
  for (const marker of ["NVivo", "45 participants", "EPES-A", "Annexes", "Chapitre 6"]) {
    assert.ok(plan.includes(marker), `marqueur manquant (plan) : ${marker}`);
  }
  const supports = read("supports.html");
  for (const marker of ["27 tableaux", "13 figures", "Figure 3.1", "Tableau 6.4", "Source : auteur"]) {
    assert.ok(supports.includes(marker), `marqueur manquant (supports) : ${marker}`);
  }
});

test("bandeau d'échanges indépendant (marqueur + rendu propre)", () => {
  for (const f of PAGES) {
    assert.ok(read(f).includes("data-action-band"), `bandeau manquant dans ${f}`);
  }
  const app = read("app.js");
  assert.ok(app.includes("data-action-band"), "app.js ne rend pas le bandeau");
  assert.ok(app.includes("Recherche doctorale"), "objet « Recherche doctorale » manquant");
});

test("jury + reprise branchés", () => {
  const jury = read("docs/JURY_SIMULE.md");
  for (const name of ["Chabanne-Rive", "Valax", "Loufrani"]) {
    assert.ok(jury.includes(name), `${name} manquant dans le jury`);
  }
  assert.ok(read("REPRISE.md").includes("Protocole obligatoire"), "protocole de reprise manquant");
});

test("jury accompagnant — question/conseil à chaque conversation", () => {
  const jury = read("docs/JURY_SIMULE.md");
  for (const marker of [
    "comité d'accompagnement",
    "une question ou un conseil",
    "Journal des échanges",
    "Les trois voix",
    "Serge",
    "Monsieur MINANG",
  ]) {
    assert.ok(jury.includes(marker), `"${marker}" manquant dans JURY_SIMULE.md`);
  }
  const reprise = read("REPRISE.md");
  assert.ok(reprise.includes("une question ou un conseil"), "temps jury absent du protocole");
  assert.ok(reprise.includes("arrête jamais net"), "clôture de conversation absente du protocole");
  assert.ok(read("README.md").includes("comité d'accompagnement"), "posture du jury absente du README");
  assert.ok(read("README.md").includes("terrain n'est pas encore réalisé"), "état empirique absent du README");
  assert.ok(jury.includes("fond scientifique avant la forme"), "priorité au fond absente du jury");
});

test("archives — mémoire systématique des conversations", () => {
  const archives = read("docs/ARCHIVES.md");
  assert.ok(archives.includes("Conversation n° 1"), "conversation n° 1 non archivée");
  assert.ok(archives.includes("sans solliciter"), "règle d'autonomie absente des archives");
  assert.ok(archives.includes("Journal des échanges"), "lien jury/archives manquant");
  const reprise = read("REPRISE.md");
  assert.ok(reprise.includes("docs/ARCHIVES.md"), "REPRISE ne pointe pas vers les archives");
  assert.ok(reprise.includes("Autonomie décisionnelle"), "autonomie décisionnelle absente du protocole");
});

test("garde-fous anti-hallucination IA (D9)", () => {
  const gf = read("docs/GARDE_FOUS_IA.md");
  for (const marker of [
    "anti-hallucination",
    "jamais générées",
    "proposition IA",
    "trou reste un trou",
    "Checklist",
  ]) {
    assert.ok(gf.includes(marker), `"${marker}" manquant dans GARDE_FOUS_IA.md`);
  }
  const reprise = read("REPRISE.md");
  assert.ok(reprise.includes("GARDE_FOUS_IA"), "REPRISE ne référence pas les garde-fous");
  assert.ok(reprise.includes("D9"), "décision D9 absente de REPRISE");
  assert.ok(read("README.md").includes("docs/GARDE_FOUS_IA.md"), "README ignore les garde-fous");
});

console.log("");
if (failed) {
  console.error(`FAILED: ${failed} test(s)\n`);
  process.exit(1);
}
console.log("All tests passed.\n");
