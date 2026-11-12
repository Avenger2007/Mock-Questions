# Blueprint — CUET (UG) 2027 Sanskrit (325)

**Syllabus:** `CUET SYLLABUS/Sanskrit - 325.pdf` (NTA "for the year 2026", the latest published). It has ten units:

1. शब्दरूपाणि – वाक्येषु विभक्तिप्रयोगाः (the listed अजन्त, हलन्त and सर्वनाम words)
2. धातुरूपाणि (18 परस्मैपदी roots in लट्, लृट्, लोट्, लङ्, विधिलिङ्; 4 आत्मनेपदी roots in लट्, लृट्, लङ्)
3. सन्धयः सन्धिविच्छेदाः च (स्वर, व्यञ्जन and विसर्ग sandhi as listed)
4. समासाः विग्रहाः च (अव्ययीभाव, द्वन्द्व, तत्पुरुष with कर्मधारय, द्विगु and उपपद, बहुव्रीहि)
5. प्रत्ययाः (11 कृत्, 6 तद्धित, 2 स्त्री प्रत्यय as listed)
6. उपपदविभक्तिप्रयोगाः
7. भाषिककार्यम् (विशेषण–विशेष्य, कर्तृ–क्रिया, पर्याय / विलोम)
8. छन्दसां सोदाहरणलक्षणपरिचयः (अनुष्टुप्, इन्द्रवज्रा, उपेन्द्रवज्रा, उपजातिः, वंशस्थम्, वसन्ततिलका, मालिनी, शिखरिणी, शार्दूलविक्रीडितम्, मन्दाक्रान्ता)
9. अलङ्काराः (अनुप्रासः, यमकम्, श्लेषः; उपमा, रूपकम्, उत्प्रेक्षा, अर्थान्तरन्यासः)
10. संस्कृतसाहित्यस्य सामान्यपरिचयः

**Sources:** NCERT *व्याकरणवीथिः*, *संस्कृतसाहित्यपरिचयः*, *भास्वती* and *शाश्वती*. The chandas and alaṅkāra definitions follow *वृत्तरत्नाकरः* and *साहित्यदर्पणः*, as quoted in the NCERT and CBSE material.

**Series:** 15 tests, `CUET/Sanskrit/CUET SANSKRIT TEST 1–15.json` (existing file names kept).

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Questions | 50, all compulsory |
| Duration | 60 minutes |
| Marking | +5 / −1 / 0 |
| Options | 4, single correct |
| Language | Questions in Sanskrit (Devanagari) |

## 2. PYQ analysis (analysed, not stored)

The 2025 and 2026 NTA papers (AglaSem image scans) were read for pattern only. They are kept outside the repo and never copied.

**Content.** Almost every question is grammar or poetics. Forms are tested inside a sentence ("बालकः ____ क्रीडति", "लभ्-धातोः लट्-लकारे मध्यमपुरुषैकवचने किं रूपम्?"). Chandas questions ask for the number of syllables in a pāda, the lakṣaṇa and the identification of a quoted line. Alaṅkāra questions ask for the lakṣaṇa, often as a fill-in or a word-order item, and the identification of a verse. Each paper has one **unseen prose passage** (a short story) with about five questions that mix comprehension with the grammar of the passage (the order of the vibhaktis used, the subject of a verb, a प्रत्यय).

**Formats.**
- Direct and fill-in-the-blank (रिक्तस्थानं पूरयत).
- Match सूची-I / सूची-II (forms ↔ vibhakti, words ↔ प्रत्यय).
- Order items (क्रमेण व्यवस्थापयत): forms in vibhakti or puruṣa–vacana order, the words of a lakṣaṇa in order.
- Multi-select ("A, B केवलम्"): which words take पञ्चमी, which words in a sentence are विशेषण.
- No assertion–reason items.

**What the old series got wrong** (audit, `docs/audit/CUET-audit-report.md`):
- One-line explanations (100% under 150 characters).
- 151 templated stems.
- 2% CUET formats.
- The key never repeated a letter.
- The correct option was the longest in 26% of items.
- There was a fake past-paper reference.

## 3. Unit weight per test (50 questions)

| Unit | Qs |
|---|---|
| S1 शब्दरूपाणि, विभक्तिप्रयोगाः | 6 |
| S2 धातुरूपाणि | 6 |
| S3 सन्धयः | 5 |
| S4 समासाः | 5 |
| S5 प्रत्ययाः | 6 |
| S6 उपपदविभक्तिः | 4 |
| S7 भाषिककार्यम् | 5 |
| S8 छन्दांसि | 4 |
| S9 अलङ्काराः | 4 |
| S10 साहित्यपरिचयः | 5 |
| **Total** | **50** |

The five passage questions count inside these quotas:
- two in S7 (a comprehension question and a कर्तृ / क्रिया / विशेषण / पर्याय question from the passage);
- one in S1 (a vibhakti question on the passage);
- one in S5 (a प्रत्यय in the passage);
- one in S3 (odd tests) or S4 (even tests).

`san_check.py` flags a unit more than one question off its quota (`QUOTA`).

## 4. Difficulty (every test)

**8 easy / 32 medium / 10 hard.**

- **Easy:** a common form (बालक, फल, रमा; गम् लट्), a basic sandhi, a well-known author–work pair.
- **Medium:**
  - a less common form (पितृ, सखि, गो, राजन्, विद्वस्, आत्मन्);
  - a लृट् / लङ् / विधिलिङ् form;
  - a sandhi-viccheda;
  - a प्रत्यय split;
  - a समास-विग्रह;
  - the syllable count or gaṇa sequence of a metre;
  - the lakṣaṇa of an alaṅkāra.
- **Hard:**
  - forms that are easily confused (नृ, स्वसृ, अक्षि, पथिन्, आत्मनेपद लङ्);
  - an order item;
  - a multi-select in which every part must be checked;
  - identifying the metre or alaṅkāra of a quoted line;
  - an inference from the passage.

## 5. Formats (every test)

| Format | Count |
|---|---|
| Unseen passage (one original prose passage, about 80–150 words like the NTA passages, 5 linked questions) | 5 |
| Match सूची-I / सूची-II | 6 |
| Multi-select / statements ("(A), (C) केवलम्"), alternating "शुद्धम्" and "अशुद्धम्" | 6 |
| Order (क्रमेण व्यवस्थापयत) | 4 |
| Direct | 29 |

The 29 direct items include at least 3 fill-in-the-blank items and at least 3 "which is अशुद्धम् / not …" items. Host units for the match, multi-select and order formats rotate from test to test, so that no unit carries the same format in consecutive tests where a fresh host is possible.

## 6. Option quality (audit fix)

- **Distractors:** all four options belong to the same paradigm: four forms of the same word or root, four sandhis of the same type, four metres, four authors. Each distractor is a real form or name that a student might confuse with the answer, such as the same vibhakti in another vacana or the neighbouring lakāra.
- **Key:**
  - 13 / 12 / 13 / 12 in odd tests and 12 / 13 / 12 / 13 in even tests.
  - No letter appears more than 3 times in a row.
  - The correct option is never clearly the longest (`LONGEST`).
- **Answer patterns:** an order answer is never A, B, C, D in that order (`SEQ-ABCD`). The six match items in a test all have different answer patterns.
- **Order:** `shuffle_test.py` gives a random exam order and keeps the passage set together.

## 7. Facts and sources

- Forms follow the standard paradigms in NCERT *व्याकरणवीथिः*.
- **Alternate forms:** where a word has accepted alternates (for example ऋकारान्त षष्ठी-बहुवचनम्, or सखि), a question either accepts only one or names the form it tests.
- **Metres:** gaṇas, syllable counts and yati follow *वृत्तरत्नाकरः*.
- **Alaṅkāras:** definitions follow *साहित्यदर्पणः*.
- **Literature:** follows NCERT *संस्कृतसाहित्यपरिचयः* (poets, works, genres and periods).
- **Verses:** example verses are well-known standard illustrations, short enough to quote. Passages are original prose written for the series.

## 8. Explanations

Explanations are in Hindi, with the Sanskrit forms and sūtras. They follow `उत्तर:` → `क्यों:` → `अन्य विकल्प क्यों नहीं:` → `मुख्य बिंदु:`.
- **Grammar items:** the explanation gives the rule or the paradigm row, and for sandhi and प्रत्यय items the split.
- **Metre items:** it gives the gaṇas, the syllable count and the yati.
- **Order items:** it gives the reason for each position.
- **Match items:** it gives each pair.

## 9. Out of syllabus — never test

- Words, roots and lakāras not in the NTA list, for example लिट् or लुङ् forms, or roots such as भू when used as a target. Such forms may appear only inside a sentence, never as the answer.
- Sandhis not listed (प्रकृतिभाव, तुगागम).
- Samāsa sub-types beyond the list.
- Prakriyā-level sūtra derivations beyond a single named rule.
- Kāvya textbook passages recalled word for word (the passage is unseen prose).
