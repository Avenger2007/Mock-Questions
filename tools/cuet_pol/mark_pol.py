# usage: mark_pol.py N polNN.json  -> add this test's targets to the coverage ledgers
import json,sys,os,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import pol_ledger
n=int(sys.argv[1]); src=json.load(open(sys.argv[2],encoding='utf-8'))['q']; tg=collections.OrderedDict()
for q in src:
    for sec,ws in pol_ledger.parse_targets(q.get('targets')).items():
        for w in ws:
            if w not in tg.setdefault(sec,[]): tg[sec].append(w)
pol_ledger.add(n,tg); print('marked',{k:len(v) for k,v in tg.items()})
