# OurMocks — CUET UG master audit report

**Date:** 27 Oct 2026. **Covers:** 15 subjects, 375 papers, 18,750 questions as they stand in `CUET/`.
**This report replaces** `2026-10-27-cuet-audit.md` (kept for history). Raw numbers are in `metrics.json` (re-run with `python3 audit_papers.py CUET --json docs/audit/metrics.json`).

**Sources used:**
- 2026 NTA syllabus PDFs in `Hermes folder/`
- the NTA Information Bulletin
- NTA's official 2024 and 2025 Accountancy papers, analysed for pattern
- the rulebook (`docs/instructions/CUET_Instructions.md`)
- `validate_papers.py`, `audit_papers.py`
- a hand (SME) check of 66 randomly sampled questions across all 15 subjects

---

## 1. Overall verdict

| Area | Standard we want | Where we are | Verdict |
|---|---|---|---|
| Structure (50 Q, 4 options, valid JSON, no duplicates, key matches explanation) | 100% clean | 100% clean in all 15 subjects (`validate_papers.py`) | ✅ Pass |
| Difficulty mix | 8 easy / 32 medium / 10 hard per paper | Old ramp (Level 1 = 35/12/3 … Level 10 = 3/15/32); **375/375 papers off target; 5,811 questions to replace** | ❌ Fail |
| Difficulty labels | Label matches real CUET difficulty | Unreliable: recall questions tagged "hard", 2-step questions tagged "easy" (all sampled subjects) | ❌ Fail |
| CUET question formats | About 30% match-list / statements / assertion-reason / sequence (NTA 2024–25) | 0–3% in all domain subjects; English and Hindi about 20% | ❌ Fail |
| Syllabus fit | 100% within the 2026 NTA syllabus | Out-of-syllabus clusters in Accountancy, Biology, Chemistry, Computer Science, Economics, Physics, Mass Media (§4) | ❌ Fail |
| Accuracy | 0 wrong keys or concepts | Sample: 5 defects in 66 questions (about 8%), 2 already fixed (§5) | ❌ Fail |
| Explanations | Structured. Math/Physics/Chemistry need step-by-step working. Explain why the wrong options are wrong | Average 78–178 characters (1–2 lines); **0% structured**; under 2% address the wrong options | ❌ Fail |
| Option quality | Plausible, similar-length distractors | Correct answer is clearly the longest option in 30–73% of questions in 9 subjects; obviously absurd distractors in Geography and Mass Media | ❌ Fail |
| Answer-key pattern | Balanced, no long runs | Balanced overall, but **Economics and History have runs of 10–15 identical answers** | ❌ Fail (2 subjects) |
| Metadata | True sources, topic + sub-topic filled | Fake PYQ references in 9 subjects; wrong syllabus file names in 6; Math has 797 empty sub-topics | ❌ Fail |
| Display readiness | Line breaks, KaTeX/mhchem, options prefixed "A) " | Works if the app keeps `\n`, renders KaTeX + mhchem, and doesn't add its own A–D letters. Math and Physics use Unicode instead of KaTeX | ⚠️ Partial |

**Bottom line:** the files are technically clean, but the content is not yet at CUET standard. Every subject needs four things: new questions to reach the right difficulty and question types, removal of out-of-syllabus content, rewritten explanations, and corrected metadata.

---

## 2. Subject scorecard

R = needs major work, A = needs moderate work, G = acceptable.

| Subject | Code | Syllabus PDF | Difficulty mix | CUET formats | Syllabus fit | Accuracy (sample) | Explanations | Options | Key pattern | Metadata | Priority |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Accountancy | 301 | ✅ | R | R (1%) | R: insolvency (29 Q) is excluded by the syllabus; Unit V AFS and its optional alternative CAS are both compulsory | R: 2/16 wrong (fixed) | A: 275 of 610 numericals have no working | G | G | A | **1** |
| Physics | 322 | ✅ | R | R (0%) | R: transistors and logic gates (≈30 Q) are not in the 2026 syllabus | G: 5/5 | **R: average 78 characters; 330 of 344 numericals are one-liners** | G | G | A | **2** |
| Chemistry | 306 | ✅ | R | R (2%) | A: equivalent conductivity (2 Q) | G: 5/5 | A: average 178 characters, no steps | A (39% longest) | G | A (fake PYQ ref) | **3** |
| Mathematics | 319 | ❌ missing | R | R (0%) | ? (no PDF); 50 Q have no topic | **R: 1/4 has two correct options** | **R: average 97 characters, no steps** | G | G | R (797 empty sub-topics, wrong syllabus name) | **4** |
| Biological Science | 304 | ✅ | R | R (0%) | **R: complement system (22 Q), next-gen sequencing (5 Q) beyond NCERT** | R: 2/5 out of syllabus | R: average 174 characters, 1 line | R (30% longest) | G | A | 5 |
| Computer Science | 308 | ✅ | R | R (0%) | **R: normalisation/BCNF (19 Q), subnetting and linked lists (41 Q), transactions** | A | R: 81% under 150 characters | G | G | A | 6 |
| Economics | 309 | ✅ | R | R (1%) | A: Hicksian decomposition (4 Q) | A: 1/5 out of syllabus | A | R (38% longest) | **R: runs of 15 identical answers in 11 papers** | A | 7 |
| History | 314 | ✅ | R | R (3%) | G | G: 4/4 | R: 69% under 150 characters | R (34% longest) | **R: runs of 13 identical answers in 12 papers** | A (theme not recorded; fake PYQ ref) | 8 |
| Political Science | 323 | ✅ | R | R (0%) | G | G: 4/4 | G: average 176 characters | R (37% longest) | G | A (fake PYQ ref) | 9 |
| Geography | 313 | ✅ | R | R (0%) | G | A: absurd distractors make questions trivial | R: 68% under 150 characters | R (35% longest) | G | A (fake PYQ ref) | 10 |
| Mass Media | 318 | ✅ | R | R (1%) | A: "Film Theory" (14 Q) not in syllabus | A | A | **R: correct is the longest option in 73%, plus 75 "(or …)" giveaways and absurd distractors** | G | A (fake PYQ ref) | 11 |
| General Test | 501 | ❌ missing | R | n/a (GK/quant/reasoning) | ? (no PDF); current affairs need a date check | G: 4/4 | A | G | G | R (wrong syllabus and PYQ names) | 12 |
| English | 101 | ❌ missing | R | A (19%) | ? (no PDF) | A: "hard" items are trivially easy | **R: 80 vacuous ("'X' means abusive")** | G | G | R (fake PYQ files) | 13 |
| Hindi | 102 | ❌ missing | R | A (21%) | ? (no PDF); only 4 literature questions | A: ambiguous antonym options | **R: average 85 characters, 96% under 150** | R (43% longest) | G | R | 14 |
| Sanskrit | 325 | ✅ | R | R (2%) | A: grammar-heavy; check passage/literature share | G: 4/4 | R: 100% under 150 characters | A | G | A (fake PYQ ref) | 15 |

The priority order puts first the subjects where students are most likely to learn something wrong (out-of-syllabus content, errors, missing worked solutions in numerical subjects), and the subjects whose PYQs and syllabi are already in hand.

---

## 3. Measured metrics per subject

### 3a. Difficulty (all 25 papers per subject)

The target per subject is 200 easy / 800 medium / 250 hard.

| Subject | Easy | Medium | Hard | Questions to replace |
|---|---|---|---|---|
| Accountancy | 449 | 465 | 336 | 398 |
| Biological Science | 449 | 465 | 336 | 398 |
| Chemistry | 390 | 470 | 390 | 373 |
| Computer Science | 449 | 465 | 336 | 398 |
| Economics | 399 | 470 | 381 | 385 |
| English | 400 | 472 | 378 | 387 |
| General Test | 448 | 466 | 336 | 398 |
| Geography | 399 | 473 | 378 | 381 |
| Hindi | 401 | 463 | 386 | 396 |
| History | 399 | 473 | 378 | 381 |
| Mass Media | 399 | 475 | 376 | 379 |
| Mathematics | 395 | 473 | 382 | 386 |
| Physics | 447 | 468 | 335 | 396 |
| Political Science | 399 | 475 | 376 | 379 |
| Sanskrit | 396 | 479 | 375 | 376 |
| **Total** | **6,219** | **7,052** | **5,479** | **5,811** |

Per paper, every subject currently follows the old ramp: Level 1 ≈ 35/12/3, Level 5 ≈ 15/22/13, Level 10 ≈ 3/15/32.

### 3b. Explanations, options and patterns

| Subject | Avg explanation length (chars) | Explanations under 150 chars | Numerical Qs / without working | Explain wrong options | Correct = clearly longest option | Longest same-answer run | CUET formats* | Passage/case | Templated stems | Very short stems | Empty sub-topic |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Accountancy | 166 | 43% | 610 / 275 | 4 | 10% | 3 | 1% | 0% | 24 | 37 | 0 |
| Biological Science | 174 | 41% | 10 / 6 | 8 | 30% | 4 | 0% | 0% | 0 | 56 | 0 |
| Chemistry | 178 | 23% | 117 / 18 | 17 | 39% | 3 | 2% | 0% | 0 | 3 | 0 |
| Computer Science | 112 | 81% | 110 / 83 | 6 | 13% | 5 | 0% | 0% | 0 | 112 | 0 |
| Economics | 167 | 37% | 109 / 52 | 9 | 38% | **15** | 1% | 0% | 0 | 29 | 0 |
| English | 111 | 83% | 8 / 8 | 9 | 12% | 6 | 19% | 33% | 132 | 42 | 0 |
| General Test | 164 | 47% | 180 / 114 | 17 | 7% | 4 | 1% | 0% | 31 | 39 | 0 |
| Geography | 141 | 68% | 53 / 39 | 14 | 35% | 1 | 0% | 0% | 0 | 0 | 0 |
| Hindi | 85 | 96% | 0 / 0 | 0 | 43% | 1 | 21% | 24% | 253 | 19 | 0 |
| History | 138 | 69% | 28 / 16 | 20 | 34% | **13** | 3% | 0% | 0 | 0 | 0 |
| Mass Media | 169 | 22% | 74 / 7 | 9 | **73%** | 1 | 1% | 0% | 0 | 0 | 0 |
| Mathematics | 97 | 89% | 142 / 130 | 0 | 3% | 5 | 0% | 0% | 53 | 306 | 797 |
| Physics | 78 | 94% | 344 / 330 | 0 | 4% | 4 | 0% | 0% | 49 | 30 | 0 |
| Political Science | 176 | 17% | 138 / 18 | 7 | 37% | 1 | 0% | 0% | 0 | 0 | 0 |
| Sanskrit | 87 | 100% | 0 / 0 | 0 | 26% | 1 | 2% | 0% | 151 | 80 | 0 |

\*Match-list + statement combinations + assertion-reason + sequence (automatic detection, approximate). No explanation in any subject is multi-line or structured. A "longest same-answer run" of 1 means the key never repeats a letter twice in a row, which is also an unnatural pattern.

### 3c. CUET pattern benchmark (from NTA's official Accountancy papers, 2024 and 2025)

| Format | NTA 2024 | NTA 2025 | Our Accountancy |
|---|---|---|---|
| Match List-I / List-II (table) | 10% | several per paper | 0% |
| Choose correct statements (A)–(D) | 12% | frequent | 0% |
| Sequence / order | 12% | present | 1% |
| Numerical (1–3 steps) | 38% | about 35% | 49% |
| Direct concept | 30% | remainder | 51% |

From 2025 onward the paper is 50 compulsory questions, 60 min, +5/−1, in English and Hindi. In Accountancy, Unit V Analysis of Financial Statements and the optional Computerised Accounting unit are alternatives. Other subjects follow the same family of formats. Science subjects add assertion-reason; humanities add chronology and source/case-based questions; languages are reading-comprehension heavy.

---

## 4. Out-of-syllabus clusters found (to remove or replace)

| Subject | Content | Approx. Qs | Why it's out |
|---|---|---|---|
| Accountancy | Insolvency of a partner / Garner v Murray | 29 | The 2026 syllabus explicitly excludes "insolvency of a Partner" |
| Accountancy | Analysis of Financial Statements **and** Computerised Accounting both compulsory | 397 | The syllabus lists Computerised Accounting as "Optional to Unit V"; NTA gives a choice |
| Physics | Transistors, logic gates (NAND/NOR) | ≈30 | Removed from the rationalised syllabus; the 2026 PDF only has semiconductors and rectifiers |
| Biological Science | Complement system / membrane attack complex | 22 | Beyond NCERT Class 12 (immunity covers innate/acquired immunity and antibodies only) |
| Biological Science | Next-generation sequencing (Illumina) | 5 | Not in NCERT |
| Computer Science | Normal forms (2NF/3NF/BCNF), transactions | 19+ | Not in the 2026 CS syllabus (DB concepts, SQL, Pandas only) |
| Computer Science | Subnetting, linked lists | ≈41 | Not in the syllabus (networks = types, devices, topologies, protocols, security) |
| Economics | Hicksian price-effect decomposition | 4 | Beyond the NCERT microeconomics syllabus |
| Chemistry | Equivalent conductivity | 2 | Removed in the rationalised NCERT |
| Mass Media | Film theory | 14 | Not in the 2026 syllabus |

This list comes from keyword scans plus sampling. The full per-question syllabus check happens during each subject's pass.

## 5. Defects found in the sample (66 questions checked by hand)

| Subject | Question | Problem | Status |
|---|---|---|---|
| Accountancy | P1 goodwill premium | Taught the wrong treatment (unpaid goodwill credited to partners) | ✅ Fixed |
| Accountancy | P1 re-issue of forfeited shares | Stem missing "forfeited"; duplicate of a Paper 8 question | ✅ Replaced with a statements question |
| Mathematics | P20 (Level 10B), shortest distance between skew lines | Options A `1/√30` and D `√30/30` are the same value, so there are two correct answers | Open |
| Biological Science | P20 (Level 10B), complement / next-gen sequencing | Out of syllabus | Open |
| Hindi | P22, antonym of 'सत्कार' | Three options are acceptable antonyms; the correct option carries "(या निरादर)" as a giveaway | Open |
| English | P22 "Choose the correct word … _____ their essays" | Tagged hard but trivially easy; explanation is "'submit' is the correct word" | Open |
| Mathematics | P17, \|x − 2\| at x = 2 | Tagged hard, but it is a standard easy question | Open |

---

## 6. Explanation standard (applies to every rewritten question)

The `explanation` stays a single string, so the app's schema doesn't change. Sections are separated by line breaks (`\n`), and formulas use KaTeX/mhchem.

**Concept questions** (Biology, History, Political Science, Geography, Economics theory, Computer Science theory, Mass Media, languages):

```
Answer: (C) <answer text>
Why: <2–4 sentences on the concept, linked to the syllabus unit/NCERT idea>
Why not the others:
(A) <one line>
(B) <one line>
(D) <one line>
Key point: <one-line takeaway / exam tip>
```

**Numerical questions** (step-by-step is mandatory for Mathematics, Physics and Chemistry, and also used for Accountancy, Economics and General Test quant):

```
Given: <data>
Concept/Formula: \( … \)
Step 1: …
Step 2: …
Step 3: …
Answer: <value with unit> → (C)
Common mistake: <the slip that leads to a distractor, e.g. option B>
```

**Language questions** (English, Hindi, Sanskrit): `Answer`, then the meaning or rule (for Sanskrit the sūtra, for Hindi the vyākaraṇa rule), why the others are wrong, and a usage example.

---

## 7. Fix plan per subject

Each subject goes through these steps in order:

1. **Syllabus pass:** remove or replace the out-of-syllabus questions (§4) and check the topic spread against the units.
2. **Accuracy pass:** check every answer and its explanation; fix wrong keys, ambiguous options and giveaways.
3. **Difficulty and format pass:** re-grade the labels, then write new questions to reach 8/32/10 per paper with about 30% CUET formats, with deeper questions at higher levels. Templated, very short and out-of-syllabus questions are replaced first.
4. **Explanation pass:** rewrite all 1,250 explanations to the §6 standard.
5. **Options and key pass:** make distractors plausible and of similar length; shuffle option order (tracking the correct answer) to break answer runs.
6. **Metadata pass:** real `syllabus_source`, `past_paper_reference: null` unless real, consistent `topic`, filled `sub_topic`.
7. **Validate** (`validate_papers.py` + `audit_papers.py`), **commit and push** so the platform can clone it.

**Effort per subject:** about 380–400 new questions plus 1,250 rewritten explanations. Expect several sessions per subject. Subjects are pushed one at a time, so the platform always has a consistent set.

## 8. Needed from you

| Item | Why |
|---|---|
| Syllabus PDFs for **English (101), General Test (501), Hindi (102), Mathematics (319)** | They're not in `Hermes folder/`. Rulebook rule 6 says not to write questions for a subject without its syllabus. |
| Decision: **Accountancy Unit V**, both compulsory, or NTA-style choice between AFS and CAS | Changes the structure of all 25 Accountancy papers |
| Confirm the **explanation format** in §6 (single formatted string) | It applies to all 18,750 explanations, and the app must keep line breaks |
