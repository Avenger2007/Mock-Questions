# OurMocks — CUET UG Mock Test Papers Repository (2026 Series)

A standardized, high-rigor repository of **375 full-length mock test papers** (18,750 total questions) for the **Common University Entrance Test (CUET UG)**, authored in strict accordance with the official National Testing Agency (NTA) syllabi, NCERT curriculum, and previous years' exam patterns.

---

## 📚 Subject Coverage (15 Subjects, 25 Papers Each)

The repository contains 25 full-length mock tests for each of the following 15 subjects:

| Subject | Code | Papers | Total Questions | Master Index |
| :--- | :---: | :---: | :---: | :---: |
| **Accountancy** | 301 | 25 | 1,250 | [`CUET/Accountancy/series_index.json`](CUET/Accountancy/series_index.json) |
| **Biological Science** | 304 | 25 | 1,250 | [`CUET/Biological Science/series_index.json`](CUET/Biological%20Science/series_index.json) |
| **Chemistry** | 306 | 25 | 1,250 | [`CUET/Chemistry/series_index.json`](CUET/Chemistry/series_index.json) |
| **Computer Science** | 308 | 25 | 1,250 | [`CUET/Computer Science/series_index.json`](CUET/Computer%20Science/series_index.json) |
| **Economics** | 309 | 25 | 1,250 | [`CUET/Economics/series_index.json`](CUET/Economics/series_index.json) |
| **English** | 101 | 25 | 1,250 | [`CUET/English/series_index.json`](CUET/English/series_index.json) |
| **General Test** | 501 | 25 | 1,250 | [`CUET/General Test/series_index.json`](CUET/General%20Test/series_index.json) |
| **Geography / Geology** | 313 | 25 | 1,250 | [`CUET/Geography/series_index.json`](CUET/Geography/series_index.json) |
| **Hindi** | 102 | 25 | 1,250 | [`CUET/Hindi/series_index.json`](CUET/Hindi/series_index.json) |
| **History** | 314 | 25 | 1,250 | [`CUET/History/series_index.json`](CUET/History/series_index.json) |
| **Mass Media** | 318 | 25 | 1,250 | [`CUET/Mass Media/series_index.json`](CUET/Mass%20Media/series_index.json) |
| **Mathematics** | 319 | 25 | 1,250 | [`CUET/Mathematics/series_index.json`](CUET/Mathematics/series_index.json) |
| **Physics** | 322 | 25 | 1,250 | [`CUET/Physics/series_index.json`](CUET/Physics/series_index.json) |
| **Political Science** | 323 | 25 | 1,250 | [`CUET/Political Science/series_index.json`](CUET/Political%20Science/series_index.json) |
| **Sanskrit** | 325 | 25 | 1,250 | [`CUET/Sanskrit/series_index.json`](CUET/Sanskrit/series_index.json) |

**Total:** 375 Papers | 18,750 Verified Questions

---

## 🎯 Examination Scheme & Blueprint

- **Questions per Paper:** Exactly 50 multiple-choice questions (MCQs)
- **Options per Question:** Exactly 4 options (`A`, `B`, `C`, `D`)
- **Marking Scheme:**
  - Correct Answer: `+5` marks
  - Incorrect Answer: `-1` mark
  - Unattempted: `0` marks
- **Duration:** 60 minutes per mock test
- **Difficulty Mix (every paper, every level):** 15% easy / 65% medium / 20% hard = 8 / 32 / 10 questions. *Target set Oct 2026; existing papers still use the old per-level ramp and are being rewritten — see `docs/reports/`.*
- **Answer Key Balance:** Balanced distribution (~25% each of A, B, C, D across the entire series)
- **Quality Assurance:** 0 self-referential / combo options (`Both A and B`, `All of the above`), 0 duplicate question stems across the entire 1,250-question pool per subject.

---

## 🗂️ Series Progression

Each subject features a structured 25-paper progression. All papers share the same easy/medium/hard mix; higher levels get harder through deeper questions inside each tier (more steps, case/assertion-reason formats, closer distractors):

1. **Original Series (Papers 1 – 10):**
   - Levels 1 to 10 covering core NCERT fundamentals progressing to advanced conceptual applications.
2. **Variant Series "B" (Papers 11 – 20):**
   - Levels 1B to 10B providing independent question banks with real-world case applications and numerical problem-solving.
3. **Mastery Series "C" (Papers 21 – 25):**
   - Curated high-yield challenge tests spanning Levels 2C through 10C for university entrance mastery.

---

## 🔍 Validation Suite

To run full validation across all papers and subjects:

```bash
# Validate a specific subject (e.g. Sanskrit)
python3 validate_papers.py CUET --subject "Sanskrit"

# Validate all subjects
python3 -c "
import subprocess
for s in ['Accountancy', 'Biological Science', 'Chemistry', 'Computer Science', 'Economics', 'English', 'General Test', 'Geography', 'Hindi', 'History', 'Mass Media', 'Mathematics', 'Physics', 'Political Science', 'Sanskrit']:
    subprocess.run(['python3', 'validate_papers.py', 'CUET', '--subject', s], check=True)
"
```