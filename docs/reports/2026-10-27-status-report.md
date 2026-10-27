# OurMocks — CUET UG status report (27 Oct 2026)

## 1. Local folder vs GitHub — balanced

- Local `main` and `origin/main` (github.com/Avenger2007/Mock-Questions) are identical as of this report.
- GitHub now has all **15 subjects (375 papers, 18,750 questions)**. Chemistry, Hindi and Sanskrit were previously local-only.
- `audit_report.md` (Avenger2007's 8 Oct audit) is now in the local folder as well.
- **Mathematics:** the 8 Oct "comprehensive remediation" (commit `7b9f71f`) was **not kept**. It added 615 corrupted `\1` strings (determinants rendered as `\left| \1 \right|`), wrapped 140 whole sentences in math mode, created 17 duplicate questions and skewed the key to 31% A. The earlier Math papers were restored. That commit's goals (empty sub-topics, short questions, templating) move into the audit below. Its auto-filled sub-topics were not reused because many were wrong (for example "Integrals" filed under Continuity and Differentiability).
- Still local-only on purpose (excluded by `.gitignore`): `scratch/` authoring scripts (191 files), stray `gen_*/generate_*` scripts in Accountancy, Physics and General Test, and General Test intermediate JSON files.

## 2. OurMocks rename

- Changed `MockStride` → `OurMocks` in `docs/question-bank.schema.json` (`$id` is now `urn:ourmocks:question-bank:1.0`), `docs/README.md`, `README.md`, `Worklog.md` and both instruction files.
- The application code is **not in this repo**. Per the decision on 27 Oct, this round covers content only. If the admin import checks the schema `$id`, update it to the new URN.

### What the app's question renderer must support (from scanning all 18,750 questions)

| Feature | Where it appears | Needed for a human-readable display |
|---|---|---|
| Line breaks `\n` | English (948 questions), Hindi (692), General Test, History, CS, Economics | Keep line breaks (CSS `white-space: pre-line`). Otherwise passages, statement lists and match-the-column tables collapse into one paragraph. |
| KaTeX `\( … \)` | Chemistry (802), Economics (40), a few elsewhere | Render KaTeX. |
| mhchem `\ce{…}` | Chemistry (543) | Load the KaTeX **mhchem** extension. Otherwise formulas show as raw code. |
| Unicode math (∫ √ ² π) | Mathematics (399), Physics (264), General Test (31) | Displays as plain text. **The rulebook requires KaTeX**, so this is an audit item: fractions, matrices and determinants are hard to read in plain text. |
| `A) ` prefix inside every option | All subjects | The app must **not** add its own A/B/C/D letters, or it must strip the prefix. Otherwise students see "A. A) …". |
| `image_reference: null` | Economics (100) | Harmless. No question actually depends on an image. |

## 3. New difficulty standard and its impact

Decision (27 Oct): **15% easy / 65% medium / 20% hard in every paper = 8 / 32 / 10.** Levels still rise from 1 to 10, but through the depth of the questions inside each tier, not through the tier mix.

Current state: every paper still follows the old ramp. Level 1 = 35/12/3 (70% easy, not 95%). Level 10 = 3/15/32 (64% hard). The validator now checks the new target and flags all 375 papers.

Questions that must be **rewritten** (not relabelled; rulebook rule 7) to reach 8/32/10:

| Subject | Rewrites | Subject | Rewrites | Subject | Rewrites |
|---|---|---|---|---|---|
| Accountancy | 398 | English | 387 | Mass Media | 379 |
| Biological Science | 398 | General Test | 398 | Mathematics | 386 |
| Chemistry | 373 | Geography | 381 | Physics | 396 |
| Computer Science | 398 | Hindi | 396 | Political Science | 379 |
| Economics | 385 | History | 381 | Sanskrit | 376 |
| **Total** | **5,811 of 18,750 (31%)** | | | | |

Low levels need easy questions replaced with medium ones, and high levels need hard questions replaced with medium ones. Mid levels (4–6) change least.

## 4. Syllabus readiness

| Subject | 2026 NTA syllabus PDF present | PYQs present |
|---|---|---|
| Accountancy, Biological Science, Chemistry, Computer Science, Economics, Geography, History, Mass Media, Physics, Political Science, Sanskrit | ✅ (text extracted; all say "For the Year 2026") | ❌ |
| **English, General Test, Hindi, Mathematics** | ❌ **missing** | ❌ |

- **No PYQ files exist anywhere in the repo.** Even so, 10 subjects' paper metadata (`past_paper_reference`) cites PYQs such as `pastpaper-english-2024.pdf` or "CUET UG Chemistry Past Papers (2022-2025)". 4 subjects' `syllabus_source` names a file that does not exist. These provenance fields must be corrected during the audit.
- The language syllabi (Bengali, Kannada, Malayalam, Tamil, Telugu) are the shared, roughly 70-word language-section syllabus.

## 5. Audit plan (next)

For each subject, in order:

1. Read the 2026 syllabus PDF and that subject's PYQs. Note the unit weightage, question formats (assertion-reason, match-the-list, case-based, statement combinations) and what real CUET easy, medium and hard questions look like.
2. Re-grade each question's difficulty against that PYQ benchmark and check it against the syllabus (out-of-syllabus, wrong answer, weak distractors, templating).
3. Fix the items `audit_report.md` raised (FAIL: Accountancy, Computer Science, English, Mathematics, Physics).
4. Rewrite questions to reach 8/32/10 per paper with level-appropriate depth.
5. Run `validate_papers.py` and correct the provenance metadata.

PYQs will be stored as `PYQ/<Subject>/<year>_<source>.pdf` with `PYQ/<Subject>/SOURCES.md` (URL, year, official/unofficial). The rulebook's rule 9 was updated to allow NTA plus coaching-site PYQs as reference only.
