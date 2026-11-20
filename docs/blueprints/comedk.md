# COMEDK UGET mock series blueprint

Provisional 2027 preparation, anchored to the three official 2026 subject PDFs. See [sources](../../COMEDK/SOURCES.md), [PYQ calibration](comedk_pyq_analysis.md), and [authoring instructions](../instructions/COMEDK_Instructions.md).

## The 25-paper schedule

| Schedule file | Role |
|---|---|
| [25-test plan](comedk_25_test_plan.csv) | Paper numbers, progression, pacing focus and exact composition |
| [Slot plan](comedk_25_test_slots.csv) | All 4,500 fixed proposed slots, class, chapter, source page, fine scope anchor, visit number and difficulty target |
| [Syllabus coverage](comedk_syllabus_coverage.csv) | 494 working scope anchors, planned counts, first scheduled slot and separate evidence fields |
| [Angle register](comedk_angle_register.csv) | The specific reasoning each approved item will test, with the closest authored or past-paper comparison |
| [Plan check](comedk_plan_check.json) | Verification of initial scope and quota reservations |

Each paper has 60 questions per subject, with 20 Class XI and 40 Class XII per subject. The class allocation is an editorial translation of COMEDK's approximate 33:67 guidance. The 9/39/12 easy/medium/hard mix is also a house target. A 180-minute paper leaves an average minute per question. As a design budget, 9 × 30 seconds plus 39 × 50 seconds plus 12 × 100 seconds per subject yields 171 minutes across PCM, leaving 9 minutes in the design budget. These are editorial estimates. Use candidate attempts when available to measure pace and identify delays.

The schedule interleaves chapters and classes before authoring. The first pass assigns every working scope anchor by Test 5. Further passes revisit the scope with a new reasoning demand each time. Each subject/class/chapter group has at least 16 reservations and each anchor has at least five. Coverage means spaced representation across the series, not identical chapter weights or every chapter on every paper. The granular anchors paraphrase source phrases and sometimes group closely related items. Before drafting a grouped anchor, choose one explicit aspect and track its evidence. At series close check PDF-level scope independently instead of inferring exhaustive coverage from the 494 counts.

Tests 1–8 establish reliable short-model choices and clean calculations. Tests 9–17 introduce more comparison and chained inference within the same timing envelope. Tests 18–25 use mixed rehearsal with greater emphasis on assumptions, endpoints and time pressure. Every paper still contains a broad subject mix. The pacing focus is guidance for a selection of items, not a chapter or question-template restriction. The schedule uses syllabus breadth to allocate slots because the available PYQs cannot support statistically defensible chapter frequencies.

## How to prevent repeated questions

The slot CSV reserves content, not question angles. Before writing a batch, assign and review a distinct task for every intended slot. Use the angle register to record the object, givens, constraints, representation, governing method, decisive inference, requested result and likely mistakes. Compare it with earlier COMEDK angles, stems and worked solutions for repeats. Use relevant COMEDK PYQs to check style, intended solution effort and accidental copying. This comparison scope is COMEDK only. Search by concept as well as wording. Require a concrete explanation of what decision changes for the student. A unique slot, different question format, new numbers or an inverse question is insufficient.

| Recurring scope | A workable pair of distinct angles | Reject as an apparent variation |
|---|---|---|
| Physics, Wheatstone network | Use a symmetric diagram to decide whether a central branch carries current. In a separate task, reason how a deliberate arm change breaks a balance and determine the sign of the detector response. | Recompute the same missing resistance on the same balanced network with larger values. |
| Physics, photoelectric effect | Recover the work function from a threshold-frequency plot. Separately compare current and maximum energy after changing intensity at fixed frequency. | Ask for the same graph intercept using rescaled axes with no new inference. |
| Chemistry, kinetics | From successive equal half-lives identify the applicable order. Separately compare two catalyst routes using the activation barrier while holding the pre-exponential factor fixed. | Change Arrhenius slopes and swap reaction labels in the same compare-the-barriers task. |
| Chemistry, organic reactions | Infer which retained structural feature explains a reagent's selectivity. Separately eliminate a proposed route using an incompatible condition. | Reuse the same reagent sequence and alter an inert substituent. |
| Mathematics, definite integrals | Use reflection of the integrand to prove cancellation on a symmetric interval. Separately build an area integral from a sign change and two bounded pieces. | Swap coefficients or reverse knowns in the same area-under-a-parabola task. |
| Mathematics, probability | Use total probability to combine mutually exclusive sources. Separately decide if conditioning changes the probability of a specified event from a supplied table. | Change only the counts in an otherwise identical conditional-draw tree. |

These are illustrations rather than reusable question skeletons. The angle register also contains 12 proposed tasks tied to actual Test 1 slots, four per subject. Their nearest evidence comparisons and difficulty still need review before approval. Return unsuitable reservations to scope review with a reason and replace them without losing coverage. Detect literal, number-masked and near-duplicate stems mechanically. Do a separate semantic review, particularly for figure-led questions or reworded calculations that text similarity misses.

## Pilot and series handoff

Draft in batches of two, working through each paper in PCM order. For the first paper in each batch, re-solve from the question text before reading its key, check the fastest valid route, and record decision steps, computation length and diagram or reading load. Recheck the label against that route. Compare representative easy, medium and hard questions in each subject with readable COMEDK PYQs at similar syllabus depth. Fix ambiguous items and strengthen or replace overlabelled items while preserving the agreed subject mix. Carry those corrections into the second paper before it is locked.

Difficulty and pacing from this process are provisional. When student data become available, use a fresh, full 180-minute attempt by a prepared COMEDK student. Record time by subject, attempted and skipped items, accuracy by difficulty tier and items that caused delays. Apply changes to the next drafts and log the evidence behind each change. Drafting can proceed while candidate timing is pending.

Keep a ledger of exact syllabus areas covered by each final question. Use canonical JSON as the source for PDFs, delivery JSON, HTML and the series index. Refresh and verify hashes for affected outputs after a stem, solution, option or figure changes. Update coverage and angle records in the same change.

Initial schedule check:

```sh
python3 tools/comedk/plan_series.py
```

The baseline checker compares generated tables against the initial schedule. After approval and authorship begin, reconcile the live ledgers from the final canonical files and preserve logged editorial changes. Do not overwrite live ledgers by rerunning the initial generator.
