"""Original question-bearing diagrams for Tests 8 and 9."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
import numpy as np
OUT=Path(__file__).resolve().parents[2]/'IISER/images';OUT.mkdir(exist_ok=True)
INK='#173746';BLUE='#367f86';RED='#b96352';PALE='#dceeea'
def base(title):
 f,a=plt.subplots(figsize=(12,9));a.set(xlim=(0,12),ylim=(0,9));a.axis('off');a.set_aspect('equal');a.text(6,8.35,title,ha='center',fontsize=27,color=INK,weight='bold');return f,a
def txt(a,x,y,s,size=23,**kw):
 kw.setdefault('ha','center');kw.setdefault('va','center');a.text(x,y,s,fontsize=size,color=INK,**kw)
def save(f,t,n):f.savefig(OUT/f'IAT_T{t:02}_Q{n:02}.png',dpi=100,facecolor='white',bbox_inches='tight',pad_inches=.35);plt.close(f)
def t8_2():
 f,a=base('Longitudinal flower section');a.add_patch(Rectangle((4,1.9),4,3.6,facecolor='#f8e6e9',edgecolor=RED,lw=3));a.add_patch(Rectangle((4.5,2.35),3,2.1,facecolor='white',edgecolor=INK,lw=2));a.plot([6,6],[4.45,7],lw=4,color=INK)
 for x in [4.2,7.8]:a.plot([x,x],[5.4,6.8],lw=3,color=BLUE);a.add_patch(Circle((x,6.8),.25,color='#edc477'))
 for x in [3.3,8.7]:a.plot([6,x],[5.5,6.3],lw=3,color=RED)
 a.plot([2.6,9.4],[5.4,5.4],color=INK,lw=2);txt(a,9.5,5.8,'Whorl attachment',18,ha='left');a.plot([6,6],[2.4,4.2],color=INK,lw=2);txt(a,5.2,3.2,'chamber 1',16);txt(a,6.9,3.2,'chamber 2',16);txt(a,6,1.2,'Ovary below attachment',21);save(f,8,2)
def t8_15():
 f,a=base('Complete restriction digest');
 for x,name,ys in [(3,'U',[5]),(6,'Normal + E',[5.9,3.9]),(9,'Mutant + E',[5])]:
  txt(a,x,7,name,21);a.add_patch(Rectangle((x-.8,2.3),1.6,4.1,fill=False,edgecolor=INK,lw=2))
  for y in ys:a.plot([x-.58,x+.58],[y,y],color=BLUE,lw=8)
 for y,label in [(5.9,'3 kb'),(5,'5 kb'),(3.9,'2 kb')]:txt(a,1.2,y,label,18)
 save(f,8,15)
def t8_17():
 f,a=base('Octahedral d⁶: compare Δ and P')
 for x,title,hi in [(3.2,'X: Δ < P',.9),(8.8,'Y: Δ > P',2.5)]:
  txt(a,x,7.3,title,24);lo=3.2;up=lo+hi
  for dx in [-.85,0,.85]:a.plot([x+dx-.3,x+dx+.3],[lo,lo],lw=3,color=INK)
  for dx in [-.45,.45]:a.plot([x+dx-.3,x+dx+.3],[up,up],lw=3,color=INK)
  a.annotate('',(x+1.4,up),(x+1.4,lo),arrowprops=dict(arrowstyle='<->',color=RED,lw=2));txt(a,x+1.8,(up+lo)/2,'Δ',20)
  # occupancy, high spin t2g4 eg2 and low spin t2g6
  for dx,s in ([( -.85,'↑↓'),(0,'↑'),(.85,'↑')] if x<6 else [(-.85,'↑↓'),(0,'↑↓'),(.85,'↑↓')]):txt(a,x+dx,lo+.28,s,20)
  if x<6:
   for dx in [-.45,.45]:txt(a,x+dx,up+.27,'↑',20)
 txt(a,6,1.1,'Same metal oxidation state and d-electron count',19);save(f,8,17)
def t8_28():
 f,a=base('Binary solution at liquid xA = 0.25')
 for y,s in [(6.4,'Pure A: 100 mmHg'),(5.2,'Pure B: 60 mmHg'),(3.9,'Observed total: 80 mmHg')]:a.add_patch(Rectangle((2.4,y-.4),7.2,.8,facecolor=PALE,edgecolor=INK));txt(a,6,y,s,24)
 txt(a,6,2.2,'Compare observed with Raoult ideal total',21);save(f,8,28)
def t8_53():
 f,a=base('Signed electric field Eₓ versus x');a.set_aspect('auto');a.plot([1.5,10.5],[3.7,3.7],color=INK,lw=2);a.plot([1.5,1.5],[1.4,7],color=INK,lw=2)
 a.plot([1.5,4.4],[6.1,6.1],lw=5,color=BLUE);a.plot([4.4,10.2],[2.5,2.5],lw=5,color=RED);a.plot([4.4,4.4],[2.5,6.1],lw=2,color=INK)
 for x,s in [(1.5,'0'),(4.4,'a'),(7.3,'2a'),(10.2,'3a')]:txt(a,x,3.3,s,19)
 txt(a,.7,6.1,'+2E₀',18);txt(a,.7,2.5,'−E₀',18);txt(a,10.7,3.7,'x',19);save(f,8,53)
def t8_58():
 f,a=base('Series-circuit rms voltage phasor');a.annotate('',(9.2,2.2),(2.5,2.2),arrowprops=dict(arrowstyle='->',lw=4,color=BLUE));a.annotate('',(9.2,7.1),(9.2,2.2),arrowprops=dict(arrowstyle='->',lw=4,color=RED));a.annotate('',(9.2,7.1),(2.5,2.2),arrowprops=dict(arrowstyle='->',lw=3,color=INK));txt(a,5.8,1.6,'Vᵣ = 30 V',23);txt(a,10.4,4.7,'V_L − V_C = +40 V',21);txt(a,5.4,5.7,'Supply 50 V',22);txt(a,6,7.8,'Resistance = 30 Ω',21);save(f,8,58)
def t9_3():
 f,a=base('Initial-rate versus substrate concentration');a.set_aspect('auto');x=np.linspace(0,10,200)
 for km,c,name in [(2,BLUE,'No inhibitor: Km=2'),(6,RED,'With X: Km=6')]:a.plot(x,10*x/(km+x),lw=4,color=c,label=name)
 a.axhline(10,color=INK,ls='--');a.text(9.2,10.25,'Vmax=10',ha='right',fontsize=20);a.set(xlim=(0,10),ylim=(0,11));a.legend(fontsize=17,loc='lower right');a.set_xlabel('[Substrate]',fontsize=21);a.set_ylabel('Rate',fontsize=21);save(f,9,3)
def t9_4():
 f,a=base('Leaf bundle and surrounding cells');a.add_patch(Circle((6,4.5),1.4,color='#f3d6ba',ec=INK,lw=3));txt(a,6,4.5,'vascular\nbundle',20)
 for angle in np.linspace(0,2*np.pi,12,endpoint=False):
  x,y=6+2.1*np.cos(angle),4.5+2.1*np.sin(angle);a.add_patch(Circle((x,y),.42,facecolor=PALE,edgecolor=BLUE,lw=2));a.add_patch(Circle((x+.12,y),.10,color='#48905b'))
 for angle in np.linspace(0,2*np.pi,20,endpoint=False):a.add_patch(Circle((6+3.15*np.cos(angle),4.5+3.15*np.sin(angle)),.37,facecolor='#ebf4db',edgecolor=INK,lw=1))
 txt(a,10.4,6.1,'Mesophyll',18);txt(a,10.1,3,'Chloroplast-rich\nbundle sheath',17);save(f,9,4)
def t9_17():
 f,a=base('Coordination sphere and donor sites');txt(a,6,4.5,'Co',31)
 for x,y,s in [(3.3,6.2,'en'),(8.7,6.2,'en'),(3.3,2.8,'Cl⁻'),(8.7,2.8,'Cl⁻')]:
  a.plot([6,x],[4.5,y],color=INK,lw=2);txt(a,x,y,s,25)
 txt(a,6,7.2,'[Co(en)₂Cl₂]⁺',27);txt(a,6,1.2,'Each en makes two donor bonds; each Cl⁻ makes one',20);save(f,9,17)
def t9_27():
 f,a=base('Vapour pressure at xA = 0.50')
 for y,s in [(6.5,'p*A = 100 kPa'),(5.2,'p*B = 40 kPa'),(3.8,'Observed total = 85 kPa')]:a.add_patch(Rectangle((2,y-.42),8,.84,facecolor=PALE,edgecolor=INK));txt(a,6,y,s,24)
 txt(a,6,2,'Compute ideal total from liquid fractions',20);save(f,9,27)
def t9_46():
 f,a=base('Applied force and static-friction threshold');a.set_aspect('auto');a.plot([2,10],[2,2],color=INK,lw=2);a.plot([2,2],[2,7],color=INK,lw=2);a.plot([2,8],[2,6],color=BLUE,lw=4);a.plot([8,10],[6,6],color=RED,lw=3,ls='--');txt(a,8,6.6,'threshold: 6 N',20);txt(a,5.5,1.3,'Applied force increasing',20);txt(a,3.8,4.5,'Block at rest',19);save(f,9,46)
def t9_53():
 f,a=base('Battery removed before dielectric insertion');
 for x,s in [(3.2,'Before'),(8.8,'After')]:
  txt(a,x,7.2,s,25);a.plot([x-1,x-1],[2.8,5.8],color=INK,lw=5);a.plot([x+1,x+1],[2.8,5.8],color=INK,lw=5)
  if x>6:a.add_patch(Rectangle((x-.87,2.9),1.74,2.8,facecolor=PALE,edgecolor=BLUE));txt(a,x,4.3,'κ = 3',23)
 txt(a,6,1.5,'Isolated plates: free charge Q fixed',21);save(f,9,53)
def t9_51():
 f,a=base('Molecular impacts on the x-normal wall');a.add_patch(Rectangle((3,2.5),5,4,fill=False,edgecolor=INK,lw=3));a.plot([8,8],[2.5,6.5],color=RED,lw=7)
 for x,y in [(4.1,3.6),(5.1,5.4),(6,4.5)]:a.add_patch(Circle((x,y),.16,color=BLUE));a.annotate('',(x+1,y),(x+.2,y),arrowprops=dict(arrowstyle='->',color=BLUE,lw=2))
 txt(a,9.6,4.5,'Wall area L²',20);txt(a,5.5,1.9,'Cube side L; N molecules of mass m',21);txt(a,6,7.2,'Mean squared x speed: ⟨cₓ²⟩',20);save(f,9,51)
def t9_59():
 f,a=base('Hydrogen energy levels')
 for n,y in [(1,2),(2,4.25),(3,5.65),(4,6.5)]:a.plot([3,9],[y,y],color=INK,lw=2);txt(a,2.3,y,f'n={n}',20)
 for x,y0,y1,s in [(4,6.5,5.65,'4→3'),(5.5,6.5,4.25,'4→2'),(7,5.65,4.25,'3→2'),(8.4,4.25,2,'2→1')]:a.annotate('',(x,y1+.1),(x,y0-.1),arrowprops=dict(arrowstyle='->',color=BLUE,lw=2));txt(a,x+.45,(y0+y1)/2,s,16)
 save(f,9,59)
if __name__=='__main__':
 for f in [t8_2,t8_15,t8_17,t8_28,t8_53,t8_58,t9_3,t9_4,t9_17,t9_27,t9_46,t9_51,t9_53,t9_59]:f()
