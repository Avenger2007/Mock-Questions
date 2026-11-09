# Blueprint — CUET (UG) 2027 Mass Media / Mass Communication (318)

**Syllabus:** `CUET SYLLABUS/md/Mass Media - 318.md` (NTA "for the year 2026", the latest published). It has eight units and no single prescribed textbook. Content follows the CBSE Class XI–XII *Mass Media Studies* curriculum that the NTA list mirrors, plus standard, checkable facts: the Constitution, Acts of Parliament, Supreme Court judgments, and official histories of AIR, Doordarshan and Indian cinema.
**Series:** 15 tests, `CUET/Mass Media/CUET MASS MEDIA TEST 1–15.json` (existing file names kept).

## 1. Paper pattern (NTA)

| Item | Value |
|---|---|
| Questions | 50, all compulsory |
| Duration | 60 minutes |
| Marking | +5 / −1 / 0 |
| Options | 4, single correct |

## 2. PYQ analysis (analysed, not stored)

Papers read for pattern only (kept outside the repo, never copied): NTA CUET (UG) Mass Media 2024, 2025 and 2026 (via AglaSem, image scans).

- **Formats.** Every year has Match List-I / List-II items. Examples are social media platforms and their features, headline types, laws and cases, and models and their authors. There are "which of the statements are correct" sets (media history dates, qualities a radio jockey needs) and chronology items (films by release year). The rest are direct questions, including fill-in-the-blank items and "which is NOT" items.
- **Content.** All eight units appear. The heaviest areas are:
  - media history and landmark dates (AIR, Doordarshan, newspapers, BBC, Voice of America);
  - journalism practice (headlines, news values, inverted pyramid);
  - media law (Article 19(1)(a), landmark cases, RTI, sedition, privacy);
  - cinema (Lumière, Grierson, Phalke, parallel cinema, film stages);
  - radio scripts and studio equipment;
  - TV production and scheduling.
- **Off-syllabus drift in the PYQs.** Some items are general knowledge (the Red Fort's main gate, Kesavananda Bharati on basic structure, corporate ownership trivia). They are **not** copied as a pattern. This series stays inside the eight syllabus units.
- **Difficulty.** Mostly moderate. Difficulty comes from close distractors:
  - Grierson vs Flaherty;
  - Lasswell vs Shannon–Weaver;
  - dynamic vs condenser microphones;
  - paid news vs advertorial;
  - stripping vs stacking.
  It also comes from four-pair matches and from ordering dates.

**What the old series got wrong** (audit, `docs/audit/CUET-audit-report.md`):
- The correct option was clearly the longest in **73%** of items.
- 75 options carried an "(or …)" giveaway.
- Distractors were absurd.
- Fourteen items were on "Film Theory", which is out of syllabus.
- 1% used CUET formats.
- There was a fake past-paper reference.

This series fixes all six.

## 3. Unit weight per test (50 questions)

| Unit | Syllabus unit | Qs |
|---|---|---|
| M1 | Communication: levels and models; culture and communication (representation, stereotyping); communication and social change; evolution of newspapers, radio, TV and new media in India | 9 |
| M2 | Journalism: news (definition, values, components); qualities of a journalist; reporting and editing (inverted pyramid, 5Ws and 1H, headlines, copy editing); photojournalism; media laws and ethics | 9 |
| M3 | Advertising (concepts and process, functions, types incl. cross promotion, merchandising and covert advertising, forms, campaigns) and Public Relations (PR and media management, brand image, tools and steps, campaigns, crisis management, the PRO) | 7 |
| M4 | TV production process (pre-production, production, post-production) and programmes, formats, audiences | 5 |
| M5 | Radio: writing for radio (script characteristics) and radio recording (studio, microphones, amplifier, mixer, speakers, transmission) | 5 |
| M6 | Cinema: early experiments (Lumière brothers, Grierson, Flaherty, Phalke); production process and stages, documentary making; genre theory and genres; parallel cinema (*Manthan*) | 6 |
| M7 | Social media: definition, platform types, role in democracy, collective identity, cyber activism, cyber crime (bullying, stalking, trolling, fraud), netiquette | 5 |
| M8 | New media: the internet as the meeting point of media; the old few-to-many model (huge organisations, infrastructure, revenue); the changed paradigm (individuals post; one medium triggers another; many sources; global, rapid distribution); socio-political implications; emerging trends; media convergence | 4 |
| **Total** | | **50** |

The 5-question case set counts inside its unit's quota. When the case unit has fewer than 5 other slots, questions are moved from a neighbouring unit (±1 per unit), and the total stays at 50.

## 4. Difficulty (every test)

**8 easy / 32 medium / 10 hard.**

- **Easy:** one well-known fact (a level of communication, a pioneer, a date, a platform type).
- **Medium:** a close distractor set, a term and its meaning, a law and its subject, a stage and its tasks, or a match whose pairs are well known.
- **Hard:** a multi-statement judgement, a chronology of four close events, a four-pair match where every pair is plausible, or the inference item in the case set.

## 5. Formats (every test)

| Format | Count |
|---|---|
| Case set (an original scenario or account: a news copy, a campaign, a radio brief, a production plan, a crisis; 5 linked questions) | 5 |
| Match List-I / List-II | 7 |
| Statements "(A)–(D), choose the correct / incorrect" | 6 |
| Sequence (chronology, process stages, story structure) | 4 |
| Direct, including at least 3 fill-in-the-blank and 2 "which is NOT / wrongly matched" items | 28 |

Assertion–reason items are not used, because none appeared in the papers analysed.

## 6. Option quality (audit fix)

- All four options come from the **same category**: four models, four microphones, four Acts or four years. Every distractor is a real term that a half-prepared student could pick.
- There are no "(or …)" glosses and no joke options.
- The key per test is 13 / 12 / 13 / 12 (rotated), with no letter more than 3 times in a row. The correct option is never clearly the longest (within 1.15× of the next-longest).
- A sequence answer is never A, B, C, D in that order.
- Match patterns differ within a test.
- `shuffle_test.py` gives a random exam order and keeps the case set together.

## 7. Facts and sources

- **Dates and firsts** follow the official histories:
  - *Hicky's Bengal Gazette* 1780;
  - the Radio Club of Bombay 1923;
  - IBC 1927, ISBS 1930, All India Radio 1936, Akashvani 1957;
  - TV in Delhi 15 Sept 1959; SITE 1975–76; Doordarshan made separate 1976;
  - colour TV and the national telecast 1982; *Hum Log* 1984;
  - Prasar Bharati 1997;
  - the Lumière show on 28 Dec 1895; *Raja Harishchandra* 1913; *Alam Ara* 1931.
- **Laws** are named by Act or Article, for example Article 19(1)(a) and 19(2), the RTI Act 2005, the Press Council Act 1978, the Cinematograph Act 1952, the IT Act 2000 and the Copyright Act 1957.
  - Where criminal law changed (defamation and the old sedition section, after the Bharatiya Nyaya Sanhita took effect on 1 July 2024), items test the concept or the judgment. They avoid an IPC section number that is no longer in force.
- **Judgments** are cited by name and year, for example Romesh Thappar (1950), Bennett Coleman (1972), Shreya Singhal (2015) and K.S. Puttaswamy (2017).
- Case sets are **original** scenarios written for the series.

## 8. Explanations

`Answer:` → `Why` → `Why not the others` → `Key point`. For statement items, the explanation names each false statement and corrects it. For sequence items, it dates or explains every step.

## 9. Out of scope — never test

- Film theory (auteur theory, montage theory and the like), which is not in the 2026 syllabus.
- Media ownership trivia, and general-knowledge items unrelated to the media.
- Constitutional law beyond freedom of speech and its limits.
- Current-affairs items that may date before 2027, such as live platform statistics and recent awards.
