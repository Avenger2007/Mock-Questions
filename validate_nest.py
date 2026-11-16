"""Validate NEST test files (structure and house rules only; not an academic check).
usage: python3 validate_nest.py "NISER/NEST TEST 1.json" [...]     (no arguments = all NISER/NEST TEST *.json)"""
import json, re, sys, csv, glob
from collections import Counter
NAMES = dict(B='Biology', C='Chemistry', M='Mathematics', P='Physics')
FORMATS = {'conceptual', 'numerical', 'graph', 'data', 'diagram', 'experiment'}
plan = {r['id']: r for r in csv.DictReader(open('NISER/NEST_25_Test_Plan.csv', encoding='utf-8'))}
register = open('NISER/NEST_images.md', encoding='utf-8').read()

def validate(path):
    e = []; d = json.load(open(path, encoding='utf-8')); n = d.get('test_number'); qs = d.get('questions', [])
    ck = lambda c, m: e.append(m) if not c else None
    ck(d.get('total_questions') == 80 and len(qs) == 80, 'need 80 questions')
    ck(d.get('duration_minutes') == 180, 'duration must be 180')
    ck(d.get('marking_scheme') == {'correct': '+3', 'incorrect': '-1', 'unattempted': '0'}, 'marking scheme')
    ck([s.get('id') for s in d.get('sections', [])] == list('BCMP'), 'sections must be B, C, M, P')
    stems = set()
    for i, q in enumerate(qs, 1):
        L = f'Q{i}'; sec = 'BCMP'[(i - 1) // 20]; key = q.get('correct_option'); x = q.get('explanation', '')
        ck(q.get('id') == f'NEST27-T{n:02}-Q{i:02}', f'{L}: id')
        ck(q.get('section') == sec and q.get('subject') == NAMES[sec], f'{L}: section or subject')
        p = plan.get(q.get('id'), {})
        ck(p.get('chapter') == q.get('topic') and p.get('difficulty_target') == q.get('difficulty') and str(p.get('class_level')) == q.get('class_level'), f'{L}: differs from its plan row')
        ck(q.get('format') in FORMATS, f'{L}: format'); ck(bool(q.get('sub_topic')), f'{L}: sub_topic')
        o = q.get('options', []); ck(len(o) == 4 and all(t.startswith(a + ') ') and len(t) > 3 for a, t in zip('ABCD', o)), f'{L}: options')
        ck(len({re.sub(r'\s+', '', t[3:]).casefold() for t in o}) == 4, f'{L}: duplicate options')
        ck(not re.search(r'(all|none) of the above', ' '.join(o), re.I), f'{L}: all/none of the above')
        ck(key in list('ABCD') and x.startswith(f'Answer: ({key})'), f'{L}: key or answer line')
        stem = re.sub(r'\W+', '', q.get('question', '')).casefold(); ck(len(stem) > 30 and stem not in stems, f'{L}: short or repeated stem'); stems.add(stem)
        need = ['Why:', 'Why not the others:', 'Key point:']
        if sec in 'MP': need += ['Given:', 'Formula/Principle:', 'Step 1:', 'Worked derivation:', 'Check:']
        else:
            need += ['Concept:']
            if q.get('format') == 'numerical': need += ['Given:', 'Formula/Principle:', 'Step 1:']
        for t in need: ck(('\n' + t) in x, f'{L}: solution lacks "{t}"')
        if sec in 'MP': ck(bool(re.search(r'Worked derivation: .*\\\[', x)) and bool(re.search(r'Check: .*\\\[', x)), f'{L}: derivation and check need display maths')
        wn = x.split('Why not the others:')[-1].split('\nKey point:')[0]
        for a in 'ABCD':
            if a != key: ck(f'({a})' in wn, f'{L}: no reason given against ({a})')
        ck(x.count('\\(') == x.count('\\)') and x.count('\\[') == x.count('\\]'), f'{L}: unbalanced maths delimiters')
        img = q.get('image_reference')
        if img: ck(img == f'NEST_T{n:02}_Q{i:02}.png' and img in register and bool(q.get('image_alt')), f'{L}: image name, register entry or alt text')
    for s in range(4):
        blk = qs[s * 20:(s + 1) * 20]; name = 'BCMP'[s]
        dc = Counter(q.get('difficulty') for q in blk); kc = Counter(q.get('correct_option') for q in blk)
        ck((dc['easy'], dc['medium'], dc['hard']) == (3, 13, 4), f'{name}: difficulty {dict(dc)}')
        ck(all(kc[a] == 5 for a in 'ABCD'), f'{name}: key balance {dict(kc)}')
        ks = ''.join(q.get('correct_option', '?') for q in blk); ck(not re.search(r'(.)\1\1\1', ks), f'{name}: a key letter four times in a row')
        ck(sum(1 for q in blk if q.get('image_reference')) <= 2, f'{name}: more than 2 image questions')
    return e

if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob('NISER/NEST TEST *.json')); bad = 0
    for f in files:
        e = validate(f); bad += bool(e); print(f, 'OK' if not e else f'{len(e)} problems'); [print('  ', m) for m in e]
    sys.exit(1 if bad else 0)
