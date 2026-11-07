"""Assemble manually authored fixed-order rows into the existing review schema."""
import csv
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[2]
# Historical TSV snapshots must never overwrite a reviewed canonical revision.
for existing in (root / 'IISER').glob('IAT*TEST*.json'):
    if json.loads(existing.read_text()).get('content_revision') == 'milestone15_fix_v1':
        raise SystemExit('Historical assembly disabled: edit the corrected canonical JSON; see IISER/revisions/README.md.')

base = json.loads((root / 'IISER/IAT NEW TEST 13.json').read_text())
plan = {(int(r['test']), int(r['question'])): r for r in csv.DictReader((root / 'docs/blueprints/iat_25_test_slots.tsv').open(), delimiter='\t')}
images = {
    14: {2: 'Five-part flower with united sepals, free petals and stamens, and superior fused ovary',
         10: 'Plants feed herbivores A and B with 1000 and 600 kJ; predator receives 100 and 90 kJ',
         16: 'Linear CO2 bond dipoles and bent water bond dipoles',
         20: 'Daniell cell with zinc and copper electrodes and labelled solution concentrations',
         27: 'Two-stage reaction pathway from A and B through C to D',
         48: 'Force versus position rising to 4 N at 2 m and remaining 4 N until 3 m',
         51: 'Upright floating block with upper and submerged height',
         53: 'Two equal positive charges at x=-a and x=+a',
         57: 'Converging lens with object 5 cm to its left and focal points 10 cm away'},
    15: {2: 'Frog heart with two atria, one ventricle, and pulmonary return to left atrium',
         4: 'Leaf cross-section with chloroplast-rich bundle sheath and surrounding mesophyll',
         17: 'Six monodentate donors and three bidentate donors filling six sites',
         24: 'Aniline to acetanilide to para-bromoacetanilide to para-bromoaniline',
         27: 'Arrhenius lines with slopes -6000 K and -3000 K',
         48: 'Open water tank accelerating right with a left-high inclined free surface',
         57: 'Glass to air interface, incidence 50 degrees and refractive indices 1.5 and 1.0',
         60: 'Two slits, thin phase sheet at one slit, and screen with distance D'},
}
for t in (14, 15):
    data = {k: v for k, v in base.items() if k != 'questions'}
    data.update(test_id=f'IAT27_TEST_{t:02}', title=f'IAT New Test {t}',
                test_number=t, revision_date='2026-11-03')
    questions = []
    for sec in 'bcmp':
        with (root / f'IISER/authoring/test{t}_{sec}.tsv').open() as f:
            for row in csv.reader(f, delimiter='\t'):
                assert len(row) == 9, (t, sec, row)
                n = int(row[0])
                slot = plan[t, n]
                assert slot['subject'].lower() == sec
                explanation = re.sub(
                    r'\\n(?=(?:Given:|Formula/Principle:|Step \d+:|Worked derivation:|Why:|Why not the others:|Key point:))',
                    '\n', row[8])
                question = dict(
                    id=slot['id'], section=sec.upper(),
                    subject={'b': 'Biology', 'c': 'Chemistry', 'm': 'Mathematics', 'p': 'Physics'}[sec],
                    topic=slot['chapter'], sub_topic=slot['focus'],
                    class_level=slot['class_level'], difficulty=slot['difficulty_target'],
                    format=row[1], question=row[2],
                    options=[f'{letter}) {value}' for letter, value in zip('ABCD', row[3:7])],
                    correct_option=row[7], explanation=explanation)
                if n in images[t]:
                    question.update(image_reference=f'IAT_T{t:02}_Q{n:02}.png',
                                    image_alt=images[t][n])
                questions.append(question)
    data['questions'] = questions
    (root / f'IISER/IAT NEW TEST {t}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
