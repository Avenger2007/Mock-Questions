# Blueprint — CUET (UG) 2027 English (101)

**Syllabus:** `CUET SYLLABUS/md/English - 101.md` (NTA "for the year 2026", latest published). Two areas: **Reading Comprehension** (three types of passage of at most 300 words: factual, narrative, literary) and **Verbal Ability** (rearranging the parts, match the following, choosing the correct word, synonyms and antonyms). The list is "not limited to" these topics, so other everyday verbal-ability formats that NTA has set (one-word substitution, voice, narration) are allowed in small numbers.
**Series:** 15 tests, `CUET/English/CUET ENGLISH TEST 1–15.json`.

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Questions | 50, all compulsory (no internal choice) |
| Duration | 60 minutes |
| Marking | +5 / −1 / 0 |
| Options | 4, single correct |

## 2. PYQ analysis (CUET 2026 English — analysed, not stored)

Source: the CUET (UG) 2026 English paper published by [AglaSem](https://docs.aglasem.com/org/nta/cuet/question-paper?subject=english) as page images (36 pages). Its question formats and counts were studied; no question or passage is copied into our tests.

| Area | About how many | What it looked like |
|---|---|---|
| Rearranging the parts | 5 | four phrases (A–D) to put in order, sometimes completing a given sentence opening; options are orders such as "C, A, D, B" |
| Match the following | 6 | idioms ↔ meanings, idioms ↔ blanks in sentences, phrasal verbs ↔ meanings, word forms ↔ sentences, figures of speech ↔ examples |
| Choosing the correct word | about 16 | fill in the blank: homophones and confusables (wreath/wrath, raze/raise, lie/lay), word forms (determined, successive, effectively), prepositions (alien to, quarrel over), conjunctions, phrasal verbs (bring about), context words (pious, instigated), the correctly spelt word |
| Synonyms and antonyms | 4 | one word in a sentence (MOMENTOUS, IMMACULATE), a single word, and "select the correct pairs of antonyms" (multi-select) |
| One-word substitution | 3 | single answer, or multi-select ("A, B and D only") |
| Voice and narration | 2 | choose the passive form; choose the indirect speech |
| Reading comprehension | about 14 | about three passages: a factual travel/heritage piece, a narrative memoir, and a third set; questions on detail, inference, character, phrase meaning ("kith and kin", "it struck me") |

**What this means for OurMocks:** exact usage — confusable words, collocations, tense in reported speech — and close distractors decide the paper. Passages are short; their questions test inference and words in context as much as details. Multi-select ("A, B and D only") and match-list items need every part right.

## 3. Area weight per test (50 questions)

| Area | Section | Qs |
|---|---|---|
| **Reading Comprehension (15)** | R1 Factual passage (≤ 300 words) | 5 |
| | R2 Narrative passage (≤ 300 words) | 5 |
| | R3 Literary passage (prose or verse, ≤ 300 words) | 5 |
| **Verbal Ability (35)** | V1 Rearranging the parts | 5 |
| | V2 Match the following | 5 |
| | V3 Choosing the correct word (fill in the blank) | 14 |
| | V4 Synonyms and antonyms | 6 |
| | V5 One-word substitution | 2 |
| | V6 Sentence transformation and correctness (voice, narration, the correct sentence) | 3 |
| **Total** | | **50** |

**V3 mix (14):** homophones and confusables 3, word forms 2, prepositions 2, conjunctions and linkers 2, phrasal verbs and collocations 2, the correctly spelt word 1, context vocabulary 2.
**V4 mix (6):** 3 synonyms and 3 antonyms; at least one word given in a sentence, and one "select the correct pairs" item.

## 4. Difficulty (every test)

**8 easy / 32 medium / 10 hard.** Rough split: RC 2 / 10 / 3, VA 6 / 22 / 7 (±1).

- **Easy:** a stated detail; a common word or idiom; an obvious connector.
- **Medium:** an inference from one or two sentences; a less common word; a confusable pair; a rearrangement with one clear link.
- **Hard:** tone, purpose or a figure of speech in a literary passage; an advanced word with close distractors; a rearrangement where two orders look possible; reported speech with tense and pronoun changes; a multi-select item.

## 5. Formats (every test)

| Format | Count |
|---|---|
| Passage sets (three passages, 5 linked questions each) | 15 |
| Order / sequence (rearranging the parts) | 5 |
| Match List-I / List-II | 5 |
| Statements / multi-select ("A, B and D only") | 3 |
| Direct (fill in the blank, synonym, antonym, one word, transformation) | 22 |

Assertion–reason is not used: NTA does not set it in English.

## 6. Passages

- **All passages are original**, written for OurMocks, at most 300 words. Factual passages give accurate, checkable information (science, environment, technology, health, society, Indian heritage); narrative passages tell a story or memoir; literary passages are descriptive prose or short verse rich in imagery and figures of speech.
- Each passage set mixes: one detail, one inference, one word or phrase in context, one main idea / title / purpose, and one tone / attitude / figure of speech (literary) or one "which is NOT stated" (factual).
- No two tests share a passage theme (see the coverage map).

## 7. Key and order

- Key per test 13 / 12 / 13 / 12 (rotate); no letter more than 3 times in a row; the correct option is never clearly the longest.
- In rearrangement items the correct order is never A, B, C, D, and the distractor orders each break one real link.
- `shuffle_test.py` gives random exam order and keeps each passage set together.

## 8. Language standard

- Indian/British English spelling and usage (as in NCERT and NTA papers). Meanings follow standard dictionaries (Oxford, Cambridge, Merriam-Webster).
- Every fill-in-the-blank has exactly one correct option; distractors are real words that fail on meaning, form or grammar, not nonsense.
- No target word, idiom, phrasal verb or one-word substitute is tested twice in the series (the coverage map keeps a ledger). Figures of speech recur with new examples.

## 9. Explanations

- `Answer:` → `Why` → `Why not the others` → `Key point`.
- Passage questions quote or point to the line that decides the answer.
- Rearrangements name the links (pronoun, connector, time order) that fix the order.
- Vocabulary items give the meaning of the answer and of each distractor.

## 10. Out of scope — never test

Literature from specific textbooks (no Flamingo/Vistas chapters: CUET English 101 has no prescribed texts), grammar terminology for its own sake (naming clause types, parsing), spelling rules of American English, and very rare words that no general reader would meet.
