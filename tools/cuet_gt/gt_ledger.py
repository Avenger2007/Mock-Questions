# shared: read/write target ledgers in docs/blueprints/general_test_coverage.md
import re
P='docs/blueprints/general_test_coverage.md'
def parse_targets(s):
    out={}
    for part in filter(None,[x.strip() for x in (s or '').split(';')]):
        k,v=part.split(':',1); out.setdefault(k.strip(),[]).extend(w.strip().lower() for w in v.split(',') if w.strip())
    return out
def read():
    led={};sec=None
    for l in open(P,encoding='utf-8').read().split('\n'):
        m=re.match(r'### ([A-Z]\d) ',l)
        if m: sec=m.group(1); led.setdefault(sec,{}); continue
        m=re.match(r'\| T(\d+) \| (.*) \|$',l)
        if sec and m:
            for w in m.group(2).split(','):
                if w.strip(): led[sec][w.strip().lower()]=int(m.group(1))
    return led
def add(n,tg):
    L=open(P,encoding='utf-8').read().split('\n'); sec=None; out=[]; i=0
    while i<len(L):
        l=L[i]; out.append(l); m=re.match(r'### ([A-Z]\d) ',l)
        if m: sec=m.group(1)
        if sec and l=='|---|---|' and tg.get(sec):
            j=i+1
            while j<len(L) and L[j].startswith('| T'): out.append(L[j]); j+=1
            out.append(f"| T{n} | {', '.join(tg[sec])} |"); i=j; sec=None; continue
        i+=1
    open(P,'w',encoding='utf-8').write('\n'.join(out))
