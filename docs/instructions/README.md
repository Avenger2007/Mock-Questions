# Instructions — one file per exam

Each exam has its own authoring rules, because the patterns, syllabi and marking differ.

| Exam | File | Status |
|---|---|---|
| CUET (UG) | [CUET_Instructions.md](CUET_Instructions.md) | Active (v3.1, CUET 2027 standard, 15 tests per subject) |
| IISER Aptitude Test (IAT) | [IAT_Instructions.md](IAT_Instructions.md) | 25 tests; authorised PYQ collection in [`PYQ/IAT/`](../../PYQ/IAT/); analysis/blueprint approval pending; 2027 pattern still to verify |
| NISER — NEST | [NISER_Instructions.md](NISER_Instructions.md) | v1 ready — 25 tests; waiting for PYQs (pattern verified from the official 2026 brochure) |
| COMEDK UGET | [COMEDK_Instructions.md](COMEDK_Instructions.md) | v1 ready — 25 tests; waiting for PYQs and official syllabus PDFs |

A new exam's file should copy the CUET file's structure: Aim, Strict Command, Genuine Authorship, Answer-Key Integrity, Reference Materials, Difficulty Standard, Series Structure, Workflow, Quality Checklist and Output Format. Then replace the exam-specific parts (pattern, marking, sections, syllabus source) with that exam's official documents.

`Hermes folder/Hermes cuet instructions.md` is a copy of the CUET file for the Hermes agent, so keep the two in sync.

Image prompts for each exam go in that exam's folder: `IISER/IAT_images.md`, `NISER/NEST_images.md`, `COMEDK/COMEDK_images.md` (and `CUET/<Subject>/CUET_<Subject>_images.md` for CUET).

**28 Oct 2026 order decision:** IAT, NEST and COMEDK are authored in final order. Do not shuffle questions/options or renumber their IDs after authoring; diagram filenames and image-register entries stay tied to those IDs. CUET keeps its own ordering workflow.
