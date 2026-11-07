"""Draw original question-bearing textbook figures at fixed IDs."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Ellipse,FancyArrowPatch,Polygon,Arc
O=Path(__file__).resolve().parents[2]/'IISER/images';O.mkdir(exist_ok=True)
ink='#173743';blue='#347d88';red='#b25f52'
def board(title):
 f,a=plt.subplots(figsize=(10,7.5));a.set_xlim(0,10);a.set_ylim(0,7.5);a.axis('off');a.text(5,7.1,title,ha='center',va='center',fontsize=20,color=ink,weight='bold');return f,a
def t(a,x,y,s,fs=16,**kw):a.text(x,y,s,color=ink,fontsize=fs,ha=kw.pop('ha','center'),va='center',**kw)
def line(a,x1,y1,x2,y2,**kw):a.plot([x1,x2],[y1,y2],lw=kw.pop('lw',2.3),color=kw.pop('color',blue),**kw)
def save(f,test,n):f.savefig(O/f'IAT_T{test:02}_Q{n:02}.png',dpi=120,facecolor='white',bbox_inches='tight',pad_inches=.25);plt.close(f)
def tree():
 f,a=board('Nested taxonomic ranks')
 for x,y,s in [(5,6,'Order'),(5,5,'Family'),(5,4,'Genus'),(2.8,2.7,'Species P'),(7.2,2.7,'Species Q')]:
  a.add_patch(Rectangle((x-1,y-.38),2,.76,edgecolor=blue,facecolor='#eef8f6'));t(a,x,y,s)
 line(a,5,5.65,5,5.38);line(a,5,4.65,5,4.38);line(a,5,3.65,2.8,3.08);line(a,5,3.65,7.2,3.08)
 t(a,5,1.4,'P and Q occupy different species boxes',14);save(f,12,1)
def leaf():
 f,a=board('Leaf cross-section; light from above')
 a.annotate('Light',xy=(5,5.95),xytext=(5,6.55),ha='center',fontsize=15,arrowprops=dict(arrowstyle='->',color=red,lw=3))
 for y,h,label in [(5.5,.55,'upper epidermis'),(4.3,1.45,'palisade mesophyll'),(2.6,1.45,'spongy mesophyll'),(1.65,.45,'lower epidermis')]:
  a.add_patch(Rectangle((1,y-h/2),8,h,facecolor='#e7f1ef',edgecolor=ink,lw=1.5));t(a,5,y,label)
 save(f,12,2)
def thylakoid():
 f,a=board('Sealed thylakoid; darkness')
 a.add_patch(Ellipse((5,3.8),6,3,facecolor='#e8f1ef',edgecolor=ink,lw=4));t(a,4,4.1,'Lumen pH 5');t(a,4,2.9,'H+ abundant')
 a.add_patch(Rectangle((7.25,3.45),.55,1.15,facecolor='#e6bcaa',edgecolor=ink,lw=2));t(a,8.65,4.45,'ATP synthase',13)
 t(a,8.1,2,'Outside pH 8');t(a,8.1,1.4,'ADP + Pi');save(f,12,4)
def plasmid():
 f,a=board('Plasmid markers and insertion site');a.add_patch(Circle((5,3.7),2.2,fill=False,edgecolor=ink,lw=4))
 t(a,5,6.1,'S intact');t(a,7.4,3.7,'R',21);a.plot([6.9,7.65],[3.4,4.0],color=red,lw=3);t(a,5,.9,'Marked cloning site in R',15);save(f,12,9)
def nitrile():
 f,a=board('Methyl cyanide bond geometry');t(a,2.7,3.7,'CH₃',23);t(a,5.1,3.7,'C',23);t(a,7.5,3.7,'N',23)
 line(a,3.5,3.7,4.5,3.7,color=ink);[line(a,5.55,3.7+d,7.05,3.7+d,color=ink,lw=2) for d in (-.17,0,.17)];t(a,5,2,'Single C–C; triple C≡N',16);save(f,12,16)
def platinum():
 f,a=board('Two square-planar placements')
 for cx,lab,lig in [(2.8,'Sketch I',['Cl','Cl','NH₃','NH₃']),(7.2,'Sketch II',['Cl','NH₃','Cl','NH₃'])]:
  a.add_patch(Circle((cx,3.7),.35,color='#e5efed',ec=ink));t(a,cx,3.7,'Pt',15)
  for dx,dy,label in [(0,1.45,lig[0]),(1.35,0,lig[1]),(0,-1.45,lig[2]),(-1.35,0,lig[3])]:
   line(a,cx+.25*np.sign(dx),3.7+.25*np.sign(dy),cx+dx*.78,3.7+dy*.78);t(a,cx+dx,3.7+dy,label,14)
  t(a,cx,1.2,lab)
 save(f,12,17)
def carbonyls():
 f,a=board('Carbonyl structures in two test samples')
 for x,label,formula in [(2.7,'X: ethanal','CH₃–C(=O)–H'),(7.3,'Y: propanone','CH₃–C(=O)–CH₃')]:
  t(a,x,5.2,label,18);t(a,x,3.7,formula,20)
 t(a,5,1.5,'Compare Tollens and iodoform observations',15);save(f,12,21)
def raoult():
 f,a=plt.subplots(figsize=(10,7.5));x=np.linspace(0,1,101);a.plot(x,20+60*x,color=blue,lw=3,label='total');a.plot(x,80*x,color=red,lw=2,label='A partial');a.plot(x,20*(1-x),color=ink,lw=2,label='B partial');a.scatter([.25],[35],s=70,color=ink);a.axvline(.25,color=ink,linestyle=':');a.set(xlabel='Liquid mole fraction of A',ylabel='Vapour pressure (kPa)',xlim=(0,1),ylim=(0,85));a.set_xticks([0,.25,.5,.75,1]);a.set_yticks([0,20,40,60,80]);a.grid(alpha=.2);a.legend();f.tight_layout();save(f,12,28)
def acceleration():
 f,a=plt.subplots(figsize=(10,7.5));a.step([0,2,6],[2,-1,-1],where='post',lw=3,color=blue);a.axhline(0,color=ink,lw=1);a.set(xlim=(0,6),ylim=(-2,3),xlabel='Time (s)',ylabel='Acceleration (m s⁻²)');a.set_xticks([0,2,6]);a.set_yticks([-1,0,2]);a.grid(alpha=.2);f.tight_layout();save(f,12,46)
def field():
 f,a=plt.subplots(figsize=(10,7.5));a.step([0,1,2],[1,-2,-2],where='post',color=blue,lw=3);a.axhline(0,color=ink,lw=1);a.set(xlim=(0,2),ylim=(-2.5,1.5),xlabel='Position x',ylabel='Field Ex');a.set_xticks([0,1,2],['0','a','2a']);a.set_yticks([-2,0,1],['−2E₀','0','+E₀']);a.grid(alpha=.2);f.tight_layout();save(f,12,53)
def prism():
 f,a=board('Symmetric ray path through a prism')
 a.add_patch(Polygon([(3,1.5),(5,4.964),(7,1.5)],closed=True,fill=False,ec=ink,lw=3))
 y=3.2;xl=3+(y-1.5)/np.sqrt(3);xr=7-(y-1.5)/np.sqrt(3)
 line(a,1.2,y-(xl-1.2)*np.tan(np.deg2rad(20)),xl,y,color=red)
 line(a,xl,y,xr,y,color=red)
 line(a,xr,y,8.8,y-(8.8-xr)*np.tan(np.deg2rad(20)),color=red)
 for x,sgn in [(xl,-1),(xr,1)]:line(a,x-1.1,y-sgn*1.1/np.sqrt(3),x+1.1,y+sgn*1.1/np.sqrt(3),color=blue,lw=1.3,ls='--')
 t(a,5,5.5,'A=60°');t(a,2.0,3.45,'i=50°');t(a,8.0,3.45,'e=50°');save(f,12,58)
def algae():
 f,a=board('Algal cell pigment and reserve')
 a.add_patch(Ellipse((5,3.7),6,4.3,fill=False,ec=ink,lw=2));a.add_patch(Ellipse((5,3.7),4.2,2.5,facecolor='#d2e9db',ec=blue,lw=2));a.add_patch(Circle((4,3.7),.45,color='#ead8aa'));t(a,6.2,4,'chloroplast');t(a,4,3.7,'starch',12);t(a,5,1,'Pigments extracted: chlorophyll a and b',15);save(f,13,1)
def flower():
 f,a=board('Longitudinal flower section');a.add_patch(Ellipse((5,4.7),.85,1.15,fill=False,ec=ink,lw=2));t(a,5,4.7,'ovary',13);line(a,5,4.1,5,1.3,color=ink,lw=4)
 for x,lab in [(2.3,'sepal'),(7.7,'petal'),(3.1,'stamen')]:line(a,5,2.65,x,4.45,color=blue);t(a,x,5.3 if x==3.1 else 4.8,lab,14)
 t(a,5,1,'Whorl insertions below ovary',14);save(f,13,2)
def primers():
 f,a=board('Target interval and primer ends')
 line(a,1,4.7,9,4.7,color=ink);line(a,1,3.0,9,3.0,color=ink)
 t(a,1,5.15,"5′");t(a,9,5.15,"3′");t(a,1,2.6,"3′");t(a,9,2.6,"5′")
 a.annotate('',(4.2,4.38),(2.4,4.38),arrowprops=dict(arrowstyle='->',lw=4,color=red));a.annotate('',(5.8,3.32),(7.6,3.32),arrowprops=dict(arrowstyle='->',lw=4,color=blue));t(a,3.4,5.8,'Left primer 3′ points right',13);t(a,6.8,1.8,'Right primer 3′ points left',13);save(f,13,9)
def gel():
 f,a=board('Complete restriction digest lanes')
 for x,lab,ys in [(3,'X',[3.3]),(7,'Y',[4.3,2.2])]:
  t(a,x,6.0,lab,20);a.add_patch(Rectangle((x-.9,1.5),1.8,3.9,fill=False,ec=ink,lw=2))
  for y in ys:line(a,x-.6,y,x+.6,y,color=blue,lw=7)
 for y,lab in [(4.3,'600 bp'),(3.3,'900 bp'),(2.2,'300 bp')]:t(a,8.9,y,lab,13)
 save(f,13,15)
def nitrogen():
 f,a=board('Nitrogen bond-pair directions')
 for x,name,outer in [(2.7,'NH₃','H'),(7.3,'NF₃','F')]:
  t(a,x,5.9,name,20);t(a,x,3.7,'N',22);t(a,x,4.55,'••',20)
  for dx in (-1,0,1):
   xx=x+dx*1.1;yy=2.2 if dx else 2.0;line(a,x,3.45,xx,yy);t(a,xx,yy-.35,outer)
 save(f,13,16)
def quotient():
 f,a=board('Pressures before reaction resumes')
 for x,lab,v1,v2 in [(3,'Old equilibrium',2,1),(7,'Just after NO₂ added',4,1)]:
  t(a,x,6,lab,15)
  for j,(name,val) in enumerate([('NO₂',v1),('N₂O₄',v2)]):
   a.add_patch(Rectangle((x-1.3+j*1.45,1.6),.9,val*.75,facecolor=blue if j==0 else red));t(a,x-.85+j*1.45,1.15,name,13);t(a,x-.85+j*1.45,1.8+val*.75,f'{val} atm',12)
 save(f,13,30)
def gauss():
 f,a=board('Enclosed versus external charges');a.add_patch(Circle((4.5,3.7),2.45,fill=False,ec=blue,lw=3));t(a,3.4,4.2,'+q',21);t(a,5.4,3.1,'−3q',21);t(a,8,4.2,'+5q',21);t(a,4.5,.9,'Closed Gaussian surface',15);save(f,13,53)
def network():
 f,a=board('Two paths between terminals A and C')
 for x,lab in [(1,'A'),(5,'B'),(9,'C')]:t(a,x,4.8,lab,20)
 for x,label in [(3,'R'),(7,'R')]:a.add_patch(Rectangle((x-.5,4.35),1,.65,fill=False,ec=ink,lw=2));t(a,x,4.68,label)
 for u,v in [(1.5,2.5),(3.5,6.5),(7.5,8.5)]:line(a,u,4.68,v,4.68)
 for u,v in [((1,4.68),(1,2.6)),((1,2.6),(4,2.6)),((6,2.6),(9,2.6)),((9,2.6),(9,4.68))]:line(a,*u,*v)
 a.add_patch(Rectangle((4,2.28),2,.65,fill=False,ec=ink,lw=2));t(a,5,2.6,'2R');save(f,13,54)
def lenz():
 f,a=board('Magnetic flux into page increases')
 a.add_patch(Circle((5,3.6),2.3,fill=False,ec=blue,lw=3))
 for x,y in [(4,4.5),(6,4.5),(4,2.7),(6,2.7)]:t(a,x,y,'×',26)
 t(a,5,6.3,'Inward B increases',18);t(a,5,.7,'Determine induced current sense',15);save(f,13,55)
def diode():
 f,a=plt.subplots(figsize=(10,7.5));v=np.linspace(-1,1,300);i=np.where(v<0,-.03,np.where(v<.6,.01*v,.01+.4*(np.exp((v-.6)*6)-1)));a.plot(v,i,color=blue,lw=3);a.axhline(0,color=ink,lw=1);a.axvline(0,color=ink,lw=1);a.set(xlabel='Diode voltage (V)',ylabel='Current (arbitrary units)',xlim=(-1,1),ylim=(-.1,4));a.set_xticks([-1,-.8,0,.2,.6,.8,1]);a.grid(alpha=.2);f.tight_layout();save(f,13,60)
if __name__=='__main__':
 for fn in (tree,leaf,thylakoid,plasmid,nitrile,platinum,carbonyls,raoult,acceleration,field,prism,algae,flower,primers,gel,nitrogen,quotient,gauss,network,lenz,diode):fn()
