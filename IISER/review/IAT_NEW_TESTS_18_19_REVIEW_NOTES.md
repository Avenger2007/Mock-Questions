# IAT New Tests 18–19: authored review and full-plan checkpoint

Prepared 5 November 2026 on branch `iat-tests-18-19`, based on `08cf347d4c5e38fc590116196f117f8d0561573f`. The two papers are original **review drafts**, pending independent hidden-key subject review and timed attempts before student release. The user's instruction authorises continued authorship and remote preservation; it is not scientific release approval.

## Deliveries and design

Each paper contains 60 single-correct questions, 15 in Biology, Chemistry, Mathematics and Physics, 180 minutes, +4/-1/0 and 240 marks. Each retains 9 easy, 42 medium and 9 hard questions. These are editorial tiers, not measured difficulty or official subject quotas. Options remain at fixed IDs with 15 correct answers per letter and no whole-paper short cyclic key.

| Paper | B E/M/H | C E/M/H | M E/M/H | P E/M/H | Images B/C/P | PDF pages |
|---|---|---|---|---|---|---|
| 18 | 2/11/2 | 3/10/2 | 2/10/3 | 2/11/2 | 3/2/4 | 44 |
| 19 | 2/11/2 | 2/11/2 | 3/10/2 | 2/10/3 | 2/3/7 | 45 |

The canonical JSON is `IISER/IAT NEW TEST 18.json` and `IISER/IAT NEW TEST 19.json`. Delivery JSON is byte-identical to canonical content. Each PDF contains the question paper and 60 worked solutions. Offline HTML embeds diagrams and parses all mathematics with strict KaTeX/mhchem. Final hashes are in `tests18_19/final_manifest.json`; final strict-expression counts are 356 and 309. The browser layout of HTML was not checked; the printable PDFs were checked independently with XeLaTeX and raster previews.

All 120 explanations include causal WHY and labelled rebuttals of the three actual alternatives. Numerical Biology and Chemistry show equations and intermediate accounting. All 30 Mathematics and Physics items per paper contain displayed worked derivations, not merely prose formula suggestions. Representative extended tasks include a charged capacitor junction, loaded-meter source calibration, reverse-osmosis endpoint, an inverse-function second derivative, refractory axon-front collision, a finite dipole in a nonuniform field, two-case mean deviation and curved-boundary escape angles.

## Syllabus and PYQ calibration

The stored official 2026 syllabus is the scope basis. The official examination page and syllabus page were sought on 5 November; direct page retrieval failed, while official indexed 2026 brochure results continued to support the 60-question/180-minute pattern. No official 2027 brochure has been verified. These are provisionally 2026-pattern preparation drafts, not verified 2027-compliant papers. Sources: https://www.iiseradmission.in/pages/admission/iat.html ; https://www.iiseradmission.in/pages/admission/syllabus.html ; https://web.iiseradmission.in/assets/pdfs/IB_IAT_2026_ENG.pdf .

The acquired PYQ analysis and ledger were revisited for task demand, scope and original wording. Every new Mathematics question has an individual recent-PYQ comparison with year, question number, original PDF/page, linked deductions and an estimated time in `tests18_19/math_pyq_calibration.json`. These 30 comparisons calibrate reasoning type; they do not assert identical difficulty. Some new easy questions are deliberately shorter than a hard reference example, and that limitation is explicit. Planned times are editorial estimates, not student timing data.

Repeated or unsafe seeds were replaced before freezing:

- Broad taxonomy repetition became delayed fungal karyogamy; repeated ovary-position diagrams became placentation and aestivation evidence.
- Routine DNA/ploidy patterns became unreduced parthenogenesis with separately fertilised endosperm, or compartment-specific protein tracking with a downstream bypass.
- Repeated ligand-counting became local versus global counting in a bridged ion. Simple common-ion or buffer substitutions became a two-observation inverse buffer problem and equivalence-point hydrolysis.
- A draft association calculation was retired in favour of a reverse-osmosis solvent-removal limit, distinct from the existing osmotic-pressure and association tasks.
- A final comparison found that the initial T18 Q31 two-axis circle was essentially the T10 Q31 task despite new coordinates and asking for a radius sum. It was replaced at its fixed ID by centre-line/chord reconstruction followed by an external tangent-length calculation.
- A routine limiting-reagent/yield draft at T18 Q27 was replaced by isotope abundance inferred from weighted atomic mass and then sample mole accounting.
- The unlisted general-series-convergence seed became odd-index and squared-term **geometric** sums. No general convergence test is used.
- Repeated lift normals, orbital ratios and uniform-field dipole rotation became limiting circular contact, off-centre tunnel dynamics, a mutual two-body orbit and exact nonuniform finite-dipole accounting.
- A spring launch now checks whether contact ends at all. A loop field reversal distinguishes zero instantaneous torque from stable equilibrium. A capacitor gap problem uses displacement-current flux areas, not conduction through the dielectric.

The late papers use unfamiliar contexts only when the required model is stated or follows from listed syllabus principles. The axon-front question explicitly supplies speed and refractoriness. The off-centre tunnel supplies uniform density and negligible removed mass. The source-in-sphere question excludes critical rays and checks both inward and outward initial directions. The ideal capacitor question states uniform field and neglects fringing. No extra named theorem or undeclared clinical inference is needed.

## Repetition review and option integrity

The full-bank text screen covers 19 papers and 1,140 questions. It finds no exact or number-masked identical stems. The two high-similarity pairs involving these papers both concern T18 Q34: T01 Q35 and T17 Q34. They were retained because the new squared-sine substitution, the earlier reflection-weighted trigonometric integral and the earlier rational polynomial division require different objects and solution choices. Generic “evaluate the integral” phrasing accounts for much of their textual similarity.

The screen did **not** detect the initially repeated two-axis circle at its threshold. That failure is recorded, rather than claiming a green screen proves originality. Nearest-wording comparisons were also read for all 120 new items, alongside the existing task focuses and stored patterns. Repeated themes remain intentional; number-swapped copies and cosmetic requests were retired. `method_signatures.json` preserves full constraints, requested result, governing reasoning and alternative mechanisms for later semantic comparison. Independent originality review is still pending.

Three explicit draft placement corrections were made in Test 19 before freezing: Q06 moved its existing correct content to A, Q28 to D and Q30 to D, with the displaced alternatives and explanation labels updated together. No random shuffling, question renumbering or correct-content change occurred in those corrections. Later scientific replacements kept T18 Q27 and Q31 at their original A positions. Calculation probes bind to literal selected contents, not letters alone.

## Full 25-test plan update

The old register covered broad families but did not establish every named subtopic. It is now accompanied by:

- `docs/blueprints/iat_25_test_plan.csv`: all 1,500 fixed slots, actual focuses/source hashes for Tests 1–19, the remaining 360 concrete briefs, named syllabus targets and review obligations.
- `docs/blueprints/iat_tests20_25_angle_briefs.tsv`: 24 section rows, each with 15 individually written future angles; no generic appended seed phrases.
- `docs/blueprints/iat_syllabus_coverage.csv`: 640 printed scope entries from the official stored syllabus, with prospective owners and explicit evidence/alignment status. The entries include related and repeated phrases, general descriptions and sentences; they are not claimed to be 640 unique independent examinable facts.
- `iat_coverage_plan_check.json`: 163/153/116/208 scope entries for B/C/M/P, zero unallocated entries and a maximum of nine scope entries per future owner.

A future owner is a **backstop for the coverage audit**. Before drafting, verify whether an earlier canonical question materially assesses the assigned scope and bind that evidence, or revise the future angle to test the outstanding topic. Literal-word evidence and wording-alignment flags are aids only. There are 211 entries without shared words in their brief, which require manual interpretation; this is not a finding of 211 missing topics. A scope entry must not be marked closed because a script assigned it or because a generic heading appeared in an explanation. This makes omissions visible without falsely asserting the whole syllabus is already exhausted.

Original family allocations, 60 slots per test, equal subject totals, fixed IDs and editorial tiers remain intact. Future questions still require full authorship, source checks and comparison against whatever has actually been authored by that time. In particular, preserve the hold on heading-only Linear Programming, and exclude general power-series tests, unlisted Doppler extensions, deleted detailed p-block units, Zener regulation and logic-gate questions unless a newer official syllabus expressly restores them.

The TSV is the established core register; the CSV is its expanded, spreadsheet-readable view. Review user edits to either before rebuilding. Canonical question JSON owns authored text. Literal future briefs own reservations, not completed questions. Do not silently overwrite a user's CSV changes.

## Verification and persistence

- All 19 papers and 1,140 items pass the structural/design validator. Tests 1–17, 1,020 canonical items, are byte-for-byte unchanged from baseline `08cf347`.
- All 85 author-side recalculation probes pass: exact rational and symbolic algebra, exhaustive small outcome spaces, Kirchhoff node equations, full dilute-acid charge balance and branch/boundary checks. They supplement the written proofs and are not an independent answer certification.
- Both PDFs contain 60 question labels and 60 solution labels, no missing-character or overfull-box warnings, and no body-empty pages. Visual review caught a header/footer-only page that the old check had incorrectly accepted. Section-ending spacing was repaired, and the exporter now removes header, footer and page number before testing content.
- All 21 figure rasters were inspected. PDF pages received contact-sheet layout review, with enlarged checks of selected multi-step solutions and the final corrected pages. This does not substitute for a fresh subject-expert reading of every equation.
- The two CSV views round-trip through workbook cells exactly, parse with 1,500 and 640 records, and agree with the core TSV on every slot. No XLSX variant is required for the requested CSV delivery.
- Remote checkpoint `9d60db0` was pushed before lengthy delivery work and its remote HEAD verified. Final delivery, plan and review changes are committed and pushed on the same named branch; previous branches and main are not overwritten.

Reproduction: run `python tools/iat/check_tests_18_19.py`, `python tools/iat/verify_tests_18_19.py` and the overlap screen. Export canonical JSON with `tools/iat/export_iat_review_tex.py` and the strict offline HTML exporter. For plan metadata run `python tools/iat/update_series_plan.py`, then execute a copy of `tools/iat/export_series_plan_csv.mjs` from a temporary directory whose node_modules links to the primary runtime, setting IAT_REPO_ROOT. Review manual CSV edits before this rebuild. Historical TSV assembly is frozen by `tests18_19_checkpoint.json`; subsequent fixes belong in canonical JSON and linked evidence.
