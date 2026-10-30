"""Validate the IAT-specific flat schema without changing authored content or order.

Usage: python validate_iat.py [path-to-test.json ...]
Checks structure and declared design constraints; not academic certification.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIELDS = ('id', 'section', 'subject', 'topic', 'sub_topic', 'class_level',
          'difficulty', 'format', 'question', 'options', 'correct_option', 'explanation')
NAMES = dict(zip('BCMP', ['Biology', 'Chemistry', 'Mathematics', 'Physics']))

def validate(path):
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)
    data = json.loads(path.read_text())
    ntest = data.get('test_number')
    check(data.get('total_questions') == 60, 'total_questions must equal 60')
    check(data.get('questions_to_attempt') == 60, 'all 60 questions must be available')
    check(data.get('duration_minutes') == 180, 'duration must be 180 minutes')
    check(data.get('maximum_marks') == 240, 'maximum must be 240 marks')
    check(data.get('marking_scheme') == {'correct': '+4', 'incorrect': '-1', 'unattempted': '0'}, 'marking scheme mismatch')
    check(data.get('status') in {'pending_revision', 'revised'}, 'invalid review status')
    for key in ['syllabus_source', 'notification_source', 'past_paper_reference', 'authoring_source', 'order_policy']:
        check(bool(data.get(key)), f'missing {key}')
    qs = data.get('questions', [])
    check(len(qs) == 60, f'{len(qs)} actual questions, expected 60')
    check([s.get('id') for s in data.get('sections', [])] == list('BCMP'), 'section metadata order must be B/C/M/P')
    tiers = Counter()
    keys = Counter()
    images = []
    seen_stems = set()
    image_registry = (ROOT / 'IISER/IAT_images.md').read_text()
    for n, q in enumerate(qs, 1):
        label = f'Q{n}'
        for key in FIELDS:
            check(key in q and bool(q[key]), f'{label}: missing {key}')
        expected_id = f'IAT27-T{ntest:02}-Q{n:02}'
        check(q.get('id') == expected_id, f'{label}: unstable/misordered ID')
        sec = 'BCMP'[(n-1)//15] if n <= 60 else None
        check(q.get('section') == sec and q.get('subject') == NAMES.get(sec), f'{label}: wrong section or subject')
        opts = q.get('options', [])
        check(len(opts) == 4, f'{label}: not four options')
        for letter, opt in zip('ABCD', opts):
            check(isinstance(opt, str) and opt.startswith(letter + ') '), f'{label}: option prefix {letter}')
        normal = [re.sub(r'\s+', '', opt[3:]).casefold() for opt in opts]
        check(len(set(normal)) == 4, f'{label}: duplicate option text')
        key = q.get('correct_option')
        check(isinstance(key, str) and key in 'ABCD' and len(key) == 1, f'{label}: invalid key')
        check(q.get('explanation', '').startswith(f'Answer: ({key})'), f'{label}: explanation/key disagreement')
        check(q.get('class_level') in {'11', '12'}, f'{label}: invalid class')
        check(q.get('difficulty') in {'easy', 'medium', 'hard'}, f'{label}: invalid tier')
        check(q.get('format') in {'conceptual', 'numerical', 'diagram', 'graph', 'data', 'experiment'}, f'{label}: invalid format')
        if q.get('format') == 'numerical':
            for part in ['Given:', 'Formula/Principle:', 'Step 1:', 'Common mistake:']:
                check(part in q.get('explanation',''), f'{label}: missing solution component {part}')
        stem = re.sub(r'\W+', '', q.get('question', '')).casefold()
        check(stem not in seen_stems, f'{label}: duplicate question stem')
        seen_stems.add(stem)
        tiers[q.get('difficulty')] += 1
        keys[key] += 1
        if 'image_reference' in q:
            image = q['image_reference']
            images.append(image)
            check(image == f'IAT_T{ntest:02}_Q{n:02}.png', f'{label}: wrong linked image ID')
            check((ROOT / data['image_base_path'] / image).is_file(), f'{label}: missing image')
            check(image in image_registry and expected_id in image_registry, f'{label}: missing image-register entry')
            check(bool(q.get('image_alt')), f'{label}: missing image alt text')
    check(tiers == Counter(easy=9, medium=42, hard=9), f'paper tiers {dict(tiers)}')
    check(keys == Counter(A=15,B=15,C=15,D=15), f'paper key balance {dict(keys)}')
    for i, sec in enumerate('BCMP'):
        rows = qs[15*i:15*(i+1)]
        expected_easy = 3 if i == (ntest-1)%4 else 2
        expected_hard = 3 if i == ntest%4 else 2
        check(Counter(q['difficulty'] for q in rows) == Counter(easy=expected_easy,medium=15-expected_easy-expected_hard,hard=expected_hard), f'{sec}: wrong tier split')
        counts = Counter(q['correct_option'] for q in rows)
        check(set(counts) == set('ABCD') and max(counts.values())-min(counts.values()) <= 1, f'{sec}: unbalanced key')
    letters = ''.join(q['correct_option'] if isinstance(q.get('correct_option'), str) else '?' for q in qs)
    check(not re.search(r'(.)\1{3}', letters), 'four identical answers in a row')
    check(len(images) == len(set(images)), 'duplicate image reference')
    report = {'file': str(path.relative_to(ROOT)), 'questions': len(qs), 'tiers':dict(tiers),
              'answer_counts':dict(keys), 'images':len(images), 'errors':errors,
              'scope':'Mechanical schema/design validation only; academic review remains required.'}
    return report

if __name__ == '__main__':
    paths = [Path(p).resolve() for p in sys.argv[1:]] or sorted((ROOT/'IISER').glob('IAT TEST *.json'))
    if not paths:
        raise SystemExit('No IAT papers found')
    reports = [validate(p) for p in paths]
    print(json.dumps(reports, indent=2))
    raise SystemExit(1 if any(r['errors'] for r in reports) else 0)
