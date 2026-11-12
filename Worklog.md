# Engineering & SME Worklog: CUET (UG) 2026 Mock Test Suite

- **Lead Engineer / Subject Matter Expert:** Antigravity (AI Agentic Coding & Test Content Specialist)
- **Repository:** [`https://github.com/Avenger2007/Mock-Questions`](https://github.com/Avenger2007/Mock-Questions)
- **Local Directory:** `c:\Users\ksg\Documents\KPSC ESSAy\MOCKS\Mock-Questions`
- **Date & Time:** October 7, 2026
- **Status:** Complete Audit Passed | Fixes Deployed | Pushed to Remote `origin/main`

---

## 1. Project Overview & Objectives

The goal was to review, audit, ground, standardize, and verify the full mock test content for the **Common University Entrance Test — Undergraduate (CUET UG 2026)** based on official National Testing Agency (NTA) regulations, NCERT Class 12 syllabi, and generation instructions (`Questionsgenerationinstructions.md` / `Hermes cuet instructions.md`).

---

## 2. Initial Discovery & Repository Acquisition

1. **Local Filespace Analysis**:
   - Initial review of the root `MOCKS` directory identified `question-bank.schema.json` (OurMocks Block AST schema v1.0, formerly MockStride), `example-question-bank.json`, and generation instructions.
   - Identified the architectural difference between the rich block AST format (`question-bank.schema.json`) and the operational flat JSON format used for test papers.
2. **Git Repository Acquisition**:
   - Authenticated with GitHub via Personal Access Token and cloned `https://github.com/Avenger2007/Mock-Questions` into `Mock-Questions`.
   - Bypassed interactive Windows credential manager prompts by configuring non-interactive credential isolation (`-c credential.helper=""`).
   - Discovered that the repository contains 275 full-length mock papers (13,750 questions) across 11 subjects, the official NTA Information Bulletin, 15+ syllabus PDFs, and a Python validation suite (`validate_papers.py`).

---

## 3. Official CUET (UG) 2026 Regulatory Grounding

Extracted and verified the examination rules from the official **NTA CUET (UG) 2026 Information Bulletin** (Chapter 2, Examination Scheme, pp. 15–16; Appendix II, pp. 37–38):

- **Testing Mode:** Computer Based Test (CBT) only.
- **Total Questions per Paper:** Exactly **50 questions**, all compulsory.
- **Duration:** Exactly **60 minutes** per test paper.
- **Marking Scheme:** **+5 marks** for correct answers, **-1 mark** for incorrect answers, **0 marks** for unattempted questions.
- **Pattern:** Objective Multiple Choice Questions (MCQs) with exactly 4 options (`A`, `B`, `C`, `D`).
- **Subject Scope:** Total of **37 subjects** (13 Languages + 23 Domain Subjects + 1 General Aptitude Test).

---

## 4. Comprehensive Audit Across All 15 Subjects (18,750 Questions)

Conducted an automated and manual Subject Matter Expert (SME) audit across all 15 existing subjects:

| Subject | Code | Papers | Total Questions | Key Distribution (A / B / C / D) | Duplicates | Passage Completeness | Audit Result |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Accountancy** | 301 | 25 | 1,250 | 24.7% / 25.0% / 25.0% / 25.3% | 0 | 100% Inline | **Passed (Fixed)** |
| **Biological Science** | 304 | 25 | 1,250 | 25.0% / 25.0% / 25.0% / 25.0% | 0 | 100% Inline | **Passed** |
| **Chemistry** | 306 | 25 | 1,250 | 25.0% / 25.0% / 25.0% / 25.0% | 0 | 100% Inline | **Passed** |
| **Computer Science** | 308 | 25 | 1,250 | 25.0% / 25.0% / 25.0% / 25.0% | 0 | 100% Inline | **Passed** |
| **Economics** | 309 | 25 | 1,250 | 25.0% / 25.0% / 25.0% / 25.0% | 0 | 100% Inline | **Passed** |
| **English** | 101 | 25 | 1,250 | 26.5% / 24.0% / 25.0% / 24.6% | 0 | 100% Inline | **Passed** |
| **General Test** | 501 | 25 | 1,250 | 25.1% / 24.9% / 25.2% / 24.8% | 0 | 100% Inline | **Passed** |
| **Geography / Geology** | 313 | 25 | 1,250 | 25.0% / 25.0% / 25.0% / 25.0% | 0 | 100% Inline | **Passed** |
| **Hindi** | 102 | 25 | 1,250 | 25.0% / 25.0% / 25.0% / 25.0% | 0 | 100% Inline | **Passed** |
| **History** | 314 | 25 | 1,250 | 25.0% / 25.0% / 25.0% / 25.0% | 0 | 100% Inline | **Passed** |
| **Mass Media** | 318 | 25 | 1,250 | 25.0% / 25.0% / 25.0% / 25.0% | 0 | 100% Inline | **Passed** |
| **Mathematics** | 319 | 25 | 1,250 | 25.1% / 25.7% / 24.4% / 24.8% | 0 | 100% Inline | **Passed (Fixed)** |
| **Physics** | 322 | 25 | 1,250 | 25.0% / 25.1% / 24.6% / 25.2% | 0 | 100% Inline | **Passed** |
| **Political Science** | 323 | 25 | 1,250 | 25.0% / 25.0% / 25.0% / 25.0% | 0 | 100% Inline | **Passed** |
| **Sanskrit** | 325 | 25 | 1,250 | 25.0% / 25.0% / 25.0% / 25.0% | 0 | 100% Inline | **Passed** |
| **TOTAL** | — | **375** | **18,750** | **Balanced (~25% each)** | **0** | **100% Inline** | **All Passed** |

---

## 5. Critical Issues Detected & Remediated

### Issue 1: Accountancy Option Alignment & Prefix Scrambling
- **Finding:** In 13 Accountancy questions across Papers 2, 3, 4, 5, 6, 7, 9, 13, 16, and 20, option string values had conflicting embedded prefixes (e.g. `options[0]` was `"C) Add values"` while `options[2]` was `"A) Find average"`).
- **Impact:** Frontend CBT renderers indexing by array position would display mismatched letters or evaluate student selections incorrectly against `correct_option`.
- **Resolution:** Sanitized and realigned all option arrays into strict canonical `A)`, `B)`, `C)`, `D)` order, ensuring that each `correct_option` precisely maps to the correct factual answer and matches the explanation.

### Issue 2: Mathematics ID Non-Standardization
- **Finding:** Mathematics papers used raw integer IDs (`1..50`) instead of the alphanumeric schema used across the rest of the repository, and stored a static `test_id` (`"CUET_MATH_2026"`) across all 25 files.
### Issue 3: Chemistry Authoring & Complete Suite Generation (Subject Code: 306)
- **Scope:** Authored the complete 25-paper mock test suite (1,250 MCQs) for CUET Chemistry based on the official NCERT Class 12 rationalized syllabus (10 core units): Solutions, Electrochemistry, Chemical Kinetics, d and f Block Elements, Coordination Compounds, Haloalkanes and Haloarenes, Alcohols, Phenols and Ethers, Aldehydes, Ketones and Carboxylic Acids, Amines, and Biomolecules.
- **Blueprint & Structure:**
  - Part A: Papers 1–10 (Levels 1–10) featuring progressive difficulty escalation.
  - Part B: Papers 11–20 (Levels 1B–10B) providing independent variant banks.
  - Part C: Papers 21–25 (Levels 2C, 4C, 6C, 8C, 10C) university entrance mastery series.
  - Unit uniformity: Exactly 5 questions per unit per paper (50 questions total per paper).
- **Quality Assurance & Standards:**
  - Balanced key distribution across 1,250 questions: A=313 (25.0%), B=313 (25.0%), C=312 (25.0%), D=312 (25.0%).
  - Maximum answer key streak $\le 3$.
  - 0 within-paper duplicate stems; 0 cross-paper duplicate stems.
  - 0 self-referential or misplaced options.
  - KaTeX mathematical and chemical equation formatting with proper `\( \ce{...} \)` and backslash escaping.
  - Master index generated: [`CUET/Chemistry/series_index.json`](CUET/Chemistry/series_index.json).

---

## 6. Git Synchronization & Deployment

- Automated validation re-check: **0 errors**, **0 prefix discrepancies**, **0 broken answer keys** across all 15 subjects (375 papers, 18,750 questions).
- Staged and committed suites:
  - Accountancy & Mathematics fixes (`407c1ca`)
  - Mass Media full suite (`42c1552`)
  - Sanskrit & Hindi full suites
  - Chemistry full 25-paper suite (Code 306, 1,250 questions)
- Working tree status: **Validated**.

---

## 7. CUET (UG) 2026 Subject Status: Remaining Subjects

Per NTA Bulletin Appendix II, there are **37 total subjects**.
- **Completed:** 15 subjects (375 mock papers, 18,750 questions).
- **Remaining:** **22 subjects**.

### Detailed Breakdown of Remaining Subjects:

#### A. Domain-Specific Subjects (11 Remaining)
1. **305 Business Studies** *(Highest Priority — completes Commerce suite: Accountancy, Economics, Business Studies)*
2. **326 Sociology** *(High Priority — Humanities)*
3. **324 Psychology** *(High Priority — Humanities)*
4. **321 Physical Education (Yoga/Sports)**
5. **302 Agriculture**
6. **307 Environmental Science**
7. **315 Home Science**
8. **312 Fine Arts / Visual Arts / Commercial Arts**
9. **320 Performing Arts (Dance, Drama, Music)**
10. **303 Anthropology**
11. **316 Knowledge Tradition & Practices in India**

#### B. Languages (11 Remaining)
1. **112 Telugu** *(Syllabus PDF present in `Hermes folder`)*
2. **106 Kannada** *(Syllabus PDF present in `Hermes folder`)*
3. **111 Tamil** *(Syllabus PDF present in `Hermes folder`)*
4. **107 Malayalam** *(Syllabus PDF present in `Hermes folder`)*
5. **104 Bengali** *(Syllabus PDF present in `Hermes folder`)*
6. **103 Assamese**
7. **105 Gujarati**
8. **108 Marathi**
9. **109 Odia**
10. **110 Punjabi**
11. **113 Urdu**

---

## 8. Recommended Next Steps

1. **Target Business Studies (Code 305)** to complete the Core Commerce group (Accountancy, Economics, Business Studies).
2. **Target regional languages with ready syllabi in `Hermes folder`:**
   - Telugu (Code 112)
   - Kannada (Code 106)
   - Tamil (Code 111)
   - Malayalam (Code 107)
   - Bengali (Code 104)
3. **Target Sociology (Code 326) and Psychology (Code 324)** for Humanities.

---

## Accountancy (301) — revised to the CUET 2027 standard (completed 27 Oct 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `4e0c506` … `0cb2a50` on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | 25 old papers (levelled names, mostly direct recall) | **16 rewritten tests** (`CUET ACCOUNTANCY TEST 1–16.json`); old Tests 17–25 removed |
| Paper structure | 50 compulsory questions | NTA Unit V choice: 60 questions per file, attempt 50 = Section A (40) + B1 Analysis of Financial Statements (10) **or** B2 Computerised Accounting System (10) |
| Difficulty | mostly easy | **8 easy / 32 medium / 10 hard on both attempt paths** in every test |
| Formats | almost all direct | per test: one 5-question case set, 2 match-list, 4 statements, 2 assertion–reason, 1 sequence (most tests), numericals and concept questions; B1/B2 each with a match and a statements question |
| Explanations | 2–3 lines | structured: `Answer:` line, then Given / Step / Common mistake (numericals, every distractor explained) or Why / Why not the others / Key point |
| Order | unit-wise | random exam order (`shuffle_test.py`); case sets kept together |
| Answer keys | unbalanced, long runs | balanced A/B/C/D per path; no letter more than 3 times in a row |
| Syllabus | included out-of-syllabus items (e.g. insolvency of a partner) | every question mapped to the 2026 NTA syllabus; removed content replaced |

**Case-set themes (one per test):** 1 interest and appropriation; 2 admission; 3 retirement; 4 debentures; 5 dissolution; 6 P&L appropriation; 7 share issue; 8 death of a partner; 9 change in profit-sharing ratio; 10 admission with hidden goodwill and capital adjustment; 11 debentures for non-cash consideration and as collateral; 12 past adjustments; 13 retirement with loan in instalments; 14 dissolution with a partner's loan and an unrecorded asset; 15 under-subscription, calls in advance and arrears; 16 admission with premium in kind and proportionate capital.

**Verification:** `validate_papers.py` — 0 parse errors, 0 key/explanation mismatches, 0 runs > 3, 0 within- or cross-paper duplicate stems. Extra duplicate checks (stem similarity, number fingerprints, sub-topic overlap) found about 26 reworded or number-swapped repeats across Tests 11–16 and Test 11; all were replaced.

**Known limits:** some concepts naturally recur across 16 tests with different numbers and set-ups; the guarantee case, forfeiture with premium unpaid and company balance-sheet notes have questions but no dedicated case set.

### Tools added
- `audit_papers.py` (formats, explanation depth, templating, option give-aways); `shuffle_test.py` (exam order); `validate_papers.py` updated for choice papers, 8/32/10 per path and answer runs.

---

## Repository changes (27 Oct 2026)

- **Series size:** CUET UG now has **15 tests per subject** (Accountancy keeps 16). Tests 16–25 of the other 14 subjects and Tests 17–25 of Accountancy were deleted (149 files); every `series_index.json` was rebuilt. Other exams (IAT, NEST, COMEDK) keep **25 tests**.
- **Syllabus Markdown:** all 23 CUET syllabus PDFs converted to `CUET SYLLABUS/md/*.md` (text extraction, cleaned). Also `IISER/IISER_Aptitude_Test_Syllabus_2026.md` and `NISER/NEST_2026_Syllabus.md` (from the official NEST 2026 brochure).
- **New instructions:** `docs/instructions/IAT_Instructions.md`, `NISER_Instructions.md` (NEST), `COMEDK_Instructions.md` — official pattern and marking, PYQ-analysis protocol (PYQs supplied by the user before work starts), 15/65/20 difficulty split per section, image-prompt files (`IISER/IAT_images.md`, `NISER/NEST_images.md`, `COMEDK/COMEDK_images.md`), workflow, pre-start / per-test / pre-release checklists, and JSON format.
- **CUET instructions v3.1:** 15 tests, read syllabus Markdown, plan-first coverage map, per-subject image list. Hermes copy synced.

---

## Biological Science (304) — revised to the CUET 2027 standard (completed 28 Oct 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `5353859` (blueprint, coverage map, pilot Test 1) … `72ba80c` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | 15 old papers (mostly direct recall) | **15 rewritten tests** (`CUET BIOLOGICAL SCIENCE TEST 1–15.json`), planned first in a coverage map |
| Paper structure | 50 questions | 50 compulsory questions, 60 min, +5 / −1 (NTA pattern) |
| Unit weights | uneven | every test: VI 11 (4/4/3), VII 14 (5/6/3), VIII 8 (5/3), IX 8 (4/4), X 9 (3/3/3) |
| Difficulty | mostly easy | **8 easy / 32 medium / 10 hard** in every test |
| Formats | almost all direct | per test: one 5-question case set, 5 match-list, 5 statements, 3 assertion–reason, 2 sequence, 2 data-based, plus direct and numerical |
| Explanations | short | `Answer:` line, then Given / Step / Common mistake (numericals and data) or Why / Why not the others / Key point; all facts from NCERT Class 12 (rationalised) |
| Order and keys | unit-wise, unbalanced | random exam order; key 12–13 per letter; no letter more than 3 times in a row; correct option never clearly the longest |
| Syllabus | included deleted topics | checked against `CUET SYLLABUS/md/Biological Science - 304.md`; no deleted chapters (Reproduction in Organisms, Strategies for Enhancement in Food Production, Environmental Issues), no nutrient cycling or succession |

**Case-set themes:** 1 menstrual cycle; 2 lac operon; 3 population growth; 4 cloning into pBR322; 5 pedigree analysis; 6 immune response and vaccination; 7 embryo sac and double fertilisation; 8 Hardy–Weinberg; 9 Bt cotton and RNAi; 10 energy flow; 11 infertile couple and ART; 12 sewage treatment and biogas; 13 DNA fingerprinting (forensic); 14 biodiversity (species–area, hotspots, loss); 15 sickle-cell disease (inheritance, diagnosis, gene therapy).

**Verification:** `validate_papers.py` — 0 parse errors, 0 key/explanation mismatches, 0 runs > 3, 0 within- or cross-paper duplicate stems, 0 difficulty deviations; key across the series A 25.7%, B 24.3%, C 24.9%, D 25.1%. Before each build, a similarity check against all earlier tests replaced near-repeats (about 30 questions across Tests 12–15).

**Fixes to earlier tests found in the final sweep:** "standing state" (part of Nutrient Cycling, not in the CUET syllabus) was removed — Test 6 Q27 rewritten as a standing-crop/biomass statements question, Test 9 Q04 replaced with a productivity-units question, and a wording fix in the Test 2 Q19 explanation.

**Known limits:** NCERT Class 12 Biology is finite, so over 15 tests some facts recur in different formats (e.g. as a distractor in one test and a stem in another); the coverage map caps each angle at three uses. Low-capacity banks (IX-2, VI-3, X-3) were extended with new NCERT angles during Tests 13–15.

### Tools added
- `docs/blueprints/biological_science.md` (pattern, PYQ analysis, weights) and `docs/blueprints/biological_science_coverage.md` (case themes and angle banks with "Used in" columns).

---

## Chemistry (306) — revised to the CUET 2027 standard (completed 29 Oct 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `0cf3166` (blueprint, coverage map, pilot Test 1) … Test 15 on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | 15 old papers (5 questions per unit, mostly direct recall) | **15 rewritten tests** (`CUET CHEMISTRY TEST 1–15.json`), planned first in a coverage map |
| Paper structure | 50 questions | 50 compulsory questions, 60 min, +5 / −1 (NTA pattern) |
| Unit weights | 5 per unit | every test: physical 15 (I 5, II 5, III 5), inorganic 11 (IV 5, V 6), organic 24 (VI 5, VII 5, VIII 6, IX 4, X 4) — organic-heavy, as in the 2025 shifts; the passage set counts inside its unit |
| Difficulty | mostly easy | **8 easy / 32 medium / 10 hard** in every test |
| Formats | almost all direct | per test: one 5-question passage set, 5 match-list, 5 statements, 3 assertion–reason, 3 order/sequence, 2 data or table, at least 6 numericals, the rest direct |
| Numbers | — | all numericals solvable without a calculator; constants and logs given in the question |
| Explanations | 1–2 lines | `Answer:` line, then Given / Step / Common mistake (numericals, data) or Why / Why not the others / Key point; all from NCERT Class 12 Chemistry |
| Order and keys | unit-wise | random exam order; key 12–13 per letter in every test; no letter more than 3 times in a row; correct option never clearly the longest; statement-question answer patterns varied |
| Syllabus | — | checked against `CUET SYLLABUS/md/Chemistry - 306.md`; no solid state, surface chemistry, p-block, metallurgy, polymers chapter or Class 11 physical chemistry |

**Passage-set themes:** 1 first-order N₂O₅ decomposition; 2 Werner's cobalt ammines; 3 Daniell cell and Nernst equation; 4 antifreeze and osmotic pressure of a protein; 5 SN1 vs SN2 (2-bromobutane, tert-butyl bromide); 6 glucose structure; 7 KMnO₄ and K₂Cr₂O₇; 8 identifying unknown carbonyl compounds; 9 diazonium salts; 10 electrolysis and Faraday's laws; 11 phenol (cumene, Kolbe, Reimer–Tiemann); 12 Arrhenius equation; 13 crystal field theory and magnetism; 14 E° trends of the 3d series; 15 ethanoic acid → HVZ → amide → amine.

**Verification:** `validate_papers.py` — 0 parse errors, 0 key/explanation mismatches, 0 runs > 3, 0 within- or cross-paper duplicate stems, 0 difficulty deviations; series key A 25.6%, B 24.3%, C 24.7%, D 25.5%. Before each build, a similarity check against all earlier tests led to rewriting or replacing near-repeats (about 25 questions across Tests 2–15). A final sweep found no out-of-syllabus topics.

**Known limits:** some calculation types (Kohlrausch's law, Nernst equation, Faraday's laws, colligative-property arithmetic) recur across tests with different substances and numbers, and some short stems share templates (e.g. "The IUPAC name of … is"). Syllabus items dropped from the rationalised NCERT (metal carbonyls, hormones, corrosion, preparation of glucose) are tested from the earlier NCERT text, as the CUET syllabus still lists them. The coverage map was extended during the series as topic banks ran low.

### Tools added
- `docs/blueprints/chemistry.md` (pattern, 2025 PYQ analysis, weights, formats, out-of-syllabus list) and `docs/blueprints/chemistry_coverage.md` (passage themes and angle banks with "Used in" columns).

---

## IAT reference collection and fixed order (28 Oct 2026)

- The user supplied the official IAT previous-paper archive URL and explicitly requested downloading/storing the PDFs, Markdown conversion and image descriptions.
- The official server returned connection failures/503 in this environment. Recovered mirror-hosted papers are transparently labelled in `PYQ/IAT/SOURCES.md` and `manifest.json`; no official-host byte-equivalence claim is made.
- Stored 17 PDFs: English for 2017, 2018, 2019, 2021, 2022, 2023, 2024, 2025 and 2026; Hindi for the same years except 2018. The 2026 documents are provisional answer-key papers, not verified final keys. A 2020 file was not recovered; no inference is made about whether the exam occurred.
- Corrected a mirror-label error: the SciAstra links labelled 2021 contain the 2022 paper. The actual 2021 files were separately obtained from public PYQP Google Drive links. Preserved the erroneous source label and correction in provenance metadata.
- Created 17 page-indexed Markdown copies, 659 original page images and 131 English page-specific figure/table descriptions. Hindi copies include their own page images/OCR, the English visual guide and matching embedded-image cross-references. OCR completed for 336 pages without process failures, but the text is a searchable draft, not a fully proofread mathematical/Hindi transcription; source PDFs/images remain authoritative.
- The 2025 English source has 59 question-labelled entries and ends at Physics Q14. Preserved the source numbering/content without inventing a missing question. The 2026 cover explicitly says the first option is correct throughout; this is answer-key ordering, not the live examination's option order.
- User decision: **no shuffling for IAT, NEST or COMEDK**. Updated their instructions, the instruction index and README. Their final question/option order, IDs and diagram references must stay fixed. `shuffle_test.py` now rejects these series before changing the target file; CUET retains its existing workflow.
- No mock questions were generated. PYQ analysis/blueprint/coverage approval, an IAT-specific validator and pilot approval remain separate next steps. The official 2027 pattern is not yet verified.

---

## IAT PYQ analysis and Test 1 review pilot (29 Oct 2026)

- The user explicitly authorised completing PYQ analysis and proceeding directly to Test 1 JSON plus a PDF with images and solutions for manual review. This supersedes the earlier separate pre-pilot approval pause; approval of the pilot standard before Tests 2–25 remains pending.
- Manually tagged 539 acquired English questions across nine papers (2017–2019, 2021–2026); the incomplete 2025 copy contributes 59. Created a source-page ledger, editable tag list, taxonomy, reproducible descriptive metrics and full chapter-count appendix. Flagged 22 historical/ambiguous-scope items. No student-performance data or calibrated predictive probabilities are claimed.
- Wrote `docs/blueprints/iat_pyq_analysis.md`, a 25-test chapter-level reservation in `iat.md`, and the detailed 60-slot Test 1 plan. Later tests still need exact angle plans and pilot feedback before authorship.
- Checked official indexed 2026 examination and brochure references for the 60-question, 180-minute, +4/-1/0 scheme and the permitted on-screen non-programmable scientific calculator. Corrected the old no-calculator assumption. No 2027 brochure has been verified; the pilot is explicitly provisional for 2027 preparation.
- Authored `IISER/IAT TEST 1.json` directly: 60 original questions, 15 each in B/C/M/P order; nine easy, 39 medium and 12 hard; 15 answers at each letter. No legacy content generator or shuffling script was used. Fixed question/option order, stable IDs and image links are preserved.
- Added six exact scientific PNG figures, their accessibility text and image-register entries. Improved circuit-label spacing during PDF review. Strengthened Chemistry Q24 to integrate selective reduction/acylation, formula tracking and stereoisomer counting; the stored correct letter remained C.
- Added `validate_iat.py`, deterministic diagram rendering, transcribed-input arithmetic probes and a KaTeX/mhchem review exporter. Generated the 49-page PDF, self-contained HTML, byte-identical delivery JSON and checksum manifest. All 328 delimited math expressions parse, 60 question/solution blocks render, all six images load, and 45 arithmetic/enumeration probes pass. These are supporting checks; they do not replace human academic and timed review.
- Updated README and IAT series index. The pilot remains `pending_revision`, with zero approved papers. No remote push or student publication was performed.

### Visual PYQ guide and full pilot audit (29 Oct 2026)

- Created the requested 14-page student-facing PYQ analysis PDF with ten data charts, including every retained chapter family, a four-year recurrence heatmap, styles, editorial difficulty, approximate Class 11/12 balance and practical study priorities. The text distinguishes the 539-item archive, 239 recent items and 231 recent current-scope items, without treating frequencies as predictions.
- Created a separate 19-page audit PDF: official structure, syllabus/chapter balance, consistent task recoding, difficulty, distractors, reading/option-length cues, key checks, model assumptions, all six image purposes and all 60 item findings. Rechecked official 2026 scheme/calculator sources; no verified 2027 rules are claimed.
- Audit verdict: useful structural pilot, revise before release. Main gaps: zero primary coordinate-geometry slot, Chemistry's numerical emphasis, several weak/supplied-answer distractors and debatable tiers. Proposed tiers are 18 easy / 32 medium / 10 hard, explicitly editorial; these were not written back into the test. No definite wrong key was identified under the stated assumptions, but independent academic and timed-student validation remain outstanding.
- All six figures are relevant and consistent with the intended models: Q11/Q46/Q53/Q54 carry representation-reading tasks; Q9/Q57 are useful setup sketches rather than equally demanding visual problems. The report reproduces and checks every figure instead of treating a file-existence check as scientific validation.
- Preserved the canonical JSON, six PNGs and original 49-page test PDF unchanged, verified by hashes. All 33 new report pages were rendered and inspected, with adjustments to chart-label size, table headings and diagram display size. Page counts, text margins, count reconciliations and character extraction pass. New files are under `output/pdf/`; source, assets and supporting verification are in `output/iat_reports/` and `tools/iat/build_analysis_reports.py`.


## IAT audit response and restoration (30 Oct 2026)

- Integrated the newer remote CUET Biology, Chemistry and Computer Science commits without overwriting them; preserved both branches of the Worklog merge.
- The available workspace contained the old draft; the previously described revised downloads/local commit were unavailable. Restored an audit-corrected revision from the baseline; no byte-identity claim to missing artifacts.
- Updated 21 item records, retaining IDs, section positions and answer letters. Difficulty policy: 9 easy / 42 medium / 9 hard. Added coordinate geometry, kidney/signalling/diffusion data, a cumulative nitrogen graph and alkene connectivity; strengthened mixture inference, SHM and beats; clarified osmosis and rail orientation.
- Preserved baseline JSON/PDF/plan and labelled the original audit as historical. Updated instructions v2, validator, blueprint, slot plan and series index. Six original images unchanged; two new exact figures. Four tables stay readable in JSON and PDF.
- Current checks: 68 supporting calculation/enumeration probes; 346 parsed math expressions; 60 questions/solutions; eight loaded images; no detected horizontal overflow or oversized blocks. All 55 pages rendered and inspected through contact sheets; new figures and dense conic working additionally inspected at larger scale. Independent academic/timed review and 2027 rule verification remain pending.


## IAT 25-test series planning (30 Oct 2026)

- Added a 1,500-slot register for 25 papers, with fixed IDs, chapter/subtopic focus, reasoning seeds, style and 9/42/9 tier reservations. Tests 2 and 3 have 120 individually specified angle briefs. Every retained syllabus family appears; chapter frequency is PYQ-informed rather than mechanically equal.
- Preserved Test 1's authored slots and verified 375 slots per subject, 15 per subject per test, broad Class 11/12 coverage and no exact duplicate chapter/angle seeds among un-authored reservations. Distinct seed labels are not a semantic originality guarantee; each future question needs independent authorship and review.
- This commit contains planning material only; it does not claim Tests 2 or 3 are authored or approved.

## Computer Science / Informatics Practices (308) — revised to the CUET 2027 standard (completed 30 Oct 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `8607e9b` (blueprint, coverage map, pilot Test 1) … `69b81f8` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | 15 old papers of 50 questions, all compulsory | **15 rewritten tests** (`CUET COMPUTER SCIENCE TEST 1–15.json`), planned first in a coverage map |
| Paper structure | single 50-question list | **85 questions per file**: Section A (15, common: database concepts, SQL, networks) + Section B1 Computer Science (35) + Section B2 Informatics Practices (35); a candidate attempts A plus one of B1/B2 = 50; 60 min, +5 / −1. Stored with `sections`, `common_sections` and `optional_sections`, as for Accountancy |
| Unit weights | — | A: DB 4, SQL I 4, SQL II 4, networks 3. B1: exceptions/files 5, stack 4, queue 3, searching 4, sorting 3, data 3, DB/SQL 6, networks 4, security 3. B2: SQL 5, Pandas I 8, Pandas II 6, Matplotlib 6, web 4, societal impacts 5, project-based learning 1. Each B section's 5-question case set counts inside its unit |
| Difficulty | mostly easy | **8 easy / 32 medium / 10 hard on both attempt paths** (A + B1 and A + B2) |
| Formats | almost all direct | per path: one case set, 5 match-list, 5 statements, 3 assertion–reason, 3 order/sequence, many output/dry-run questions (SQL results, Python and Pandas output, postfix values, search and sort passes), the rest direct |
| Code and outputs | — | every Python, Pandas and file-handling output was run before release (Pandas 2.3.3); SQL results worked out with MySQL rules and cross-checked in SQLite where possible; weekday names checked with Python |
| Explanations | 1–2 lines | `Answer:` line, then Given / Step / Common mistake (outputs) or Why / Why not the others / Key point; all from NCERT CS and IP Classes 11–12 |
| Order and keys | unit-wise | random order within each section; key about 4/4/4/3 in A and 9/9/9/8 in B1/B2; no letter more than 3 times in a row; correct option never clearly the longest; statement and assertion–reason answers varied |
| Syllabus | — | checked against `CUET SYLLABUS/md/Computer Science - 308.md`; no OOP, sub-queries, views, OSI layers, subnetting or collision-resolution methods |

**Case-set themes (B1 / B2):** 1 postfix evaluation / Series from a dictionary; 2 reading a text file / DataFrame loc–iloc; 3 try–except–else–finally trace / line-plot code; 4 ticket-counter queue / GROUP BY–HAVING sales; 5 binary search dry run / DataFrame statistics; 6 bubble sort passes / missing values; 7 pickle records / histogram and bar chart; 8 hashing and collisions / merge–concat; 9 infix-to-postfix conversion / SQL date functions; 10 class marks statistics / CSV import–export; 11 selection vs insertion sort / e-waste and health; 12 school campus network / website hosting and browsers; 13 security incident / cybercrime and the IT Act; 14 library database SQL / groupby, sorting and pivot; 15 data communication / SQL text functions.

**Verification:** `validate_papers.py` — 0 parse errors, 0 key/explanation mismatches, 0 runs > 3, 0 self-referential options, 0 within- or cross-paper duplicate stems, 0 difficulty deviations; series key A 25.8%, B 25.3%, C 25.4%, D 23.5%. Before each build, a similarity check against all earlier tests led to renaming or rewording near-repeats.

**Known limits:** output-type questions (ROUND/MID/INSTR results, postfix values, bubble and selection passes, groupby sums) recur across tests with new data, as the coverage map allows; some stems share templates such as "What is the output of the following MySQL query?". MySQL rounding of exact halves (e.g. ROUND(10.5) = 11) follows MySQL's rule for exact values. The coverage map was extended twice (before Tests 5 and 10) as topic banks ran low.

### Tools added
- `docs/blueprints/computer_science.md` (pattern, 2025 PYQ analysis, weights, formats, out-of-syllabus list) and `docs/blueprints/computer_science_coverage.md` (case themes and angle banks with "Used in" columns).

## IAT New Tests 2 and 3 — fresh review drafts (31 Oct 2026)

- Recreated both papers from the 25-test slot plan under distinct `IAT NEW TEST` names after the previous uncommitted drafts were unavailable. Each has 60 questions (15 per subject), editorial tiers 9/42/9, balanced A–D keys and detailed worked explanations including why the alternatives fail.
- Added six exact, question-bearing figures per paper: two each for Biology, Chemistry and Physics. Updated the image register, figure generator, instructions and authored slot records. Replaced two semantic repeats found against Test 1.
- Exported answer-and-explanation review PDFs (46 and 45 pages). The validator and render checks confirm the JSON/PDF hashes, 60 questions and solutions, loaded images, and no detected layout overflow. The item-level mathematics calibration and remaining review requirements are recorded in `IISER/review/IAT_NEW_TESTS_2_3_REVIEW_NOTES.md`.
- These are authoring drafts awaiting independent subject-expert and timed-student review, and 2027 brochure verification. The session workflow now requires a verified commit and remote push before treating a paper as safely stored.
- After remote authentication became available, pushed the two draft commits to `iat-new-tests-2-3` and verified remote HEAD. Added `docs/blueprints/iat_series_continuity.md` and `tools/iat/check_series_overlap.py` to restart from versioned PYQs, the slot plan and every authored test. The series-wide text screen reports zero candidates among Tests 1–3 at its default threshold; semantic angle comparison remains an editorial task.

## IAT New Tests 4 and 5 — review drafts (31 Oct 2026)

- Authored 120 further questions from the reserved slots, each paper with 15 questions per subject, editorial tiers 9/42/9 and 15 keys per letter. Explanations include a worked WHY and alternatives; both papers remain pending independent academic and timed-student review.
- Generated six purpose-built figures in Test 4 and eight in Test 5. Review PDFs contain 60 questions and 60 solutions each, with loaded images and no detected overflow. Replaced three Test 5 Mathematics items after a cross-paper similarity screen identified close earlier stems; a looser pass led to three additional method/data revisions. The default screen now reports zero candidates across Tests 1–5. See `IISER/review/IAT_NEW_TESTS_4_5_REVIEW_NOTES.md` for the 30-item mathematics task review.
- Updated the 25-test register: 300 authored draft slots across Tests 1–5, with 1,200 reserved for Tests 6–25. Remote push verification remains required before calling this session durable.

## IAT New Tests 2–5 — explanation revision (1 Nov 2026)

- Audited all 240 explanations and revised each for explanatory depth. All 120 Mathematics/Physics items now include a displayed worked derivation; Biology/Chemistry `Why` sections were expanded with evidence, mechanism and constraints. See `IISER/review/IAT_NEW_TESTS_2_5_EXPLANATION_REVISION.md` for the measured results and review limits.
- Added strict explanation rules and a release checklist to the IAT instructions, plus a mechanical validator gate for the Mathematics/Physics derivation in every new paper. Regenerated four delivery bundles after the last source edit; each PDF contains 60 solutions, figures and parsed mathematics with no reported overflow.
- The papers remain `pending_revision` for independent hidden-key subject review and timed attempt; a committed review PDF is not academic approval.

## IAT New Tests 6 and 7 — authored review drafts (1 Nov 2026)

- Completed 120 individually authored questions from the reserved slots, with 15 per subject and 9/42/9 editorial tiers per paper. Final keys are 15 per letter. Each of the 60 Mathematics/Physics items has a displayed worked derivation and every distractor has an individually labelled explanation.
- Drew and registered six question-bearing figures for each paper: two Biology, two Chemistry and two Physics. Generated delivery JSON, HTML and 51-page PDF for each. Source/delivery/PDF checksums, parsed mathematics, all loaded images and zero detected overflow are recorded in the render checks.
- Replaced five weak hard-labelled Mathematics tasks with multi-stage problems and replaced one integral too close in method to Test 1. The default cross-paper text similarity screen reports zero candidates among Tests 1–7. Updated the 25-test slot register to 420 authored draft slots and 1,080 reservations.
- See `IISER/review/IAT_NEW_TESTS_6_7_REVIEW_NOTES.md` for the item-level review and limits. Both papers remain pending independent hidden-key academic review and timed-student calibration.

## IAT New Tests 8 and 9 — authored review drafts (1 Nov 2026)

- Authored 120 new questions from the 25-test reservations. Each test has 15 questions per subject, 9/42/9 editorial difficulty tiers, balanced keys and detailed explanations; all Mathematics and Physics questions have displayed derivations.
- Drew and registered six figures for Test 8 and eight for Test 9, including at least two per Biology, Chemistry and Physics. Generated canonical JSON and delivery JSON/HTML/PDF with strict math parsing and no detected overflow; pages and item-level mathematics audit are in `IISER/review/IAT_NEW_TESTS_8_9_REVIEW_NOTES.md`.
- Reworked same-method candidate tasks and upgraded hard Mathematics slots. One text-overlap candidate remains after semantic review: Test 4's coordinate-plane projection and Test 9's oblique-line projection use distinct calculations. Updated the 25-test register to 540 authored draft slots, 960 reserved.
- Independent hidden-key academic and timed-student review remains pending. Verify the remote branch HEAD before treating the session as durable.

## IAT New Tests 10 and 11 — authored review drafts (3 Nov 2026)

- Authored 120 new items against fixed syllabus slots. Each paper has 15 questions per subject, editorial tiers 9/42/9, balanced A–D keys and detailed `Why` plus distractor analyses; all Mathematics and Physics items have displayed derivations.
- Drew and registered eight figure-linked questions in Test 10 and twelve in Test 11. Rendered 31- and 33-page review PDFs using the versioned XeLaTeX exporter, with 60 question/solution pairs each, source/delivery/PDF/image checksums, no empty pages, no overfull lines and no missing glyphs.
- Replaced repeated reasoning tasks found against earlier papers, including cardiac output, capacitor charge, fixed telescoping sum and simple two-factor integral, then replaced further Hardy–Weinberg, rms-speed and hydrogen-transition ratio repeats in a manual scan. The series-wide default similarity screen now reports zero candidates. The 25-test slot register has 660 authored review-draft slots and 840 reservations.
- See `IISER/review/IAT_NEW_TESTS_10_11_REVIEW_NOTES.md` for item-level Mathematics review and remaining independent academic and timed-student checks.

## Economics (309) — revised to the CUET 2027 standard (completed 3 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `6216323` (blueprint, coverage map, pilot Test 1) … `020da25` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | 15 old papers of 50 questions, mostly easy (about 35 / 12 / 3), status `pending_revision` | **15 rewritten tests** (`CUET ECONOMICS TEST 1–15.json`), planned first in a coverage map; status `revised` |
| Paper structure | 50 compulsory | unchanged: 50 compulsory questions, 60 min, +5 / −1 (NTA pattern) |
| Unit weights | — | Micro 16 (M1 6, M2 4, M3 4, M4 2); Macro 19 (C1 5, C2 4, C3 4, C4 3, C5 3); IED 15 (D1 5, D2 3, D3 5, D4 2). The 5-question case set counts inside its unit; where that unit's quota is below 5, the extra questions come from another unit of the same course |
| Difficulty | mostly easy | **8 easy / 32 medium / 10 hard in every test** |
| Formats | almost all direct | per test: one case set (5), 5 match-list, 5 statements, 3 assertion–reason, 3 sequence, 2 data-table, at least 6 numericals, the rest direct |
| Numericals | few | calculator-free numbers, every answer worked out step by step (national income, elasticity, costs, multiplier, deficits, money multiplier, BoP) |
| Explanations | 1–2 lines | `Answer:` line, then Given / Step / Common mistake (numericals, data, case sets) or Why / Why not the others / Key point; all from NCERT Classes 11–12 Economics |
| Order and keys | unit-wise | random order; key about 13 / 12 / 13 / 12 per test; no letter more than 3 times in a row; correct option never clearly the longest; statement and assertion–reason answers varied |
| Syllabus | — | checked against `CUET SYLLABUS/md/Economics - 309.md`; no Statistics for Economics, monopoly or oligopoly theory, IS–LM, or the poverty and infrastructure chapters |

**Case-set themes:** 1 national income from a data table; 2 consumer equilibrium and budget line; 3 money creation by banks; 4 land reforms and the Green Revolution; 5 production and cost schedule; 6 two-sector income determination; 7 human capital and employment (district workforce data); 8 firm under perfect competition (cost table, profit, shut-down); 9 state government budget (revenue, fiscal and primary deficits); 10 reforms since 1991 and GST (incl. a disinvestment calculation); 11 price ceiling and price floor (grain market schedule); 12 balance of payments table; 13 India–China–Pakistan indicators; 14 price elasticity by the percentage, expenditure and geometric methods; 15 environment and sustainable development (district report).

**Verification:** `validate_papers.py CUET --subject "Economics"` — 0 parse errors, 0 wrong counts, 0 key/explanation mismatches, 0 runs > 3, 0 self-referential options, 0 within- or cross-paper duplicate stems, 0 difficulty deviations; series key A 25.3%, B 24.9%, C 25.6%, D 24.1%. Before each build, a check against all earlier revised tests (sub-topic and stem similarity) led to renaming or rewording near-repeats; a scan for out-of-syllabus terms found only harmless uses (e.g. "Britain kept a monopoly over India's trade").

**Known limits:** numerical and data angles marked [O] (national income, multiplier, deficits, money creation, BoP balances, elasticity) recur across tests with new numbers, as the coverage map allows; one non-numerical angle (M1 17, substitutes and complements) was used 4 times, once more than the cap, each time in a different format. The Test 13 indicator table uses approximate figures that follow the pattern of NCERT's comparison, so questions ask about comparisons rather than exact values. The coverage map was extended twice (before Tests 6 and 11) as angle banks ran low.

### Tools added
- `docs/blueprints/economics.md` (pattern, 2025 PYQ analysis, weights, difficulty, formats, out-of-syllabus list) and `docs/blueprints/economics_coverage.md` (15 case themes and 275 angles with "Used in" columns).

## English (101) — revised to the CUET 2027 standard (completed 4 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `b780495` (blueprint, coverage map, pilot Test 1) … `bdcb6ca` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | 15 old papers of 50 questions, mostly easy (about 35 / 12 / 3), status `pending_revision` | **15 rewritten tests** (`CUET ENGLISH TEST 1–15.json`), planned first in a coverage map; status `revised` |
| Paper structure | 50 compulsory | unchanged: 50 compulsory questions, 60 min, +5 / −1 (NTA pattern) |
| Area weights | — | Reading Comprehension 15 (factual, narrative and literary passages, 5 questions each); Verbal Ability 35 (rearranging 5, match 5, correct word 14, synonyms/antonyms 6, one-word substitution 2, voice/narration/correct sentence 3) |
| Passages | — | 45 original passages (≤ 300 words; verse in alternate tests), one theme each, never reused; factual passages checked against standard sources |
| Difficulty | mostly easy | **8 easy / 32 medium / 10 hard in every test** |
| Formats | almost all direct | per test: 15 passage, 5 sequence, 5 match-list, 3 statements / multi-select, 22 direct; no assertion–reason (NTA does not set it in English) |
| Explanations | 1–2 lines | `Answer:` line, then Why / Why not the others / Key point; passage answers quote the deciding line; rearrangements name the links that fix the order |
| Order and keys | section-wise | random order with each passage set kept together; key 13 / 12 / 13 / 12 (or 12 / 13 / 12 / 13) per test; no letter more than 3 times in a row; correct option never clearly the longest |
| Syllabus | — | checked against `CUET SYLLABUS/md/English - 101.md`; no textbook literature, grammar terminology for its own sake or American spelling |

**Coverage ledgers:** 631 targets, none tested twice — 313 words (synonyms, antonyms, vocabulary, spelling, one-word substitutes), 69 idioms, 102 phrasal verbs and collocations, 147 confusables, word forms, prepositions and linkers (`docs/blueprints/english_coverage.md` §C). Figures of speech recur with new examples, as the blueprint allows.

**Verification:** `validate_papers.py CUET --subject "English"` — 0 parse errors, 0 wrong counts, 0 key/explanation mismatches, 0 runs > 3, 0 self-referential options, 0 within- or cross-paper duplicate stems, 0 RC questions missing their passage, 0 difficulty deviations; series key A 25.5%, B 24.5%, C 25.9%, D 24.1%. `eng_check.py` was run on every draft (counts, key, passage length, longest-option, ledger repeats, overlap with earlier tests).

**Known limits:** the instruction stems of the verbal-ability formats ("Choose the word most similar in meaning to …") repeat by design, so the overlap check flags them; the targets differ in every case. In rearrangement items, adverbial phrases can often move, so distractor orders were checked by hand for a second readable order; one such distractor in Test 4 (`14cf7ef`) and four more in Tests 2–4 (`cba8ede`) were replaced after shipping. In a few easy rearrangements, the only wrong orders are ones that start with a lower-case part.

### Tools added
- `docs/blueprints/english.md` (pattern, 2026 PYQ analysis, weights, difficulty, formats, passage rules, out-of-scope list) and `docs/blueprints/english_coverage.md` (passage themes, slot plan, target ledgers).
- `tools/cuet_english/` — compact draft format and converter, builder, checker, ledger marker, ship script, item patcher (`patch_item.py`) and series re-indexer (`reindex_series.py`); drafts of all 15 tests in `drafts/`. The `.py` files are now tracked (`.gitignore` exception, as for `tools/iat`).

## General Test (501) — revised to the CUET 2027 standard (completed 4 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `045851f` (blueprint, coverage map, pilot Test 1) … `bbb3580` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | 15 old papers of 50 questions, status `pending_revision` | **15 rewritten tests** (`CUET GENERAL TEST TEST 1–15.json`), planned first in a coverage map; status `revised` |
| Paper structure | 50 compulsory | unchanged: 50 compulsory questions, 60 min, +5 / −1 (NTA pattern) |
| Section weights | — | quantitative aptitude 10, data interpretation set 5, mental ability 7, logical reasoning 6, static GK 8, general science and environment 9, current affairs 5 |
| Data sets | — | 15 original tables, one theme each (enrolment, rainfall, shop sales, marks, village literacy, family budget, electricity, crops, cricket runs, train tickets, library books, factory shifts, tourist arrivals, hospital patients, mobile data) |
| Difficulty | uneven | **8 easy / 32 medium / 10 hard in every test** |
| Formats | almost all direct | per test: 5 data-set, 3 match-list, 3 statements, 2 assertion–reason, 2 sequence, the rest direct or numerical |
| Explanations | 1–2 lines | quantitative: Given / Step / Common mistake; reasoning: Answer steps / Why not the others / Key point; GK, science and current affairs: Why / Why not the others / Key point |
| Order and keys | section-wise | random order with the data set kept together; key 13 / 12 / 13 / 12 per test; no letter more than 3 times in a row; correct option never the longest |
| Current affairs | dated | 75 items from Jan 2025 to Oct 2026, each checked online before writing, with its date in the explanation; political and sensitive topics left out |

**Coverage ledgers:** each test marks 31 targets (14 static GK, 12 science and environment, 5 current affairs) in `docs/blueprints/general_test_coverage.md`; `gt_check.py` flags any target used before (`REPEAT-TARGET`), and every flag was replaced before shipping. Quantitative and reasoning sub-topics were rotated so that no question type repeats across the series.

**Verification:** `validate_papers.py CUET --subject "General Test"` — 0 parse errors, 0 wrong counts, 0 key/explanation mismatches, 0 runs > 3, 0 self-referential options, 0 within- or cross-paper duplicate stems, 0 difficulty deviations; series key A 26.0%, B 24.0%, C 26.0%, D 24.0%. `gt_check.py` was run on every draft (difficulty, key, formats, longest-option, ledger repeats, overlap with earlier tests).

**Known limits:** a few current-affairs facts rest on news reports rather than an official release (for example medal tables of the 2026 Asian and Commonwealth Games); items avoid figures where sources disagreed. Reasoning instruction stems (syllogism and assumption options) repeat by design.

### Tools added
- `docs/blueprints/general_test.md` (pattern, weights, difficulty, formats, out-of-scope list) and `docs/blueprints/general_test_coverage.md` (data-set themes, slot rotation, target ledgers).
- `tools/cuet_gt/` — compact draft format and converter, checker, builder, ledger marker, ship script, item patcher and series re-indexer; drafts of all 15 tests in `drafts/`.

## Geography (313) — revised to the CUET 2027 standard (completed 5 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `9575066` (blueprint, coverage map and tools), `b75b5a4` (pilot Test 1) … `02b718f` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | 15 old papers of 50 questions, status `pending_revision` | **15 rewritten tests** (`CUET GEOGRAPHY TEST 1–15.json`), planned first in a coverage map; status `revised` |
| Paper structure | 50 compulsory | unchanged: 50 compulsory questions, 60 min, +5 / −1 (NTA pattern) |
| Syllabus | mixed, with dropped topics | only the rationalised NCERT Class XII books: *Fundamentals of Human Geography* (24 questions per test) and *India: People and Economy* (26 per test), with fixed unit quotas |
| Case sets | — | 15 original passages or tables, one per test (Indira Gandhi Canal command area, land use, human development, waterways and highway corridors, exports and imports, slums and urban waste, watershed management, Bharmaur tribal region, location of manufacturing, seaports and hinterlands, among others) |
| Difficulty | uneven | **8 easy / 32 medium / 10 hard in every test** |
| Formats | almost all direct | per test: 5 case-set, 5 match-list, 5 statements, 3 assertion–reason, 3 sequence, 2 numerical, 27 direct |
| Explanations | 1–2 lines | concept items: Why / Why not the others / Key point; numericals: Given / Step / Common mistake; statement items name the false statement |
| Order and keys | section-wise | random order with the case set kept together; key 13 / 12 / 13 / 12 per test; no letter more than 3 times in a row; correct option never clearly the longest |

**Coverage ledger:** every answer fact is a key in `docs/blueprints/geography_coverage.md` §C, used at most twice in the series, in different tests and different formats; `geo_check.py` flags any key already used twice (`REPEAT-TARGET`), duplicate keys within a test, and sub-topic or stem overlap with earlier tests. Every flag was cleared before shipping.

**Verification:** `validate_papers.py CUET --subject "Geography"` — 0 parse errors, 0 wrong counts, 0 key/explanation mismatches, 0 runs > 3, 0 self-referential options, 0 within- or cross-paper duplicate stems, 0 passage gaps, 0 difficulty deviations; series key A 25.1%, B 24.9%, C 25.1%, D 24.9%.

**Known limits:** a few location-order items (Damodar coalfields, iron-ore mines, Konkan Railway and Australian Trans-Continental stations) rely on map positions rather than NCERT text. Late tests reuse single-use facts in a new format because fresh NCERT facts were running out.

### Tools added
- `docs/blueprints/geography.md` (pattern, PYQ analysis, unit quotas, difficulty, formats, out-of-scope list) and `docs/blueprints/geography_coverage.md` (case-set plan, unit rotation, fact ledger).
- `tools/cuet_geo/` — compact draft format and converter, checker, builder, ledger marker, ship script, item patcher and series re-indexer; drafts of all 15 tests in `drafts/`.

## Hindi (102) — revised to the CUET 2027 standard (completed 6 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `8baeb60` (blueprint, coverage map and tools), `7d76330` (pilot Test 1) … `9109907` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | old papers, status `pending_revision` | **15 rewritten tests** (`CUET HINDI TEST 1–15.json`), planned first in a coverage map; status `revised` |
| Paper structure | 50 compulsory | unchanged: 50 compulsory questions, 60 min, +5 / −1 (NTA pattern) |
| Reading | mixed passages | per test 3 original passages × 5 questions: a factual prose passage, a narrative passage, and a literary piece (verse in odd tests, lalit prose in even tests). Themes include rainwater harvesting, Hindi journalism (उदंत मार्तंड), tiger conservation, the Indian postal system, a daughter's bicycle and a farewell speech |
| Verbal ability | uneven | 35 questions in six fixed blocks: क्रम-व्यवस्था 4, सुमेलन 5, सही शब्द / शुद्ध प्रयोग 7, शब्द-भंडार 7, व्याकरण 8, काव्यांग और साहित्य 4, with rotating slots (संधि / समास, रस → अलंकार → छंद, मुहावरे / लोकोक्तियाँ, लेखक-रचना / श्रुतिसम / उपसर्ग) |
| Difficulty | uneven | **8 easy / 32 medium / 10 hard in every test**; each passage runs easy, medium ×3, hard |
| Formats | almost all direct | per test: 15 passage, 5 match-list, 4 sequence, 3 multi-select statements (in three different sections), 23 direct |
| Explanations | 1–2 lines | every item: क्यों / अन्य विकल्प क्यों नहीं / मुख्य बिंदु |
| Order and keys | section-wise | key 13 / 12 / 13 / 12 (odd tests) and 12 / 13 / 12 / 13 (even tests); sequence answers never in A-B-C-D order; match patterns differ within a test; correct option never clearly the longest |

**Coverage ledger:** every target word, idiom, grammar example and literary example is recorded in `docs/blueprints/hindi_coverage.md` §C (C1 शब्द, C2 मुहावरे-लोकोक्तियाँ, C3 व्याकरण, C4 काव्यांग-साहित्य) and used once in the series. `hin_check.py` flags repeated targets (`REPEAT-TARGET`), sub-topic or stem overlap with earlier tests (`OVERLAP`) and over-long correct options (`LONGEST`). Every flag was cleared before shipping.

**Verification:** `validate_papers.py CUET --subject "Hindi"` — 0 parse errors, 0 wrong counts, 0 key/explanation mismatches, 0 runs > 3, 0 self-referential options, 0 within- or cross-paper duplicate stems, 0 passage gaps, 0 difficulty deviations; series key A 25.1%, B 24.9%, C 25.1%, D 24.9%.

**Known limits:** PYQs were analysed for pattern only; no question is copied. Classical example lines (दोहे, पद and well-known poems) are quoted as illustrations, as textbooks do. A few later छंद items (हरिगीतिका, बरवै, छप्पय, उल्लाला, गण) go slightly beyond the commonest school list because the core examples were already used.

### Tools added
- `docs/blueprints/hindi.md` (pattern, PYQ analysis, section plan, difficulty, formats, out-of-scope list) and `docs/blueprints/hindi_coverage.md` (passage themes, slot rotation, target ledgers).
- `tools/cuet_hindi/` — compact draft format and converter, checker, ledger marker, ship script, item patcher, text editor and series re-indexer; drafts of all 15 tests in `drafts/`.

## History (314) — revised to the CUET 2027 standard (completed 6 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `04ce0a9` (blueprint, coverage map, tools and pilot Test 1), `1a75466` (authoring scripts) … `a28414a` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | old papers, status `pending_revision` | **15 rewritten tests** (`CUET HISTORY TEST 1–15.json`), planned first in a coverage map; status `revised` |
| Paper structure | 50 compulsory | unchanged: 50 compulsory questions, 60 min, +5 / −1 (NTA pattern) |
| Syllabus | mixed, including dropped chapters | NCERT *Themes in Indian History* I–III, 12 in-syllabus themes (H1–H12); Kings and Chronicles, Colonial Cities and Partition left out as out of syllabus |
| Theme balance | uneven | Part I 17 / Part II 16 / Part III 17 in every test (quotas 5-4-4-4, 4-4-4-4, 4-4-5-4); the passage theme takes 5 |
| Source passage | rare | one original source-based passage × 5 questions per test, rotating across themes (e.g. Mohenjodaro drains, the Chishti khanqah, the Salt March, the Mahanavami, Bernier on crown ownership, the Deccan riots, Harappan craft production) |
| Difficulty | uneven | **8 easy / 32 medium / 10 hard in every test** |
| Formats | almost all direct | per test: 5 case-based, 7 match-list, 6 statements, 4 sequence, 28 direct (≥3 fill-in-the-blank, ≥2 incorrect-pair) |
| Explanations | 1–2 lines | every item: Why / Why not the others / Key point |
| Order and keys | uneven | key 13 / 12 / 13 / 12 (odd tests) and 12 / 13 / 12 / 13 (even tests); sequence answers never in A-B-C-D order; match patterns differ within a test; correct option never clearly the longest |

**Coverage ledger:** every answer fact is recorded per theme and test in `docs/blueprints/history_coverage.md` §C, and no fact is used more than twice in the series (in different tests and formats). `his_check.py` flags repeated targets (`REPEAT-TARGET`), sub-topic or stem overlap with earlier tests (`OVERLAP`), over-long correct options (`LONGEST`) and quota drift (`QUOTA`). Every flag was cleared before shipping.

**Verification:** `validate_papers.py CUET --subject "History"` — 0 parse errors, 0 wrong counts, 0 option-count errors, 0 key/explanation mismatches, 0 runs > 3, 0 self-referential options, 0 within- or cross-paper duplicate stems, 0 passage gaps, 0 difficulty deviations; series key A 25.1%, B 24.9%, C 25.1%, D 24.9%.

**Known limits:** PYQs were analysed for pattern only; no question is copied, and items close to known PYQs were avoided. Passages are original summaries of NCERT content, not quotations from sources. Later tests use some non-chronological sequences (north to south, west to east, story order, stupa parts) because the main chronologies were already used.

### Tools added
- `docs/blueprints/history.md` (pattern, PYQ analysis, theme quotas, difficulty, formats, out-of-scope list) and `docs/blueprints/history_coverage.md` (passage themes, sequence rotation, answer-fact ledgers).
- `tools/cuet_his/` — compact draft format and converter, checker, ledger marker, ship script, item patcher, match relabeller and series re-indexer; drafts of all 15 tests in `drafts/`.
## Mass Media (318) — revised to the CUET 2027 standard (completed 9 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `8067283` (blueprint, coverage map, tools and pilot Test 1), `f61a11b` (Test 2) … `8aaebdc` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | old papers, status `pending_revision` | **15 rewritten tests** (`CUET MASS MEDIA TEST 1–15.json`), planned first in a coverage map; status `revised` |
| Paper structure | 50 compulsory | unchanged: 50 compulsory questions, 60 min, +5 / −1 (NTA pattern) |
| Syllabus | mixed | CUET Mass Media / Mass Communication syllabus in 8 units (M1 communication, M2 journalism, M3 advertising and PR, M4 television, M5 radio, M6 cinema, M7 social media, M8 new media) |
| Unit balance | uneven | quotas M1 9, M2 9, M3 7, M4 5, M5 5, M6 6, M7 5, M8 4 in every test; the case unit takes 5, borrowing ±1 from a neighbour only where needed |
| Case set | rare | one original case × 5 questions per test, rotating across units (e.g. editing a flood report, a millet-snack launch, a farm radio show, *Manthan*, a cyberbullying incident, a food-recall crisis, a sting and paid-news complaint, a migrant workers' photo essay, Lumière–Flaherty–Grierson, a hashtag campaign for a lake, a TV serial's portrayal of a hill community) |
| Difficulty | uneven | **8 easy / 32 medium / 10 hard in every test** |
| Formats | almost all direct | per test: 5 case-based, 7 match-list (each in a different unit), 6 statements, 4 sequence, 28 direct (≥3 fill-in-the-blank, ≥2 NOT/wrongly) |
| Explanations | 1–2 lines | every item: Why / Why not the others / Key point |
| Order and keys | uneven | key 13 / 12 / 13 / 12 (odd tests) and 12 / 13 / 12 / 13 (even tests); sequence answers never in A-B-C-D order; match patterns differ within a test; correct option never clearly the longest |

**Coverage ledger:** every answer fact is recorded per unit and test in `docs/blueprints/mass_media_coverage.md` §C, and no fact is used more than twice in the series. `mm_check.py` flags repeated targets (`REPEAT-TARGET`), sub-topic or stem overlap with earlier tests (`OVERLAP`), over-long correct options (`LONGEST`) and quota drift. Every flag was cleared before shipping; one Test 10 sub-topic overlap found after shipping was renamed in `1570e4c`.

**Verification:** `validate_papers.py CUET --subject "Mass Media"` — 0 parse errors, 0 wrong counts, 0 option-count errors, 0 key/explanation mismatches, 0 runs > 3, 0 self-referential options, 0 within- or cross-paper duplicate stems, 0 passage gaps, 0 difficulty deviations; series key A 25.1%, B 24.9%, C 25.1%, D 24.9%.

**Known limits:** PYQs were analysed for pattern only; no question is copied. Cases are original scenarios, not real reports. Later tests draw some sequences from laws, court rulings and film or programme release order because the main media chronologies were already used twice.

### Tools added
- `docs/blueprints/mass_media.md` (pattern, PYQ analysis, unit quotas, difficulty, formats) and `docs/blueprints/mass_media_coverage.md` (case rotation, answer-fact ledgers).
- `tools/cuet_mm/` — compact draft format and converter, checker, ledger marker, ship script, item patcher, match relabeller and series re-indexer; drafts of all 15 tests in `drafts/`.

## Mathematics / Applied Mathematics (319) — revised to the CUET 2027 standard (completed 11 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `d8cf87e` (blueprint, coverage map, tools and pilot Test 1), `a7d3be2` (Test 2) … `aaa937e` (Test 15) on `main`, with fixes `07eb034` and `07dfc49`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | old 50-question papers, status `pending_revision` | **15 rewritten tests** (`CUET MATHEMATICS TEST 1–15.json`), planned first in a coverage map; status `revised` |
| Paper structure | 50 questions, one section | NTA pattern: **85 questions per file** — Section A (common) 15, Section B1 (Mathematics) 35, Section B2 (Applied Mathematics) 35; a candidate attempts A + either B1 or B2 = 50; 60 min, +5 / −1 |
| Syllabus | mixed, some out-of-scope items | gated to the NTA 2026 syllabus (latest published): 6 common units, 13 Mathematics units, 8 Applied Mathematics units; inverse-trig properties and composition left out |
| Unit balance | uneven | fixed quotas in every test: A — C1 4, C2 3, C3 3, C4 2, C5 2, C6 1; B1 — M1 3, M2 2, M3 2, M4 3, M5 4, M6 3, M7 4, M8 1, M9 3, M10 3, M11 3, M12 1, M13 3; B2 — AM1 6, AM2 4, AM3 8, AM4 5, AM5 3, AM6 3, AM7 4, AM8 2 |
| Difficulty | uneven | **A 2 / 10 / 3 and B1, B2 6 / 22 / 7 (easy / medium / hard) in every test**; Tests 11–15 carry the hardest items |
| Formats | almost all direct | per test: 7 match-list (A 1, B1 3, B2 3, each in a different unit, all with different answer patterns) and 10 statement items (A 2, B1 4, B2 4) alternating "correct" / "NOT correct"; the rest numerical or direct |
| Explanations | 1–2 lines | numericals: Given / Formula / Step-by-step / Common mistake / Key point; concept items: Why / Why not the others / Key point |
| Order and keys | uneven | key A 4/4/4/3, B1 and B2 9/8/9/9 (odd tests) and A 3/4/4/4, B1 and B2 9/9/8/9 (even tests); no answer run longer than 3; correct option never clearly the longest |

**Coverage ledger:** every test's items are listed per unit in `docs/blueprints/mathematics_coverage.md`, and `math_index.py` prints every earlier sub-topic per unit. `math_check.py` flags sub-topic or stem overlap with earlier tests (`OVERLAP`), over-long correct options (`LONGEST`), quota and difficulty drift. Close repeats of earlier NCERT-style items found by the checker were replaced before shipping (about 40 across Tests 13–15).

**Verification:** `validate_papers.py CUET --subject "Mathematics"` — 0 parse errors, 0 wrong counts, 0 option-count errors, 0 key/explanation mismatches, 0 runs > 3, 0 within- or cross-paper duplicate stems, 0 difficulty deviations; series key A 25.3%, B 24.6%, C 24.8%, D 25.3%.

**Known limits:** PYQs were analysed for pattern only; no question is copied. Some standard NCERT results (for example the King property integrals and the parallel-lines distance formula) appear in more than one test with different numbers.

### Tools added
- `docs/blueprints/mathematics.md` (pattern, PYQ analysis, unit quotas, difficulty, formats, out-of-scope list) and `docs/blueprints/mathematics_coverage.md` (host units for match and statement items, per-test item ledger).
- `tools/cuet_math/` — compact draft format and converter, checker, item index, ledger marker, ship script, item patcher and replacer, match relabeller and series re-indexer; drafts of all 15 tests in `drafts/`.

## Physics (322) — revised to the CUET 2027 standard (completed 11 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `ab6d6ca` (blueprint, coverage map, tools and pilot Test 1), `feaf2bd` (authoring tools), `488a8b2` (Test 2) … `f3263e5` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | old 50-question papers, status `pending_revision` | **15 rewritten tests** (`CUET PHYSICS TEST 1–15.json`), planned in a coverage map; status `revised` |
| Paper structure | 50 questions | NTA pattern: 50 questions, all compulsory; 60 min, +5 / −1; no calculator, so every number works by hand |
| Syllabus | mixed, some out-of-scope items | gated to the NTA 2026 syllabus (latest published), 9 units; radioactivity, Davisson–Germer, polarisation, eddy-current theory, LC oscillations, the cyclotron and Curie's law left out |
| Unit balance | uneven | fixed quotas in every test: P1 7, P2 6, P3 7, P4 6, P5 3, P6 9, P7 4, P8 5, P9 3 |
| Difficulty | uneven | **8 / 32 / 10 (easy / medium / hard) in every test**; Tests 11–15 carry the hardest multi-step items |
| Formats | almost all direct | per test: 6 match-list (each in a different unit, all with different answer patterns), 6 statement items alternating "correct" / "NOT correct", 3 sequence items (answer never A-B-C-D), at least 20 numericals; host units rotate in three sets across the series |
| Explanations | 1–2 lines | numericals and match/sequence: Given / Formula / Step / Common mistake / Key point; statement items: Why / Why not the others / Key point |
| Order and keys | uneven | key A 13 / B 12 / C 13 / D 12 (odd tests) and A 12 / B 13 / C 12 / D 13 (even tests); question order shuffled; no answer run longer than 3 |

**Coverage ledger:** every test's items are listed per unit in `docs/blueprints/physics_coverage.md`, and `phy_index.py` prints every earlier sub-topic and stem. `phy_check.py` flags quota, format, key and difficulty drift and sub-topic or stem overlap with earlier tests (`OVERLAP`); close repeats were reworded or replaced before shipping.

**Verification:** `validate_papers.py CUET --subject "Physics"` — 0 parse errors, 0 wrong counts, 0 option-count errors, 0 key/explanation mismatches, 0 runs > 3, 0 within- or cross-paper duplicate stems, 0 difficulty deviations; series key A 25.1%, B 24.9%, C 25.1%, D 24.9% (750 questions).

**Known limits:** PYQs were analysed for pattern only; no question is copied. Some standard NCERT results (for example rectifier pulse frequency and series capacitor sharing) appear in more than one test with different numbers or framing.

### Tools added
- `docs/blueprints/physics.md` (pattern, PYQ analysis, unit quotas, difficulty, formats, out-of-scope list) and `docs/blueprints/physics_coverage.md` (format host rotation, per-test item ledger).
- `tools/cuet_phy/` — compact draft format and converter, checker, item index, ledger marker, ship script, item patcher and replacer, match relabeller and series re-indexer; drafts of all 15 tests in `drafts/`.

## Political Science (323) — revised to the CUET 2027 standard (completed 12 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `ebe5e59` (blueprint, coverage map, tools and pilot Test 1), `ba7e4ec` (Test 2) … `9341188` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | old 50-question papers, status `pending_revision` | **15 rewritten tests** (`CUET POLITICAL SCIENCE TEST 1–15.json`), planned in a coverage map; status `revised` |
| Paper structure | 50 questions | NTA pattern: 50 questions, all compulsory; 60 min, +5 / −1 |
| Syllabus | mixed, some out-of-scope items | gated to the NTA 2026 syllabus (latest published) and the current NCERT books: *Politics in India since Independence* (9 units) and *Contemporary World Politics* (7 units); the Cold War Era and US Hegemony chapters, the Popular Movements chapter and Class 11 content left out |
| Unit balance | uneven | 25 questions from each book in every test; base quotas I1 3, I2 3, I3 2, I4 3, I5 3, I6 3, I7 3, I8 3, I9 2 and W1–W4 4, W5–W7 3; the passage unit takes 5 and other units of the same book give way in rotation |
| Difficulty | uneven | **8 / 32 / 10 (easy / medium / hard) in every test** |
| Formats | almost all direct | per test: one original 5-question passage (unit rotates across the series), 6 match-list (all with different answer patterns, none the identity), 6 statement items alternating "correct" / "NOT correct", 4 sequence items (answer never A-B-C-D) and 29 direct items, including at least 3 NOT, 3 reason and 2 fill-in-the-blank items; host units rotate test by test |
| Explanations | 1–2 lines | Why / Why not the others / Key point, resting on NCERT |
| Order and keys | uneven | key A 13 / B 12 / C 13 / D 12 (odd tests) and A 12 / B 13 / C 12 / D 13 (even tests); question order shuffled with each passage set kept together; no answer run longer than 3 |

**Coverage ledger:** every test's answer facts are recorded per unit by `mark_pol.py` in the ledger, and `pol_check.py` flags quota, key and difficulty drift, over-long correct options (`LONGEST`), sub-topic or stem overlap with earlier tests (`OVERLAP`) and answer facts already used twice (`REPEAT-TARGET`); flagged items were reworded or replaced before shipping. Test 15 carries 5 I3 questions (base 2) because its passage is on the early Five Year Plans, as the coverage map planned.

**Verification:** `validate_papers.py CUET --subject "Political Science"` — 0 parse errors, 0 wrong counts, 0 option-count errors, 0 key/explanation mismatches, 0 runs > 3, 0 within- or cross-paper duplicate stems, 0 missing passages, 0 difficulty deviations; series key A 25.1%, B 24.9%, C 25.1%, D 24.9% (750 questions).

**Known limits:** PYQs were analysed for pattern only; no question is copied. With only 16 short units, a few high-yield facts (for example the 1969 split and the Kyoto Protocol) are tested in more than one test from different angles; no answer fact is used more than twice.

### Tools added
- `docs/blueprints/political_science.md` (pattern, PYQ analysis, unit quotas, difficulty, formats, out-of-scope list) and `docs/blueprints/political_science_coverage.md` (passage rotation, format host rotation, per-unit topic lists).
- `tools/cuet_pol/` — compact draft format and converter, checker, answer-fact ledger and marker, ship script, item patcher, match relabeller and series re-indexer; drafts of all 15 tests in `drafts/`.

## Sanskrit (325) — revised to the CUET 2027 standard (completed 12 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `92a43f0` (blueprint, coverage map, tools and pilot Test 1), `69f6f56` (Test 2) … `c526fcc` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | old 50-question papers, status `pending_revision` | **15 rewritten tests** (`CUET SANSKRIT TEST 1–15.json`), planned in a coverage map; status `revised` |
| Paper structure | 50 questions | NTA pattern: 50 questions, all compulsory; 60 min, +5 / −1 |
| Syllabus | mixed, some out-of-scope items | gated to the NTA 2026 Sanskrit (325) syllabus (latest published): grammar (शब्दरूप, धातुरूप, सन्धि, समास, प्रत्यय, उपपदविभक्ति), language work, छन्द, अलङ्कार and history of Sanskrit literature |
| Unit balance | uneven | fixed quotas in every test: S1 शब्दरूप 6, S2 धातुरूप 6, S3 सन्धि 5, S4 समास 5, S5 प्रत्यय 6, S6 उपपद 4, S7 भाषिककार्य 5, S8 छन्द 4, S9 अलङ्कार 4, S10 साहित्य 5 |
| Difficulty | uneven | **8 / 32 / 10 (easy / medium / hard) in every test** |
| Formats | almost all direct | per test: one original 80–150-word Sanskrit passage with 5 questions (comprehension, कर्ता/विशेष्य/पर्याय/विलोम, vibhakti reason, प्रत्यय, and सन्धि in odd tests / समास in even tests; 15 different themes), 6 match-list (all with different answer patterns, none the identity), 6 statement items alternating "correct" / "NOT", 4 sequence items (paradigm order, metre and alaṅkāra lakṣaṇa reconstruction, literary order; answer never A-B-C-D) and 29 direct items, including at least 3 NOT/incorrect and 3 fill-in items; host units rotate test by test |
| Explanations | 1–2 lines | Hindi: क्यों / अन्य विकल्प क्यों नहीं / मुख्य बिंदु |
| Order and keys | uneven | key A 13 / B 12 / C 13 / D 12 (odd tests) and A 12 / B 13 / C 12 / D 13 (even tests); question order shuffled with the passage set kept together; no answer run longer than 3 |

**Coverage ledger:** every test's answer facts are recorded per unit by `mark_san.py` in `docs/blueprints/sanskrit_coverage.md`, and `san_check.py` flags quota, key and difficulty drift, short passages, over-long correct options (`LONGEST`), near-identical sub-topics or stems against earlier tests (`OVERLAP`, threshold 0.95 because paradigm items share templates by design) and answer facts already used twice (`REPEAT-TARGET`); flagged items were reworded or replaced before shipping, and stems that matched old unrevised papers were reworded when the validator caught them.

**Verification:** `validate_papers.py CUET --subject "Sanskrit"` — 0 parse errors, 0 wrong counts, 0 option-count errors, 0 key/explanation mismatches, 0 runs > 3, 0 within- or cross-paper duplicate stems, 0 missing passages, 0 difficulty deviations; series key A 25.1%, B 24.9%, C 25.1%, D 24.9% (750 questions).

**Known limits:** PYQs were analysed for pattern only; no question is copied. Metre and alaṅkāra lakṣaṇa-order items reuse each classical definition at most twice, and a few high-yield literature facts (for example Bhavabhūti's plays and the Bṛhattrayī) appear in more than one test from different angles; no answer fact is used more than twice.

### Tools added
- `docs/blueprints/sanskrit.md` (pattern, PYQ analysis, unit quotas, difficulty, formats, out-of-scope list) and `docs/blueprints/sanskrit_coverage.md` (passage themes, format host rotation, answer-fact ledgers).
- `tools/cuet_san/` — compact draft format and converter, checker, answer-fact ledger and marker, ship script, item patcher, match relabeller and series re-indexer; drafts of all 15 tests in `drafts/`.

## IAT New Tests 12 and 13 — authored review drafts (3 Nov 2026)

- Authored 120 questions from reserved syllabus slots. Each paper has 15 questions per subject, editorial tiers 9/42/9, balanced 15-per-letter keys, detailed WHY and distractor analyses, and displayed derivations for all Mathematics/Physics items.
- Drew and registered 11 question-bearing figures in Test 12 and 10 in Test 13. The 31- and 30-page review PDFs contain 60 questions and 60 solutions each, with source/delivery/PDF/image hashes, no empty pages, no overfull text and no missing glyphs. Expanded all one-sentence `Why` sections and replaced pooled distractor rationales with individual errors.
- Replaced text-similar combustion, divisibility, monotonicity, trigonometry and lattice-path tasks; documented residual method-distinct overlap-screen candidates. Updated the 25-test register to 780 authored review-draft slots and 720 reservations, and merged independent `main` Economics/Computer Science changes into this IAT branch without changing `main`.
- See `IISER/review/IAT_NEW_TESTS_12_13_REVIEW_NOTES.md` for 30 Mathematics task checks and remaining independent academic, timed-student and 2027-notification review gates.


## IAT milestone corrections — 3 November 2026

Branch `fix-iat-milestone-15` applies the documented Tests 1–15 audit repairs to canonical JSON at fixed IDs: scientific assumptions, listed-syllabus replacements, repeated task angles, demand, detailed explanations and figures. The correction report, item change ledger, source-bound checks and rebuilt review PDFs/HTML are in `IISER/review/milestone15_fixes/`. Strict validation covers all 900 items; arithmetic probes are targeted author-side checks, not an independent 900-answer certificate. The bank remains pending hidden-key academic and timed review. `main` and earlier test branches are preserved.


## IAT Tests 16–17 — 5 November 2026

Completed two original 60-item review drafts on iat-tests-16-17, based on corrected-bank commit 1de7c68. Added 19 exact scientific diagrams, detailed WHY and individual alternative explanations, displayed Mathematics/Physics working, 30 recent-PYQ Mathematics comparisons and 84 calculation checks. Replaced repeated/unlisted planning seeds, retained the 9/42/9 editorial mix and preserved all previous 900 canonical items. A remote content checkpoint preceded final visual-review and documentation changes. Review notes record verification and pending independent academic/timed review. Main and earlier branches remain unchanged.

## 5 November 2026 — Tests 18–19 and full-plan tracking

Authored 120 items, 21 exact diagrams and detailed worked solutions on iat-tests-18-19; saved remote checkpoint 9d60db0 before long delivery checks. Replaced a repeated two-axis circle task with centre/chord/tangent reasoning and a routine yield task with isotope abundance. All 85 numerical probes pass. Updated all 1,500 plan rows, wrote 360 literal future angle briefs and a 640-entry official-scope checklist with owners and honest evidence/alignment states. Repaired a header/footer-only page and strengthened the exporter to reject such pages. Previous 1,020 canonical items remain unchanged. Final academic and timed review remain pending.

## 5 November 2026 — IAT Tests 20–21

Authored 120 fixed-ID review items with detailed WHY, labelled distractor analysis, explicit Mathematics/Physics derivations and 15 exact figures. All 21 papers / 1,260 questions pass structural validation; the previous 1,140 items are unchanged. Passed 86 source-bound calculation probes and recorded 30 item-level Mathematics PYQ comparisons. Replaced near-repeated tangent, common-root and midpoint-chord drafts; removed a beyond-NCERT colour mechanism. Updated all 1,500 plan slots and 640 scope phrases, distinguishing 143 material evidence aspects from remaining future backstops. Final PDFs, offline HTML, manifests and recovery bundle accompany the drafts. Local branch iat-tests-20-21: GitHub rejected the supplied transient token, so remote preservation is not complete. Main and older branches were not overwritten. Independent academic and timed review remain pending.

## 6 November 2026 — restored workspace and IAT Tests 22–23

Restored the existing repository and all 75 saved draft rows, then completed 120 individually authored questions on iat-tests-22-23. Added 17 exact scientific figures, full causal explanations and displayed Mathematics/Physics derivations. Direct comparison rejected ten near-repeated drafts before freeze; the edit log preserves their replacements and explicit pre-freeze option exchanges. Passed 105 source-bound numerical probes and 30 Mathematics/PYQ comparisons. All 23 papers / 1,380 questions pass structural validation; the earlier 1,260 canonical questions remain byte-unchanged. Reconciled the 1,500-slot CSV/TSV and 640-entry scope checklist: 291 entries have limited material-aspect evidence with 316 links; 349 retain future backstops. Corrected several overbroad scope mappings and revised Test 24 P59. PDFs and offline HTML were rebuilt after final replacements. GitHub rejected the old credential; recovery bundle/package preserve unpublished Tests 20–23. Main and earlier branches were not overwritten. Independent academic and timed review remain pending.

## 6 November 2026 — IAT Tests 24–25 and completed draft index

Authored 120 fixed-ID questions on iat-tests-24-25, checkpointing each subject pair before assembly. Added 18 exact figures, detailed explanations, explicit numerical working and 30 recent-PYQ Mathematics comparisons. Replaced repeated reservation angles, rejected a statistical error-analysis draft under the printed Units scope, and strengthened two hard Biology experiments. Passed 127 exact calculation/enumeration probes, all 25 structural checks and final PDF/HTML source bindings. Previous 1,380 questions are byte-unchanged. Updated the all 25 index and 1,500-slot plan;544 links evidence aspects of 412 of 640 printed scope entries, while 228 remain honestly unmapped for whole-bank review. PDFs 43/44pages were visually inspected. Noninteractive clean-URL push failed for missing authentication; recovery bundle preserves unpublished Tests 20–25. Academic, timed and exhaustive scope review remain pending.

## 7 November 2026 — verified IAT25 remote preservation

Pushed iat-tests-24-25 successfully using transient authentication and a clean remote URL. GitHub exactly matched authored-content checkpoint ba97e4b5abad20e6ad5e8539ce3be8608d6c880c. This preserves the previously unpublished Tests20–25 commits and all25 authored drafts on the named branch. Updated current continuity and preservation metadata while retaining historical failure records. No test question, option, figure, PDF or syllabus mapping changed. Main and earlier branches were not force-pushed or deleted. Academic, timed and residual-scope review remain pending.


## 7 November 2026 — integrate all 25 IAT review drafts into main

Merged the completed IAT series from iat-tests-24-25 into the current main history, retaining the newer CUET subject revisions and both work logs. All 25 canonical papers, 1,500 questions, review deliveries, figures, 25-test plan and audit evidence are preserved. Canonical paper content is unchanged by this integration. Academic, timed-student and residual-scope review remain pending. The separate IAT notes-agent instructions are outside the repository and excluded from this commit.

## Agriculture (302) — new CUET 2027 series (completed 12 Nov 2026)

**Author:** Claude (Claude Code), for Nithish Reddy. **Commits:** `3b1ad34` (blueprint, coverage map and tools), `2987831` (Test 1) … `1f51e16` (Test 15) on `main`, plus the final commit for this entry.

### What changed
| Item | Before | After |
|---|---|---|
| Tests | none (syllabus only) | **15 new tests** (`CUET AGRICULTURE TEST 1–15.json`) and `series_index.json`; status `revised` |
| Paper structure | — | NTA pattern: 50 questions, all compulsory; 60 min, +5 / −1 |
| Syllabus | — | gated to the NTA 2026 Agriculture (302) syllabus: Unit I Agrometeorology, Genetics & Plant Breeding, Biochemistry and Microbiology; Unit II Livestock Production; Unit III Crop Production; Unit IV Horticulture |
| Unit balance | — | sub-unit quotas per test (U1 16 / U2 10 / U3 16 / U4 8: A1 3, A2 5, A3 3, A4 3, A5 2; L1 3, L2 4, L3 2, L4 1; C1 3, C2 4, C3 3, C4 2, C5 4; H1 3, H2 3, H3 2); the passage's sub-unit carries 5 items and other sub-units shift by at most one |
| Difficulty | — | **8 / 32 / 10 (easy / medium / hard) in every test**; hard = 2 passage inference/calculation items, 4 sequences, 2 statement sets, 1 match, 1 calculation |
| Formats | — | per test: one original ~200–240-word passage with 5 questions on 15 different themes (rice, cattle, jam/jelly, semi-dwarf wheat, Soil Health Card/INM, layer flock, drip/sprinkler, monsoon advisories, mango, millets, biofertilizers, market milk, *Phalaris minor* resistance, composite fish culture, conservation/precision farming), 6 match-list (all with different answer patterns, none the identity), 6 statement items alternating "correct" / "NOT", 4 sequence items (answer never A-B-C-D) and 29 direct items, including at least 3 NOT, 2 fill-in and 2 "Why" items and one worked calculation |
| Explanations | — | Why / Why not the others / Key point; calculations show numbered steps |
| Order and keys | — | key A 13 / B 12 / C 13 / D 12 (odd tests) and A 12 / B 13 / C 12 / D 13 (even tests); question order shuffled with the passage set kept together; no answer run longer than 3 |

**Coverage ledger:** every test's answer facts are recorded per sub-unit by `mark_agri.py` in `docs/blueprints/agriculture_coverage.md`; `agri_check.py` flags quota, key and difficulty drift, over-long correct options (`LONGEST`), near-identical sub-topics or stems against earlier tests (`OVERLAP`), repeated match patterns and identity matches. From Test 10 onward the full ledger was also read by hand before writing, and 26 Test 10 drafts that repeated earlier facts in new wording were replaced before shipping.

**Verification:** `validate_papers.py CUET --subject "Agriculture"` — 0 parse errors, 0 wrong counts, 0 option-count errors, 0 key/explanation mismatches, 0 runs > 3, 0 within- or cross-paper duplicate stems, 0 missing passages, 0 difficulty deviations; series key A 25.1%, B 24.9%, C 25.1%, D 24.9% (750 questions).

**Known limits:** PYQs were analysed for pattern only; no question is copied. A few high-yield facts (for example the Indian major carps, Phalaris in wheat, soil types) recur across tests from different angles. Statistics that change year to year (leading states, production ranks) were kept to long-stable facts but should be rechecked before CUET 2027. Explanations have not yet been proofread by a subject teacher.

### Tools added
- `docs/blueprints/agriculture.md` (pattern, PYQ analysis, quotas, difficulty, formats) and `docs/blueprints/agriculture_coverage.md` (passage themes, slot rotation, answer-fact ledgers).
- `tools/cuet_agri/` — compact draft format and converter, checker, ledger and marker, ship script, item patcher, match relabeller and series re-indexer (only `build_agri.py` is tracked, since `.gitignore` excludes `*.py`); drafts of all 15 tests in `drafts/`.
