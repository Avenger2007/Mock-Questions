# OurMocks — CUET UG audit against syllabus, pattern and difficulty (27 Oct 2026)

**Scope:** all 15 subjects, 375 papers, 18,750 questions.
**Method:**
1. `audit_papers.py` takes mechanical measurements of every question (raw numbers in `metrics.json`).
2. Each subject's topic labels are compared with the units in its 2026 NTA syllabus PDF.
3. The real CUET pattern was benchmarked from NTA's 2024 and 2025 Accountancy papers. These were analysed in place, not collected (rule 9).
4. A hand check of a sample of Accountancy questions.

Re-run the measurements with `python3 audit_papers.py CUET --json docs/audit/metrics.json`.

## 1. Headline findings

1. **Question formats don't match CUET.** In real CUET papers, roughly a third of the questions are structured formats: Match List-I/List-II, "choose the correct statements (A)(B)(C)(D)", sequencing, and assertion-reason. Our domain subjects have **0–2%** of these. Every domain subject is almost entirely single-line direct or numerical questions. This is the single biggest gap from CUET standard.
2. **The difficulty mix is off target in all 375 papers.** Against the new 8/32/10 standard, **5,811 questions** must be replaced (this needs new questions, not relabelling).
3. **Difficulty labels are unreliable.** In the Accountancy sample, one-line recall questions were tagged "hard" (for example, the journal entry for issuing debentures at par), and two-step numericals were tagged "easy". Labels must be re-graded against the PYQ benchmark before rewriting starts. Otherwise the 8/32/10 count is meaningless.
4. **Accuracy:** the Accountancy hand check found 2 defective questions out of 16, and both are now fixed. One taught a wrong concept: it said the unpaid goodwill is credited to the old partners. The other had a stem missing the word "forfeited", and was also a duplicate of a Paper 8 question. A full SME pass per subject is needed. A 12% error rate in a sample is too high to assume the rest is clean.
5. **Repeated templates** (same problem with different numbers or words) are still present: English 132, Hindi 253, Sanskrit 151, Mathematics 53, Physics 49, General Test 31, Accountancy 24. For example, Accountancy has 10+ "amount transferred to Capital Reserve after re-issue" numericals. Language vocabulary frames ("opposite in meaning to 'X'") are a real CUET format and lower priority. Number-swapped numericals break rulebook rule 7.
6. **Paper provenance metadata is false.** `past_paper_reference` cites PYQ files that never existed (English, General Test, Chemistry, Geography, Hindi, History, Mass Media, Political Science, Sanskrit). `syllabus_source` names files that don't exist (English, General Test, Hindi, Mathematics, parts of Biology, CS and Physics).

## 2. CUET pattern benchmark

**Measured from the official NTA Accountancy papers:**

| Format | 2024 NTA paper | 2025 NTA paper (sampled) | Our Accountancy |
|---|---|---|---|
| Match List-I / List-II | 10% | present (several per paper) | **0%** |
| Choose correct statements (A)–(D) | 12% | frequent | **0%** |
| Sequence / order | 12% | present | 1% |
| Numerical | 38% | about 35% | 49% |
| Direct concept | 30% | remainder | 51% |

Stems are short, and options are close and conceptual. Numericals are usually 1–2 steps, and harder ones combine 2–3 adjustments. 2025 onward: 50 compulsory questions, 60 min, +5/−1, bilingual.

**Other subjects** (based on general knowledge of 2023–2025 CUET papers, to be verified per subject during the audit):

| Group | Formats to include (aim for about 30% non-direct per paper) |
|---|---|
| Sciences (Physics, Chemistry, Biology) | Assertion-reason, match-list, statement combinations, 1–3 step numericals; direct NCERT lines are common at the easy level |
| Humanities (History, Political Science, Geography) | Chronological sequence, match-list (events/leaders/places), statement combinations, source/case-based passages, assertion-reason |
| Commerce (Accountancy, Economics) | As in the table above, plus graph/schedule interpretation in Economics |
| Computer Science, Mass Media | Code-output and SQL-output questions, match-list of terms, statement combinations |
| Mathematics | Single-concept MCQs, shortcut-friendly numericals, a few statement-based ones; no long derivations |
| Languages (English, Hindi, Sanskrit) | Reading comprehension (factual, narrative, literary), rearrangement, vocabulary, grammar, match-list |
| General Test | GK/current affairs, quant (Class 8–10 level), logical and analytical reasoning |

### What easy, medium and hard should mean (all subjects)

- **Easy:** one fact or one step, taken straight from an NCERT line.
- **Medium:** applying a concept, a 2-step numerical, a match-list or statements question where you need to know 3–4 facts.
- **Hard:** combining concepts, 3+ steps or several adjustments, assertion-reason with a subtle link, case/data interpretation, or closely matched distractors.

Levels 1→10 go deeper within each tier (rulebook rule 5).

## 3. Per-subject results

E/M/H is the current total across 25 papers. The target is 200 / 800 / 250.

| Subject | E / M / H | Rewrites | CUET-style formats* | Templated | Syllabus coverage | Other |
|---|---|---|---|---|---|---|
| Accountancy | 449 / 465 / 336 | 398 | 1% | 24 | All 6 units covered. ⚠️ Unit V "Analysis of Financial Statements" and its *optional alternative* "Computerised Accounting System" are both compulsory in every paper; NTA offers a choice | 37 very short stems; 2 errors fixed |
| Biological Science | 449 / 465 / 336 | 398 | 0% | 0 | All 5 units covered | Topic labels inconsistent ("&" vs "and"); 56 very short stems |
| Chemistry | 390 / 470 / 390 | 373 | 2% | 0 | All 10 units, exactly 125 questions each ✅ | Best-formatted (KaTeX + mhchem) |
| Computer Science | 449 / 465 / 336 | 398 | 0% | 0 | Covered | 21 different topic spellings; 112 very short stems; 52 short explanations (from audit_report.md) |
| Economics | 399 / 470 / 381 | 385 | 0% | 0 | Micro and Macro covered (both are in the 2026 syllabus) | 30+ topic spellings |
| English | 400 / 472 / 378 | 387 | 15% sequence, 33% RC, 3% match | 132 | RC + verbal ability only. ⚠️ Check that the literary and narrative passage types are included | 42 very short stems; key skewed to A (331) |
| General Test | 448 / 466 / 336 | 398 | 1% | 31 | ⚠️ No syllabus PDF | Current affairs must be date-checked (2025–26 events) |
| Geography | 399 / 473 / 378 | 381 | 0% | 0 | Both books covered | — |
| Hindi | 401 / 463 / 386 | 396 | 15% sequence, 24% RC, 6% match | 253 | ⚠️ No syllabus PDF | Only 4 literary-comprehension questions |
| History | 399 / 473 / 378 | 381 | 2% | 0 | All 3 parts covered. Topic field holds only "Part I/II/III", so per-theme coverage of the 12 themes can't be checked | — |
| Mass Media | 399 / 475 / 376 | 379 | 1% | 0 | Mostly covered. ⚠️ "Film Theory" (14 questions) is not in the 2026 syllabus | — |
| Mathematics | 395 / 473 / 382 | 386 | 0% | 53 | ⚠️ No syllabus PDF; 50 questions have a blank topic | 797 empty sub-topics; 306 very short stems; written in Unicode instead of KaTeX |
| Physics | 447 / 468 / 335 | 396 | 0% | 49 | All 9 units covered | 183 short explanations (from audit_report.md) |
| Political Science | 399 / 475 / 376 | 379 | 0% | 0 | Both books covered | — |
| Sanskrit | 396 / 479 / 375 | 376 | 2% | 151 | Grammar-heavy. ⚠️ Check the share of passages and literature against the syllabus | 80 very short stems |

\*CUET-style formats = match-list + assertion-reason + statement combinations + sequence, detected automatically. The numbers are approximate; Hindi and Sanskrit detection is weaker.

## 4. Fix plan per subject (in this order)

1. **Re-grade** every question's difficulty against the benchmark in §2.
2. **Fix errors:** wrong answers or concepts, out-of-syllabus questions, broken stems.
3. **Rewrite to reach 8/32/10**, and make about 30% of each paper CUET-style formats. Use the rewrite to replace templated and very short questions first, because the swaps that are needed anyway (easy→medium, hard→medium) can absorb them.
4. **Correct the metadata:** real `syllabus_source`, honest `past_paper_reference` (or `null`), consistent topic labels, filled sub-topics.
5. **Validate** with `validate_papers.py` and `audit_papers.py`.

Suggested order: Accountancy (PYQs already in hand), then the remaining Commerce and Science subjects, Humanities, and finally the languages and General Test once their syllabus PDFs are provided.

**Effort:** about 380–400 new questions per subject, written individually by hand (rulebook rule 7), plus an SME review of the remaining about 850. That is several sessions per subject.

## 5. Needed from you

- Syllabus PDFs for **English, General Test, Hindi and Mathematics**.
- A decision on **Accountancy Unit V**: keep both Analysis of Financial Statements and Computerised Accounting System compulsory, or mirror NTA's choice. For example, a paper could have about 40 common questions plus 10 AFS or 10 CAS, with the student choosing.
