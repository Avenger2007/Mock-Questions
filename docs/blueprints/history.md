# Blueprint — CUET (UG) 2027 History (314)

**Syllabus:** `CUET SYLLABUS/md/History - 314.md` (NTA "for the year 2026", the latest published). It lists twelve themes from NCERT *Themes in Indian History* Parts I–III (Class 12, rationalised editions). Chapters removed in rationalisation (Kings and Chronicles, Colonial Cities, Understanding Partition) are not in the syllabus and are never tested.
**Series:** 15 tests, `CUET/History/CUET HISTORY TEST 1–15.json` (existing file names kept).

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Questions | 50, all compulsory (2025 onward; in 2024 candidates answered 40 of 50) |
| Duration | 60 minutes |
| Marking | +5 / −1 / 0 |
| Options | 4, single correct |

## 2. PYQ analysis (analysed, not stored)

Papers read for pattern only (kept outside the repo, never copied): the NTA 2022 paper (Set HIS05, `PYQ/History/`, git-ignored), the 2024 paper (code 314, booklet A) and the 2026 paper (both via AglaSem).

- **2024:** 11 match-list items, 8 statement sets ("which are correct / not correct / true"), 3 fill-in-the-blank items, one 5-question passage on the Mughal state, and a 5-question block on the Constitution. The rest were direct. There were no assertion–reason items.
- **2026:** chronological-order items in nearly every part (textual traditions, religious teachers, eighteenth-century events). Also match-lists on terms (*jama*, *hasil*, *amil-guzar*), fill-in-the-blank items, "identify the incorrect pair" items, and a 5-question source passage from a Constituent Assembly speech with a statement item inside the set. Archaeogenetics (DNA studies of ancient populations) appeared under Harappan archaeology.
- **Content:** spread across all twelve themes. Part III (colonialism, 1857, Gandhi, the Constitution) and Harappan archaeology carry slightly more weight. Questions turn on NCERT names, terms, sources, sites and dates.
- **Difficulty:** mostly moderate. The difficulty comes from close distractors (Kalibangan vs Banawali, *amil-guzar* vs *diwan*, Fifth Report vs Sixth Report, Nana Sahib vs Kunwar Singh) and from ordering events.

**What the old series got wrong (audit, `docs/audit/CUET-audit-report.md`):**
- 70% of questions were easy.
- Only 3% used CUET formats.
- 69% of explanations ran under 150 characters.
- The correct option was the longest in 34% of items.
- Twelve papers had runs of 13 identical answers.
- The theme was not recorded, and there was a fake past-paper reference.

This series fixes all six.

## 3. Theme weight per test (50 questions)

| Part | Theme (NCERT chapter) | Qs |
|---|---|---|
| **I (17)** | H1 Harappan civilisation and archaeology (*Bricks, Beads and Bones*) | 5 |
| | H2 Political and economic systems in early states: inscriptional evidence (*Kings, Farmers and Towns*) | 4 |
| | H3 Social histories: the Mahabharata (*Kinship, Caste and Class*) | 4 |
| | H4 Buddhism and Jainism: cultural developments (*Thinkers, Beliefs and Buildings*) | 4 |
| **II (16)** | H5 Medieval society through travellers' accounts (*Through the Eyes of Travellers*) | 4 |
| | H6 Bhakti–Sufi traditions | 4 |
| | H7 Vijayanagara: politics, economy and architecture (*An Imperial Capital*) | 4 |
| | H8 The Mughal empire and agrarian society (*Peasants, Zamindars and the State*) | 4 |
| **III (17)** | H9 Colonialism and rural society: evidence from official reports (*Colonialism and the Countryside*) | 4 |
| | H10 The Revolt of 1857: patterns and representations (*Rebels and the Raj*) | 4 |
| | H11 Mahatma Gandhi and the national movement | 5 |
| | H12 The making of the Constitution (*Framing the Constitution*) | 4 |
| **Total** | | **50** |

The 5-question source passage counts inside its theme's quota. When that quota is 4, one question is moved from another theme of the same part, so each part stays at 17 / 16 / 17 (±1).

## 4. Difficulty (every test)

**8 easy / 32 medium / 10 hard.**

- **Easy:** one NCERT fact (a site, a ruler, a text, a date).
- **Medium:** a close distractor set, a term and its meaning, a source and its author, a cause–effect link, or a match whose pairs are well known.
- **Hard:** a multi-statement judgement, a chronology of four events spread over a short span, a four-pair match where every pair is plausible, or an inference from the source passage.

## 5. Formats (every test)

| Format | Count |
|---|---|
| Source passage (one original passage on an NCERT source, 5 linked questions; one may be a statement item) | 5 |
| Match List-I / List-II | 7 |
| Statements "(A)–(D), choose the correct / incorrect" | 6 |
| Chronological or other order (sequence) | 4 |
| Direct, including at least 3 fill-in-the-blank and 2 "identify the incorrect pair" items | 28 |

Assertion–reason items are not used, because none appeared in the History papers analysed.

## 6. Option quality (audit fix)

- All four options come from the **same category**: four sites, four rulers, four reports or four years. Every distractor is a real NCERT name that a half-prepared student could pick.
- Stems carry context. Match, statement and sequence items and the source set are always long.
- The key per test is 13 / 12 / 13 / 12 (rotated), with no letter more than 3 times in a row. The correct option is never clearly the longest.
- Statement and sequence answers vary. A sequence answer is never A, B, C, D in that order.
- `shuffle_test.py` gives a random exam order and keeps the source set together.

## 7. Facts and sources

- Every fact follows the rationalised NCERT text, plus the Rakhigarhi archaeogenetics update in the current *Bricks, Beads and Bones* chapter.
- Dates are NCERT's dates. Where NCERT gives a range or an approximate date (c. 2600 BCE, sixth century BCE), the item tests the order or the period, not a precise year.
- Source passages are **original summaries** of the sources NCERT discusses (Mackay on drainage, the *Ain-i Akbari*, Paes, Ibn Battuta, Bernier, Buchanan, Assembly debates). At most a few words are quoted, so no NCERT source box is reproduced.

## 8. Explanations

`Answer:` → `Why` → `Why not the others` → `Key point`. For statement items, the explanation names each false statement and says what is wrong with it. For sequence items, it gives the date or period of every event.

## 9. Out of syllabus — never test

- *Kings and Chronicles* (the Mughal court, *Akbar Nama* as a chronicle, court ceremonial).
- *Colonial Cities*.
- *Understanding Partition*, including Partition films and memoirs.
- Material removed from the rationalised chapters, such as the detailed Mauryan administration under Ashoka and the Harappan "end of the civilisation" debate beyond what NCERT keeps.

Pre-Harappan prehistory and post-1950 history are also excluded.
