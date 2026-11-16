"""Mechanical only: assemble NISER/NEST TEST <N>.json from NISER/authoring/testNN_B.txt, _C, _M, _P and the plan CSV.
usage: python3 tools/nest/build_test.py N [--mark]     (--mark also sets state/source/hash in the plan CSV)

Authoring block (written by hand, never generated):
@@ Q07
format: conceptual | numerical | graph | data | diagram | experiment
sub_topic: specific sub-topic
Q: question text (may span lines)
A) ...
B) ...
C) ...
D) ...
KEY: X
SOL:
Answer: (X) ...
Chapter, class and difficulty come from the plan row and are never typed twice."""
import csv, json, re, sys, hashlib
n = int(sys.argv[1]); PLAN = 'NISER/NEST_25_Test_Plan.csv'
NAMES = dict(B='Biology', C='Chemistry', M='Mathematics', P='Physics')
rows = list(csv.DictReader(open(PLAN, encoding='utf-8')))
plan = {int(r['question']): r for r in rows if int(r['test']) == n}
import glob
src = '\n'.join(open(f, encoding='utf-8').read() for f in sorted(glob.glob(f'NISER/authoring/test{n:02}_*.txt')))
parts = re.split(r'^@@ Q(\d\d)\n', src, flags=re.M)
qs = []
for num, body in zip(parts[1::2], parts[2::2]):
    k = int(num)
    m = re.match(r'format:\s*(\S+)\nsub_topic:\s*(.+)\nQ:\s*(.*?)\nA\) (.*)\nB\) (.*)\nC\) (.*)\nD\) (.*)\nKEY: ([ABCD])\nSOL:\n(.*)$', body.strip(), flags=re.S)
    assert m, f'Q{num}: block does not match the authoring format'
    r = plan[k]; sol = m.group(9).strip()
    assert sol.startswith(f'Answer: ({m.group(8)})'), f'Q{num}: solution does not start with the key'
    q = dict(id=r['id'], section=r['section'], subject=NAMES[r['section']], topic=r['chapter'], sub_topic=m.group(2).strip(),
             class_level=str(r['class_level']), difficulty=r['difficulty_target'], format=m.group(1),
             question=m.group(3).strip(), options=[f'{L}) {m.group(i).strip()}' for i, L in zip(range(4, 8), 'ABCD')],
             correct_option=m.group(8), explanation=sol)
    qs.append((k, q))
qs.sort(); assert [k for k, _ in qs] == list(range(1, 81)), 'need Q01..Q80 exactly once'
test = dict(test_id=f'NEST27_TEST_{n:02}', series_id='NEST27', exam='NEST 2027 (NISER Bhubaneswar and UM-DAE CEBS Mumbai)',
            title=f'NEST Test {n}', test_number=n, status='pending_revision', syllabus_source='NISER/Syllabus.md (official NEST 2026 syllabus)',
            notification_source='NEST 2026 Information Brochure, www.nestexam.in (2027 brochure not yet published)',
            past_paper_reference='NEST 2024-2026 papers analysed for pattern only; no question copied',
            duration_minutes=180, total_questions=80, questions_to_attempt='any 3 or all 4 sections; best three sections count',
            maximum_marks=180, marking_scheme={'correct': '+3', 'incorrect': '-1', 'unattempted': '0'},
            scoring_rule='Total = sum of the best three section scores (each section out of 60)',
            order_policy='authored in final order; never shuffle or renumber',
            instructions=['The paper has four sections: Biology, Chemistry, Mathematics and Physics, with 20 questions each.',
                          'Each question has four options and only one is correct.',
                          'Correct answer: +3. Wrong answer: -1. Unanswered: 0.',
                          'You may attempt all four sections. Your best three section scores are added for the total.',
                          'Time allowed: 3 hours. Only a simple calculator is allowed.'],
            sections=[dict(id=s, title=NAMES[s], question_range=f'{a}-{a+19}', questions=20, marks=60) for s, a in zip('BCMP', (1, 21, 41, 61))],
            questions=[q for _, q in qs])
out = f'NISER/NEST TEST {n}.json'
json.dump(test, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2); open(out, 'a').write('\n')
print('wrote', out, len(qs), 'questions')
if '--mark' in sys.argv:
    for r in rows:
        if int(r['test']) == n:
            q = dict(qs)[int(r['question'])]
            r['state'] = 'authored'; r['source_json'] = out
            r['question_sha256'] = hashlib.sha256((q['question'] + '\n' + '\n'.join(q['options'])).encode()).hexdigest()
    with open(PLAN, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print('plan rows marked authored for test', n)
