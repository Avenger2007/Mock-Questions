"""Print a compact per-unit index of every drafted item (sub_topic and stem start) to avoid repeats."""
import glob,json,re,sys
units={}
for f in sorted(glob.glob('tools/cuet_math/drafts/math[0-9][0-9].json')):
    t=int(re.search(r'math(\d+)',f).group(1))
    for q in json.load(open(f))['q']:
        s=re.sub(r'\\\(|\\\)|\\dfrac|\\displaystyle|\\int','',q['question'].split('\n')[0])
        units.setdefault(q['unit'],[]).append(f"T{t} {q['sub_topic'][:55]} :: {s[:70]}")
want=sys.argv[1:] or sorted(units,key=lambda u:(u[0],len(u),u))
for u in want:
    print('##',u); print('\n'.join(units.get(u,[])))
