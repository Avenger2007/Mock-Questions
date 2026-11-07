"""Apply explicit equation-layout amendments with no numerical changes."""
import csv,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[2];groups={}
for ident,label,value in csv.reader((R/'IISER/revisions/milestone15_layout.tsv').open(),delimiter='\t'):
 groups.setdefault(int(ident[7:9]),[]).append((ident,label,value.replace('<br>','\n')))
for t,rows in groups.items():
 p=R/('IISER/IAT TEST 1.json' if t==1 else f'IISER/IAT NEW TEST {t}.json');d=json.loads(p.read_text())
 for ident,label,value in rows:
  q=next(q for q in d['questions'] if q['id']==ident);replacement=label+': '+value
  if replacement in q['explanation']:continue
  q['explanation'],count=re.subn(r'(?m)^'+re.escape(label)+r':.*$',lambda m:replacement,q['explanation']);assert count==1,ident
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
