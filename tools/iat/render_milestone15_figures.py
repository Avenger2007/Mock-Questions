"""Exact line diagrams for corrected questions; fixed image IDs are retained."""
from pathlib import Path
import json,re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Ellipse,Rectangle,Polygon
from PIL import Image
R=Path(__file__).resolve().parents[2];O=R/'IISER/images'
plt.rcParams.update({'font.size':16,'axes.labelsize':17,'xtick.labelsize':14,'ytick.labelsize':14})
def board(title):
 f,a=plt.subplots(figsize=(10,7.5));a.set(xlim=(0,10),ylim=(0,7.5));a.axis('off');a.text(5,7.13,title,ha='center',fontsize=19,weight='bold');return f,a
def text(a,x,y,s,size=15):a.text(x,y,s,ha='center',va='center',fontsize=size)
def line(a,x,y,u,v,style='-'):a.plot([x,u],[y,v],style,color='black',lw=2)
def arrow(a,p,q):a.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',lw=2,color='black'))
def save(f,t,n):
 f.savefig(O/f'IAT_T{t:02}_Q{n:02}.png',dpi=150,bbox_inches='tight',pad_inches=.2,facecolor='white');plt.close(f)

f,a=board('Electrolysis: measured current and time')
a.add_patch(Rectangle((1.5,1.3),7,3.9,fill=False,lw=2))
for x,sgn in [(3,'−'),(7,'+')]:
 a.add_patch(Rectangle((x-.12,2.6),.24,3,fill=False,lw=2));text(a,x,5.95,sgn,21)
line(a,3,5.6,3,6.35);line(a,3,6.35,7,6.35);line(a,7,6.35,7,5.6)
text(a,5,6.72,'DC supply: I = 2.00 A; t = 4825 s',15)
text(a,5,1.95,'Concentrated aqueous CuCl₂',17)
text(a,3,3.7,'Inert cathode',12);text(a,7,3.7,'Inert anode',12)
save(f,5,28)

f,a=board('Octahedral positions and connected donor pairs')
pts={'z+':(0,1.65),'z-':(0,-1.65),'x+':(1.6,0),'x-':(-1.6,0),'y+':(.95,.95),'y-':(-.95,-.95)}
for cx,lab,chlor,pairs in [(2.65,'Arrangement X',{'z+','x+'},[('z-','y-'),('x-','y+')]),(7.35,'Arrangement Y',{'z+','z-'},[('x+','y+'),('x-','y-')])]:
 text(a,cx,3.65,'Co',16)
 for name,(dx,dy) in pts.items():
  line(a,cx+.25*np.sign(dx),3.65+.25*np.sign(dy),cx+dx*.78,3.65+dy*.78,'--' if name=='y-' else '-')
  text(a,cx+dx,3.65+dy,'Cl' if name in chlor else 'N',14)
 for u,v in pairs:
  x,y=pts[u];xx,yy=pts[v]
  a.annotate('',xy=(cx+x,3.65+y),xytext=(cx+xx,3.65+yy),
             arrowprops=dict(arrowstyle='-',connectionstyle='arc3,rad=.35',lw=1.8))
 text(a,cx,1.05,lab,14)
text(a,5,.45,'Each joined N pair belongs to one en ligand; projections are schematic',12)
save(f,8,17)

f,a=plt.subplots(figsize=(10,7.5));s=np.linspace(0,30,301)
a.plot(s,10*s/(2+s),color='black',lw=2.5,label='No inhibitor')
a.plot(s,10*s/(6+s),color='black',lw=2.5,ls='--',label='With X')
a.axhline(10,color='black',ls=':',lw=1);a.axhline(5,color='black',ls=':',lw=1)
a.set(xlabel='Substrate concentration (relative units)',ylabel='Initial rate (relative units)',xlim=(0,30),ylim=(0,11),xticks=[0,2,6,10,20,30],yticks=[0,5,10])
a.legend(loc='lower right');f.tight_layout();save(f,9,3)

f,a=plt.subplots(figsize=(10,7.5));x=np.linspace(0,1,201);ideal=50+10*x;actual=ideal+140*x*(1-x)
a.plot(x,actual,'k-',lw=2.5,label='Measured equilibrium pressure')
a.plot(x,ideal,'k--',lw=1.5,label='Ideal comparison')
# Exact extremum of 50+150x-140x².
xm=150/280;pm=50+150*xm-140*xm*xm
a.plot([xm],[pm],'ko');a.axvline(xm,color='black',ls=':',lw=1)
a.annotate('Vapour and liquid compositions coincide',xy=(xm,pm),xytext=(.12,102),fontsize=12,arrowprops=dict(arrowstyle='->',color='black'))
a.set(xlabel='Liquid mole fraction of A',ylabel='Vapour pressure (kPa)',xlim=(0,1),ylim=(0,110),xticks=[0,.25,.5,.75,1],yticks=[0,25,50,75,100])
a.legend(loc='lower right',fontsize=12);f.tight_layout();save(f,9,27)

f,a=board('Four different ligands in a square plane')
text(a,5,3.7,'M',22)
for dx,dy,s in [(0,1.8,'A'),(1.8,0,'B'),(0,-1.8,'C'),(-1.8,0,'D')]:
 line(a,5+.35*np.sign(dx),3.7+.35*np.sign(dy),5+dx*.8,3.7+dy*.8);text(a,5+dx,3.7+dy,s,21)
text(a,5,.65,'A, B, C and D denote four distinct monodentate ligands',14);save(f,12,17)

f,a=board('Flower: whorls and longitudinal attachment')
cx,cy=2.6,3.8
a.add_patch(Circle((cx,cy),2.1,fill=False,ec='black',lw=1.8))
for radius,letter in [(2.1,'K'),(1.5,'C'),(.9,'A')]:
 for j in range(5):
  th=np.pi/2+j*2*np.pi/5;x,y=cx+radius*np.cos(th),cy+radius*np.sin(th)
  a.add_patch(Ellipse((x,y),.55,.38,angle=np.degrees(th),fc='white',ec='black'))
  text(a,x,y,letter,11)
text(a,cx,cy,'G(2)',13);text(a,2.6,.55,'K: joined calyx; C and A: free members',11)
a.add_patch(Ellipse((7.3,4.65),1.15,1.65,fill=False,lw=2));line(a,7.3,3.83,7.3,1.7);line(a,7.3,5.48,7.3,6.35)
line(a,6.85,6.35,7.75,6.35);line(a,7.3,3.1,5.8,4.0);line(a,7.3,3.1,8.8,4.0)
line(a,7.3,3.1,6.2,3.5);line(a,7.3,3.1,8.4,3.5)
line(a,7.3,3.1,6.5,4.6);line(a,7.3,3.1,8.1,4.6)
text(a,7.3,4.65,'ovary',12);text(a,7.3,1.1,'Longitudinal section',13)
text(a,7.3,2.6,'Other whorls attach here',11)
save(f,14,2)

f,a=board('Trophic production and measured transfers')
for x,y,name,detail in [(5,5.7,'Plants','GPP 10000; respiration 4000 kJ'),(2.5,3.65,'Herbivore A','Assimilation 2000; respiration 1400'),(7.5,3.65,'Herbivore B','Assimilation 1000; respiration 700'),(5,1.35,'Predator','Assimilates 80%; respiration 250 kJ')]:
 a.add_patch(Rectangle((x-2.15,y-.55),4.3,1.1,fill=False,lw=1.5));text(a,x,y+.18,name,15);text(a,x,y-.25,detail,10)
arrow(a,(4.4,5.1),(3,4.25));arrow(a,(5.6,5.1),(7,4.25))
arrow(a,(3,3.0),(4.4,2.0));arrow(a,(7,3.0),(5.6,2.0))
text(a,2.1,2.5,'½ of A production',11);text(a,7.9,2.5,'⅔ of B production',11)
save(f,14,10)

f,a=board('Initial particles and two oxidation stages')
for x in (1.1,2,2.9):a.add_patch(Circle((x,5.4),.3,fill=False,lw=2));text(a,x,5.4,'S',13)
for x in (4.5,5.8,7.1,8.4):
 for xx in (x-.18,x+.18):a.add_patch(Circle((xx,5.4),.19,fill=False,lw=1.5));text(a,xx,5.4,'O',10)
text(a,2,6.2,'3 mol S atoms',15);text(a,6.5,6.2,'4 mol O₂ molecules',15)
text(a,5,4.35,'Each particle symbol represents 1 mol of that species',12)
for cx,n in [(2.5,2),(7.5,3)]:
 text(a,cx,2.5,'S',18)
 angles=[40,140] if n==2 else [90,210,330]
 for deg in angles:
  dx,dy=.9*np.cos(np.deg2rad(deg)),.9*np.sin(np.deg2rad(deg))
  line(a,cx+.2*np.sign(dx),2.5+.2*np.sign(dy),cx+dx*.75,2.5+dy*.75)
  text(a,cx+dx,2.5+dy,'O',16)
 text(a,cx,.8,'SO₂ intermediate' if n==2 else 'SO₃ final product',14)
arrow(a,(4.0,2.45),(5.6,2.45));text(a,5,3.05,'Further O₂',13)
save(f,14,27)

f,a=board('Nitrite donor-atom connectivity')
text(a,1.0,5.5,'X',18);text(a,1.0,2.3,'Y',18)
for cy,chain in [(5.2,['Co(NH₃)₅','N','O⁻']),(2.0,['Co(NH₃)₅','O','N'])]:
 text(a,3,cy,chain[0],18);text(a,5.6,cy,chain[1],20);text(a,7.7,cy,chain[2],20)
 line(a,4.15,cy,5.2,cy);line(a,6,cy,7.3,cy)
 if cy>3:
  text(a,5.6,cy+1.0,'O',19);line(a,5.5,cy+.25,5.5,cy+.7);line(a,5.7,cy+.25,5.7,cy+.7)
 else:
  text(a,8.8,cy+.9,'O',19);line(a,7.9,cy+.2,8.5,cy+.7);line(a,8.0,cy+.1,8.6,cy+.6)
text(a,5,.55,'Both coordination cations have charge +2; each has two external Cl⁻',13)
save(f,15,17)

f,a=board('Aniline protection, substitution and deprotection')
def ring(cx,cy,group,bromine=False):
 ang=np.deg2rad(np.arange(90,450,60));xy=np.c_[cx+.58*np.cos(ang),cy+.58*np.sin(ang)]
 a.add_patch(Polygon(xy,closed=True,fill=False,lw=2));a.add_patch(Circle((cx,cy),.30,fill=False,lw=1))
 line(a,cx,cy+.58,cx,cy+.95);text(a,cx,cy+1.22,group,14)
 if bromine:line(a,cx,cy-.58,cx,cy-.95);text(a,cx,cy-1.18,'Br',15)
ring(2.5,5.0,'NH₂');ring(7.5,5.0,'NH–C(=O)–CH₃')
ring(7.5,2.0,'NH–C(=O)–CH₃',True);ring(2.5,2.0,'NH₂',True)
arrow(a,(3.6,5.0),(6.2,5.0));text(a,5,5.5,'Acetylation',13)
arrow(a,(9,4.8),(9,2.2));text(a,9.1,3.5,'Br₂',13)
arrow(a,(6.2,2.0),(3.6,2.0));text(a,5,2.5,'Hydrolysis',13)
save(f,15,24)

f,a=board('Tank frame: final surface is not supplied')
line(a,1.5,5.5,1.5,1.5);line(a,1.5,1.5,8.5,1.5);line(a,8.5,1.5,8.5,5.5)
text(a,5,3.5,'Water',19);text(a,5,2.8,'Equilibrium free-surface shape to be determined',12)
arrow(a,(6.5,6.0),(8.5,6.0));text(a,7.5,6.45,'Tank acceleration a',14)
arrow(a,(2,0.8),(4,0.8));text(a,4.4,.8,'+x',13)
arrow(a,(.7,1.8),(.7,3.8));text(a,.7,4.2,'+z',13)
save(f,15,48)

f,a=plt.subplots(figsize=(10,7.5));x=np.linspace(0,.0032,100)
a.plot(x,24-6000*x,'k-',lw=2.5,label='X: slope −6000 K')
a.plot(x,24-3000*x,'k--',lw=2.5,label='Y: slope −3000 K')
a.set(xlabel='Reciprocal temperature 1/T (K⁻¹)',ylabel='ln k',xlim=(0,.0033),ylim=(0,26),xticks=[0,.001,.002,.003])
a.legend();a.grid(alpha=.15);f.tight_layout();save(f,15,27)

f,a=board('Field and loop area both change')
a.add_patch(Circle((5,3.8),2.1,fill=False,lw=2.5))
for x,y in [(4,4.8),(6,4.8),(4,2.8),(6,2.8)]:text(a,x,y,'×',25)
line(a,5,3.8,7.1,3.8);text(a,6.1,4.2,'r(t)',15)
text(a,5,6.3,'B(t) = B₀(1 − αt), into page',17)
text(a,5,.8,'r(t) = r₀(1 + αt);  0 < t < 1/α',16)
save(f,7,56)

f,a=board('A tangential impulse at fixed orbital radius')
a.add_patch(Circle((4.5,3.6),2.2,fill=False,lw=1.5,ls='--'))
a.add_patch(Circle((4.5,3.6),.35,fill=False,lw=2));text(a,4.5,3.6,'M',14)
a.add_patch(Circle((6.7,3.6),.12,color='black'))
line(a,4.9,3.6,6.5,3.6);text(a,5.7,3.2,'r',17)
arrow(a,(6.7,3.8),(6.7,5.5));text(a,8.1,5.2,'v after impulse',13)
text(a,5,.8,'v = √[3GM/(2r)]; position unchanged during impulse',14)
save(f,10,52)

f,a=board('Infer acceleration from the measured periods')
for x,length,name in [(3,2.8,'P'),(7,1.4,'Q')]:
 a.add_patch(Circle((x,5.5),.07,color='black'));line(a,x,5.5,x+.7,5.5-length)
 a.add_patch(Circle((x+.7,5.5-length),.17,fill=False,lw=2))
 text(a,x,6.1,name,20);text(a,x+1.0,5.1-length/2,'L' if name=='P' else 'L/2',16)
text(a,3,1.5,'Lab: g',17);text(a,7,1.5,'Lift: a upward (unknown)',14)
arrow(a,(8.8,2.2),(8.8,3.5));text(a,5,.6,'Measured TQ / TP = 1/2',17)
save(f,11,52)

specs={
(5,28):('An inert-electrode copper chloride cell, DC supply, 2.00 A and 4825 s, with correct electrode signs.','An electrolytic cell with inert positive and negative electrodes and measured current and time.'),
(7,56):('A circular loop, inward field symbols, radius r(t)=r0(1+alpha t), field B(t)=B0(1-alpha t), and allowed time interval; no induced-current arrow.','An expanding loop lies in an inward field whose magnitude decreases according to the displayed formula.'),
(8,17):('Two octahedral site projections with chloride positions and explicit en donor-pair connections; no optical-isomer count.','Adjacent versus opposite chloride sites with connected pairs of nitrogen donors.'),
(9,3):('Substrate axis with ticks 0,2,6,10,20,30; rate axis 0,5,10; solid and dashed kinetic curves, common asymptote at 10.','Enzyme-rate curves with different half-maximum substrate concentrations and equal limiting rate.'),
(9,27):('Pressure in kPa versus liquid mole fraction, pure endpoints, ideal comparison and an interior maximum marked as equal phase compositions.','A vapour-pressure curve has an interior maximum with coincident liquid and vapour compositions.'),
(10,52):('A circular initial orbit with radius r, central mass M, fixed impulse position and tangential final speed sqrt(3GM/(2r)); no final circular orbit.','A satellite receives a tangential speed change at the same labelled radius r.'),
(11,52):('Pendulum P length L in lab gravity g; Q length L/2 in a lift of unknown upward acceleration a; measured period ratio one half.','Two pendulums have specified lengths and a measured period ratio, with lift acceleration left unknown.'),
(12,17):('A square-planar metal centre and four distinct ligand labels A,B,C,D; no isomer total.','Four different ligands occupy sites of a square-planar coordination complex.'),
(14,2):('Five joined calyx members K, five free petals C, five free stamens A, fused two-carpel ovary and longitudinal whorl insertion below it.','Floral whorls and a section showing the ovary above the insertion of other whorls.'),
(14,10):('Four trophic compartments, the stated production and respiration quantities, specified consumed fractions and predator assimilation fraction.','A trophic budget links two herbivores to a predator with measured transfer fractions.'),
(14,16):('Linear CO2 and bent H2O bond directions with equal within-molecule bond-dipole arrows.','Bond dipoles oppose in linear carbon dioxide and form an angle in water.'),
(14,20):('Zinc and copper electrodes in separately labelled solutions, salt bridge, wire and copper dilution note.','A Daniell cell before copper-ion dilution has labelled electrodes, ions and salt bridge.'),
(14,27):('Three sulfur atom symbols and four diatomic oxygen symbols, each representing one mole, followed by explicit SO2 and SO3 connectivity sketches.','Initial sulfur and oxygen particle counts precede two structurally drawn sulfur oxide stages.'),
(14,48):('Position in metres 0 to 3; force in newtons rising linearly 0 to 4 over 0 to 2 then constant to 3.','A force-position curve rises linearly then has a constant second segment.'),
(14,51):('An upright block intersecting the waterline and both densities 600 and 1000 kg per cubic metre.','A partly immersed uniform block has its density and the water density labelled.'),
(14,53):('Two equal positive point charges at -a and +a on a common x-axis, with origin indicated.','Equal positive charges lie symmetrically on the x-axis.'),
(14,57):('Converging lens, an object 5 cm left of it, and focal points 10 cm away; no final image or solved ray.','A converging lens has an object inside its left focal distance.'),
(15,2):('Two frog atria and one ventricle, separate labelled lung and systemic inflow arrows.','Frog-heart chambers have labelled pulmonary and systemic return pathways.'),
(15,4):('Vascular bundle, chloroplast-rich bundle-sheath cell ring and outer mesophyll cells.','A leaf vascular bundle is surrounded by bundle sheath and mesophyll.'),
(15,17):('The same five-ammonia cobalt centre attached to nitrite through N in X and O in Y; external chlorides stated.','Two complexes differ in the nitrite donor atom attached to cobalt.'),
(15,24):('Four benzene-ring structures retaining nitrogen, showing NH2 to NHCOCH3 protection, para bromination and NH2 regeneration.','Structural drawings track aniline acetylation, para bromination and hydrolysis.'),
(15,27):('ln k against inverse temperature, slopes -6000 and -3000 K, with the same intercept for equal pre-exponential factors.','Two Arrhenius lines have a common intercept and different negative slopes.'),
(15,48):('Open tank, water, rightward acceleration and x/z axes, without an inclined equilibrium waterline.','An accelerating open tank specifies axes and acceleration without providing the final surface slope.'),
(15,57):('Glass index 1.5, air index 1.0, interface, normal, incident ray and 50-degree angle measured to normal.','A ray reaches a glass-to-air boundary at a labelled incidence angle.'),
(15,60):('Two slits, a thin phase sheet beside one, and a screen at distance D; no fringe-spacing result.','A two-slit apparatus has a thin sheet at one slit and a screen at distance D.'),
}
registry=R/'IISER/IAT_images.md';content=registry.read_text()
# The abbreviated 14/15 tables were the final sections; replace them with full specifications.
content=content.split('## Test 14 — question figures')[0].rstrip()+'\n'
for (t,n),(must,alt) in specs.items():
 p=R/f'IISER/IAT NEW TEST {t}.json';d=json.loads(p.read_text());q=d['questions'][n-1]
 q['image_alt']=alt
 if (t,n)==(14,2):
  q['question']='The diagram shows five united sepals, five free petals, five stamens and two fused carpels. Use the longitudinal section to infer ovary position. Which floral formula matches both views? Here brackets denote fusion.'
 if (t,n)==(5,2):q['difficulty']='medium'
 d['questions'][n-1]=q;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 filename=q['image_reference'];w,h=Image.open(O/filename).size
 block=f"## Test {t} — Q{n} ({q['id']}) — {q['subject']}\n- **File name:** {filename}\n- **Purpose:** {q['sub_topic']}; interpret the encoded structure, control or quantitative relation.\n- **Aspect ratio / size:** {w} × {h} px.\n- **Style:** Textbook diagram on white with clear labelled lines and contrasting line styles.\n- **Must show:** {must}\n- **Axes (graphs):** Quantities, units and ticks as specified above; not applicable to non-graph structures.\n- **Text in image:** Only the stated labels and experimental data, no solution.\n- **Must NOT show:** Answer letters, a computed result, or a derived conclusion that the student must supply.\n- **Alt text:** {alt}\n"
 if t<14:
  pattern=rf"## Test {t} — Q{n} \({q['id']}\).*?(?=\n## |\Z)"
  content,count=re.subn(pattern,lambda m:block.rstrip()+'\n',content,flags=re.S)
  if count==0:
   oldlines=content.splitlines(keepends=True)
   selected=[s for s in oldlines if s.startswith('|') and q['id'] in s]
   assert len(selected)==1,(t,n,len(selected))
   content=''.join(s for s in oldlines if s not in selected)+'\n'+block
  else:assert count==1,(t,n,count)
 else:content+='\n'+block
registry.write_text(content)
print('Rebuilt 15 corrected figures and wrote complete specifications for',len(specs),'images')
