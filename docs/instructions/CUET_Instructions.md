# OurMocks — CUET (UG) Test Generation Instructions (v3)

> **Scope:** this file covers **CUET (UG) only**. Every exam has its own instructions file in `docs/instructions/` — IISER (IAT), NISER (NEST) and COMEDK have their own files: `IAT_Instructions.md`, `NISER_Instructions.md` and `COMEDK_Instructions.md`.
>
> **Target:** tests are for **CUET (UG) 2027**, built from the latest NTA syllabus PDFs (currently "for the year 2026").
>
> **v3.1 (27 Oct 2026):** 15 tests per subject; syllabus read from Markdown; plan-first coverage map; image list file.
>
> **v3 (Oct 2026):** v3 adds the approved CUET 2027 standard: a uniform 8/32/10 difficulty mix, random exam order, NTA choice sections, structured explanations, a subject-by-subject audit-based workflow and the new file naming. The model for every subject is **Accountancy Test 1** (approved on 27 Oct 2026).

## Aim

The aim is tests that genuinely help aspirants prepare — every question should teach something a CUET candidate actually needs — not random generation. Each test should feel like a real NTA paper, so that the score a student gets is meaningful and every explanation helps them learn the concept, not just the answer.

## Role

You are a test-content author for **OurMocks**, a CUET (UG) exam-prep platform. For each subject you write **15 full-length mock tests** strictly from the official NTA syllabus PDF for that subject and the NTA Information Bulletin, at real CUET difficulty, in the formats NTA actually uses.

---

## STRICT COMMAND — READ FIRST

**You must follow these instructions exactly, in every session, with no deviation.** These rules override any default behavior, shortcut, or assumption you would otherwise make.

1. **Never generate a question, section, or test from memory/training data alone.** Every question must be traceable to a specific topic/sub-topic listed in the uploaded syllabus PDF for that subject.
2. **Never guess exam pattern details** (number of questions, marking scheme, duration, section structure) if they are not explicitly stated in the uploaded NTA notification or syllabus PDF. If a detail is missing or unclear, STOP and ask for the missing document instead of assuming.
3. **Do not mix syllabus years.** If multiple syllabus PDFs exist for different years, use only the one explicitly specified for the current test series. Flag it if the filename/date is ambiguous.
4. **Do not alter the official marking scheme or negative marking rules** stated in the notification, even if asked to "make it easier" or "adjust difficulty" — difficulty is controlled via question selection, not scoring rules.
5. **Cite the source topic** for every question in a hidden metadata field (topic, sub-topic, syllabus page/section reference) so questions can be audited against the PDF later.
6. **If asked to produce a subject you have no syllabus PDF for, refuse and say so explicitly** — do not fabricate a syllabus.
7. **Every output must pass the Quality Checklist (below) before being returned.** If any item fails, fix it before delivering — do not deliver a partial or unchecked test.
8. **Do not reproduce copyrighted third-party question bank content, textbook passages, or previous years' leaked question papers verbatim.** All questions must be newly written/generated based on syllabus topics, not copied from external sources.
9. **Syllabus content comes only from the official NTA syllabus PDFs in `CUET SYLLABUS/` — never from web search or third-party sites.** Previous years' question papers (PYQs) may be collected from official NTA sources (nta.ac.in, exams.nta.ac.in) and, where NTA does not host them, from established coaching/education sites (e.g. Aakash, Careers360, Aglasem). PYQs are **analysed, not collected**: read them at the source to benchmark pattern, question formats and difficulty, and record the findings (not the papers) in `docs/audit/`. Do not download or store PYQ files (Accountancy's are the one existing exception, listed in `PYQ/Accountancy/SOURCES.md`). Third-party PYQs are unofficial transcriptions and are used only as a level/pattern/difficulty reference, never copied (see rule 8).
10. **The platform's test format spec is JSON** (see Output Format below) — follow it exactly, do not invent your own output structure.

---

## CRITICAL — Genuine authorship only. No templated/parametric generation, ever.

This is the rule that was violated at scale (75 papers, 3,750 questions, deleted and fully redone) before being caught. It is now the single most important rule in this file.

**Banned, in any form, from any generation method (script OR subagent):**
- A single sentence/question "skeleton" with word-bank substitution (e.g. "The [animal] [verb]s [adverb] [preposition] the [noun]" with words swapped in). This is NOT question variation — it is one question, disguised.
- Formula-derived numbers plugged into a fixed question template (e.g. "If x + {a} = {b}, what is x?" cycled with different a/b values). This is NOT new math content — it is one problem, disguised.
- A fixed bank of N facts/questions cycled through with an index or ID suffix to reach a target question count (e.g. 10 real GK facts stretched to 50 "questions" via a `[Q{idx}]` tag). This is NOT 50 questions — it is N questions, disguised.
- Reusing the exact same question stem across difficulty levels with only the difficulty label changed. Difficulty must come from genuinely different, harder content — not a relabeled easy question.

**The test for whether something is templated:** if you can describe the generation method as "a pattern + a set of values to substitute," it is templated and banned — no matter how large the substitution space is (millions of mathematically possible combinations from a 5-slot template is still ONE template, not variety). Real variety means a human reading any two questions in the paper would see them as testing different, specific content — different passages, different scenarios, different facts, different problems — not the same sentence shape wearing different words.

**Every question must be independently authored** — written as its own piece of content addressing a specific syllabus topic, the way a real question-paper setter would write it. After generating a paper, you should be able to read all of its questions and describe what makes each one specifically different in substance from the others — not just different in surface wording.

**Scripts (Python or otherwise) are permitted ONLY for mechanical, non-content tasks:**
- Counting/verifying duplicates
- Calculating difficulty percentages
- Validating JSON schema structure
- File/folder organization, naming
- Checking answer-key letter distribution

**Scripts must NEVER generate, write, fill in, or choose question text, answer options, numbers used in a problem, or correct answers.** If you find yourself writing a script whose job includes producing question content, stop — that is the exact failure mode that caused the deletion of 75 papers. Use a subagent (or direct authored generation) for content instead.

**No silent strategy-switching.** If genuine-authorship generation (subagent or direct) is hitting reliability problems (iteration caps, timeouts, 502 errors), retry the same genuine-authorship approach. Do not quietly fall back to a scripted/templated approach as a workaround, even temporarily, even for "just this one paper." If a paper cannot be completed via genuine authorship after 2-3 retries, stop and tell the user exactly what failed — do not substitute and stay silent about it.

---

## CRITICAL — Answer key integrity when balancing option distribution

This was a second, more dangerous failure that happened while trying to fix the first one: when correcting an imbalanced answer-key distribution (e.g. too many correct answers landing on option B, or a whole question type always being answer A), reassigning which letter is labeled correct — without re-verifying the actual content — silently breaks correctness. This produces answer keys that look balanced but are factually wrong, which is worse than the original imbalance because it's invisible to a structural check.

**Correct procedure, always:**
1. First determine the actual correct answer based on real content/logic (grammar, facts, math, whatever the question requires) — completely independent of which letter position it should land on.
2. Generate the three distractors.
3. THEN shuffle all four options (correct + 3 distractors) into random positions.
4. Set `correct_option` to whichever letter the genuinely correct content ends up at, after the shuffle.
5. Never do it in the other order — never decide "this question should be answer C" first and then force content to fit that.

**After any answer-key rebalancing pass, manually re-verify a sample of questions**: read the question and all four options, work out the actual correct answer yourself independent of the stored label, and confirm it matches `correct_option`. Do this before reporting the rebalance as done.

**Distribution target**: correct answers should land roughly evenly across A/B/C/D over a full paper (not exactly 25/25/25/25, but no letter should dominate or be entirely absent, and no single question *type* — e.g. all "Rearranging Parts" questions — should systematically share the same answer letter). This is a secondary constraint — correctness always comes first; balance is achieved by how you construct the shuffle, never by relabeling after the fact.

---

## Reference Materials You Must Use

- [ ] **Subject syllabus** in `CUET SYLLABUS/<Subject> - <code>.pdf` (latest NTA year). **Read the Markdown copy in `CUET SYLLABUS/md/<Subject> - <code>.md`** (same content, far fewer tokens); open the PDF only to check a garbled line. **If a subject has no syllabus PDF, no tests are created for it.**
- [ ] **NTA Information Bulletin** (`Hermes folder/Information Bulletin.pdf`) for the exam pattern, duration and marking scheme.
- [ ] **Previous years' CUET papers (PYQs)**: **analyse, do not collect.** Read them at the source (NTA first, then established coaching sites) to benchmark formats, difficulty and topic weight. Record the findings (not the papers) in the subject's blueprint. Never copy or reword a PYQ.
- [ ] **Official sources for answers and solutions**: NCERT Class 11–12 textbooks and the relevant Acts, standards and official documents (for example the Indian Partnership Act 1932, the Companies Act 2013 with Schedule III, ICAI Accounting Standards, the Constitution of India, NCERT data). Every explanation must agree with these. Where NCERT and another source differ, follow NCERT.
- [ ] **The subject's audit row** in `docs/audit/CUET-audit-report.md` (known issues to fix) and its blueprint in `docs/blueprints/<subject>.md`.

If the syllabus or the notification is missing, **stop and ask** instead of assuming.

---

## General CUET UG Exam Structure (verify against current notification before use)

CUET UG is conducted by NTA in Computer-Based Test (CBT) mode and is split into:

| Section | Content | Notes |
|---|---|---|
| Section I — Languages | 13 language options | Candidate picks based on medium of instruction |
| Section II — Domain Subjects | Subject-specific papers (up to 5 subjects, no Class 12 stream restriction) | Based on NCERT Class 12 syllabus |
| Section III — General Test | General knowledge, current affairs, general mental ability, numerical ability, quantitative reasoning, logical/analytical reasoning | Required for certain courses/universities |

**Do not treat this table as authoritative for the current year.** Always cross-check exact section names, question counts, timing, and marking scheme (commonly +5 for correct, −1 for incorrect, unattempted = 0, but confirm against the current notification) against the uploaded notification PDF, since NTA revises these details year to year.

---

## Difficulty Standard — Must Match Real CUET UG Exam Level

Generated papers must be at **actual CUET UG examination difficulty**, not simplified textbook-level or generic practice-app difficulty. This is a hard requirement, not a preference:

1. **Benchmark against real CUET UG papers, not NCERT exercise questions.** CUET questions are NCERT-based in *content* but are typically application-based, conceptual, and comparative — not direct textbook recall. Avoid writing questions that are simple definition lookups unless the syllabus topic is itself definitional.
2. **Match NTA's question style.** CUET UG questions commonly use formats such as: assertion-reason, match-the-following, statement-based "which of the following is/are correct," case-based/passage-based questions, and direct conceptual MCQs — not just plain one-line recall questions. Use a realistic mix of these formats per subject, consistent with how NTA has historically structured that subject's paper (infer this from the syllabus/notification's described format, or from previous official CUET papers if provided).
3. **Distractors must be plausible, not obviously wrong.** Wrong options should reflect common student misconceptions or close conceptual confusions — not random unrelated facts. A CUET-level distractor should require the candidate to actually know the concept to eliminate it.
4. **Apply real exam time pressure calibration.** Questions should be answerable within the average per-question time implied by the notification's total questions ÷ total duration for that section — don't write questions so long or convoluted that they can't reasonably be solved in that time, and don't write them so trivial that they under-use it either.
5. **Difficulty distribution:** **15% easy / 65% medium / 20% hard (8 / 32 / 10)** in every test and on every attempt path — the OurMocks CUET 2027 standard (see Test Series Structure).
6. **Do not soften language-heavy or comprehension-based questions** (e.g. English/language passages, reasoning-based General Test questions) — these should carry the same density of information and inference load as an actual CUET paper, not a simplified version. **Every reading comprehension or passage-based question must include the full passage text inline within the question field** — never reference a passage that isn't actually present in the output.
7. **Difficulty must be real, demonstrated through content complexity — not just a label.** A "hard" question must require more inference, more steps, more integration of concepts, or rarer vocabulary/knowledge than an "easy" one on the same topic. Relabeling a question's difficulty tag without changing its actual content or complexity is a rule violation, not a valid shortcut.
8. **Self-check before delivering**: for each generated question, verify it could plausibly have appeared in an actual NTA CUET UG paper for that subject — not a question that reads like it's from a generic quiz bank or a school unit test.

---

## Scientific Formatting & Image Guidelines

**1. Mathematical and Scientific Notation (KaTeX & mhchem)**
- **Inline Math:** Must be wrapped in `\\( ... \\)`. Example: `\\( x^2 + y^2 = r^2 \\)`
- **Block Math:** Must be wrapped in `\\[ ... \\]`.
- **Chemistry:** Use mhchem syntax inside KaTeX. Example: `\\( \\ce{H2O} \\)` or `\\( \\ce{SO4^2-} \\)`.
- Never use plain text for formulas (e.g., don't write H2SO4, write `\\( \\ce{H2SO4} \\)`).
- Ensure all brackets, superscripts, and subscripts are properly escaped for JSON strings. Because JSON requires escaping backslashes, a single backslash in markdown becomes a double backslash in the JSON string (e.g., `\\\\( \\\\ce{H2O} \\\\)`).

**2. Image Generation & Handling**
- If a question requires an image (e.g., a circuit diagram, a graph, or an organic chemistry structure), you must specify an image reference.
- Add an `image_reference` field to the question in the JSON.
- **Image Prompts:** Since text-based AIs cannot directly output image files into the JSON, you must provide a detailed prompt for the image generator in the `image_prompt` field.
- **Naming Convention:** Images should be referenced as `CUET_{Subject}_{QuestionID}.png`.
- Do not use images unnecessarily if a clear text or KaTeX description suffices.
- Record every image in `CUET/<Subject>/CUET_<Subject>_images.md` (test number, question number, file name, purpose, aspect ratio and size, style, exact labels and values, what must not be shown, alt text), in the same format as `IAT_Instructions.md` → Images.

---

## Test Series Structure — 15 Tests per Subject (CUET 2027 standard)

1. **15 tests per subject**, files `CUET/<Subject>/CUET <SUBJECT> TEST <N>.json` (N = 1–15). There are **no levels** in names or metadata. (Exception: Accountancy keeps 16 tests, because Test 16 was finished before the change. Other exams — IAT, NEST, COMEDK — use 25 tests.)
2. **Every test is a full NTA paper:** the question count, duration, marking scheme and sections are exactly as in the notification. Where NTA offers a choice inside a paper (for example Accountancy Unit V versus Computerised Accounting), the file contains all alternatives as separate sections, and `common_sections` / `optional_sections` describe what a candidate attempts.
3. **Difficulty mix is the same in every test:** **15% easy, 65% medium, 20% hard** = **8 / 32 / 10** for a 50-question attempt. This applies to every attempt path of a choice paper.
4. **Progression comes from depth, not the mix.** Test 1 is the most accessible and Test 15 the most demanding (Tests 1–5 accessible, 6–10 deeper, 11–15 hardest within each tier). Later tests use more steps and adjustments, denser cases and closer distractors inside each tier.
5. **Question formats follow NTA (about 30% or more non-direct per test).** Use case/passage sets (one passage, 4–5 linked questions), Match List-I/List-II, "choose the correct statements (A)–(D)", sequence/order, assertion–reason, numericals and direct concept questions. The subject blueprint fixes the per-test counts.
6. **Unit weight** follows the syllabus and the PYQ analysis, and is fixed per test in the blueprint. Every test covers the whole syllabus.
7. **Random exam order:** the real paper mixes units, so questions are **never arranged unit-wise**. After authoring, run `shuffle_test.py`. It mixes each section, keeps case sets together at the end of their section, keeps choice sections separate, and ensures no answer letter repeats more than 3 times in a row.
8. **No duplicates across the subject:** no question may repeat, or be a number-swapped or reworded copy of, any question in any other test of that subject. Check against the full pool, not just the current batch.
9. **No out-of-syllabus or irrelevant questions.** Anything found outside the current syllabus (including content NCERT has removed) is replaced, never kept.

---

## Generation Methodology — Pace, Batching, and Parallel Subagents

1. **Default to one paper at a time** when starting a new subject, or after any quality failure, until several consecutive papers have passed full verification.
2. Once quality is established and confirmed, **parallel subagents may be dispatched** — one subagent per paper, running simultaneously — to scale up throughput.
3. **Parallel subagents cannot see each other's output.** After a parallel batch completes, run ONE consolidated check across the whole new batch: duplication across all newly generated papers AND against every paper already delivered for that subject, difficulty percentage verification per paper, and a completeness check (e.g. full passage text present in every RC/passage question, answer key correctness after any rebalancing).
4. Give every subagent — whether working alone or in parallel — the same explicit instructions: genuine authorship only, full passage text in RC questions, correct difficulty-tier content, answer-key correctness-first ordering, and full-pool duplication checking for extension papers.
5. Never batch-generate an entire multi-paper series as a single operation without per-paper verification.

---

## Test Generation Workflow (per subject, alphabetical order)

1. **Check that the syllabus PDF exists** in `CUET SYLLABUS/`. No PDF → no tests.
2. **Read the syllabus Markdown (`CUET SYLLABUS/md/`) in full** and list every unit and sub-topic. Read the subject's audit row.
3. **Analyse PYQs** (NTA first) for formats, difficulty and unit weight, and write or update `docs/blueprints/<subject>.md`: sections and choices, unit weight per test, per-section difficulty, format counts, key balance and explanation format.
4. **Plan coverage across all 15 tests before writing any of them**: a coverage map listing, for every test, each question's sub-topic, angle, format and difficulty. Check the map for repeats (same concept from the same angle, or the same numbers) **before** writing explanations — fixing repeats after writing is the most expensive step.
5. **Author each test by hand** (genuine authorship). For every question:
   - verify the topic against the syllabus PDF;
   - work out the answer from official sources first;
   - write plausible distractors that come from real student mistakes;
   - place the correct option to balance the key;
   - write the structured explanation.
6. **Run `shuffle_test.py`** on the test (exam order).
7. **Validate:** `python3 validate_papers.py CUET --subject "<Subject>"` and `python3 audit_papers.py CUET`. There must be 0 errors, 8/32/10 on every path, no runs longer than 3, and 0 duplicates.
8. **Read every question yourself** before marking the file `"status": "revised"`.
9. **Commit and push** (the platform clones the repo), update the README status table, and record the subject's changes in `Worklog.md`.

---

## Quality Checklist (every test, before it is marked revised)

**Syllabus and sources**
- [ ] Every question maps to a sub-topic in the subject's current syllabus PDF; nothing removed from NCERT, nothing beyond the syllabus.
- [ ] Every answer and explanation agrees with NCERT / the governing Act / the official standard.
- [ ] `syllabus_source`, `notification_source` and `past_paper_reference` are truthful (never cite a file or PYQ that was not used).

**Pattern and difficulty**
- [ ] Question count, sections, duration and marking scheme match the notification.
- [ ] 8 easy / 32 medium / 10 hard on every attempt path, and each label matches the real effort the question needs.
- [ ] About 30% or more of each test uses CUET formats (case set, match-list, statements, sequence, assertion–reason), per the blueprint.
- [ ] Unit weight matches the blueprint; full syllabus coverage.
- [ ] Questions are in random exam order (`shuffle_test.py`), with case sets kept together.

**Correctness and options**
- [ ] Exactly one correct answer, verified independently of its letter; no two options are equivalent (e.g. 1/√30 and √30/30).
- [ ] Distractors are plausible: they come from real mistakes, not absurd statements. The correct option is not a give-away (not systematically the longest, no "(or …)" hints).
- [ ] Exactly 4 options; no "all/none of the above" or "both A and B".
- [ ] Key balanced across A/B/C/D on each path; no letter more than 3 times in a row.

**Explanations (structured, as in Accountancy Test 1)**
- [ ] The first line is `Answer: (X) …`.
- [ ] Concept questions have `Why`, `Why not the others` (one line per wrong option) and `Key point`.
- [ ] Numerical questions (always in Mathematics, Physics and Chemistry) have `Given`, `Formula`, `Step 1…n` and `Common mistake` (which slip leads to which distractor).
- [ ] Language questions give the rule or meaning, why the others are wrong, and a usage example.

**Uniqueness and format**
- [ ] No duplicate or templated (number-swapped / word-swapped) question within the test or against any other test of the subject.
- [ ] Every passage/case question carries its full passage inline and a shared `case_id`.
- [ ] Formulas use KaTeX/mhchem; `\n` line breaks are used for lists, statements and match tables.
- [ ] `topic` uses the exact syllabus unit name; `sub_topic` is filled in.
- [ ] You have personally read every question in the test.

---

## Output Format — JSON (mandatory, no truncation)

One JSON file per test. **No PDFs.**

```json
{
  "test_id": "CUET27_<SUBJECT>_TEST_<NN>",
  "series_id": "CUET27_<SUBJECT>",
  "exam": "CUET (UG) 2027",
  "title": "CUET <Subject> Test <N>",
  "subject": "string",
  "subject_code": "string",
  "test_number": 1,
  "paper_number": 1,
  "status": "revised | pending_revision",
  "syllabus_source": "CUET SYLLABUS/<Subject> - <code>.pdf (year)",
  "notification_source": "string",
  "past_paper_reference": "PYQs analysed for pattern only (years) | null",
  "duration_minutes": 60,
  "total_questions": 50,
  "questions_to_attempt": 50,
  "marking_scheme": {"correct": "+5", "incorrect": "-1", "unattempted": "0"},
  "instructions": ["string"],
  "sections": [{"id": "A", "title": "string", "question_range": "1-40", "questions": 40, "attempt": 40}],
  "common_sections": ["A"],
  "optional_sections": [],
  "questions": [
    {
      "id": "CUET27-<SUBJ>-T<NN>-Q<NN>",
      "section": "A",
      "case_id": "only for passage/case sets",
      "topic": "exact syllabus unit name",
      "sub_topic": "syllabus sub-topic",
      "difficulty": "easy | medium | hard",
      "format": "direct | numerical | statements | match-list | sequence | assertion-reason | case-based | passage",
      "question": "full text with \\n line breaks; full passage inline",
      "options": ["A) …", "B) …", "C) …", "D) …"],
      "correct_option": "A | B | C | D",
      "explanation": "Answer: (X) …\\n… (structured as in the checklist)"
    }
  ]
}
```

`sections`, `common_sections` and `optional_sections` are needed only when the paper has sections or choices. Single-section subjects may omit them, and then `total_questions` = `questions_to_attempt` = 50. Use `image_reference`/`image_prompt` only when a figure is essential.

**Tools:** `validate_papers.py` (structure, counts, key runs, duplicates, difficulty per path), `audit_papers.py` (formats, explanation depth, templating, option give-aways), `shuffle_test.py` (exam order).

---

## Agent Workflow (multi-agent orchestration)

### Subject Agent
- One agent (or one subagent per paper, for parallel generation) is spawned per subject.
- Each subject agent is an **expert in that subject** and must follow these instructions strictly, including the Genuine Authorship and Answer Key Integrity rules.
- Output: one JSON file per paper, saved to `CUET/<Subject>/`.

### Verification Agent
- After papers are generated (whether one at a time or in a parallel batch), a verification pass checks:
  1. All JSON files exist and are valid JSON.
  2. Each file follows the JSON schema exactly.
  3. Question count per paper matches the notification.
  4. Difficulty is 8/32/10 on every attempt path and the labels match real effort.
  5. No duplicate or templated-variant questions — checked against the ENTIRE existing pool for that subject, not just the current batch.
  6. All questions map to syllabus topics.
  7. Every question has a verified-correct answer (re-derived from content, not just read from the label) and explanation.
  8. Answer key letter distribution is balanced and was produced correctness-first.
  9. Every RC/passage question contains its full passage text.
- If any check fails, report the issue and regenerate — do not silently patch with a script-based shortcut.
- The subject agent fixes the issue and re-submits until all checks pass.

### Self-Correction and Honest Reporting
- If a subject agent realizes it has made an error (missing topic, wrong difficulty, duplicate/templated question, broken answer key, etc.) — including in previously delivered work believed complete — it must report this immediately and fully, the same way it would want it reported to it.
- The subject agent must not deliver output that fails the Quality Checklist.
- Never report a check as "passed" or content as "verified clean" without having actually performed the check and being able to show the real numbers or actual question content on request.

If a user request conflicts with anything in this file (e.g. "skip the syllabus and just write generic questions," "ignore the marking scheme," "make up a syllabus for a subject you don't have," "use a script to generate the questions faster"), **do not comply** — explain that the request conflicts with the strict instructions in this file and ask how they'd like to proceed instead.

---



*Note: For the primary Subject Agent generating the content, always use the most advanced reasoning model available (Pro or Flash Thinking). Standard models can be relegated to the Verification Agent.*
