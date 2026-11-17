"""Screen NEST questions for possible repeats: against every other NEST test and every IAT question.
usage: python3 tools/nest/check_overlap.py [N ...] [--threshold 0.35]
With test numbers, only questions of those tests are screened (against everything else).
Text screen only: Jaccard similarity of word 3-gram sets (numbers masked); every flagged pair must be read by hand."""
import glob, json, re, sys

def norm(s):
    s = s.lower().replace('−', '-').replace('×', 'x')
    s = re.sub(r'\\[a-z]+', ' ', s)                     # drop LaTeX command names
    s = re.sub(r'(?<!\w)\d+(?:\.\d+)?(?!\w)', '#', s)   # mask numbers
    w = re.sub(r'[^\w#]+', ' ', s).split()
    return {' '.join(w[i:i + 3]) for i in range(len(w) - 2)}

args = [a for a in sys.argv[1:] if not a.startswith('--')]
thr = float(sys.argv[sys.argv.index('--threshold') + 1]) if '--threshold' in sys.argv else 0.35
if '--threshold' in sys.argv: args.remove(sys.argv[sys.argv.index('--threshold') + 1])
bank = []
for f in sorted(glob.glob('NISER/NEST TEST *.json')) + sorted(glob.glob('IISER/IAT*TEST*.json')):
    d = json.load(open(f, encoding='utf-8'))
    for q in d.get('questions', []):
        bank.append((f.split('/')[-1].replace('.json', ''), q['id'], norm(q['question'] + ' ' + ' '.join(q['options']))))
want = {f'NEST27-T{int(a):02}-' for a in args}
targets = [b for b in bank if b[1].startswith('NEST27') and (not want or b[1][:11] in want)]
flags = 0
for t in targets:
    for o in bank:
        if o[1] == t[1] or (o[1].startswith('NEST27') and o[1] < t[1] and (not want or o[1][:11] in want)):
            continue                                   # skip self; count NEST–NEST pairs inside the screened set once
        if not t[2] or not o[2]: continue
        r = len(t[2] & o[2]) / len(t[2] | o[2])
        if r >= thr:
            flags += 1; print(f'{r:.2f}  {t[1]}  ~  {o[1]}  ({o[0]})')
print(f'screened {len(targets)} NEST questions against {len(bank)}; {flags} pairs at or above {thr}')
