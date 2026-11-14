"""Search every IAT test for a regex: python3 tools/iat/grep_bank.py 'pat1' 'pat2' ..."""
import json,glob,re,sys
for p in sys.argv[1:]:
    print('==',p)
    for f in sorted(glob.glob('IISER/IAT*.json'),key=lambda s:int(re.findall(r'(\d+)\.json',s)[0])):
        n=int(re.findall(r'(\d+)\.json',f)[0])
        d=json.load(open(f)); qs=d['questions'] if isinstance(d,dict) else d
        for i,q in enumerate(qs,1):
            o=q.get('options',[]); o=o.values() if isinstance(o,dict) else o
            t=q.get('question','')+' '+' '.join(map(str,o))
            if re.search(p,t): print(f'  T{n} Q{i}',q.get('question','')[:110].replace('\n',' '))
