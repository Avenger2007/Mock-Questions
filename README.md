# OurMocks — CUET (UG) 2027 Mock Test Repository

Full-length mock tests for **CUET (UG) 2027**, written for the **OurMocks** platform. The admin panel imports these JSON files and shows each question in a human-readable form.
The aim is tests that **genuinely help aspirants prepare**: real NTA pattern and difficulty, strictly within the official syllabus, and structured explanations that teach the concept.

---

## 🧭 How this repository works

| Item | Where |
|---|---|
| Test files | `CUET/<Subject>/CUET <SUBJECT> TEST <N>.json` (N = 1–15; Accountancy 1–16) |
| Official syllabi (source of truth) | [`CUET SYLLABUS/`](CUET%20SYLLABUS/) — `<Subject> - <code>.pdf`, NTA "for the year 2026" (latest published); Markdown copies in [`CUET SYLLABUS/md/`](CUET%20SYLLABUS/md/) |
| NTA Information Bulletin | [`Hermes folder/Information Bulletin.pdf`](Hermes%20folder/) |
| Authoring rules (CUET) | [`docs/instructions/CUET_Instructions.md`](docs/instructions/CUET_Instructions.md) (one instructions file per exam — see [`docs/instructions/`](docs/instructions/)) |
| Subject blueprints | [`docs/blueprints/`](docs/blueprints/) |
| Audit report (what each subject must fix) | [`docs/audit/CUET-audit-report.md`](docs/audit/CUET-audit-report.md) |
| History of changes | [`Worklog.md`](Worklog.md) |

**Rules in brief:**
- No syllabus PDF → no tests for that subject.
- Subjects are revised in **alphabetical order**.
- Every test: **8 easy / 32 medium / 10 hard**, about 30% or more NTA-style formats, **random exam order**, no duplicates across a subject's 15 tests, nothing out of syllabus, and structured explanations (step-by-step for numericals).

---

## 🚧 Revision status (CUET 2027 standard)

Each file's `status` field reads `revised` (meets the standard) or `pending_revision` (older content, still being rewritten).

| # | Subject | Code | Syllabus PDF | Revised tests | Blueprint |
|---|---|---|---|---|---|
| 1 | Accountancy | 301 | ✅ | **16 / 16** ✅ | [accountancy.md](docs/blueprints/accountancy.md) |
| 2 | Biological Science | 304 | ✅ | 15 / 15 | [biological_science.md](docs/blueprints/biological_science.md) |
| 3 | Chemistry | 306 | ✅ | 15 / 15 | [chemistry.md](docs/blueprints/chemistry.md) |
| 4 | Computer Science | 308 | ✅ | — | — |
| 5 | Economics | 309 | ✅ | — | — |
| 6 | English | 101 | ✅ | — | — |
| 7 | General Test | 501 | ✅ | — | — |
| 8 | Geography | 313 | ✅ | — | — |
| 9 | Hindi | 102 | ✅ | — | — |
| 10 | History | 314 | ✅ | — | — |
| 11 | Mass Media | 318 | ✅ | — | — |
| 12 | Mathematics | 319 | ✅ | — | — |
| 13 | Physics | 322 | ✅ | — | — |
| 14 | Political Science | 323 | ✅ | — | — |
| 15 | Sanskrit | 325 | ✅ | — | — |

Syllabi are also available for Agriculture, Anthropology, Business Studies, Environmental Science, Home Science, Performing Arts, Psychology and Sociology. These subjects have no tests yet.

---

## 🎯 Exam scheme

- **Pattern (NTA):** computer-based test, 60 minutes, 50 compulsory questions, **+5 / −1 / 0**, 4 options per question.
- **Accountancy follows NTA's Unit V choice:** each file has 60 questions, and the candidate attempts 50. That is Section A (Units I–IV, 40 questions) plus EITHER B1 (Analysis of Financial Statements, 10) OR B2 (Computerised Accounting System, 10). The fields `sections`, `common_sections` and `optional_sections` describe this, and every question has a `section` field.
- **Difficulty:** every test is 8 easy / 32 medium / 10 hard, on every attempt path. Tests get harder from Test 1 to the last test through question depth, not the mix.
- **Question order** is random across units, as in the real exam. Case sets stay together.

## 🧾 JSON format (per question)

`id`, `section`, `case_id` (for case/passage sets), `topic` (syllabus unit), `sub_topic`, `difficulty`, `format` (direct, numerical, statements, match-list, sequence, assertion-reason, case-based, passage), `question` (uses `\n` line breaks), `options` (`A) …` to `D) …`), `correct_option`, and `explanation`.

Explanations start with `Answer: (X)`, then:
- **concept questions:** Why / Why not the others / Key point;
- **numericals:** Given / Formula / Step 1…n / Common mistake.

The full schema is in the instructions file.

**For the app:** keep line breaks (`white-space: pre-line`), render KaTeX + mhchem, and don't add extra A–D letters (the options already carry them).

---

## 🔍 Tools

```bash
python3 validate_papers.py CUET --subject "Accountancy"   # structure, counts, key runs, duplicates, 8/32/10 per path
python3 audit_papers.py CUET                              # formats, explanation depth, templating, give-aways
python3 shuffle_test.py "CUET/Accountancy/CUET ACCOUNTANCY TEST 2.json"   # put a test in exam order
```

## Other exams

Each exam has its own instructions file and 25 tests per series. Work on each starts only after the user supplies its PYQs.

| Exam | Instructions | Folder | Syllabus | Status |
|---|---|---|---|---|
| IISER Aptitude Test (IAT) | [IAT_Instructions.md](docs/instructions/IAT_Instructions.md) | [`IISER/`](IISER/) | `IISER_Aptitude_Test_Syllabus_2026.md` | Instructions ready; waiting for PYQs |
| NISER / NEST | [NISER_Instructions.md](docs/instructions/NISER_Instructions.md) | [`NISER/`](NISER/) | `NEST_2026_Syllabus.md` | Instructions ready; waiting for PYQs |
| COMEDK UGET | [COMEDK_Instructions.md](docs/instructions/COMEDK_Instructions.md) | [`COMEDK/`](COMEDK/) | to be added (official PDFs) | Instructions ready; waiting for PYQs and syllabus PDFs |
