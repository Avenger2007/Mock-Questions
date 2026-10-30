# Test 1 verification and manual-review notes

29 October 2026. Canonical source: `IISER/IAT TEST 1.json`. Status: `pending_revision`; not approved for student publication.

## Completed verification

- 60 questions in stable order; 15 per subject; correct section ranges; 180 minutes; maximum 240; +4/-1/0.
- Editorial tiers: Biology 3 easy / 9 medium / 3 hard; Chemistry, Mathematics and Physics each 2/10/3. Total 9/39/12.
- Exactly four labelled options per question; key/explanation agreement; each answer letter occurs 15 times overall and three or four times per subject; no run exceeds three. No identical normalized stems or option text detected within the paper. This is not a guarantee against every semantic similarity.
- All six exact diagrams are present and linked to the correct IDs, with alt text and image-register entries. Q54 supply and resistor labels were spaced apart during visual review. Figures are enlarged for legibility in the final PDF.
- 328 delimited expressions parse with KaTeX and mhchem in strict error mode; all images load; no detected horizontal overflow or oversized question/solution blocks.
- Read all 60 stems and solutions during authorship and review; rechecked numerical derivations. Forty-five additional arithmetic/enumeration probes pass, including exhaustive arrangements for Q32/Q40, numerical quadrature for Q35/Q44/Q46/Q59, direct vector operations for Q36/Q45, connected-circuit KCL for Q54 and integer coincidence search for Q60. Inputs were transcribed from the stems: this is a supporting computational check, not an independent academic examiner.
- Rendered all 49 PDF pages for visual inspection, with detailed checks of figures and chemical/mathematical typography. Questions occupy pages 2–23, key page 24 and worked solutions pages 25–49. No blank pages or observed clipped/overlapping content remain.
- The delivery JSON is a byte-identical copy of the canonical source. The render-check manifest binds the source, delivery copy, PDF, HTML and diagrams by SHA-256. If content changes, regenerate and recheck; do not assume this record applies to a later revision.
- Confirmed the final regenerated PDF matches all 49 visually inspected page renders pixel for pixel; every Q1–Q60 heading occurs once in the paper and once in the solutions. Confirmed all C/M/P chapter profiles contain 15 slots and jointly cover all their retained taxonomy families. Validator negative checks detect a wrong section, missing image, null key and a 59-question file.

## Changes resolved during review

- Q40 distractors now represent specific counting mistakes: four-cycles only, choosing the correct pair only, or allowing extra fixed points. The correct value remains 3/16 (C).
- Q24 now requires selective functional-group tracking, molecular formula changes and stereocentre/E/Z eligibility. Its result is C8H14O2 and four stereoisomers (C); it no longer uses the earlier, less demanding functional-group-only wording.
- Q55 covers nuclear decay bookkeeping, replacing the initial gravitation slot in the draft plan. The Physics section now has seven Class 11 and eight Class 12 primary topics. Gravitation is explicitly reserved in later profiles.
- Calculator instructions follow the official 2026 brochure: an on-screen non-programmable scientific calculator is available; personal calculators are not allowed.

## Human review required

1. Check all 60 selected answers and alternatives for scientific accuracy, ambiguity and single-answer uniqueness. Review the longer assumptions in B4/B11/B13, C20/C24 and P49/P54/P60 especially carefully.
2. Confirm current syllabus fit at sub-topic level. Q24 combines organic isomerism with carbonyl and alcohol reactions; Q33 combines functions and optimisation; Q53 uses electrostatic work in addition to the field graph. These connections should remain accessible from the listed syllabus.
3. Review difficulty and length in a timed attempt. The 168-minute estimate is editorial, not measured; some candidates may spend substantially longer in Mathematics or Physics.
4. Consider distractor quality and language accessibility. A balanced answer key is a formatting property, not evidence that question difficulty is correct.
5. Check diagram fidelity and whether each displayed label is sufficient. No diagram filename, question ID or option order should be shuffled during corrections.
6. Verify the eventual 2027 syllabus, notification and calculator policy before claiming target-year compliance. PYQ priorities are descriptive and do not guarantee the next paper's topics.

## Scope of the PYQ findings

Nine English papers, 539 questions, missing 2020, incomplete 2025 English copy, provisional reordered 2026 key. Difficulty tags are editorial; answer-key certification was not part of the topic-tagging exercise. No reliable score/percentile, cut-off or item-level probability forecast can be produced from these data alone. The 25-test chapter reservation is complete at that level; exact subsequent question angles remain future work after pilot feedback.
