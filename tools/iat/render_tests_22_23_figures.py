"""Exact diagrams individually specified for the fixed Test 22–23 IDs."""
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
def txt(a,x,y,s,size=15):a.text(x,y,s,ha='center',va='center',fontsize=size,bbox={'fc':'white','ec':'none','pad':.5})
def line(a,p,q,style='-'):a.plot([p[0],q[0]],[p[1],q[1]],style,color='black',lw=2)
def arrow(a,p,q):a.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','lw':2})
def save(f,t,n,subject,purpose,show,alt):
 f.savefig(O/f'IAT_T{t:02}_Q{n:02}.png',dpi=150,facecolor='white');plt.close(f)
 specs.append(dict(test=t,question=n,subject=subject,purpose=purpose,must_show=show,alt=alt,prohibited='No selected option, calculated result, answer-specific classification or solution.'))
f,a=board('Adult frog: posterior duct schematics')
for cx,lab in [(2.6,'Male'),(7.4,'Female')]:
 txt(a,cx,6.4,lab,17);a.add_patch(Ellipse((cx,4.7),.65,1.3,fill=False,lw=2));txt(a,cx-.85,4.8,'Kidney',12);a.add_patch(Rectangle((cx-.7,1.6),1.4,.6,fill=False,lw=2));txt(a,cx,1.9,'Cloaca',12);line(a,(cx,4.05),(cx,2.2));txt(a,cx+.35,3.1,'U')
a.add_patch(Ellipse((1.2,5.8),.55,.7,fill=False,lw=2));txt(a,1.2,6.4,'Testis',12);arrow(a,(1.45,5.6),(2.25,5.0));txt(a,1.05,3.7,'Sperm path\nvia kidney',12)
a.add_patch(Ellipse((9,5.8),.6,.6,fill=False,lw=2));txt(a,9,6.4,'Ovary',12);arrow(a,(9,5.3),(8.75,4.9));a.plot([8.4,8.8,8.4,8.8,8.4,8.4],[5,4.5,4,3.5,3,2.2],'k',lw=2);line(a,(8.4,2.2),(8.1,2.2));txt(a,9.1,3.5,'V');txt(a,5,.6,'Separate female oviduct; shared terminal chamber. Not to scale.',13)
save(f,22,2,'Biology','Read sex-specific duct connectivity before assigning transport roles.','Two panels; testis sperm pathway enters male kidney/ureter U; female kidney U separate from oviduct V; ovary separate from oviduct funnel; common cloaca each.','Male sperm pathway joins kidney-associated U; female V is separate from renal U, with both reaching the cloaca.')
f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.17,bottom=.16,right=.94,top=.92);wl=[400,450,550,650,700];a.plot(wl,[30,80,5,90,15],'k-o',label='Bacterial accumulation');a.plot(wl,[35,85,10,80,12],'k--',label='Extracted-pigment absorption');a.set(xlabel='Wavelength (nm)',ylabel='Relative response (normalised units)',xticks=wl,yticks=[0,20,40,60,80,100],ylim=(0,110));a.legend(fontsize=12)
save(f,22,4,'Biology','Compare a spatial oxygen action pattern with absorption.','Five wavelength bands; high bacterial and absorption responses near450/650,low550; axes and two distinct line styles.','Bacterial accumulation and extracted-pigment absorption have blue/red peaks and a low green-band response.')
f,a=board('Three tissue structures: schematic')
for j,x in enumerate([1.1,2.1,3.1]):
 a.add_patch(Rectangle((x,2.8),.8,2.8,fill=False,lw=1.5))
 for px,py in [(x,2.8),(x+.8,2.8),(x,5.6),(x+.8,5.6)]:a.add_patch(Circle((px,py),.10,color='black'))
txt(a,2.4,1.9,'P: living; corner thickening',12)
for x in [4.8,5.5]:a.add_patch(Ellipse((x,4.2),.5,3.1,fill=False,lw=5))
txt(a,5.2,1.9,'Q: dead; lignified',12)
a.add_patch(Rectangle((7.6,2.6),1.0,3.1,fill=False,lw=4));line(a,(7.6,4.2),(7.85,4.2));line(a,(8.35,4.2),(8.6,4.2));txt(a,8.1,1.9,'R: perforated tube',12);txt(a,8.1,1.3,'Vascular bundle',12)
save(f,23,2,'Biology','Connect wall architecture and tissue position to support and transport.','P adjacent elongated living cells with thickened corners; Q narrow-lumen thick-walled fibres; R thick-walled tube with partial perforated end wall.','P has thick corners; Q has thick narrow-lumen walls; R is a perforated conducting tube in vascular tissue.')
f,a=board('Nucleotide polarity: labelled connectivity')
for x,name,base in [(2.7,'Sugar 1','G'),(7.2,'Sugar 2','U')]:
 a.add_patch(Rectangle((x-.8,3.5),1.6,1.2,fill=False,lw=2));txt(a,x,4.1,name,13);line(a,(x,4.7),(x,5.6));txt(a,x,5.9,"1′ — "+base,14);line(a,(x,3.5),(x,2.6));txt(a,x,2.25,"2′ OH",14)
line(a,(.7,4.1),(1.9,4.1));txt(a,.7,5,"Free 5′\nphosphate",12)
line(a,(3.5,4.1),(6.4,4.1));txt(a,4.95,4.65,"3′O — P — O5′",14)
line(a,(8,4.1),(9.3,4.1));txt(a,9.0,5,"Free 3′ OH",12);txt(a,5,1,"Boxes show sugar attachment positions; bases and OH labels are explicit.",12)
save(f,23,14,'Biology','Read sugar composition and the exposed backbone extension end.','Two sugars each2OH; G/Ubasesat1;free5phosphateleft;internucleotide3O-P-O5 link;free3OHright.','Two 2-prime-hydroxyl sugars are connected from 3-prime oxygen through phosphate to 5-prime oxygen; a free 3-prime OH is on the right.')
f,a=board('Nitrophenol positional isomers')
for cx,sub,lab in [(2.5,np.pi/6,'X: ortho'),(7.5,-np.pi/2,'Y: para')]:
 ang=np.pi/2+np.arange(7)*np.pi/3;pts=np.column_stack([cx+1.15*np.cos(ang),4.2+1.15*np.sin(ang)]);a.plot(pts[:,0],pts[:,1],'k',lw=2);a.add_patch(Circle((cx,4.2),.57,fill=False,lw=1.5));line(a,(cx,5.35),(cx,5.8));txt(a,cx,6.1,'OH',16)
 p=np.array([cx,4.2])+1.15*np.array([np.cos(sub),np.sin(sub)]);q=np.array([cx,4.2])+1.7*np.array([np.cos(sub),np.sin(sub)]);line(a,p,q);txt(a,*(q+.25*np.array([np.cos(sub),np.sin(sub)])),'NO₂',15);txt(a,cx,1.2,lab,16)
save(f,22,16,'Chemistry','Compare the geometrical opportunities for internal hydrogen bonding.','Two aromatic rings; OH atC1both;NO2adjacentX/oppositeY; no hydrogen-bond or dimer answer arrows.','The nitro group is adjacent to OH in X and opposite OH in Y.')
f,a=board('Unsaturated hydroxy acid: explicit substituents')
for y in [3.94,4.06]:line(a,(4.2,y),(5.8,y))
txt(a,4,4,'C',20);txt(a,6,4,'C',20)
for p,q,lab in [((3.8,4.2),(2.5,5.4),'CH₂OH'),((3.8,3.8),(2.5,2.6),'H'),((6.2,4.2),(7.5,5.4),'H'),((6.2,3.8),(7.5,2.6),'COOH')]:line(a,p,q);txt(a,*q,lab,18)
save(f,22,25,'Chemistry','Assign principal group, locants and double-bond configuration.','C=C withCH2OHupperleft/Hlowerleft;Hupperright/COOHlowerright; no name or E/Zdescriptor.','CH2OH and COOH lie on opposite sides of the central double bond.')
f,a=board('Seven-proton species: supplied orbital occupancy')
for x,lab,ar in [(1.4,'1s','↑↓'),(3.0,'2s','↑'),(4.6,'2p','↑'),(5.7,'','↑'),(6.8,'','↑'),(8.6,'3s','↑')]:
 a.add_patch(Rectangle((x-.45,3.4),.9,1.0,fill=False,lw=2));txt(a,x,3.9,ar,24)
 if lab:txt(a,x,2.7,lab,18)
line(a,(4.15,2.15),(7.25,2.15));txt(a,5.7,1.65,'Three separate 2p orbitals',14)
save(f,23,18,'Chemistry','Count occupation and spin before classifying charge and excitation.','1spair,2ssingle,threeparallel2psingles,3ssingle;nucleus7protons; no element or charge answer.','The diagram contains one paired 1s orbital and five singly occupied orbitals across 2s, 2p and 3s.')
f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.16,bottom=.14,right=.95,top=.93);xx=[0,1,2,3,4];yy=[0,40,-40,30,-20]
for j in range(4):
 u=np.linspace(0,1,80);a.plot(j+u,(yy[j]+yy[j+1])/2+(yy[j]-yy[j+1])/2*np.cos(np.pi*u),'k',lw=2)
for x,y,lab in zip(xx,yy,['Reactants','TS1','Intermediate','TS2','Products']):a.plot(x,y,'ko');a.annotate(f'{lab}\n{y:+d}',(x,y),xytext=(0,12 if y>=0 else -28),textcoords='offset points',ha='center',fontsize=12)
a.axhline(0,color='black',ls='--',lw=.7);a.set(xlim=(-.5,4.5),ylim=(-65,65),xticks=[],yticks=[-40,-20,0,20,40,60],xlabel='Reaction coordinate',ylabel='Energy (kJ mol⁻¹)')
save(f,23,19,'Chemistry','Measure each local barrier from its own minimum.','Twopeaks40,30;intermediate-40;reactants0;products-20;axesunits; no barrier differences.','A deeper intermediate separates a 40-unit first peak from a 30-unit second peak.')
f,a=board('Fused aromatic skeleton: one bond contributor');a.set_aspect('equal')
for cx,doubles in [(3.7,[0,2,4]),(3.7+1.5*np.sqrt(3),[0,4])]:
 angles=np.pi/6+np.arange(6)*np.pi/3;pts=np.column_stack([cx+1.5*np.cos(angles),4.2+1.5*np.sin(angles)])
 for j in range(6):
  p,q=pts[j],pts[(j+1)%6];line(a,p,q)
  if j in doubles:
   centre=np.array([cx,4.2]);p2=.83*p+.17*centre;q2=.83*q+.17*centre;line(a,p2,q2)
txt(a,5,.9,'Unlabelled vertices are carbon; hydrogens omitted.',13)
save(f,23,20,'Chemistry','Count shared ring vertices and junction valences.','Twohexagonssharingoneverticaledge;fivealternatingdoublebondsinonevalidKekulematching; no molecularformula.','Two fused hexagons share two junction carbons and one edge; only one resonance contributor is drawn.')
f,a=board('Banked circular road: transverse section');a.set_aspect('equal')
line(a,(2.7,1.8),(7,6.1));line(a,(2.7,1.8),(5,1.8),'--');a.add_patch(Arc((2.7,1.8),2,2,theta1=0,theta2=45,lw=1.4));txt(a,4,2.25,'45°',14);a.add_patch(Rectangle((4.65,3.8),.5,.4,angle=45,fill=False));arrow(a,(5,4.1),(3.9,5.2));txt(a,3.7,5.55,'N');arrow(a,(5,4.1),(5,2.4));txt(a,5.4,2.7,'mg');arrow(a,(2.5,4),(1,4));txt(a,1.6,4.6,'Toward centre',12);txt(a,5,.6,'Static friction direction is to be determined.',13)
save(f,22,47,'Physics','Read bank orientation and force geometry without fixing friction prematurely.','45degreebankrisesright;Nnormalup-left;mgdown;centreleft;no friction arrow or speed answers.','The road rises outward, with normal force tilted inward and weight vertical.')
f,a=board('Same Gaussian surface geometry; changed charge positions')
for cx,lab,inside,outside,ox in [(2.5,'X','+q','−2q',.5),(7.5,'Y','−2q','+q',9.4)]:
 a.add_patch(Circle((cx,4),1.25,fill=False,lw=2));txt(a,cx,4,inside,18);txt(a,ox,5.7,outside,18);txt(a,cx,1.7,lab,18)
save(f,22,53,'Physics','Track which signed charge is enclosed at each stage.','Xencloses+qandexternal-2q;Yencloses-2qandexternal+q;identicalclosedcircles; no flux labels.','The +q and -2q charges exchange inside and outside positions between stages X and Y.')
f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.15,bottom=.15,right=.94,top=.91);tt=np.linspace(0,np.pi,200);a.plot(tt,np.sin(tt),'k',lw=2);a.plot(3*np.pi/4,1/np.sqrt(2),'ko');a.axvline(3*np.pi/4,color='black',ls='--');a.set(xlim=(0,np.pi),ylim=(0,1.95),xticks=[0,np.pi/2,3*np.pi/4,np.pi],xticklabels=['0','π/2','3π/4','π'],yticks=[0,.5,1],xlabel='Phase ωt',ylabel='Current I / I₀');a.plot([.35,1.1],[1.5,1.5],'k');a.plot([2.1,2.75],[1.5,1.5],'k');u=np.linspace(0,1,200);a.plot(1.1+u,1.5+.15*np.abs(np.sin(4*np.pi*u)),'k');a.text(.35,1.75,'A');a.text(2.75,1.75,'B');a.text(1.55,1.8,'Ideal inductor L',ha='center',fontsize=12);a.annotate('I',xy=(1.0,1.5),xytext=(.6,1.5),arrowprops={'arrowstyle':'->'},va='center')
save(f,22,55,'Physics','Relate marked current direction and graph slope to passive terminal voltage.','A-left/B-rightinductor;IentersA;sinusoidalpositivecurrentgraphmarked3pi/4;no derivative or voltage signs.','At the marked phase current is positive on the descending part of a sine curve; current enters terminal A.')
f,a=board('Two finite slits: dimensions before the screen')
for p,q in [((3,1),(3,2)),((3,3),(3,5)),((3,6),(3,6.5))]:line(a,p,q)
line(a,(8,1),(8,6.5));line(a,(3,4),(8,4),'--');arrow(a,(1.4,2),(1.4,3));txt(a,.9,2.5,'a');arrow(a,(1.4,5),(1.4,6));txt(a,.9,5.5,'a');line(a,(3.4,2.5),(4,2.5),'--');line(a,(3.4,5.5),(4,5.5),'--');arrow(a,(4,2.5),(4,5.5));txt(a,4.8,4.0,'d=3a');txt(a,8.8,3,'Screen',14)
save(f,22,58,'Physics','Read slit width separately from centre separation.','Twoverticalgapswidtha;centresseparation3a;screen;no intensity envelope or missing-order labels.','Each slit has width a and their centres are separated by three slit widths.')
f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.15,bottom=.15,right=.94,top=.93);a.plot([0,2,4],[-1,1,-1],'k-o',lw=2);a.axhline(0,color='black',lw=.8);a.set(xlim=(0,4),ylim=(-1.4,1.4),xticks=[0,1,2,3,4],yticks=[-1,0,1],xlabel='Time (s)',ylabel='Velocity (m s⁻¹)')
save(f,23,46,'Physics','Read signed and unsigned areas after two direction reversals.','Continuousline(0,-1)to(2,+1)to(4,-1);axesunitsandzerocrossingsat1,3; no area or displacement answers.','Velocity rises from -1 to +1 and falls back to -1 over four seconds.')
f,a=board('Isolated capacitor with partial dielectric overlap')
line(a,(2,3),(8,3));line(a,(2,5),(8,5));a.add_patch(Rectangle((1,3.15),4,1.7,fill=False,lw=2));txt(a,3.2,4,'κ=3',18);txt(a,7,4,'Empty gap',13);txt(a,8.5,5,'+Q');txt(a,8.5,3,'−Q');arrow(a,(2,2),(5,2));txt(a,3.5,1.55,'Inserted length x');arrow(a,(2,6),(8,6));txt(a,5,6.45,'Plate length L');arrow(a,(9,3),(9,5));txt(a,9.45,4,'d');txt(a,5,.6,'Width b is perpendicular to page; no battery.',13)
save(f,23,54,'Physics','Identify the two parallel plate-area regions and the fixed-charge constraint.','ParallelplateslengthLgapd;dielectric3fillsfullgapoverlapxandwidthb;emptyL-x;isolated+Q/-Q; no force arrow.','A dielectric slides into part of an isolated plate area while charge remains fixed.')
f,a=board('Crossed-field selector followed by magnetic analyser')
for x,w in [(2,2.5),(6.2,2.8)]:
 a.add_patch(Rectangle((x,2.5),w,3,fill=False,lw=1.5))
 for xx in np.arange(x+.4,x+w,.8):
  for yy in [3,4,5]:a.add_patch(Circle((xx,yy),.09,fill=False));a.plot(xx,yy,'k.',ms=3)
arrow(a,(.5,4),(2,4));txt(a,1,4.6,'+ ions');arrow(a,(3.3,3.1),(3.3,4.9));txt(a,3.7,4.9,'E',14);arrow(a,(4.6,4),(6.1,4));txt(a,3.2,1.8,'Selector B along +z',12);txt(a,7.6,1.8,'Analyser Bₐ along +z',12);txt(a,5,.7,'Selected beams enter the analyser at the same velocity.',13)
save(f,23,55,'Physics','Separate the speed-setting stage from the radius-measurement stage.','SelectorEupBoutandincident+xpositiveions;followingpureBanalysersamefieldforbothbeams; no radius paths or ratio answers.','Positive ions cross an electric-plus-magnetic selector before entering a magnetic-only analyser.')
f,a=board('Moving loop at its first contact with a field stripe')
a.add_patch(Rectangle((4,2),4,4,fill=False,lw=1.5));a.add_patch(Rectangle((4-4/3,3),4/3,4/3,fill=False,lw=2));arrow(a,(1,3.7),(2.6,3.7));txt(a,1.6,4.3,'v');txt(a,2.8,2.4,'Side a');arrow(a,(4,6.3),(8,6.3));txt(a,6,6.6,'Stripe width 3a',14)
for x in [4.5,5.5,6.5,7.5]:
 for y in [2.6,3.6,4.6,5.6]:txt(a,x,y,'×',17)
txt(a,6,1.1,'Uniform B into page');txt(a,2.6,1.1,'t=0',14)
save(f,23,56,'Physics','Determine entry, full immersion and exit overlap intervals.','Squareloopsideaentersstripewidth3a;leadingedgeatleftboundaryt0;vright;Bintopage; no currents or interval answers.','The leading edge of a square loop first touches a stripe three times its side length wide.')
(R/'IISER/authoring/tests22_23_images.json').write_text(json.dumps(specs,ensure_ascii=False,indent=2)+'\n');print('Rendered',len(specs),'exact figures at 1200×900')
