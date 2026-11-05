"""Render exact authored scientific diagrams, never infer or generate question content."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Ellipse,Arc
R=Path(__file__).resolve().parents[2];O=R/'IISER/images';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'axes.labelsize':14,'xtick.labelsize':13,'ytick.labelsize':13})
def board(title):
 f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.04,right=.96,bottom=.04,top=.96)
 a.set(xlim=(0,10),ylim=(0,7.5));a.axis('off');a.text(5,7.1,title,ha='center',va='center',fontsize=16,weight='bold')
 return f,a
def txt(a,x,y,s,size=14):a.text(x,y,s,ha='center',va='center',fontsize=size)
def line(a,x,y,u,v,style='-',width=1.8):a.plot([x,u],[y,v],style,color='black',lw=width)
def arrow(a,p,q):a.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',color='black',lw=1.8))
def bond(a,p,q,n=1):
 p=np.array(p,dtype=float);q=np.array(q,dtype=float);d=q-p;normal=np.array([-d[1],d[0]])/np.linalg.norm(d)
 for delta in np.arange(n)-(n-1)/2:
  u=p+.075*delta*normal;v=q+.075*delta*normal;line(a,*u,*v)
def save(f,t,n):f.savefig(O/f'IAT_T{t:02}_Q{n:02}.png',dpi=150,facecolor='white');plt.close(f)
def ring(a,cx,cy,r=.85):
 pts=np.array([(cx+r*np.cos(k*np.pi/3),cy+r*np.sin(k*np.pi/3)) for k in range(6)])
 a.add_patch(Polygon(pts,closed=True,fill=False,lw=1.8));a.add_patch(Circle((cx,cy),r*.5,fill=False,lw=1.5))

f,a=board('Transverse vascular arrangements X and Y')
cx,cy=2.5,4.6
a.add_patch(Circle((cx,cy),1.8,fill=False,lw=1.5))
for th in np.arange(4)*np.pi/2:
 end=np.array([cx,cy])+1.45*np.array([np.cos(th),np.sin(th)])
 line(a,cx,cy,*end,width=6);a.add_patch(Circle(end,.10,fc='black',ec='white',lw=.8))
for th in np.arange(4)*np.pi/2+np.pi/4:
 a.add_patch(Circle((cx+1.15*np.cos(th),cy+1.15*np.sin(th)),.20,fill=False,lw=1.5))
txt(a,2.5,2.35,'X',17);txt(a,2.5,1.65,'Tip dots: protoxylem',12);txt(a,2.5,1.1,'Circles between arms: phloem',12)
cx,cy=7.5,4.8
a.add_patch(Circle((cx,cy),1.6,fill=False));txt(a,cx,cy,'Pith',13)
for th in np.arange(8)*np.pi/4:
 for rad,mk,size in [(1.0,'s',55),(1.16,'|',80),(1.32,'o',40)]:
  a.plot(cx+rad*np.cos(th),cy+rad*np.sin(th),marker=mk,ms=np.sqrt(size),mfc='white',mec='black',color='black')
txt(a,7.5,2.7,'Y: one bundle enlarged below',12)
for x,w,label in [(6.5,.65,'X'),(7.15,.4,'C'),(7.55,.65,'P')]:
 a.add_patch(Rectangle((x,1.6),w,.65,fill=False,lw=1.7));txt(a,x+w/2,1.92,label,13)
txt(a,5.85,1.92,'Pith',12);txt(a,8.8,1.92,'Outer',12)
txt(a,7.3,.8,'X: xylem   C: cambium   P: phloem',12);save(f,16,2)

f,a=board('Two E sites: circular versus linear DNA')
cx,cy,r=2.6,4.1,1.65
a.add_patch(Circle((cx,cy),r,fill=False,lw=2))
for th in [np.pi/2,np.pi/2-2*np.pi/3]:
 p=np.array([cx,cy])+r*np.array([np.cos(th),np.sin(th)])
 line(a,*(p-.18*np.array([np.cos(th),np.sin(th)])),*(p+.18*np.array([np.cos(th),np.sin(th)])))
 txt(a,p[0]+.4*np.cos(th),p[1]+.4*np.sin(th),'E',14)
txt(a,3.15,4.55,'2 kb',13);txt(a,1.9,3.8,'4 kb',13);txt(a,2.6,1.6,'Circular: 6 kb',14)
line(a,5.3,4.1,9.5,4.1)
for x in [6.7,8.1]:line(a,x,3.85,x,4.35);txt(a,x,4.65,'E',14)
for x,label in [(6,'2 kb'),(7.4,'2 kb'),(8.8,'2 kb')]:txt(a,x,3.5,label,12)
txt(a,7.4,1.6,'Linear: 6 kb',14);save(f,16,9)

f,a=board('One connected multifunctional molecule')
nodes=[(1.0,3.7,'CH₂'),(2.5,3.7,'CH'),(4.0,3.7,'C'),(5.4,3.7,'O'),(6.8,3.7,'CH₂'),(8.3,3.7,'C'),(9.4,3.7,'N')]
for x,y,s in nodes:txt(a,x,y,s,17)
for j,n in enumerate([2,1,1,1,1,3]):
 x,y,_=nodes[j];xx,yy,_=nodes[j+1];bond(a,(x+.40,y),(xx-.35,yy),n)
txt(a,4,5.3,'O',18);bond(a,(4,4.05),(4,4.95),2);save(f,16,16)

f,a=board('Lewis proposals P and Q')
def dots(x,y,vertical=False):
 if vertical:a.plot([x,x],[y-.08,y+.08],'ko',ms=3.5)
 else:a.plot([x-.08,x+.08],[y,y],'ko',ms=3.5)
for cx,title,n in [(2.5,'P',3),(7.5,'Q',2)]:
 txt(a,cx,5.8,title,18);txt(a,cx-.75,3.8,'C',24);txt(a,cx+.75,3.8,'O',24)
 bond(a,(cx-.4,3.8),(cx+.4,3.8),n);dots(cx-1.25,3.8,True);dots(cx+1.25,3.8,True)
 if n==2:dots(cx+.75,4.45)
txt(a,5,1.5,'Each dot pair represents one lone pair',14);save(f,16,18)

f,a=board('Reactant connectivity')
ring(a,5,3.8,1.15)
line(a,3.85,3.8,2.9,3.8);txt(a,2.55,3.8,'C',18)
bond(a,(2.55,4.1),(2.55,5.0),2);txt(a,2.55,5.35,'O',18)
line(a,2.2,3.8,1.5,3.8);txt(a,1.15,3.8,'H',17)
line(a,6.15,3.8,7.0,3.8);txt(a,7.35,3.8,'C',18)
bond(a,(7.35,4.1),(7.35,5),2);txt(a,7.35,5.35,'O',18)
line(a,7.7,3.8,8.4,3.8);txt(a,8.95,3.8,'CH₃',17)
save(f,16,21)

f,a=board('The single reductive-ozonolysis product')
xs=[1.2,2.7,4.2,5.7,7.2,8.7]
for j,x in enumerate(xs):txt(a,x,3.7,'CH' if j in [0,5] else 'CH₂',16)
for x,xx in zip(xs,xs[1:]):bond(a,(x+.42,3.7),(xx-.42,3.7))
for x in [xs[0],xs[-1]]:
 bond(a,(x,4.05),(x,5),2);txt(a,x,5.35,'O',18)
save(f,16,29)

f,a=board('Uniform-area ideal siphon')
line(a,1,1,1,4.5);line(a,1,1,5,1);line(a,5,1,5,4.5);line(a,1,4,5,4)
txt(a,2.5,3.35,'Reservoir',14);txt(a,2.5,4.4,'Surface z = 0',13)
a.plot([3.8,3.8,6.5,6.5,8.7],[2.0,6.2,6.2,2.0,2.0],color='black',lw=3)
txt(a,5.2,6.6,'Crest z = H',13);txt(a,8.25,1.45,'Outlet z = −5 m',12)
txt(a,7.7,4.6,'Air pressure',12);txt(a,7.7,4.05,'head: 10 m',12)
txt(a,7.7,3.3,'Vapour head: 1 m',12);save(f,16,51)

f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.15,right=.94,bottom=.15,top=.9)
pts={'A':(1,1),'D':(1,2),'C':(2,2),'B':(2,1)}
a.plot([1,1,2,2,1],[1,2,2,1,1],'k-',lw=2)
for label,(x,y) in pts.items():a.plot(x,y,'ko');a.text(x+.06,y+.06,label,fontsize=16)
for p,q in [('A','D'),('D','C'),('C','B'),('B','A')]:
 u=np.array(pts[p]);v=np.array(pts[q]);arrow(a,u+.35*(v-u),u+.65*(v-u))
a.set(xlim=(0,2.5),ylim=(0,2.5),xlabel='Volume, V',ylabel='Pressure, P',xticks=[0,1,2],yticks=[0,1,2],xticklabels=['0','V₀','2V₀'],yticklabels=['0','P₀','2P₀'])
save(f,16,52)

f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.15,right=.94,bottom=.15,top=.94)
x=np.linspace(-1.5,1.5,501);a.plot(x,(x*x-1)**2,'k-',lw=2)
a.set(xlim=(-1.5,1.5),ylim=(0,1.65),xlabel='Position, x/a',ylabel='Potential, V/V₀',xticks=[-1,0,1],yticks=[0,.5,1,1.5])
save(f,16,53)

f,a=board('Prism angles are measured from normals')
left=np.array([2.7,2.]);right=np.array([7.3,2.]);apex=np.array([5.,2+2.3*np.sqrt(3)])
a.add_patch(Polygon([left,right,apex],closed=True,fill=False,lw=2))
txt(a,5,5.5,'60°',14);txt(a,5,2.6,'n = √3',16);txt(a,1.2,6.2,'Air',14)
p=np.array([3.85,2+1.15*np.sqrt(3)])
m=np.tan(np.deg2rad(-2));qx=(2+np.sqrt(3)*7.3-p[1]+m*p[0])/(np.sqrt(3)+m)
q=np.array([qx,p[1]+m*(qx-p[0])])
# An unsolved asymmetric example, with both air rays obeying Snell's law.
inc=np.arcsin(np.sqrt(3)*np.sin(np.deg2rad(28)))-np.pi/6
out=np.pi/6-np.arcsin(np.sqrt(3)*np.sin(np.deg2rad(32)))
line(a,*p,*q);arrow(a,p-1.5*np.array([np.cos(inc),np.sin(inc)]),p);arrow(a,q,q+1.5*np.array([np.cos(out),np.sin(out)]))
for point,direction in [(p,np.array([np.sqrt(3)/2,-.5])),(q,np.array([np.sqrt(3)/2,.5]))]:
 line(a,*(point-direction),*(point+direction),'--')
txt(a,3.0,3.6,'i',16);txt(a,4.3,3.6,'r₁',16);txt(a,5.85,3.55,'r₂',16);txt(a,7.1,3.5,'e',16)
save(f,16,57)

f,a=board('Leaf transverse section')
a.add_patch(Rectangle((1,2),8,3.9,fill=False,lw=1.8))
line(a,1,5.5,9,5.5);line(a,1,2.4,9,2.4)
for y in [5.7,2.2]:
 for x in [2,7.8]:
  a.add_patch(Ellipse((x-.17,y),.23,.32,fill=False));a.add_patch(Ellipse((x+.17,y),.23,.32,fill=False))
for x in [4.1,4.65,5.2]:a.add_patch(Ellipse((x,5.25),.56,1.3,fc='white',ec='black',lw=1.4))
for x in np.linspace(1.5,8.5,9):
 for y in [3.,3.7,4.35]:
  if abs(x-6)<.7 and abs(y-3.7)<.8:continue
  a.add_patch(Ellipse((x,y),.55,.42,fill=False,lw=1))
a.add_patch(Ellipse((6,3.7),1.2,1.4,fc='white',ec='black',lw=1.6));txt(a,6,3.7,'V',14)
txt(a,4.7,6.45,'Enlarged upper epidermal cells',12)
txt(a,5,1.25,'V: vascular bundle; similar mesophyll throughout',12);save(f,17,2)

f,a=board('Separate plasmids in the same cell')
for cx,title in [(2.5,'P'),(7.5,'Q')]:
 a.add_patch(Circle((cx,4.2),1.6,fill=False,lw=2));txt(a,cx,4.2,title,20)
txt(a,2.5,6.2,'ori',15);txt(a,2.5,1.9,'No resistance gene',12)
txt(a,7.5,6.2,'ori deleted',14);txt(a,8.9,1.9,'Insert',12);txt(a,6.1,1.9,'Resistance',12)
line(a,6.1,2.2,6.6,2.86);line(a,8.9,2.2,8.4,2.86)
a.add_patch(Arc((7.5,4.2),3.2,3.2,theta1=220,theta2=255,lw=5,color='black'))
a.add_patch(Arc((7.5,4.2),3.2,3.2,theta1=285,theta2=320,lw=5,color='black'))
txt(a,5,.9,'No fusion, recombination or integration',12);save(f,17,9)

f,a=board('Candidate electron-domain sites')
cx,cy=2.5,4.1;txt(a,cx,cy,'S',18)
for dx,dy,lab in [(0,1.65,'Ax'),(0,-1.65,'Ax'),(1.5,0,'Eq'),(-1.05,.9,'Eq'),(-1.05,-.9,'Eq')]:
 line(a,cx+.3*np.sign(dx),cy+.3*np.sign(dy),cx+.8*dx,cy+.8*dy);a.add_patch(Circle((cx+dx,cy+dy),.27,fc='white',ec='black'));txt(a,cx+dx,cy+dy,lab,12)
txt(a,2.5,1.3,'4 F + 1 lone pair',13)
cx=7.4;txt(a,cx,cy,'Xe',18)
for dx,dy in [(0,1.6),(0,-1.6),(1.4,0),(-1.4,0),(.9,.9),(-.9,-.9)]:
 line(a,cx+.28*np.sign(dx),cy+.28*np.sign(dy),cx+.8*dx,cy+.8*dy);a.add_patch(Circle((cx+dx,cy+dy),.2,fc='white',ec='black'))
txt(a,7.4,1.3,'4 F + 2 lone pairs',13);save(f,17,16)

f,a=board('Octahedral coordinate occupancies')
sites={'x+':(1.45,0),'x-':(-1.45,0),'y+':(.85,.95),'y-':(-.85,-.95),'z+':(0,1.75),'z-':(0,-1.75)}
for cx,title,aset in [(2.5,'P',{'x+','y+','z+'}),(7.5,'Q',{'x+','x-','z+'})]:
 txt(a,cx,4,'M',17)
 for site,(dx,dy) in sites.items():
  line(a,cx+.25*np.sign(dx),4+.25*np.sign(dy),cx+.8*dx,4+.8*dy,'--' if site=='y-' else '-')
  txt(a,cx+dx,4+dy,('A' if site in aset else 'B')+' '+site,12)
 txt(a,cx,1.1,title,18)
save(f,17,17)

f,a=board('The controlled crossed-aldol reactants')
ring(a,2.0,4.2,.9);line(a,2.9,4.2,3.5,4.2);txt(a,3.85,4.2,'C',18)
bond(a,(3.85,4.5),(3.85,5.3),2);txt(a,3.85,5.65,'O',18);line(a,4.15,4.2,4.65,4.2);txt(a,4.95,4.2,'H',16)
txt(a,2.7,2.1,'Benzaldehyde',14)
txt(a,6.4,4.2,'CH₃',17);line(a,6.85,4.2,7.5,4.2);txt(a,7.85,4.2,'C',18)
bond(a,(7.85,4.5),(7.85,5.3),2);txt(a,7.85,5.65,'O',18);line(a,8.15,4.2,8.7,4.2);txt(a,9,4.2,'H',16)
txt(a,7.7,2.1,'Ethanal',14);save(f,17,23)

f,a=plt.subplots(figsize=(8,6));f.subplots_adjust(left=.16,right=.94,bottom=.15,top=.91)
a.plot([0,4],[0,-8],'k-',lw=2);a.set(xlim=(0,4.2),ylim=(-8.5,.5),xlabel='Time, t (s)',ylabel='Acceleration, a (m s⁻²)',xticks=[0,1,2,3,4],yticks=[0,-2,-4,-6,-8]);a.text(.2,-7.4,'Initial v = +4 m s⁻¹',fontsize=14)
save(f,17,46)

f,a=board('Eight small cubes surround the central charge')
def project(x,y,z):return np.array([5+1.5*(x+.45*y),3.8+1.5*(z+.3*y)])
for axis in range(3):
 for u in [-1,0,1]:
  for v in [-1,0,1]:
   p=[0.,0.,0.];q=[0.,0.,0.];other=[j for j in range(3) if j!=axis]
   p[other[0]]=q[other[0]]=u;p[other[1]]=q[other[1]]=v;p[axis]=-1;q[axis]=1
   line(a,*project(*p),*project(*q),':' if u==0 and v==0 else '-',width=.9)
face=np.array([project(1,y,z) for y,z in [(0,0),(1,0),(1,1),(0,1)]])
a.add_patch(Polygon(face,closed=True,fill=False,lw=3));p=project(1,.5,.5);txt(a,p[0]+.4,p[1],'F',17)
p=project(0,0,0);a.plot(*p,'ko',ms=7);txt(a,p[0]-.45,p[1]-.15,'q',17)
txt(a,5,1.0,'Each small cube has side a; q is the common corner',12);save(f,17,53)

f,a=board('Bridge: only the right arms share the bath')
nodes={'top':(5,6.1),'left':(2.4,3.9),'right':(7.6,3.9),'bottom':(5,1.7)}
for p,q,label in [('top','left','100 Ω'),('left','bottom','100 Ω'),('top','right','100(1+0.004T) Ω'),('right','bottom','200(1−βT) Ω')]:
 u=np.array(nodes[p]);v=np.array(nodes[q]);c=(u+v)/2;d=(v-u)/np.linalg.norm(v-u);normal=np.array([-d[1],d[0]])
 line(a,*u,*(c-.45*d));line(a,*(c+.45*d),*v)
 a.add_patch(Polygon([c-.45*d-.15*normal,c+.45*d-.15*normal,c+.45*d+.15*normal,c-.45*d+.15*normal],closed=True,fill=False,lw=1.6))
 txt(a,c[0]+(-.8 if c[0]<5 else .6),c[1]+(.45 if c[1]>3.9 else -.5),label,12)
line(a,2.4,3.9,4.65,3.9);line(a,5.35,3.9,7.6,3.9);a.add_patch(Circle((5,3.9),.35,fc='white',ec='black'));txt(a,5,3.9,'G',14)
line(a,5,6.1,.8,6.1);line(a,.8,6.1,.8,4.3);line(a,.8,3.5,.8,1.7);line(a,.8,1.7,5,1.7)
line(a,.4,4.3,1.2,4.3);line(a,.55,3.9,1.05,3.9);line(a,.8,3.9,.8,3.5);txt(a,1.1,4.8,'+',14);txt(a,1.5,3.3,'12 V',13)
txt(a,5,.55,'Right arms: controlled temperature T',13);save(f,17,54)

f,a=board('Ideal diodes and a loaded output')
def resistor(p,q,label):
 p=np.array(p,dtype=float);q=np.array(q,dtype=float);d=q-p
 c=(p+q)/2;u=d/np.linalg.norm(d);half=.5 if abs(d[0])>abs(d[1]) else .45
 line(a,*p,*(c-half*u));line(a,*(c+half*u),*q)
 if abs(d[0])>abs(d[1]):a.add_patch(Rectangle(c-[.5,.15],1,.3,fill=False,lw=1.7));txt(a,c[0],c[1]+.45,label,13)
 else:a.add_patch(Rectangle(c-[.15,.45],.3,.9,fill=False,lw=1.7));txt(a,c[0]-.65,c[1],label,13)
def diode(p,q,label):
 p=np.array(p,dtype=float);q=np.array(q,dtype=float);v=(q-p)/np.linalg.norm(q-p);n=np.array([-v[1],v[0]]);c=(p+q)/2
 line(a,*p,*(c-.28*v));line(a,*(c+.28*v),*q)
 a.add_patch(Polygon([c-.28*v+.25*n,c-.28*v-.25*n,c+.18*v],closed=True,fc='white',ec='black',lw=1.7))
 line(a,*(c+.25*v+.3*n),*(c+.25*v-.3*n))
 txt(a,*(c-.6*v+.45*n),'A',12);txt(a,*(c+.6*v+.45*n),'K',12);txt(a,*(c-.55*n),label,13)
resistor((.8,4),(4,4),'1 kΩ');txt(a,.6,4.65,'Vin',14);a.plot(4,4,'ko');txt(a,4.3,4.3,'O',15)
resistor((4,4),(4,.65),'1 kΩ')
for y,w in [(.6,.4),(.45,.28),(.3,.15)]:line(a,4-w,y,4+w,y)
line(a,4,4,4,6);diode((4,6),(8.4,6),'U');txt(a,9,6,'+3 V',14)
line(a,4,4,7.7,4);line(a,7.7,4,7.7,3.2);diode((7.7,.9),(7.7,3.2),'L');txt(a,7.7,.45,'−2 V',14)
save(f,17,59)
