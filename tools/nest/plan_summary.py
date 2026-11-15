"""Rewrite NISER/NEST_25_Test_Plan.md from the plan CSV, the generator taxonomy and the PYQ calibration file.
usage: python3 tools/nest/plan_summary.py      (documentation only; never changes the CSV)"""
import csv, collections, json, importlib.util
spec = importlib.util.spec_from_file_location('p', 'tools/nest/plan_25_tests.py'); p = importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
rows = list(csv.DictReader(open('NISER/NEST_25_Test_Plan.csv', encoding='utf-8')))
cal = json.load(open('docs/blueprints/nest_plan_calibration.json'))
d = collections.Counter((r['chapter_code'], r['difficulty_target']) for r in rows)
st = collections.Counter(r['state'] for r in rows)
nch = sum(len(p.CH[s]) for s in 'BCMP'); nf = sum(len(c[4]) for s in 'BCMP' for c in p.CH[s])
o = []; A = o.append
A('# NEST 25-test plan\n')
A(f"Status on 15 November 2026: **plan only; no NEST test is written yet** ({st['planned']} of {len(rows)} slots are `planned`). The slot table is [NEST_25_Test_Plan.csv](NEST_25_Test_Plan.csv). It is built and checked by `tools/nest/plan_25_tests.py`; this page is rewritten by `tools/nest/plan_summary.py`. Rules: [NISER_Test_Instructions.md](NISER_Test_Instructions.md). Syllabus: [Syllabus.md](Syllabus.md). Past-paper analysis: [nest_pyq_analysis.md](../docs/blueprints/nest_pyq_analysis.md).\n")
A('## What the plan fixes\n')
A('- **25 tests × 80 questions = 2,000 slots**, 500 per subject: Biology Q1–20, Chemistry Q21–40, Mathematics Q41–60, Physics Q61–80.\n- **Fixed IDs** `NEST27-TNN-QNN`.\n- **Difficulty:** 3 easy, 13 medium, 4 hard in every section of every test; each chapter gets about 15% easy and 20% hard of its own slots.\n- **Coverage:** every chapter of the official syllabus has slots, spread evenly over the 25 tests, and every focus line is used at least once.\n- **No repetition by design:** every slot has a different (chapter, focus, angle). The focus is the syllabus sub-topic; the angle is the kind of task.\n')
A('## How it was built, and its limits\n')
A('- Method taken from the IAT plan (`docs/blueprints/iat_25_test_plan.md` and `.csv`): fixed slots, a chapter taxonomy from the official syllabus, a stated difficulty mix, and one record per question that is updated when the test is written.\n- Added after the IAT audit: uniqueness of (chapter, focus, angle) is enforced by the checker; plan and tests are reconciled in the same commit; topics not in the syllabus have no slots.\n- **Chapter weights = 60% syllabus breadth + 40% share in the NEST 2024 (two sessions), 2025 and 2026 papers**, rounded to 5, minimum 5. The past-paper sample is 80 questions per subject, so the weights are a guide, not a forecast.\n- The NEST 2027 syllabus was not published on 15 November 2026; the plan uses the NEST 2026 syllabus.\n- The `angle` is a brief, not a format label. The question `format` is set when the question is written.\n')
A('## CSV columns\n')
A('| Column | Meaning |\n|---|---|\n| `test`, `question`, `id` | fixed position and ID |\n| `section`, `subject` | B, C, M or P |\n| `chapter_code`, `chapter`, `class_level` | chapter from `Syllabus.md` |\n| `focus` | the syllabus sub-topic the question must test |\n| `angle` | the kind of task |\n| `difficulty_target` | easy, medium or hard |\n| `state` | `planned`, then `authored`, then `audited` |\n| `source_json`, `question_sha256` | filled when the question exists |\n| `notes` | reason for any change to the slot |\n')
A('## Task angles\n')
for s, name, _ in p.SUBJECTS: A(f'- **{name}:** ' + '; '.join(p.ANGLES[s]) + '.')
A('\n## Chapter allocation\n')
A('"Past papers" is the number of questions from that chapter in the four papers analysed (out of 80 per subject). "Breadth" is the slot count before calibration.\n')
for s, name, _ in p.SUBJECTS:
    c11 = sum(c[3] for c in p.CH[s] if c[2] == 11)
    A(f'### {name} (500 slots; Class 11: {c11}, Class 12: {500 - c11})\n')
    A('| Code | Chapter | Class | Past papers | Breadth | Slots | Easy / Medium / Hard | Focus lines |\n|---|---|---:|---:|---:|---:|---:|---:|')
    for code, ch, cls, n, foci in p.CH[s]:
        k = f'{s}-{code}'
        A(f"| `{k}` | {ch} | {cls} | {cal['pyq_counts_4_papers'][s].get(code, 0)} | {cal['breadth_slots_before_calibration'][s][code]} | {n} | {d[(k,'easy')]} / {d[(k,'medium')]} / {d[(k,'hard')]} | {len(foci)} |")
    A('')
A('## Focus lines by chapter\n')
for s, name, _ in p.SUBJECTS:
    A(f'### {name}\n')
    for code, ch, cls, n, foci in p.CH[s]: A(f'- **{ch}** (`{s}-{code}`): ' + '; '.join(foci) + '.')
    A('')
A('## Using the plan\n')
A('1. Print the 80 rows of the test you are about to write.\n2. Write each question to its row. If a row cannot be met, edit the row and give the reason in `notes`; keep the chapter total.\n3. After the test is written, set `state`, `source_json` and `question_sha256` for its 80 rows in the same commit.\n4. Run `python3 tools/nest/plan_25_tests.py --check`. It fails if a (chapter, focus, angle) is used twice, if a section is not 20 questions with 3/13/4, or if a focus line has no slot.\n5. The generator refuses to rewrite the CSV once any row is no longer `planned`, so authored tests cannot be overwritten.\n')
A('## Checks passed\n')
A(f'- {len(rows)} slots, {len({r["id"] for r in rows})} different IDs.\n- {len({(r["chapter_code"], r["focus"], r["angle"]) for r in rows})} different (chapter, focus, angle) tasks.\n- Every one of the 100 sections has 20 slots with 3 easy, 13 medium, 4 hard.\n- All {nch} chapters and all {nf} focus lines have at least one slot.\n- Most questions from one chapter in one section: {max(collections.Counter((r["test"], r["chapter_code"]) for r in rows).values())}.\n')
open('NISER/NEST_25_Test_Plan.md', 'w', encoding='utf-8').write('\n'.join(o))
print('wrote NISER/NEST_25_Test_Plan.md', nch, 'chapters', nf, 'focus lines')
