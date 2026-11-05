"""Draw the 21 individually specified exact scientific figures for Tests 18 and 19."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Ellipse,Arc,FancyArrowPatch
R=Path(__file__).resolve().parents[2];O=R/'IISER/images'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'axes.labelsize':14,'xtick.labelsize':13,'ytick.labelsize':13})
def board(title):
 f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.04,right=.96,bottom=.06,top=.94)
 a.set(xlim=(0,10),ylim=(0,7.5));a.axis('off');a.text(5,7.1,title,ha='center',va='center',fontsize=16,weight='bold');return f,a
def txt(a,x,y,s,size=14):a.text(x,y,s,ha='center',va='center',fontsize=size,bbox=dict(fc='white',ec='none',pad=.3))
def line(a,x,y,u,v,style='-',width=1.8):a.plot([x,u],[y,v],style,color='black',lw=width)
def arrow(a,p,q):a.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',color='black',lw=1.8))
def save(f,t,n):f.savefig(O/f'IAT_T{t:02}_Q{n:02}.png',dpi=150,facecolor='white');plt.close(f)
def graph(xlabel,ylabel):
 f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.16,right=.95,bottom=.16,top=.92);a.set(xlabel=xlabel,ylabel=ylabel);return f,a

f,a=board('Ovary cross-sections: X and Y')
for cx,title in [(2.5,'X'),(7.5,'Y')]:
 a.add_patch(Circle((cx,4),1.7,fill=False,lw=2));txt(a,cx,1.6,title,18)
 if title=='X':
  for th in np.arange(3)*2*np.pi/3:
   line(a,cx,4,cx+1.7*np.cos(th),4+1.7*np.sin(th))
   for delta in [-.25,.25]:
    ang=th+delta;line(a,cx,4,cx+.45*np.cos(ang),4+.45*np.sin(ang));a.add_patch(Ellipse((cx+.55*np.cos(ang),4+.55*np.sin(ang)),.30,.20,angle=np.degrees(ang),fill=False,lw=1.7))
 else:
  for th in np.arange(3)*2*np.pi/3:
   for delta in [-.11,.11]:
    ang=th+delta;line(a,cx+1.7*np.cos(ang),4+1.7*np.sin(ang),cx+1.50*np.cos(ang),4+1.50*np.sin(ang));a.add_patch(Ellipse((cx+1.45*np.cos(ang),4+1.45*np.sin(ang)),.32,.20,angle=np.degrees(ang),fill=False,lw=1.7))
txt(a,5,1.0,'Lines: septa; small ovals: ovules',13);txt(a,5,.45,'Outer circle: ovary wall',13);save(f,18,2)
f,a=graph('Light intensity (arbitrary units)','Net CO₂ exchange (arbitrary units)');a.plot([0,1,2,3,4],[-2,0,3,6,7],'k-o');a.axhline(0,color='black',lw=.8);a.plot([3,3,0],[-2,6,6],'k--');a.text(3,-2.7,'L',ha='center');a.set(xlim=(0,4.3),ylim=(-3,8),xticks=[0,1,2,3,4],yticks=[-2,0,2,4,6,8]);save(f,18,4)
f,a=board('Circular recombinant maps: junctions came from E')
for cx,title,site in [(2.5,'X',1),(7.5,'Y',2)]:
 cy=4.2;r=1.45;a.add_patch(Circle((cx,cy),r,fill=False,lw=2));txt(a,cx,cy,title,19)
 points=[0,site,3,7,8]
 for s,label in [(0,'J'),(site,'H'),(3,'J'),(7,'H')]:
  th=np.pi/2-s*np.pi/4;u=np.array([np.cos(th),np.sin(th)]);p=np.array([cx,cy])+r*u
  line(a,*(p-.13*u),*(p+.13*u));txt(a,*(p+.36*u),label,14)
 for s,e in zip(points,points[1:]):
  th=np.pi/2-(s+e)/2*np.pi/4
  txt(a,cx+1.02*np.cos(th),cy+1.02*np.sin(th),f'{e-s} kb',13)
 txt(a,cx,1.7,'Insert J–J: 3 kb',13);txt(a,cx,1.15,'Backbone: 5 kb',13)
save(f,18,15)
f,a=board('Ideal planar C–F bond-vector model')
for cx,title,cis in [(2.5,'cis',True),(7.5,'trans',False)]:
 p=np.array([cx-.55,4]);q=np.array([cx+.55,4]);txt(a,*p,'C',18);txt(a,*q,'C',18)
 for dy in [-.06,.06]:line(a,p[0]+.2,4+dy,q[0]-.2,4+dy)
 for c,dx,left in [(p,-1,True),(q,1,False)]:
  for sy in [-1,1]:
   label='F' if (sy==1 if left or cis else sy==-1) else 'H';v=np.array([.6*dx,1.04*sy]);end=c+v
   line(a,*(c+.22*v),*(c+.79*v));txt(a,*end,label,17)
   if label=='F':arrow(a,c+.30*v+np.array([.18,0]),c+.72*v+np.array([.18,0]));txt(a,*(c+.56*v+np.array([.4*dx,0])),'d',13)
 txt(a,cx,1.7,title,17)
save(f,18,16)
f,a=board('Hexane-1,6-dial: labelled carbon positions')
xs=np.linspace(.8,9.2,6)
for j,x in enumerate(xs):
 txt(a,x,4,'OHC' if j==0 else 'CHO' if j==5 else 'CH₂',16);txt(a,x,5.1,f'C{j+1}',14)
 if j<5:line(a,x+.42,4,xs[j+1]-.42,4)
save(f,18,19)
f,a=board('Straight tunnel through a uniform spherical planet');a.set_aspect('equal')
O0=np.array([5,3.7]);rad=2.5;a.add_patch(Circle(O0,rad,fill=False,lw=2));h=rad/2;half=np.sqrt(rad**2-h**2)
line(a,5-half,3.7+h,5+half,3.7+h,width=3);a.plot(5-half,3.7+h,'ko',ms=9);txt(a,5-half-.35,3.7+h+.45,'Bead',13)
line(a,5,3.7,5,3.7+h,'--');txt(a,5.45,4.25,'R/2');line(a,5,3.7,7.5,3.7);txt(a,6.3,3.35,'R');txt(a,4.7,3.4,'O');arrow(a,(5,5.35),(6.5,5.35));txt(a,5.7,5.65,'s');save(f,18,48)
f,a=board('Two capacitors with an isolated charged junction')
for x in [2.8,6.6]:
 line(a,x,3.4,x,4.6);line(a,x+.3,3.4,x+.3,4.6)
line(a,1,4,2.8,4);line(a,3.1,4,6.6,4);line(a,6.9,4,9,4)
for x,lab in [(1,'A: 0'),(5,'M'),(9,'B: V')]:a.plot(x,4,'ko');txt(a,x,5.05,lab,16)
txt(a,2.95,2.8,'C',17);txt(a,6.75,2.8,'2C',17);txt(a,5,1.8,'M isolated: Qₘ = +CV',15);save(f,18,53)
f,a=board('Equal positive rings on a common axis')
line(a,1,3.8,9.4,3.8);arrow(a,(8.9,3.8),(9.5,3.8));txt(a,9.4,3.35,'x')
for cx,lab in [(2.6,'−a'),(7.4,'+a')]:
 a.add_patch(Ellipse((cx,3.8),.8,3.8,fill=False,lw=2));txt(a,cx,6.1,'+Q');txt(a,cx,1.3,lab)
line(a,2.6,3.8,2.6,5.7,'--');txt(a,2.05,4.85,'R');txt(a,5,3.25,'O: 0');a.plot(5.55,3.8,'ko',ms=7);txt(a,5.65,4.45,'+q');arrow(a,(5,2.5),(5.55,2.5));txt(a,5.3,2.1,'x');save(f,18,55)
f,a=board('Cell with a finite-resistance voltmeter')
# Upper rail includes the cell and series internal resistance; lower rail closes both branches.
line(a,1,2,1,5.3);line(a,1,5.3,2,5.3);line(a,2,4.9,2,5.7);line(a,2.3,5.1,2.3,5.5);line(a,2.3,5.3,3.1,5.3);txt(a,2.15,6.25,'E',16);txt(a,1.7,5.85,'+',13)
a.add_patch(Rectangle((3.1,5.05),1.2,.5,fill=False,lw=1.7));txt(a,3.7,6.1,'r',16);line(a,4.3,5.3,8.4,5.3)
line(a,1,2,8.4,2);line(a,6,5.3,6,4.3);a.add_patch(Rectangle((5.75,3),.5,1.3,fill=False,lw=1.7));line(a,6,3,6,2)
line(a,8.4,5.3,8.4,4.25);a.add_patch(Circle((8.4,3.65),.6,fill=False,lw=1.7));txt(a,8.4,3.65,'Vₘ',15);line(a,8.4,3.05,8.4,2)
txt(a,4.5,3.6,'R = 6 or 3 Ω',13);txt(a,8.1,1.1,'Meter: 6 Ω',14)
for p in [(6,5.3),(6,2),(8.4,5.3),(8.4,2)]:a.plot(*p,'ko',ms=4)
save(f,18,56)

f,a=board('Petal-overlap maps: arrow means overlaps')
for j,th in enumerate(np.pi/2-np.arange(5)*2*np.pi/5):
 p=np.array([2.5,4.4])+1.45*np.array([np.cos(th),np.sin(th)]);a.add_patch(Circle(p,.36,fill=False));txt(a,*p,str(j+1),14)
 th2=np.pi/2-(j+1)*2*np.pi/5;q=np.array([2.5,4.4])+1.45*np.array([np.cos(th2),np.sin(th2)]);d=(q-p)/np.linalg.norm(q-p);arrow(a,p+.43*d,q-.43*d)
P={'S':(7.5,5.95),'W1':(6.4,4.4),'W2':(8.6,4.4),'K1':(6.8,2.9),'K2':(8.2,2.9)}
for k,p in P.items():a.add_patch(Ellipse(p,1.25 if k=='S' else .95,.65,fill=False));txt(a,*p,k,14)
for u,v in [('S','W1'),('S','W2'),('W1','K1'),('W2','K2')]:
 p=np.array(P[u]);q=np.array(P[v]);d=(q-p)/np.linalg.norm(q-p);arrow(a,p+.43*d,q-.43*d)
txt(a,2.5,1.5,'X',17);txt(a,7.5,1.5,'Y',17);txt(a,7.5,.8,'Posterior above; anterior below',13);save(f,19,2)
f,a=graph('pH','Initial rate (arbitrary units)');x=np.linspace(0,12,500);a.plot(x,10*np.exp(-((x-2)/1.6)**2),'k-');a.plot(x,10*np.exp(-((x-8)/1.6)**2),'k--');a.text(2.4,9.8,'X');a.text(8.4,9.8,'Y');a.set(xlim=(0,12),ylim=(0,11),xticks=range(0,13,2),yticks=[0,5,10]);save(f,19,14)
f,a=board('Bridged coordination ion: overall charge 4+')
for cx,sgn in [(3,-1),(7,1)]:
 txt(a,cx,4,'Co',18)
 for y in [5.5,4.7,3.3,2.5]:
  nx=cx+sgn*1.3;line(a,cx+sgn*.3,4,nx-sgn*.2,y);txt(a,nx,y,'N',15)
 for yy in [5.1,2.9]:
  nx=cx+sgn*1.3;a.add_patch(Arc((nx,yy),1,.8,theta1=90 if sgn<0 else -90,theta2=270 if sgn<0 else 90,lw=1.6));txt(a,nx+sgn*.65,yy,'en',13)
for yy in [5.7,2.3]:
 txt(a,5,yy,'OH',16)
 for cx in [3,7]:line(a,cx+(0.25 if cx==3 else -.25),4.15 if yy>4 else 3.85,4.65 if cx==3 else 5.35,yy)
txt(a,5,1.15,'en neutral; each OH has charge −1',13);save(f,19,17)
f,a=board('Carbon configurations P and Q')
for y,name,occ in [(5.2,'P',[2,2,1,1,0]),(2.7,'Q',[2,1,1,1,1])]:
 txt(a,.7,y,name,18)
 for j,(x,n) in enumerate(zip([2,3.65,5.5,6.45,7.4],occ)):
  a.add_patch(Rectangle((x-.35,y-.38),.7,.76,fill=False,lw=1.7));txt(a,x,y,'↑↓' if n==2 else'↑' if n else'',18)
 for x,lab in [(2,'1s'),(3.65,'2s'),(6.45,'2p')]:txt(a,x,y-.95,lab,15)
save(f,19,18)
f,a=board('Starting ether connectivity')
xs=[.7,2.3,3.8,5.4,7,8.7];labs=['Ph','O','CH₂','CH₂','O','CH₃']
for j,(x,lab) in enumerate(zip(xs,labs)):
 txt(a,x,4,lab,18)
 if j<5:line(a,x+.42,4,xs[j+1]-.42,4)
txt(a,5,2,'Ph = C₆H₅',16);save(f,19,22)
f,a=graph('Time, t (s)','Platform upward acceleration (m/s²)');a.plot([0,3],[0,6],'k-',lw=2);a.text(1.5,4.3,'aₚ = 2t');a.set(xlim=(0,3.2),ylim=(0,6.7),xticks=[0,1,2,3],yticks=[0,2,4,6]);save(f,19,46)
f,a=board('Initial block position across two liquid layers')
line(a,1,1.5,1,6.3);line(a,1,1.5,8,1.5);line(a,8,1.5,8,6.3);line(a,1,6.1,8,6.1);line(a,1,3.8,3.5,3.8);line(a,5.5,3.8,8,3.8)
a.add_patch(Rectangle((3.5,2.3),2,3,fill=False,lw=2));line(a,3.5,3.8,5.5,3.8,'--');txt(a,2,4.9,'ρ/2');txt(a,2,2.6,'ρ');txt(a,6.9,4.15,'z = 0',13)
for y1,y2,lab in [(2.3,3.8,'H/2'),(3.8,5.3,'H/2')]:
 a.annotate('',xy=(6.1,y1),xytext=(6.1,y2),arrowprops=dict(arrowstyle='<->',color='black'));txt(a,6.75,(y1+y2)/2,lab,13)
txt(a,4.5,.65,'After removal: lower free surface stays at z = 0',13);save(f,19,49)
f,a=graph('Position, x (m)','Displacement, y (cm)');xx=np.linspace(-.1,.7,500);a.plot(xx,2*np.sin(5*np.pi*xx),'k-',lw=2);a.axhline(0,color='black',lw=.7);a.plot(0,0,'ko');a.annotate('',xy=(0,1.6),xytext=(0,.1),arrowprops=dict(arrowstyle='->',color='black',lw=2));a.text(.015,1.45,'vᵧ = +π m/s',fontsize=13);a.text(-.04,-.45,'P');a.set(xlim=(-.1,.7),ylim=(-2.6,2.8),xticks=np.arange(0,.7,.1),yticks=[-2,0,2]);save(f,19,51)
f,a=board('Finite dipole and external source')
line(a,1,4,9,4);xs=[1.5,3.2,4.9,6.6,8.3]
for x,lab in zip(xs,['−a','0','+a','2a','3a']):line(a,x,3.8,x,4.2);txt(a,x,3.3,lab,15)
for x,lab in [(1.5,'−q'),(4.9,'+q'),(8.3,'+Q')]:a.add_patch(Circle((x,4),.32,fc='white',ec='black',lw=1.5,zorder=3));txt(a,x,4.9,lab,17)
line(a,1.5,2.5,4.9,2.5);line(a,1.5,2.5,1.5,2.7);line(a,4.9,2.5,4.9,2.7);txt(a,3.2,1.9,'Rigid dipole',14);save(f,19,53)
f,a=board('Two dielectric arrangements; same plate area A')
for cx,lab in [(2.5,'X'),(7.5,'Y')]:
 for yy in [2.5,5.5]:line(a,cx-1.7,yy,cx+1.7,yy,width=3)
 line(a,cx-1.7,2.5,cx-1.7,5.5,':');line(a,cx+1.7,2.5,cx+1.7,5.5,':');txt(a,cx,6.1,lab,17)
 if lab=='X':line(a,cx,2.5,cx,5.5);txt(a,cx-.85,4,'K');txt(a,cx+.85,4,'Air');txt(a,cx-.85,1.7,'A/2',13);txt(a,cx+.85,1.7,'A/2',13)
 else:line(a,cx-1.7,4,cx+1.7,4);txt(a,cx,4.75,'K; d/2');txt(a,cx,3.25,'Air; d/2')
 txt(a,cx,1,'Gap d',14)
save(f,19,54)
f,a=board('Cube network: every edge is a resistor R');a.set(xlim=(-1,6),ylim=(-.9,6.5));a.texts[0].set_position((2.5,5.9))
pts={f'{x}{y}{z}':np.array([3*x+y,3*z+1.5*y]) for x in range(2) for y in range(2) for z in range(2)}
for s,p in pts.items():
 for j in range(3):
  if s[j]=='0':
   ss=s[:j]+'1'+s[j+1:];q=pts[ss];line(a,*p,*q,width=3 if {s,ss}=={'100','110'} else 1.5)
for s,p in pts.items():
 a.plot(*p,'ko',ms=5);txt(a,p[0]-.22,p[1]+.22,('A: ' if s=='000' else'B: ' if s=='111' else'')+s,12)
p=pts['100'];q=pts['110'];arrow(a,p+.32*(q-p)+np.array([.28,-.1]),p+.7*(q-p)+np.array([.28,-.1]));txt(a,4.55,.7,'I_edge',13)
txt(a,2,-.65,'V_A − V_B = V',14);save(f,19,55)
f,a=board('Ray from an off-centre source in a sphere');a.set_aspect('equal')
c=np.array([4.5,3.8]);rad=2.5;p=c+np.array([.75*rad,0]);u=np.array([np.cos(2.0),np.sin(2.0)])
d=p-c;t=-np.dot(d,u)+np.sqrt(np.dot(d,u)**2+rad**2-np.dot(d,d));s=p+t*u
a.add_patch(Circle(c,rad,fill=False,lw=2));line(a,*c,*p);line(a,*c,*s,'--');line(a,*p,*(p+np.array([1.1,0])),'--');arrow(a,p,s)
a.plot(*c,'ko');a.plot(*p,'ko');txt(a,c[0]-.3,c[1]-.3,'O',15);txt(a,p[0],p[1]-.35,'P',15);txt(a,s[0]+.25,s[1]+.25,'S',15)
a.add_patch(Arc(p,.8,.8,theta1=0,theta2=np.degrees(2.0),lw=1.5));txt(a,p[0]+.35,p[1]+.65,'α',14)
theta1=np.degrees(np.arctan2(*(c-s)[::-1]));theta2=np.degrees(np.arctan2(*(p-s)[::-1]));lo,hi=sorted([theta1,theta2]);a.add_patch(Arc(s,.7,.7,theta1=lo,theta2=hi,lw=1.4));mid=np.deg2rad((lo+hi)/2);txt(a,*(s+.55*np.array([np.cos(mid),np.sin(mid)])),'i',14)
txt(a,5.5,3.05,'OP = 3R/4',13);txt(a,4.6,5.15,'R',15);txt(a,3.7,2.3,'n = 2',15);txt(a,8,5.8,'Air',15);save(f,19,58)
print('Rendered 21 exact figures, each 1200 x 900.')
