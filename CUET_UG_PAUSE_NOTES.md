# CUET UG — pause notes (14 Nov 2026)

The CUET UG workstream is paused. No CUET file is to be changed until it is resumed.

**Last CUET commit on `main`:** `4480841` (docs(agriculture): series index, README row and worklog for the completed series)

## Done (16 subjects, 241 tests, 13,260 questions; every file has status `revised`)

Accountancy (16 tests), Agriculture, Biological Science, Chemistry, Computer Science, Economics, English, General Test, Geography, Hindi, History, Mass Media, Mathematics, Physics, Political Science, Sanskrit (15 tests each).

`validate_papers.py CUET` reports zero issues for each of these subjects at the commit above.

## Pending (7 subjects with a syllabus PDF but no tests, in A–Z order)

1. Anthropology (303) — next
2. Business Studies (305)
3. Environmental Science (307)
4. Home Science (315)
5. Performing Arts (320)
6. Psychology (324)
7. Sociology (326)

## Open issues

- No subject teacher has proofread the explanations.
- Answers that rest on figures that change each year (leading states, production ranks) need a recheck before CUET 2027.
- Only Agriculture Tests 10–15 were checked by hand against the coverage ledger for the same fact asked in new wording. Agriculture Tests 1–9 and the other 15 subjects relied on the automatic overlap check, which compares wording only.
- Untracked macOS " 2" duplicate files and stray scripts in `CUET/Physics` are left as they are, on purpose.

## How to resume

Read `docs/blueprints/<subject>.md` and its `_coverage.md`, copy `tools/cuet_agri/` for the new subject, and follow the Agriculture entry in `Worklog.md`.
