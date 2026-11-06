"""Draw exact scientific schematics for literal authored items; no question generation."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Ellipse,Rectangle,Arc
R=Path(__file__).resolve().parents[2];out=R/'IISER/images'
plt.rcParams.update({'font.size':24,'axes.labelsize':24,'xtick.labelsize':24,'ytick.labelsize':24,'axes.titlesize':26})
S=[]
def spec(t,q,subject,purpose,show,alt):
 S.append(dict(test=t,question=q,subject=subject,purpose=purpose,must_show=show,alt=alt,prohibited='No selected answer, derived result, field-result arrow or decorative elements.'))
def canvas(t,q,title='',xlim=(0,10),ylim=(0,7)):
 f,a=plt.subplots(figsize=(12,9),dpi=100);a.set(xlim=xlim,ylim=ylim);a.set_aspect('equal');a.axis('off');a.set_title(title,pad=24);return f,a
def line(a,x,y,**kw):a.plot(x,y,color='black',lw=2.5,**kw)
def txt(a,x,y,s,**kw):a.text(x,y,s,ha=kw.pop('ha','center'),va=kw.pop('va','center'),fontsize=24,**kw)
def arrow(a,p,q,label=None):
 a.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',lw=2.5,color='black'))
 if label:txt(a,(p[0]+q[0])/2,(p[1]+q[1])/2+.25,label)
def save(f,t,q):f.savefig(out/f'IAT_T{t}_Q{q:02}.png',dpi=100);plt.close(f)
# Guard cells: paired reniform and dumbbell cells surrounding explicit pores.
f,a=canvas(24,2,'Epidermal stomatal complexes (schematic)')
for cx,label,kind in [(2.5,'P','kidney'),(7.5,'Q','dumbbell')]:
 a.add_patch(Rectangle((cx-1.8,1),3.6,4.6,fill=False,lw=2))
 if kind=='kidney':
  for side in [-1,1]:
   th=np.linspace(-math.pi/2,math.pi/2,100);xx=cx+side*(.22+.7*np.cos(th));yy=3.3+1.5*np.sin(th)
   line(a,xx,yy);line(a,[cx+side*.22]*2,[1.8,4.8])
   for dy in [-.8,0,.8]:a.add_patch(Circle((cx+side*.62,3.3+dy),.10,color='black'))
 else:
  for side in [-1,1]:
   # Two enlarged terminal regions joined by a narrow middle.
   x0=cx+side*.52
   for yy in [2.1,4.5]:a.add_patch(Ellipse((x0,yy),.65,1.0,fill=False,lw=2.5))
   line(a,[x0-.13]*2,[2.5,4.1]);line(a,[x0+.13]*2,[2.5,4.1])
   for yy in [2.0,2.3,4.3,4.6]:a.add_patch(Circle((x0,yy),.07,color='black'))
 txt(a,cx,.5,label)
txt(a,5,6.3,'Dark bodies: chloroplasts in guard cells');save(f,24,2)
spec(24,2,'Biology','Compare specialised guard cells with ordinary epidermis.','P kidney-like pair and Q dumbbell pair around pores; chloroplasts only inside guard cells.','Two stomatal pairs have different guard-cell shapes and localised chloroplasts.')
# ECG and pressures aligned on the same time coordinates.
f,axs=plt.subplots(2,1,figsize=(12,9),dpi=100,sharex=True,gridspec_kw={'height_ratios':[1,2]});f.subplots_adjust(left=.17,right=.94,bottom=.14,top=.91,hspace=.28)
t=np.linspace(0,.6,601);ecg=.18*np.exp(-((t-.07)/.015)**2)-.25*np.exp(-((t-.145)/.006)**2)+1.15*np.exp(-((t-.16)/.005)**2)-.35*np.exp(-((t-.175)/.006)**2)+.3*np.exp(-((t-.43)/.03)**2)
axs[0].plot(t,ecg,'k',lw=2);axs[0].set_ylabel('ECG\nrelative');axs[0].set_yticks([0,1]);axs[0].text(.16,1.2,'QRS',ha='center',fontsize=24)
vent=np.interp(t,[0,.17,.19,.24,.32,.40,.48,.6],[5,5,20,80,125,100,5,5]);ao=np.interp(t,[0,.24,.32,.40,.43,.6],[80,80,110,100,85,80]);atr=np.full_like(t,10)
axs[1].plot(t,vent,'k',lw=3,label='Ventricle');axs[1].plot(t,ao,'k--',lw=2,label='Aorta');axs[1].plot(t,atr,'k:',lw=2,label='Atrium')
axs[1].set(ylabel='Pressure / mmHg',xlabel='Time / s',ylim=(0,140),xlim=(0,.6));axs[1].legend(fontsize=24,loc='upper right');axs[1].set_xticks([0,.2,.4,.6])
for ax in axs:
 for x,l in [(.19,'X'),(.24,'Y')]:ax.axvline(x,color='.4',ls=':',lw=1.4)
axs[1].text(.19,132,'X',ha='right');axs[1].text(.24,132,'Y',ha='left');save(f,24,13)
spec(24,13,'Biology','Align an electrical event with separate mechanical pressure thresholds.','QRS before X; ventricular pressure above atrial but below aortic at X; reaches aortic at Y.','An ECG is aligned with ventricular, aortic and atrial pressures and markers X and Y.')
# Nine doublets versus nine triplets, no solution names.
f,a=canvas(24,14,'Transverse microtubule organisations')
for cx,n,label in [(2.5,2,'P'),(7.5,3,'Q')]:
 for j in range(9):
  th=2*math.pi*j/9
  for k in range(n):
   off=(k-(n-1)/2)*.19;px=cx+1.45*math.cos(th)-off*math.sin(th);py=3.3+1.45*math.sin(th)+off*math.cos(th)
   a.add_patch(Circle((px,py),.115,fill=False,lw=2))
 if n==2:
  for dx in [-.16,.16]:a.add_patch(Circle((cx+dx,3.3),.115,fill=False,lw=2))
 txt(a,cx,.8,label)
save(f,24,14);spec(24,14,'Biology','Read peripheral group size and central microtubule presence.','P nine doublets plus central pair; Q nine triplets without a central pair.','Two microtubule cross-sections differ in peripheral multiplicity and centre.')
# MO levels state the given ordering without filling the requested electrons.
f,a=canvas(24,16,'C2: given valence MO ordering',ylim=(0,8))
for y,label,segments in [(1,'sigma(2s)',[(4,7)]),(2.6,'sigma*(2s)',[(4,7)]),(4.4,'pi(2px), pi(2py)',[(3.8,5.1),(6,7.3)]),(6.2,'sigma(2pz)',[(4,7)])]:
 for lo,hi in segments:line(a,[lo,hi],[y,y])
 txt(a,1.9,y,label)
arrow(a,(8.5,.8),(8.5,7));txt(a,9.35,3.9,'Energy');txt(a,5,7.5,'Eight valence electrons; bond axis z');save(f,24,16)
spec(24,16,'Chemistry','Fill the stated MO ordering rather than assuming localised sigma/pi occupancy.','Unfilled sigma2s, sigma*2s, degenerate pi2p, then sigma2pz levels in ascending order.','An empty valence MO diagram specifies orbital order and a z bond axis.')
# Allylic radical pair.
f,a=canvas(24,22,'Allylic radical: two contributors')
txt(a,2.5,3.6,'CH₂=CH—CH₂•');txt(a,7.5,3.6,'•CH₂—CH=CH₂');a.annotate('',xy=(5.9,3.6),xytext=(4.1,3.6),arrowprops={'arrowstyle':'<->','lw':2.5});txt(a,5,1.8,'Same three-carbon framework');save(f,24,22)
spec(24,22,'Chemistry','Compare electron assignment without changing skeleton or total electron number.','CH2=CH–CH2 radical and terminally reversed contributor; double-headed resonance arrow.','Two neutral allylic-radical contributors shift the double bond and unpaired electron.')
# Cis/trans alkenes with explicit substituents.
f,a=canvas(24,23,'Two but-2-ene geometries')
for cx,lab,cis in [(2.5,'cis',True),(7.5,'trans',False)]:
 line(a,[cx-.5,cx+.5],[3.2,3.2]);line(a,[cx-.5,cx+.5],[3.35,3.35])
 for side in [-1,1]:
  for sy in [-1,1]:
   line(a,[cx+side*.5,cx+side*1.05],[3.27,3.27+sy*.8]);isMe=(sy==1) if (cis or side==-1) else (sy==-1)
   txt(a,cx+side*1.35,3.27+sy*1.15,'CH₃' if isMe else 'H')
 txt(a,cx,1,lab)
save(f,24,23);spec(24,23,'Chemistry','Read substituent geometry before applying the stated anti-addition rule.','Cis and trans C=C structures with both CH3 and H explicitly placed; no products.','Two but-2-ene drawings differ in methyl groups being on the same or opposite sides.')
# Step impact, actual contact geometry.
f,a=canvas(24,49,'Wheel approaching a step',xlim=(-2.3,2.5),ylim=(-.3,2.8));cx=-math.sqrt(.75)
a.add_patch(Circle((cx,1),1,fill=False,lw=2.5));line(a,[-2.3,0,0,2.5],[0,0,.5,.5]);a.plot(0,.5,'ko');txt(a,.25,.28,'R/2');arrow(a,(cx,1),(cx+.65,1),'v');line(a,[cx,0],[1,.5]);txt(a,cx+.45,.92,'R');txt(a,.25,.8,'Corner');save(f,24,49)
spec(24,49,'Physics','Locate the corner relative to centre and ground for impact angular momentum.','Solid wheel radius R touches step corner at height R/2; centre at height R; velocity right.','A rolling wheel contacts a raised corner halfway up its radius.')
# Immersed spring block.
f,a=canvas(24,51,'Spring-supported block at equilibrium')
line(a,[2,8],[6.6,6.6]);xx=[5,5]+[5+(.25 if j%2 else -.25) for j in range(10)]+[5,5];yy=[6.6,6.3]+list(np.linspace(6.15,4.8,10))+[4.65,4.5];line(a,xx,yy)
a.add_patch(Rectangle((4,1.7),2,2.8,fill=False,lw=2.5));line(a,[1,9],[2.4,2.4]);txt(a,2.2,2.7,'Liquid surface');line(a,[7.1,7.1],[1.7,4.5]);txt(a,8.0,3.7,'H=0.20 m');txt(a,7.5,1.8,'h₀=0.050 m');txt(a,5,3.5,'2.0 kg');txt(a,5.7,5.4,'k');save(f,24,51)
spec(24,51,'Physics','Read finite immersion boundaries around the equilibrium displacement.','Block height0.20 m; bottom0.050 m below surface; supporting vertical spring; liquid surface.','A spring supports a block with only its lower quarter submerged.')
# Translating rail rod.
f,a=canvas(24,56,'Moving rod in a transverse field gradient')
line(a,[1,8],[1.5,1.5]);line(a,[1,8],[5.5,5.5]);line(a,[1,1],[1.5,3]);line(a,[1,1],[4,5.5]);a.add_patch(Rectangle((.7,3),.6,1,fill=False,lw=2));txt(a,.3,3.5,'R');line(a,[6,6],[1.5,5.5]);arrow(a,(6.2,3.5),(8,3.5),'v');txt(a,6,1,'y=0');txt(a,6,6,'y=L')
for y,n in [(2.1,2),(3,3),(4,4),(5,5)]:
 for x in np.linspace(2,5,n):a.add_patch(Circle((x,y),.085,fill=False,lw=1.5));a.plot(x,y,'k.',ms=3)
txt(a,4.3,6.7,'Bz=B₀(y/L)², out of page');save(f,24,56)
spec(24,56,'Physics','Read rod orientation, speed and nonuniform field for a motional integral.','Closed rectangular rails with left resistor; right rod moves+x; lower y0 upper yL; Bz quadratic outward.','A translating vertical rod closes a rail circuit in an outward field increasing with height.')
# Root modifications: three genuine origins.
f,a=canvas(25,2,'Root modifications (schematic)')
for x0,l in [(1.7,'P'),(5,'Q'),(8.3,'R')]:
 line(a,[x0-1.4,x0+1.4],[2,2]);txt(a,x0,.7,l)
line(a,[.5,2.8],[1.5,1.5])
for x in [.8,1.5,2.3]:line(a,[x,x],[1.5,3.6])
txt(a,1.7,4.7,'Waterlogged soil')
line(a,[4,6.3],[5,5]);line(a,[5.5,5.5],[2,5.8])
for x in [4.2,4.8]:line(a,[x,x],[5,2])
line(a,[8.3,8.3],[2,5.8]);
for y in [3,3.8]:
 a.plot(8.3,y,'ko');line(a,[8.3,7.2],[y,1.7]);line(a,[8.3,9.4],[y,1.7])
save(f,25,2);spec(25,2,'Biology','Read root origin and direction relative to soil, branch and stem.','P upward roots from waterlogged substrate; Q descending branch roots; R oblique roots from lower stem nodes.','Three root arrangements differ in upward projection, branch descent and oblique stem origin.')
# Pulse-labelled mitotic entry window: observations, no duration result.
f,a=plt.subplots(figsize=(12,9),dpi=100);f.subplots_adjust(left=.16,right=.94,bottom=.17,top=.88)
a.plot([0,2,2,7,7,10],[0,0,1,1,0,0],'k',lw=3);a.set(xlim=(0,10),ylim=(-.05,1.25),xlabel='Time after short pulse / h',ylabel='Labelled cells entering M\n(relative indicator)');a.set_xticks([0,2,7,10]);a.set_yticks([0,1]);a.text(2,1.1,'First',ha='center');a.text(7,1.1,'Last',ha='center');a.set_title('Fixed-duration model: labelled cohort');save(f,25,14)
spec(25,14,'Biology','Read first and last mitotic entry times of a pulse-labelled S cohort.','Short pulse at0; first labelled mitotic entry2 h; last7 h; schematic relative entry window.','A pulse-labelled cohort enters mitosis between two and seven hours after labelling.')
# Orbital orientation panels; phases shown with plus/minus.
f,a=canvas(25,16,'Orbital overlap: z is the internuclear axis',ylim=(-.5,7))
for y,lab,kind in [(5.5,'P','end'),(3.2,'Q','side'),(.9,'R','cancel')]:
 line(a,[2,9],[y,y],ls=':');txt(a,1,y,lab);txt(a,9.4,y,'z')
 if kind=='end':
  for cx in [4,6.5]:
   for sg in [-1,1]:a.add_patch(Ellipse((cx+sg*.5,y),.95,.65,fill=False,lw=2));txt(a,cx+sg*.5,y,'+' if sg==1 else '−')
 elif kind=='side':
  for cx in [4,6.5]:
   for sg in [-1,1]:a.add_patch(Ellipse((cx,y+sg*.48),.65,.95,fill=False,lw=2));txt(a,cx,y+sg*.48,'+' if sg==1 else '−')
 else:
  a.add_patch(Circle((4,y),.6,fill=False,lw=2));txt(a,4,y,'+')
  for sg in [-1,1]:a.add_patch(Ellipse((6.2,y+sg*.48),.65,.95,fill=False,lw=2));txt(a,6.2,y+sg*.48,'+' if sg==1 else '−')
save(f,25,16);spec(25,16,'Chemistry','Compare end-on, sideways and parity-cancelled overlap using phases.','Three z-axis panels: pz-pz end-on; px-px side; s-px symmetric opposite lobes; phase signs.','Three orbital pairs differ in orientation and sign symmetry around their common z axis.')
# Parallel Arrhenius plots.
f,a=plt.subplots(figsize=(12,9),dpi=100);f.subplots_adjust(left=.16,right=.95,bottom=.16,top=.89);x=np.linspace(.001,.004,100)
a.plot(x,10-2500*x,'k',lw=3);a.plot(x,10-math.log(100)-2500*x,'k--',lw=3);a.set(xlabel='1/T / K⁻¹',ylabel='ln k');a.set_xticks([.001,.002,.003,.004]);a.set_title('Two Arrhenius traces');xx=.0025;lo=10-math.log(100)-2500*xx;hi=10-2500*xx;a.annotate('',xy=(xx,hi),xytext=(xx,lo),arrowprops={'arrowstyle':'<->','lw':2});a.text(xx+.0001,(hi+lo)/2,'ln 100',va='center');save(f,25,24)
spec(25,24,'Chemistry','Read equal slopes and a specified logarithmic offset.','Parallel ln k versus1/T lines, upper separated byln100, units on inverse-temperature axis.','Two straight Arrhenius plots have equal slope and constant vertical separation.')
# Haloalkane structures carry actual branching.
f,a=canvas(25,30,'Isomeric haloalkane connectivity')
txt(a,5,5.4,'CH₃—CH₂—CH₂—CH₂—Cl');txt(a,5,4.5,'1-chlorobutane')
txt(a,5,2.2,'C');txt(a,3.1,2.2,'CH₃');txt(a,6.9,2.2,'Cl');txt(a,5,3.5,'CH₃');txt(a,5,.9,'CH₃');line(a,[3.7,4.6],[2.2,2.2]);line(a,[5.4,6.4],[2.2,2.2]);line(a,[5,5],[2.55,3.1]);line(a,[5,5],[1.2,1.85]);txt(a,5,.15,'2-chloro-2-methylpropane');save(f,25,30)
spec(25,30,'Chemistry','Compare isomer branching and the carbon bearing chlorine.','Explicit 1-chlorobutane chain and tertiary chloride centre with three methyl groups.','Two C4H9Cl structures contrast a straight primary chloride with a branched tertiary chloride.')
# Movable-pulley rope traced continuously.
f,a=canvas(25,46,'One movable pulley and one fixed pulley',xlim=(-2,3),ylim=(-.5,4.2));line(a,[-1.8,2.6],[3.8,3.8]);line(a,[-.5,-.5],[3.8,1.6]);a.add_patch(Arc((0,1.6),1,1,theta1=180,theta2=360,lw=2.5));line(a,[.5,.5],[1.6,3.2]);a.add_patch(Arc((.9,3.2),.8,.8,theta1=0,theta2=180,lw=2.5));line(a,[1.3,1.3],[3.2,1.8]);line(a,[.9,.9],[3.6,3.8]);a.add_patch(Circle((0,1.6),.42,fill=False,lw=1.5));line(a,[0,0],[1.6,.7]);a.add_patch(Rectangle((-.5,0),1,.7,fill=False,lw=2));txt(a,0,.35,'3 kg');a.add_patch(Rectangle((.8,1),1,.8,fill=False,lw=2));txt(a,1.3,1.4,'2 kg');save(f,25,46)
spec(25,46,'Physics','Read two supporting segments and the different rope-end motion.','Ceiling-fixed left end; rope under movable pulley carrying3kg; over fixed upper pulley;2kg at free end.','A movable pulley supports a three-kilogram load and a separate fixed pulley redirects its free rope end.')
# Hysteretic mechanical path.
f,a=plt.subplots(figsize=(12,9),dpi=100);f.subplots_adjust(left=.16,right=.95,bottom=.16,top=.9);a.plot([0,.02],[0,200],'k',lw=3,label='Load');a.plot([.02,.005],[200,0],'k--',lw=3,label='Unload');a.set(xlim=(-.001,.022),ylim=(-5,220),xlabel='Strain',ylabel='Stress / MPa');a.set_xticks([0,.005,.02]);a.set_yticks([0,100,200]);a.legend();a.set_title('Loading and unloading');save(f,25,49)
spec(25,49,'Physics','Compare loading and unloading areas and the zero-stress intercept.','Straight loading0,0→.020,200MPa; straight unloading→.005,0; axesunits and leg styles.','Stress–strain loading and unloading lines enclose a nonreturned work area and leave residual strain.')
# Capacitor spring geometry.
f,a=canvas(25,53,'Voltage-controlled movable plate')
line(a,[1.4,1.4],[1.5,5.5]);line(a,[5.2,5.2],[1.5,5.5]);line(a,[6.4,6.4],[1.5,5.5],ls=':');line(a,[9,9],[2,5]);xx=np.linspace(5.2,9,21);yy=np.array([3.5+(.25 if j%2 else -.25) for j in range(21)]);yy[0]=yy[-1]=3.5;line(a,xx,yy);txt(a,7.2,4.1,'k');a.annotate('',xy=(5.2,1.1),xytext=(1.4,1.1),arrowprops={'arrowstyle':'<->','lw':2});txt(a,3.3,.7,'gap d−x');a.annotate('',xy=(5.2,6),xytext=(6.4,6),arrowprops={'arrowstyle':'<->','lw':2});txt(a,5.8,6.4,'x');txt(a,1.4,6,'Fixed');txt(a,6.8,1.7,'Unforced\nposition');line(a,[1.4,1.4,3],[1.5,.25,.25]);line(a,[5.2,5.2,3.8],[1.5,.25,.25]);txt(a,3.4,.25,'V');save(f,25,53)
spec(25,53,'Physics','Distinguish initial gap, present gap and inward spring displacement.','Fixed left plate, moving right plate, spring to right anchor; dotted unforcedposition; gapd−x; voltage connection.','A spring-mounted capacitor plate moves inward from a dotted unforced position under a fixed voltage.')
# Symmetric but nonuniform line charge, no field arrows.
f,a=canvas(25,55,'Nonuniform positive line charge')
line(a,[1,9],[1.8,1.8]);a.plot(5,5.2,'ko');txt(a,5.4,5.2,'P=(0,a)',ha='left');line(a,[5,5],[1.5,5.4],ls=':')
for x in [1,1.3,1.65,2.1,2.7,3.5,6.5,7.3,7.9,8.35,8.7,9]:txt(a,x,1.8,'+')
txt(a,1,1,'−L');txt(a,5,1,'0');txt(a,9,1,'L');txt(a,5,6.4,'λ(x)=λ₀|x|/L');save(f,25,55)
spec(25,55,'Physics','Use reflection symmetry of an even line density at an off-axis point.','Horizontalchargedrod−L..L, densityeven increasingtowardends; P0,a above midpoint; no resulting field arrows.','A positive rod has mirror-symmetric density increasing toward both ends, with an observation point above its midpoint.')
(R/'IISER/authoring/tests24_25_images.json').write_text(json.dumps(S,indent=2)+'\n');print('Rendered',len(S),'scientific figures at1200x900.')
