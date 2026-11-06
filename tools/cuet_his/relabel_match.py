# usage: relabel_match.py draft.txt 'sub_topic' NEW  (NEW e.g. II,IV,I,III = new numerals for the old I,II,III,IV)
# Renames List-II numerals of one match item throughout its block (list, options, explanation) and re-sorts List-II.
import sys,re
p,st,new=sys.argv[1],sys.argv[2],sys.argv[3].split(',')
s=open(p,encoding='utf-8').read(); i=s.index('|'+st+'|'); i=s.rindex('@@ ',0,i); j=s.find('\n@@ ',i+3); j=len(s) if j<0 else j+1
blk=s[i:j]; old=['I','II','III','IV']; m=dict(zip(old,new))
blk=re.sub(r'\((IV|III|II|I)\)',lambda x:'(@'+m[x.group(1)]+')',blk).replace('(@','(')
L=blk.split('\n'); k=next(n for n,l in enumerate(L) if l.startswith('List-II'))
idx=[n for n in range(k+1,k+6) if re.match(r'\((IV|III|II|I)\) ',L[n])]
rows=sorted((L[n] for n in idx),key=lambda l:old.index(re.match(r'\((IV|III|II|I)\)',l).group(1)))
for n,r in zip(idx,rows): L[n]=r
open(p,'w',encoding='utf-8').write(s[:i]+'\n'.join(L)+s[j:]); print('relabelled',st)
