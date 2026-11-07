"""Draw exact figures tied to authored IAT New Tests 10 and 11."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle,Rectangle,Ellipse,FancyArrowPatch,Polygon
OUT=Path(__file__).resolve().parents[2]/'IISER/images';OUT.mkdir(exist_ok=True)
INK='#183847';SEA='#367e86';CORAL='#b46155';PALE='#dceeea'
def base(title):
 f,a=plt.subplots(figsize=(12,9));a.set_xlim(0,12);a.set_ylim(0,9);a.axis('off');a.set_aspect('equal');a.text(6,8.3,title,fontsize=25,color=INK,ha='center',weight='bold');return f,a
def txt(a,x,y,s,size=22,**kw):kw.setdefault('ha','center');kw.setdefault('va','center');a.text(x,y,s,fontsize=size,color=INK,**kw)
def save(f,t,n):f.savefig(OUT/f'IAT_T{t:02}_Q{n:02}.png',dpi=100,facecolor='white',bbox_inches='tight',pad_inches=.3);plt.close(f)
def cards(t,n,title,lines):
 f,a=base(title)
 for j,line in enumerate(lines):
  y=7.1-j*1.35;a.add_patch(Rectangle((1,y-.5),10,1,facecolor=PALE if j%2==0 else '#f2f6f5',edgecolor=SEA,lw=1.5));txt(a,6,y,line,22)
 save(f,t,n)
def heart():
 f,a=base('Frog circulation: follow the inflows')
 for x,name,col in [(3.5,'Right atrium','#d5e4ec'),(8.5,'Left atrium','#f3d5cb')]:a.add_patch(Ellipse((x,5.3),2.6,1.9,facecolor=col,edgecolor=INK,lw=2));txt(a,x,5.3,name,18)
 a.add_patch(Ellipse((6,2.7),4.0,2.2,facecolor='#e7dce8',edgecolor=INK,lw=3));txt(a,6,2.7,'Single ventricle',21)
 for x in (3.5,8.5):a.annotate('',(6,3.55),(x,4.35),arrowprops=dict(arrowstyle='->',lw=3,color=SEA))
 txt(a,2.1,7.1,'Q from body',19);txt(a,9.7,7.1,'P from lungs',19)
 a.annotate('',(3.5,6.25),(2.4,6.8),arrowprops=dict(arrowstyle='->',lw=3,color=SEA));a.annotate('',(8.5,6.25),(9.5,6.8),arrowprops=dict(arrowstyle='->',lw=3,color=CORAL));save(f,10,2)
def chromosome():
 f,a=base('Diploid G1 versus pattern X before division')
 for cx,label,rep in [(3.4,'G1: 2C DNA',False),(8.5,'X: 4C DNA',True)]:
  txt(a,cx,7.1,label,25)
  for j,(dx,dy) in enumerate([(-.8,.7),(.7,.6),(-.7,-.8),(.8,-.7)]):
   x,y=cx+dx,4.5+dy
   if rep:
    a.plot([x-.24,x+.24],[y+.5,y-.5],lw=6,color=SEA);a.plot([x+.24,x-.24],[y+.5,y-.5],lw=6,color=CORAL)
   else:a.plot([x,x],[y+.5,y-.5],lw=6,color=SEA)
  txt(a,cx,2,'Centromeres: same count',19)
 save(f,10,3)
def protein():
 f,a=base('Induction and target-protein assay')
 for x,label,band in [(3,'X + inducer',True),(6,'Y + inducer',False),(9,'X before induction',False)]:
  txt(a,x,7,label,21);a.add_patch(Rectangle((x-.8,2.4),1.6,4,fill=False,edgecolor=INK,lw=2))
  if band:a.plot([x-.5,x+.5],[4.4,4.4],color=SEA,lw=8)
 txt(a,1.6,4.4,'Target mass',17);txt(a,6,1.4,'All colonies survive antibiotic selection',21);save(f,10,9)
def energy_profile():
 f,a=base('Alternative paths: identical endpoints');a.set_aspect('auto')
 x=np.linspace(1,11,300);y1=2+4*np.exp(-((x-5)/1.4)**2)+.17*(x-1);y2=2+2.4*np.exp(-((x-5)/1.5)**2)+.17*(x-1)
 a.plot(x,y1,lw=4,color=CORAL,label='Y');a.plot(x,y2,lw=4,color=SEA,label='X');a.legend(fontsize=25);txt(a,1.5,1.3,'Reactants',19);txt(a,10.3,4.2,'Products',19);save(f,10,23)
def orbit():
 f,a=base('Two circular orbital states')
 for r in (1.6,3.2):a.add_patch(Circle((6,4.3),r,fill=False,edgecolor=SEA,lw=3))
 a.add_patch(Circle((6,4.3),.3,color=CORAL));txt(a,6,4.3,'M',17);txt(a,7.1,4.9,'r',23);txt(a,8.5,5.4,'2r',23)
 for x in (7.6,9.2):a.add_patch(Circle((x,4.3),.13,color=INK))
 txt(a,6,.55,'Satellite mass m, same central planet M',20);save(f,10,52)
def charges():
 f,a=base('Opposite charges on the x-axis');a.plot([1,11],[4.3,4.3],color=INK,lw=2)
 for x,label,pos in [(5,'+q','0'),(7.5,'−4q','3a')]:a.add_patch(Circle((x,4.3),.35,facecolor=PALE,edgecolor=SEA,lw=3));txt(a,x,5.2,label,27);txt(a,x,3.6,pos,21)
 txt(a,2.5,3.5,'−3a',20);txt(a,10,3.5,'6a',20);save(f,10,53)
def mirror():
 f,a=base('Concave mirror: object inside focus')
 a.plot([1.5,10.5],[3.5,3.5],color=INK,lw=2);a.plot([9,9],[1.2,6.7],color=SEA,lw=5)
 txt(a,9,7,'mirror',20);txt(a,5.7,3.1,'F: 10 cm',20);txt(a,7.5,3.1,'object: 5 cm',19)
 a.annotate('',(7.5,5.2),(7.5,3.6),arrowprops=dict(arrowstyle='->',lw=3,color=CORAL));a.plot([7.5,9],[5.2,5.2],color=CORAL,lw=2);a.plot([9,5.6],[5.2,6.6],color=CORAL,lw=2);a.plot([9,10.9],[5.2,4.4],color=CORAL,lw=2,ls='--');save(f,10,58)
def seed():
 f,a=base('Angiosperm fruit and seed section');a.add_patch(Ellipse((6,4.2),4.2,3.2,facecolor='#f2d7bf',edgecolor=CORAL,lw=4));a.add_patch(Ellipse((6,4.2),2.2,1.65,facecolor=PALE,edgecolor=INK,lw=3));a.add_patch(Ellipse((6,4.2),.9,.7,facecolor='#e8c28e',edgecolor=INK))
 txt(a,9.7,5.8,'Ovary-derived fruit wall',19);txt(a,9.5,3.6,'Seed coat',19);txt(a,6,4.2,'embryo',16);save(f,11,1)
def root():
 f,a=base('Young root transverse section');a.add_patch(Circle((6,4.5),3.1,fill=False,edgecolor=INK,lw=3));a.add_patch(Circle((6,4.5),2.3,fill=False,edgecolor=SEA,lw=2))
 pts=[]
 for j in range(16):
  th=j*np.pi/8;r=1.8 if j%4==0 else .55 if j%2 else .75;pts.append((6+r*np.cos(th),4.5+r*np.sin(th)))
 a.add_patch(Polygon(pts,closed=True,facecolor=PALE,edgecolor=SEA,lw=2))
 for th in np.pi/4+np.arange(4)*np.pi/2:a.add_patch(Ellipse((6+1.65*np.cos(th),4.5+1.65*np.sin(th)),.47,.3,facecolor='#e7bca9',edgecolor=CORAL))
 txt(a,6,1,'Central xylem star; phloem between arms',19);save(f,11,2)
def wet_test():cards(11,17,'Immediate BaCl₂ addition', ['X: [Co(NH₃)₅Br]SO₄','Y: [Co(NH₃)₅SO₄]Br','No ligand exchange during the test'])
def cyanide():
 f,a=base('Electron-pair movement in ethanal addition');txt(a,6,5.8,'CH₃–CH=O',31);txt(a,2.8,4.1,'CN⁻',29)
 a.annotate('',(5.4,5.2),(3.4,4.35),arrowprops=dict(arrowstyle='->',lw=3,color=SEA,connectionstyle='arc3,rad=-.2'));a.annotate('',(7.7,5.9),(6.3,5.65),arrowprops=dict(arrowstyle='->',lw=3,color=CORAL,connectionstyle='arc3,rad=.3'));txt(a,6,2.1,'CN pair attacks carbonyl carbon; π electrons move to O',20);save(f,11,22)
def freeze():
 f,a=base('Freezing point of 0.10 m A₂B solution');a.set_aspect('auto')
 a.plot([1.5,10.5],[5.8,5.8],color=INK,lw=2);a.plot([1.5,10.5],[3.4,3.4],color=SEA,lw=3)
 txt(a,6,6.25,'Pure solvent reference: 0.00°C',21);txt(a,6,2.8,'Solution plateau: −0.42°C',21);txt(a,6,1.4,'Kf = 1.86 K kg mol⁻¹',22);save(f,11,28)
def stress():
 f,a=base('Two strain regimes');a.set_aspect('auto');a.plot([2,5],[2,6],color=SEA,lw=4);a.plot([5,10],[6,7],color=CORAL,lw=4)
 txt(a,5,6.5,'(0.002, 100 MPa)',21);txt(a,3,3.8,'elastic',19);txt(a,8,7.4,'plastic',19);txt(a,6,1.1,'Strain',20);txt(a,1.2,4,'Stress',20);save(f,11,49)
def pendulum():
 f,a=base('Small oscillations in two environments')
 for x,name,pend,caption in [(3,'P',3.2,'Lab: gravity g'),(9,'Q',1.6,'Lift upward at g')]:
  txt(a,x,7.4,name,28);a.add_patch(Circle((x,6.5),.17,color=INK));a.plot([x,x+.6],[6.5,6.5-pend],lw=3,color=INK);a.add_patch(Circle((x+.6,6.5-pend),.3,color=CORAL));txt(a,x,1.6,caption,19);txt(a,x+1.1,5.7,'L' if x<6 else 'L/2',20)
 save(f,11,52)
def layers():
 f,a=base('Three parallel optical layers')
 for y in (5.8,3.1):a.plot([1.5,10.5],[y,y],color=INK,lw=3)
 txt(a,2.5,7,'A: n=2',22);txt(a,2.5,4.5,'B: n=√2',22);txt(a,2.5,2,'air: n=1',22)
 a.plot([5.8,6.9],[8,5.8],color=SEA,lw=3);a.plot([6.9,8.5],[5.8,3.1],color=SEA,lw=3);a.plot([8.5,10.5],[3.1,3.1],color=CORAL,lw=3);txt(a,7.3,6.8,'30°',19);save(f,11,57)
def photo():
 f,a=base('Stopping potential against light frequency');a.set_aspect('auto');a.plot([2,10],[2,2],color=INK,lw=2);a.plot([2,2],[2,7],color=INK,lw=2);a.plot([4.5,9],[2,6.2],color=SEA,lw=4)
 txt(a,4.5,1.6,'5×10¹⁴ Hz',19);txt(a,9,1.6,'7.5×10¹⁴ Hz',19);txt(a,9.5,6.2,'1 V',20);txt(a,6,7.4,'Vstop',20);save(f,11,58)
def levels():
 f,a=base('Hydrogen: direct path and cascade')
 for n,y in [(1,1.8),(2,3.8),(3,5.3),(4,6.4)]:a.plot([2.5,9.7],[y,y],color=INK,lw=2);txt(a,1.6,y,f'n={n}',20)
 for x,y0,y1,label in [(4.5,6.4,3.8,'A: 4→2'),(7,6.4,5.3,'B: 4→3'),(8.5,5.3,3.8,'C: 3→2')]:
  a.annotate('',(x,y1+.06),(x,y0-.06),arrowprops=dict(arrowstyle='->',lw=3,color=SEA));txt(a,x+.7,(y0+y1)/2,label,17)
 save(f,11,59)
if __name__=='__main__':
 heart();chromosome();protein();energy_profile();orbit();charges();mirror();seed();root();wet_test();cyanide();freeze();stress();pendulum();layers();photo();levels()
 cards(10,18,'Calorimeter: equilibrium data',['Water: 200 g at 25°C','Metal: 100 g at 85°C','Final temperature: 30°C; water c=4.2 J g⁻¹ K⁻¹'])
 cards(11,8,'Two food fermentations',['P: dough → ethanol + CO₂','Q: milk → lactic acid in curd'])
 cards(11,9,'Two noncompatible sticky ends',['Vector: E / 5′–AATT  ...  H / 5′–AGCT','Insert: E-compatible left ... H-compatible right','E and H overhangs do not pair with each other'])
