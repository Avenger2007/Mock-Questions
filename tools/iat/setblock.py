"""Replace or add blocks in an audit solution file.
usage: python3 tools/iat/setblock.py N blocks.txt   (blocks.txt holds '@@Q Qnn' / '@@ Qnn' blocks)"""
import re,sys
n=int(sys.argv[1]); p=f'IISER/audit/solutions/test{n:02d}.txt'
s=open(p).read(); new=open(sys.argv[2]).read()
for b in re.split(r'(?m)^(?=@@Q? Q\d+\n)',new):
    if not b.strip(): continue
    head=b.split('\n',1)[0]
    b=b.rstrip('\n')+'\n\n'
    pat=re.compile(r'(?ms)^'+re.escape(head)+r'\n.*?(?=^@@Q? Q\d+\n|\Z)')
    if pat.search(s): s=pat.sub(lambda m:b,s,count=1); print('replaced',head)
    else:
        if head.startswith('@@Q'):
            m=re.search(r'(?m)^@@ Q\d+\n',s); s=s[:m.start()]+b+s[m.start():]
        else: s=s.rstrip('\n')+'\n\n'+b
        print('added',head)
open(p,'w').write(s.rstrip('\n')+'\n')
