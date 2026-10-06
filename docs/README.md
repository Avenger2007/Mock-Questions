# Standard question JSON — version 1.0

This is the agreed starting specification for future admin import, not an importer already available in the application. Use [question-bank.schema.json](question-bank.schema.json) as the machine-readable contract and [example-question-bank.json](example-question-bank.json) as a complete template.

## What to generate

One UTF-8 JSON object per bundle, with `schemaVersion: "1.0"`, `bundleType: "question_bank"`, a stable `bundleId`, title, language (`en` or `hi`) and 1–1,000 questions. Do not include Markdown fences, comments or trailing commas in files intended for import.

Each question requires `externalId`, `type: "single_choice"`, subject, topics, difficulty, stem, exactly four options with unique IDs, answer, explanation and source. Supported subjects: mathematics, physics, chemistry, biology, english, general-aptitude. Difficulties: easy, moderate, hard.

IDs use lowercase letters/numbers separated by hyphens or underscores. Retain an external ID when requesting a revision; create a new ID for a different question. `answer.correctOptionId` identifies the correct option, independent of shuffled display order. V1 permits exactly one correct answer; numeric-response, multi-select and passage-group questions need a later explicit extension.

Marks, negative marks, exam mapping, duration and section rules belong to the test blueprint, not the reusable question. Exam patterns must be checked before publication; this schema alone does not certify full exam compatibility.

## Content blocks

`stem`, each option’s `content` and `explanation` use the same ordered array of typed blocks. The renderer reads explicit types; it does not guess whether ordinary text is a formula.

| Block          | Required content                     | Use                                          |
| -------------- | ------------------------------------ | -------------------------------------------- |
| `paragraph`    | `runs` array                         | Mix ordinary text and inline formulas        |
| `display_math` | `latex`, `spokenText`                | A separate equation line                     |
| `image`        | `assetId`, `alt`; optional `caption` | Managed diagram or graph uploaded separately |
| `table`        | `caption`, `headers`, `rows`         | Structured cells containing text/math runs   |

A paragraph/table-cell run is either `{ "type": "text", "text": "Find " }` or `{ "type": "math", "latex": "x^2", "spokenText": "x squared" }`. Do not insert raw HTML. Plain text supports Unicode characters and Hindi; mathematical notation uses explicit math runs.

In JSON source, every LaTeX backslash must be doubled:

```json
{
  "type": "display_math",
  "latex": "E = \\frac{1}{2}mv^2",
  "spokenText": "Energy equals one half times mass times velocity squared"
}
```

After JSON parsing, this is ordinary `\frac` LaTeX. Do not wrap the `latex` value in `$`, `$$` or Markdown. Use supported KaTeX syntax, `\mathrm{}` for unit text, and mhchem commands for chemistry, such as JSON `"\\ce{2H2 + O2 -> 2H2O}"`. `spokenText` is a required accessible description, not an alternative answer.

Diagram example, once an admin upload has created the referenced asset:

```json
{
  "type": "image",
  "assetId": "physics-circuit-001",
  "alt": "A 6 volt source connected in series to resistors of 2 ohms and 4 ohms",
  "caption": "Circuit for this question"
}
```

Do not use a remote URL, local file path or base64 image in place of `assetId`. Alternative text should convey the information needed to answer without revealing the solution. Tables must have the same number of cells in every row as in `headers`; each cell is an array of text/math runs.

## Validation and review

Schema validation checks structure, types, lengths and allowed fields. The eventual importer must also check unique question IDs, unique option IDs, answer references, rectangular tables, asset existence/permissions, supported TeX and total payload size. These cross-reference rules are not all expressible in this JSON Schema.

`source.kind` is `original`, `ai_assisted` or `licensed`. `source.reference` records provenance, such as author/review reference, generation record or licence reference; it is not proof of correctness or permission. AI-generated bundles must use `ai_assisted`. Every question still needs academic review, including options, explanations, units and accessibility text.

Keep complete answer-containing bundles inside authorized admin storage. Student test endpoints must return a separate projection without `answer` or unreleased `explanation`; hiding those fields with CSS is insufficient.

The example bundle illustrates a derivative, kinetic energy, chemical balancing and an organelle table. It is demonstration content awaiting academic review, not a published mock test.

## Instructions for your question generator

Provide the schema and example file with this instruction:

> Return only a JSON object conforming exactly to question-bank.schema.json version 1.0. Generate four-option single-choice questions in the requested subject, topics and difficulty. Use stable unique IDs, exactly one correctOptionId per question, and complete worked explanations. Represent formulas using math runs or display_math blocks; escape backslashes correctly in JSON. Use mhchem notation for chemical equations. Include meaningful spokenText for every formula. Do not invent asset IDs: omit image blocks unless supplied valid uploaded asset IDs. Set source.kind to ai_assisted and record the provided generation reference. Do not include marks, timing, HTML, unsupported fields or Markdown fences. Check the calculation, units, options and explanation agree before returning.

A generator’s self-check does not replace the importer’s validation or human approval. See [development phases](../DEVELOPMENT-PHASES.md) for the implementation and acceptance criteria.
