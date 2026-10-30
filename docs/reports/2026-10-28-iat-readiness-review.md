# OurMocks: project understanding and IAT readiness review

Reviewed 28 October 2026. Baseline: `main`, commit `574145ded0b49d6a2311e816ae49d1f9c6295549`.
Repository: https://github.com/Avenger2007/Mock-Questions

## Decision

I can author original IAT questions, produce the required JSON, develop mechanical validation, review solutions, and make local Git commits. Uploading commits to GitHub also requires authenticated write access; successful cloning of this public repository does not establish that access, and push access was not tested.

The repository is ready for IAT preparation work, but its own pre-start requirements are not yet satisfied for Test 1. There are no IAT PYQs, approved IAT blueprint, series coverage map, IAT-specific validator, or pilot paper in the checkout. A verified 2027 brochure was not located during this review. The existing 2026 syllabus is available.

Recommended production commitment: one 60-question pilot first, followed by batches of 3 full papers (180 questions), with up to 5 papers (300 questions) as a conditional session target after the process is established. This is a planning estimate, not a guaranteed maximum or evidence that 300 questions have already been checked. Solution complexity, diagrams, source access, corrections and session limits determine the actual count.

## Review coverage and limits

The baseline has 319 tracked files: 45 Markdown files, 244 JSON files, 25 PDFs, four Python utilities and `.gitignore`. The companion `2026-10-28-repository-inventory.json` accounts for every baseline tracked file.

The review covered repository instructions, current and historical status/audit documents, blueprints, source registers, schema/example, indexes, utilities and exam syllabi. All 244 JSON files were parsed. Every existing test was traversed by the mechanical validation/audit routines. Text extraction succeeded for all 25 PDFs. The IAT syllabus Markdown was read, and the PDF text was checked as a source counterpart. Other syllabi and the long historical audit were scanned for scope, structure and relevant warnings.

This is a repository and generation-readiness review, not a fresh academic certification of all 11,460 existing questions. Representative content was inspected; all existing solutions were not independently re-solved. PDF text extraction is not a visual verification of every page or diagram. Historical claims are distinguished below from newly measured facts.

## Project purpose, goals and intended outcomes

**OurMocks is an exam-content repository.** The application frontend, backend and importer implementation are absent. Its operational deliverable is a collection of complete mock papers in UTF-8 JSON for the platform to consume, together with authoring instructions, syllabi, provenance, coverage plans, image specifications and review tools.

The educational goal is realistic preparation: questions within the official syllabus, genuine reasoning at the target exam's level, meaningful timed practice, plausible distractors and explanations that teach a method and identify mistakes. Producing a large file count is secondary to correctness, variety and preparation value.

The engineering goal is reproducible, traceable delivery: stable question IDs, consistent metadata, explicit paper rules, machine-readable sections and answers, validated files, accurate indexes and a Git history the platform can consume.

The scope now extends beyond CUET to IAT, NEST and COMEDK, each with separate instructions. CUET currently targets 15 tests per subject, with Accountancy retaining 16. The other three exam series each target 25 tests. Their marking, timing, section rules and authoring styles must remain distinct.

## Actual current contents

| Area | Measured state |
|---|---|
| CUET | 15 subjects, 226 papers, 11,460 stored questions |
| Accountancy | 16 papers, 960 stored questions; all marked `revised` |
| Other CUET subjects | 14 subjects × 15 papers × 50 questions = 10,500 questions; all marked `pending_revision` |
| CUET syllabus | 23 PDFs and 23 corresponding Markdown files |
| IAT / `IISER/` | 2026 syllabus PDF and Markdown, empty image register; zero test JSON files |
| NEST / `NISER/` | syllabus Markdown and empty image register; zero test JSON files |
| COMEDK | empty image register; instructions elsewhere; no syllabus PDFs or test JSON files |
| PYQs | Accountancy and History source registers; no committed PYQ PDFs and no IAT source collection |
| Blueprints | Accountancy blueprint and coverage plan only |

Accountancy stores 60 questions because students attempt the 40-question common section plus either of two 10-question alternatives. Its intended difficulty is checked on each 50-question attempt path, not across all 60 stored questions.

Older reports and the beginning of `Worklog.md` describe 375 papers and 18,750 questions. These are historical snapshots predating deletion of 149 papers and the Accountancy revisions. They must not be used as current totals. Some old reports also say syllabus PDFs are missing even though those PDFs now exist.

## The IAT series I understand you want

The target is **25 original full-length IAT 2027 preparation papers**, stored as `IISER/IAT TEST 1.json` through `IAT TEST 25.json`: **1,500 questions and worked explanations**, 375 questions per subject over the series.

The official 2026 examination material supports 60 single-correct MCQs, 15 each from Biology, Chemistry, Mathematics and Physics, 180 minutes, +4 correct / −1 incorrect / 0 unanswered, and 240 maximum marks. These are confirmed 2026 facts, not a verified 2027 notification.

The repository's editorial difficulty target is 9 easy / 39 medium / 12 hard per full paper. One subject has 3/9/3; each other subject has 2/10/3, rotating the extra easy allocation between tests. This is an OurMocks policy, not an official IAT quota. Tests 1–8 are more accessible, 9–17 deeper and 18–25 most demanding, with the same numerical mix throughout.

Questions should vary in substance and approach: conceptual reasoning, multistep numerical work, graphs/data, experiments and necessary diagrams. Biology must test mechanisms and evidence as well as facts. Chemistry must balance physical, organic and inorganic work from the PYQ benchmark. Mathematics and Physics must reward understanding and correct methods.

Each question needs an ID, subject/section, exact syllabus topic and sub-topic, class level, difficulty, format, complete stem, four options, correct answer and structured explanation. Numerical explanations require data, principle, working with units and mistake analysis. Conceptual explanations require reasoning, elimination of the wrong options and a takeaway. Maths uses KaTeX, chemistry uses mhchem, and JSON escaping must be checked after parsing.

The proposed section IDs are B/C/M/P; the actual order is to be confirmed from the supplied papers. Shuffle within subjects. Do not import CUET's marking scheme, optional Accountancy paths or paper-wide subject mixing into IAT.

Every item must be independently authored. No copied or lightly paraphrased PYQs, parameter-swapped question skeletons, recycled fact banks or difficulty changes achieved only through relabelling. Scripts may perform mechanical checks and organisation; they must not manufacture question content.

Coverage means representative coverage of the major syllabus areas in each paper and planned sub-topic coverage across the series. The phrase “whole syllabus in every test” needs an operational definition in the blueprint: 15 questions per subject cannot explicitly assess every listed sub-topic separately.

## Requirements before generation

These gates come directly from `docs/instructions/IAT_Instructions.md`:

1. **User-supplied PYQs.** Strict Command 1 says: “Never start IAT work without the user's PYQs.” It also prohibits searching for/downloading them unless the user asks. This review did not download PYQs. Recent complete papers with final keys would be the most useful starting material.
2. **Verified exam policy.** The instructions explicitly require the official 2027 brochure before Test 1. I could retrieve indexed official 2026 material, but did not verify a 2027 brochure; direct official-page fetches also timed out. Either supply the current brochure or explicitly approve revising the repository policy to allow clearly labelled provisional 2027-preparation papers based on verified 2026 rules, with a mandatory check when 2027 material becomes available. Do not cite a nonexistent 2027 brochure in metadata.
3. **PYQ analysis and blueprint approval.** Create `docs/blueprints/iat_pyq_analysis.md` and `docs/blueprints/iat.md`, analysing topic weights, style, steps/time, distractors, diagrams, difficulty and changes across years. The file requires: “Show the analysis summary to the user and get approval” before Test 1.
4. **Series coverage map.** Plan the 1,500 question slots by topic, angle, difficulty and style, checking conceptual overlap before full authorship. Topic repetition is inevitable; repetition of the same assessed reasoning with cosmetic changes is the problem to prevent.
5. **IAT-aware checks.** Adapt the tooling before marking papers revised.
6. **Pilot approval.** Author and verify Test 1, then obtain the standard approval required by the repository before Tests 2–25.

These are concrete repository requirements, not a request for blanket permission to clone, inspect files or prepare tooling. Preparation can proceed without waiting for approval of unfinished work.

## Findings that affect readiness

### 1. Calculator policy needs correction

The IAT instructions say to assume no calculator and require hand-solvable questions. The official 2026 brochure, section 23, explicitly provides an **online non-programmable scientific calculator** and prohibits bringing a personal calculator. Keep reasonable arithmetic and timing, but correct the description of the official testing conditions. Re-check for 2027.

### 2. Two different JSON contracts exist

The papers use flat fields such as `question`, string `options`, `correct_option`, and difficulty `medium`. The separate future question-bank schema uses typed blocks, option IDs, `answer.correctOptionId`, source objects and difficulty `moderate`. Its README says the importer is not already implemented.

IAT should use its specified flat paper format unless the delivery contract is deliberately changed. The rich schema cannot validate IAT paper JSON unchanged. A conversion layer would need explicit mappings for text/math, IDs, difficulty, provenance, images and separate exam blueprints. Image filenames in papers are also not the managed `assetId` required by the future schema. No end-to-end platform import could be tested because application code is absent.

### 3. The validator can report misleading success

`validate_papers.py` is CUET-specific. Difficulty checks on papers without sections run only if `difficulty_level` matches its legacy table. New pending-revision files often omit that field, so their difficulty check is skipped. This produced zero reported difficulty deviations despite all 210 non-Accountancy papers being off the current exact 8/32/10 target in a separate count.

The section branch assumes CUET optional attempt paths. An IAT paper has four compulsory subject sections and no optional paths, so simply passing it through this branch would not check IAT difficulty. The script also prints problems without returning a failing process status, does not enforce all required metadata, and does not establish academic answer correctness. Matching the letter in an explanation to the stored letter is only a consistency check.

An IAT validator should fail with a nonzero status on invalid files and enforce counts, section membership/order/ranges, 9/39/12 plus the rotated section splits, duration and marking, valid and unique IDs, option prefixes, required fields, answer/explanation agreement, image-register links, key balance/runs and series-level duplicates. Similarity checks should flag possible paraphrases or number swaps for review rather than certify semantic uniqueness.

### 4. Audit metrics need exam awareness and careful interpretation

`audit_papers.py` hard-codes the CUET 8/32/10 whole-file target. It consequently flags all 16 revised Accountancy files even though all 32 candidate paths were separately confirmed to have the exact intended mix. It would also misgrade IAT's 9/39/12 target.

Its duplicate-option check lowercases all option content. The two flags observed in Biology and Computer Science are not confirmed duplicate defects: genotype case and string case can be meaningful. This illustrates why mechanical warnings need domain review.

### 5. Shuffling must preserve diagram links

`shuffle_test.py` already retains separate subject sections, but renumbers question IDs without changing `image_reference` filenames or image-register entries. Before IAT diagram questions use this workflow, either assign their position-based references after final shuffling or update all related references atomically.

Image prompts alone are not a renderable diagram. A release containing essential figures also needs accurate figure assets and a visual check. The PDF exporter does not currently render `image_reference` assets.

### 6. Other documentation and tooling drift

- Accountancy's index has stale easy-count summaries in 14 entries (Tests 2–6 and 8–16) despite revised paper content. Indexes should be derived from the final files.
- The Accountancy blueprint/coverage documents still discuss a 25-paper series although the current series has 16. Some early planned case themes differ from the completed worklog.
- The rich-schema documentation links `DEVELOPMENT-PHASES.md`, which is absent.
- The Sanskrit syllabus Markdown contains 49 NUL characters; its extracted text needs repair or source inspection before authoring Sanskrit content.
- `export_test_pdf.py` hard-codes a macOS Chrome executable and loads KaTeX from a remote CDN. Its rendering cannot be assumed portable or offline-ready in this Linux environment.
- `.gitignore` ignores Python files by default except four named utilities. Prefer extending an existing tracked utility, or explicitly allow a new validator so it is actually committed.
- There is no tracked application, dependency manifest or automated CI workflow to establish platform acceptance.

## Mechanical checks performed

- Cloned `main` and inspected recent history; the starting worktree was clean.
- Parsed all 244 baseline JSON files without a parse error.
- Ran the existing validation routines across all 15 CUET subjects. They reported zero count/option-count/invalid-answer-letter/explanation-letter/exact-stem-duplicate issues. Their limits above prevent interpreting this as academic correctness or release certification.
- Counted the real paper statuses, questions, difficulty labels, explanation structure and missing sub-topics independently of the historical reports.
- Independently confirmed exact 8/32/10 on all 32 Accountancy attempt paths.
- Found 43 existing papers with answer-letter runs longer than three, including History runs up to 13 and Economics runs up to 15.
- Found 600 empty Mathematics sub-topics. None of the 10,500 pending-revision questions starts its explanation with the required `Answer:` prefix; all 960 Accountancy questions do.
- Confirmed the CUET instruction file and its Hermes copy are byte-for-byte identical.
- Extracted text from all 25 PDFs successfully. This checks extractability, not factual correctness or visual layout.
- Inspected the rich schema and example; full JSON Schema execution was not performed because `jsonschema` is unavailable in the current Python environment.
- Confirmed local Git author name/email are configured. Did not inspect or expose credentials and did not attempt a push.

## Proposed delivery and Git workflow

1. Prepare IAT validation and correct the identified IAT rule issues on a work branch, preserving the existing CUET collection.
2. Obtain the missing reference papers and settle the official/provisional 2027 policy.
3. Produce the PYQ analysis, blueprint and series coverage map for review.
4. Author the pilot question by question, solve before writing distractors, validate the final JSON, check the rendered maths/figures, and present the complete pilot for approval.
5. Generate subsequent papers in reviewable batches, checking every paper and comparing against the entire existing IAT pool. Keep a coverage ledger so later batches do not silently repeat earlier approaches.
6. Before release, independently re-solve the required random 10% series sample (150 questions across 25 papers), alongside the initial solving and per-paper reading. Automation cannot replace academic review of ambiguity, distractors and solution validity.
7. Update the IAT image register, series index, README status and Worklog with the delivered batch; commit coherent changes locally. Push or open a PR when authenticated repository write access is available and the requested workflow authorizes publication.

This assessment adds a report and a mechanical inventory only. No mock questions were generated, no existing content/tooling was changed, and no commit or push was made.

## Session capacity

| Stage | Sensible target | Interpretation |
|---|---|---|
| Initial setup | Analysis, coverage plan and validation work | Do not combine all setup with a promise of five publishable papers |
| Pilot | 1 paper / 60 questions | Stop at the repository-required review gate |
| Established process | 3 papers / 180 questions | Recommended planning batch |
| Favourable established session | Up to 5 papers / 300 questions | Conditional target matching the IAT instruction's approximate five-test batching guidance |
| Whole series | 25 papers / 1,500 questions | Several sessions; not a responsible single-session quality promise |

There is no fixed universal single-session maximum. A smaller fully checked batch is the deliverable if a larger batch cannot satisfy the stated standard. Figures and rigorous re-solving can materially reduce throughput.

## Official references checked

- Official IAT examination page: https://www.iiseradmission.in/pages/admission/iat.html — indexed 2026 question count, subject split, timing and marking.
- Official 2026 brochure, examination section: https://info.iiseradmission.in/assets/pdfs/IB_IAT_2026_ENG.pdf — indexed section 19 confirms the 2026 pattern.
- Official 2026 brochure, examination-day instructions: https://payment.iiseradmission.in/assets/pdfs/IB_IAT_2026_ENG.pdf — indexed section 23 confirms the on-screen scientific calculator.

Direct official page/PDF fetches timed out in several attempts, so these observations rely on indexed official-source passages. No official 2027 brochure was successfully verified in this review; that is a verification limit, not proof that no such document exists.
