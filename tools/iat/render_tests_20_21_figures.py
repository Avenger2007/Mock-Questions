"""Exact, individually specified instructional diagrams; no raster image generation."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Ellipse,Arc
R=Path(__file__).resolve().parents[2];O=R/'IISER/images';specs=[]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15})
def board(title):
 f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.05,right=.95,bottom=.07,top=.93);a.set(xlim=(0,10),ylim=(0,7.5));a.axis('off');a.text(5,7.1,title,ha='center',fontsize=17,weight='bold');return f,a
def text(a,x,y,s,size=15):a.text(x,y,s,ha='center',va='center',fontsize=size,bbox={'fc':'white','ec':'none','pad':.4})
def line(a,p,q,style='-'):a.plot([p[0],q[0]],[p[1],q[1]],style,color='black',lw=2)
def arrow(a,p,q):a.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','lw':2})
def save(f,t,n,subject,purpose,show,alt,prohibited='No selected option, calculated answer or explanatory solution.'):
 f.savefig(O/f'IAT_T{t:02}_Q{n:02}.png',dpi=150,facecolor='white');plt.close(f)
 specs.append(dict(test=t,question=n,subject=subject,purpose=purpose,must_show=show,alt=alt,prohibited=prohibited))
f,a=board('Floral organisation: schematic, not to scale')
ths=np.linspace(0,2*np.pi,500);rad=1.7+.25*np.cos(5*ths);a.plot(3+rad*np.cos(ths),4+rad*np.sin(ths),'k',lw=2)
for th in np.arange(5)*2*np.pi/5:
 p=(3+1.2*np.cos(th),4+1.2*np.sin(th));line(a,p,(3+.6*np.cos(th),4+.6*np.sin(th)));a.add_patch(Ellipse(p,.25,.4,angle=np.degrees(th),fill=False,lw=2))
a.add_patch(Ellipse((7.3,4),1.8,2.4,fill=False,lw=2));line(a,(7.3,2.8),(7.3,5.2))
for x in [7.0,7.6]:
 for y in [3.5,4.4]:a.add_patch(Ellipse((x,y),.25,.35,fill=False))
text(a,3,1.5,'United corolla; five attached stamens');text(a,7.3,2.2,'Ovary cross-section');text(a,5,.6,'K(5), C(5), A5; superior G(2)')
save(f,20,2,'Biology','Combine floral organisation with vegetative and fruit characters.','Five-lobed united corolla with five attached stamens; two locules, central ovules; superior G(2).','A radial five-parted flower and a two-loculed ovary with central ovule attachment.')
f,a=board('Plant cell after chromosome segregation')
a.add_patch(Rectangle((1,1.8),8,4.5,fill=False,lw=2))
for x in [3,7]:a.add_patch(Circle((x,4),.7,fill=False,lw=2));text(a,x,4,'N')
for y in [2.6,3.2,3.8,4.4,5]:a.add_patch(Circle((5,y),.14,fill=False,lw=2))
arrow(a,(4,3),(4.7,3.3));arrow(a,(6,5.3),(5.3,4.8));text(a,5,1,'Golgi-derived vesicles; fusion blocked');save(f,20,14,'Biology','Distinguish completed karyokinesis from blocked cell-plate assembly.','Two separated nuclei within one plant-cell wall; unfused vesicles at the midline; no completed cell plate.','Two nuclei flank a midline row of separate vesicles inside one cell.')
f,a=board('Underground food-storing structures P and Q')
line(a,(1,4.3),(5,4.3))
for x in [1.5,2.8,4.1]:
 line(a,(x,3.9),(x,4.7));line(a,(x,4.5),(x+.3,5));a.add_patch(Circle((x+.25,4.65),.10,fill=False));line(a,(x,4.1),(x-.2,3.3))
a.add_patch(Ellipse((7.5,4.3),1.3,3,fill=False,lw=2))
for y in [3.4,4,4.7]:line(a,(7.95,y),(8.8,y-.4))
text(a,3,2,'P: nodes, scale leaves\nand axillary buds',13);text(a,7.5,2,'Q: lateral roots;\nno nodes',13);save(f,21,2,'Biology','Homologous organ diagnosis despite a shared storage function.','P horizontal nodal swollen axis with scale leaves and buds; Q vertical swollen axis with lateral roots and no nodes.','P is a nodal underground axis; Q has lateral roots without nodes.')
f,a=board('Cereal embryo: axis and lateral structure')
line(a,(6,2.2),(6,5.7));a.add_patch(Ellipse((6,5.8),1.3,1.6,fill=False,lw=2));a.add_patch(Ellipse((6,2),1.2,1.5,fill=False,lw=2));a.add_patch(Ellipse((3.7,4),2.8,3.8,fill=False,lw=2));line(a,(4.7,4),(6,4));text(a,6,5.7,'Plumule',13);text(a,6,2,'Radicle',13);text(a,7.5,5.9,'P');text(a,7.5,2,'Q');text(a,3.7,4,'R',20);save(f,21,15,'Biology','Read the two protective sheaths and lateral cotyledon.','Embryonal axis with plumule above and radicle below; enclosing upper P and lower Q; a large lateral R attached to the axis.','P surrounds the plumule, Q surrounds the radicle, and R is lateral to the embryonal axis.')
f,a=board('Frontier orbital occupancies before ionisation')
line(a,(1,4),(4,4));text(a,2.5,4.5,'↑↓',24);text(a,2.5,3.3,'N₂: bonding σ2p');
for x in [6.3,8.5]:line(a,(x-.6,4),(x+.6,4));text(a,x,4.5,'↑',24)
text(a,7.4,3.3,'O₂: antibonding π*2p');text(a,5,1.4,'All omitted occupied orbitals are paired');save(f,20,16,'Chemistry','Identify the bonding character of the removed frontier electron.','One paired N2 sigma2p level; two degenerate O2 pi-star2p levels with parallel single arrows.','N2 has a paired bonding frontier level; O2 has one electron in each antibonding frontier level.')
f,a=board('TLC of the same compound in two eluents')
for x,h,spot,lab in [(2.8,4.5,.9,'X'),(7.2,3.6,2.16,'Y')]:
 a.add_patch(Rectangle((x-1,1.7),2,4.9,fill=False,lw=2));line(a,(x-1,2),(x+1,2));line(a,(x-1,2+h),(x+1,2+h),'--');a.add_patch(Circle((x,2+spot),.12,color='black'));text(a,x,1,lab,18)
text(a,2.8,6.9,'Front 10 cm; spot 2 cm',13);text(a,7.2,6.1,'Front 8 cm; spot 4.8 cm',13);save(f,20,22,'Chemistry','Compare distances normalised to their own solvent front.','Two silica TLC plates with common baseline; X front10 spot2 cm; Y front8 spot4.8 cm; no Rf labels.','X spot and solvent distances are 2 and 10 cm; Y distances are 4.8 and 8 cm.')
f,a=board('Lewis-pair donation: reactants')
text(a,3,4,'B',23)
for p in [(1.5,4),(3.7,5.3),(3.7,2.7)]:line(a,(3,4),p);text(a,*p,'F',20)
text(a,7,4,'N',23)
for p in [(7,5.5),(8.6,4),(7,2.5)]:line(a,(7,4),p);text(a,*p,'H',20)
text(a,6.45,4,':',24);arrow(a,(6.1,4),(3.45,4));text(a,5,1.2,'One nitrogen lone pair is donated to boron');save(f,21,16,'Chemistry','Identify the acceptor geometry after pair donation.','Trigonal BF3; pyramidal ammonia drawn as a Lewis schematic; nitrogen pair and arrow to boron; no product geometry.','A nitrogen lone pair points toward the three-coordinate boron of BF3.')
f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.17,bottom=.17,right=.94,top=.91);a.plot([20,80],[10,50],'k-o',lw=2,label='A');a.plot([20,80],[0,0],'k--',lw=2,label='B');a.set(xlim=(10,90),ylim=(-3,56),xticks=[20,80],yticks=[0,10,30,50],xlabel='Temperature (°C)',ylabel='Solubility (g / 100 mL solvent)');a.legend();save(f,21,22,'Chemistry','Choose hot filtration before finite-recovery recrystallisation.','A solubility10 at20C and50 at80C; Bzero atboth; labelled axes and units.','A solubility increases from 10 to 50 grams while B remains insoluble.')
f,a=board('Specified glycosidic links and selective cleavage')
for x,lab in [(1.5,'Glucose G2'),(5,'Glucose G1'),(8.5,'Fructose F')]:a.add_patch(Rectangle((x-1.25,3.3),2.5,1.5,fill=False,lw=2));text(a,x,4.05,lab,14)
line(a,(2.75,4.05),(3.75,4.05));line(a,(6.25,4.05),(7.25,4.05));text(a,3.25,5.1,'C1—O—C6',14);text(a,6.75,5.1,'C1—O—C2',14);arrow(a,(3.25,2.1),(3.25,3.8));arrow(a,(6.75,2.1),(6.75,3.8));text(a,3.25,1.5,'H cleaves this link');text(a,6.75,1.5,'J cleaves this link');save(f,21,26,'Chemistry','Track which anomeric carbon is freed by each selective cleavage.','Three sugar boxes; G2C1-O-G1C6 and G1C1-O-FC2; separate H/J cleavage arrows; no reducing labels.','G2 C1 links G1 C6, while G1 C1 links fructose C2; H and J cut different links.')
f,a=board('Cavity charge and grounding sequence')
a.add_patch(Circle((4.4,4),2.2,fill=False,lw=2));a.add_patch(Circle((4.0,4),1.15,fill=False,lw=2));a.plot(4.45,4.3,'ko');text(a,4.6,4.8,'+q');line(a,(6.6,4),(8,4));line(a,(8,4),(8,3));
for y,w in [(3,1),(2.8,.7),(2.6,.4)]:line(a,(8-w/2,y),(8+w/2,y))
text(a,5,.9,'Ground → disconnect → deposit +2q');text(a,2.1,6,'Outer radius R');save(f,20,53,'Physics','Track conductor charge across grounding, isolation and deposition.','Spherical outer conductor; off-centre cavity charge; initial ground lead; explicit ordered three-stage caption.','An off-centre cavity charge remains while grounding is disconnected and 2q is then added.')
f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.15,bottom=.15,right=.94,top=.94);x=np.linspace(0,4,200);a.plot(x,x*x,'k-',label='Device: V=I² (SI)');a.plot([0,6],[12,0],'k--',label='Source: V=12−2I');a.set(xlim=(0,6),ylim=(0,16),xticks=range(7),yticks=range(0,17,4),xlabel='Current I (A)',ylabel='Terminal voltage V (V)');a.legend();save(f,20,54,'Physics','Locate the nonohmic operating point through two characteristics.','Device quadratic V=I², source line V12-2I; SI axes and ticks; no marked intersection value.','An increasing quadratic device curve crosses a declining source load line.')
f,a=board('Secondary dot polarities and connection rules')
for x,turns in [(3,40),(7,60)]:
 a.add_patch(Rectangle((x-.6,3),1.2,2,fill=False,lw=2));line(a,(x,5),(x,5.7));line(a,(x,3),(x,2.3));a.add_patch(Circle((x-.35,5.25),.08,color='black'));text(a,x,4,f'{turns} turns',13);text(a,x,6.2,'Dotted end',13);text(a,x,1.8,'Undotted end',13)
text(a,5,.9,'X joins unlike ends; Y joins dotted ends');save(f,20,55,'Physics','Read relative winding polarity before series combination.','40-turn and60-turn isolated windings with upper dot and lower undotted terminals; separate connection rules X/Y.','Both upper ends are dotted; X joins unlike terminals and Y joins the dotted terminals.')
f,a=board('Single spherical air–glass interface')
line(a,(.4,3.8),(9.5,3.8));a.add_patch(Arc((8,3.8),6,7,theta1=120,theta2=240,lw=2));text(a,2,6,'Air: n=1');text(a,7.5,6,'Glass: n=1.50');
for x,lab in [(1,'Object -60 cm'),(3,'Object -30 cm'),(5,'Vertex 0'),(8,'Centre +20 cm')]:a.plot(x,3.8,'ko');text(a,x,2.5 if x in [1,5] else 4.8,lab,12)
text(a,5,1,'Axis schematic; positions not drawn to scale');save(f,20,57,'Physics','Determine signed conjugates at one convex refracting surface.','Air left, glass right; surface vertex0; curvature centre+20; object positions-30/-60; no image rays.','Two incident-side objects face one convex air-to-glass surface with centre on the glass side.')
f,a=board('Four fixed charges; test point at the origin')
line(a,(1,3.8),(9,3.8));line(a,(5,1),(5,6.5));
for p,lab in [((2.5,3.8),'+q'),((7.5,3.8),'+q'),((5,1.5),'−q'),((5,6.1),'−q')]:a.add_patch(Circle(p,.3,fill=False,lw=2));text(a,*p,lab,14)
text(a,5.4,4.2,'O');text(a,8.8,3.2,'x');text(a,5.7,6.3,'y');text(a,2,1,'Charge positions: (±a,0), (0,±a)',13);save(f,21,53,'Physics','Assess separate constrained displacement directions.','Equal positive charges on xaxis and negative on yaxis; origin; axes; perpendicular z indicated in text only.','Positive charges flank the origin horizontally and negative charges vertically.')
f,a=board('Finite magnetic stripe: entry geometry')
a.add_patch(Rectangle((3,1.5),4.5,4.6,fill=False,lw=2));line(a,(3,.9),(3,6.4),'--');line(a,(7.5,.9),(7.5,6.4),'--');arrow(a,(.6,4.5),(2.9,4.5));text(a,1.6,5,'+q, speed v');text(a,3, .5,'x=0');text(a,7.5,.5,'x=d=3R/2');
for x in [4,5.5,7]:
 for y in [2.3,3.8,5.3]:a.add_patch(Circle((x,y),.11,fill=False));a.plot(x,y,'k.',ms=3)
text(a,5.2,6.65,'B along +z (out of page)');save(f,21,56,'Physics','Compare available stripe width with the magnetic penetration radius.','Entry fromleft velocity+x,positiveq; finite0<x<3R/2stripe; out-of-pageB symbols; no trajectory or exit arrow.','A positive particle enters an out-of-page magnetic stripe whose width is 3R/2.')
(R/'IISER/authoring/tests20_21_images.json').write_text(json.dumps(specs,ensure_ascii=False,indent=2)+'\n')
print('Rendered',len(specs),'figures at 1200 by 900')
