# helpers for editing compact eco files: blocks split on '\n@@ '
import re
def load(p):
    t=open(p,encoding='utf-8').read(); head,*bl=t.split('\n@@ '); return head,bl
def save(p,head,bl): open(p,'w',encoding='utf-8').write(head+''.join('\n@@ '+b for b in bl))
def find(bl,sub):
    m=[i for i,b in enumerate(bl) if b.split('\n',1)[0].split('|')[1]==sub]; assert len(m)==1,sub; return m[0]
def opts(bl,sub,o):
    i=find(bl,sub); L=bl[i].split('\n'); k=0
    for j,l in enumerate(L):
        if re.match(r'[ABCD]\) ',l): L[j]=l[:3]+o[k]; k+=1
    assert k==4,sub; bl[i]='\n'.join(L)
def hdr(bl,sub,new=None,diff=None,fmt=None):
    i=find(bl,sub); h,r=bl[i].split('\n',1); f=h.split('|')
    if new: f[1]=new
    if diff: f[2]=diff
    if fmt: f[3]=fmt
    bl[i]='|'.join(f)+'\n'+r
def stem(bl,sub,old,new):
    i=find(bl,sub); assert old in bl[i],old; bl[i]=bl[i].replace(old,new)
def drop(bl,sub): del bl[find(bl,sub)]
def add(bl,after,text):
    bl.insert(find(bl,after)+1,text.strip('\n').removeprefix('@@ ')+'\n')
