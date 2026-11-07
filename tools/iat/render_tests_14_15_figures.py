"""Draw exact, question-bearing diagrams for the two authored papers."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Rectangle, Ellipse, Polygon

out = Path(__file__).resolve().parents[2] / 'IISER/images'
out.mkdir(exist_ok=True)
ink, blue, red = '#1d3942', '#377985', '#b25147'

def board(title):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set(xlim=(0, 10), ylim=(0, 7))
    ax.axis('off')
    ax.text(5, 6.65, title, ha='center', fontsize=19, color=ink, weight='bold')
    return fig, ax

def label(ax, x, y, value, size=16):
    ax.text(x, y, value, ha='center', va='center', fontsize=size, color=ink)

def segment(ax, x1, y1, x2, y2, color=blue, width=2.4):
    ax.plot([x1, x2], [y1, y2], color=color, lw=width)

def arrow(ax, a, b, caption=None):
    ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle='->', lw=2.4, color=blue))
    if caption:
        label(ax, (a[0]+b[0])/2, (a[1]+b[1])/2+.33, caption, 14)

def save(fig, paper, question):
    fig.savefig(out / f'IAT_T{paper:02}_Q{question:02}.png', dpi=150,
                facecolor='white', bbox_inches='tight', pad_inches=.22)
    plt.close(fig)

# Test 14
f,a=board('Flower: whorls and ovary position')
for radius, n, symbol, shade in [(2.55,5,'sepal','#dcece5'),(1.9,5,'petal','#f1e5e1'),(1.25,5,'stamen','#eadbbd')]:
    for k in range(n):
        theta=2*np.pi*k/n+np.pi/2
        x,y=5+radius*np.cos(theta),3.65+radius*np.sin(theta)
        a.add_patch(Ellipse((x,y),.8,.46,angle=np.degrees(theta),fc=shade,ec=ink,lw=1.4))
        label(a,x,y,symbol[0].upper(),10)
a.add_patch(Ellipse((5,3.65),.95,1.12,fc='#e4f1ea',ec=ink,lw=2))
label(a,5,3.65,'2 fused\ncarpels',12)
label(a,5,.42,'United sepals; free petals and stamens; superior ovary',13)
save(f,14,2)

f,a=board('Energy transfers in the food web')
for x,y,name in [(5,5.55,'Plants'),(2.6,3.7,'Herbivore A'),(7.4,3.7,'Herbivore B'),(5,1.5,'Predator')]:
    a.add_patch(Rectangle((x-1.15,y-.38),2.3,.76,ec=ink,fc='#e6f1ef',lw=1.5))
    label(a,x,y,name,14)
for start,end,value in [((4.4,5.1),(3.0,4.1),'1000 kJ'),((5.6,5.1),(7.0,4.1),'600 kJ'),
                        ((3.0,3.2),(4.45,1.9),'100 kJ'),((7.0,3.2),(5.55,1.9),'90 kJ')]:
    arrow(a,start,end,value)
save(f,14,10)

f,a=board('Bond arrangement and bond dipoles')
label(a,2.1,4.45,'O',23); label(a,4,4.45,'C',23); label(a,5.9,4.45,'O',23)
segment(a,2.4,4.45,3.6,4.45);segment(a,4.4,4.45,5.6,4.45)
arrow(a,(3.95,4.9),(2.7,4.9));arrow(a,(4.05,4.9),(5.3,4.9))
label(a,7.9,5.0,'CO₂: 180°',16)
label(a,4,2.55,'O',23);label(a,2.55,1.2,'H',23);label(a,5.45,1.2,'H',23)
segment(a,3.68,2.28,2.8,1.45);segment(a,4.32,2.28,5.2,1.45)
arrow(a,(2.95,1.7),(3.56,2.25));arrow(a,(5.05,1.7),(4.44,2.25))
label(a,7.9,2.1,'H₂O: bent',16)
save(f,14,16)

f,a=board('Daniell cell before dilution')
for x,metal,ion in [(2.6,'Zn(s)','Zn²⁺: 1 M'),(7.4,'Cu(s)','Cu²⁺: 1 M')]:
    a.add_patch(Rectangle((x-1.55,1.55),3.1,3.0,ec=ink,fc='#e7f1f4',lw=1.8))
    a.add_patch(Rectangle((x-.15,2.25),.3,3.0,ec=ink,fc='#d2d6d6'))
    label(a,x,5.45,metal);label(a,x,2.05,ion,14)
segment(a,2.6,5.25,2.6,6);segment(a,2.6,6,7.4,6);segment(a,7.4,6,7.4,5.25)
segment(a,4.15,3.9,5.85,3.9)
label(a,5,3.55,'salt bridge',12)
label(a,7.4,.8,'Cu²⁺ is diluted next',14)
save(f,14,20)

f,a=board('Two-step preparation')
for x,y,name in [(2,4.2,'A + 2B'),(5,4.2,'C'),(8,4.2,'D')]:
    a.add_patch(Rectangle((x-1.1,y-.52),2.2,1.04,ec=ink,fc='#e8f0ef'))
    label(a,x,y,name,18)
arrow(a,(3.15,4.2),(3.85,4.2));arrow(a,(6.15,4.2),(6.85,4.2),'+ B')
label(a,5,2,'Initial amounts: A = 3 mol; B = 8 mol',17)
save(f,14,27)

fig,ax=plt.subplots(figsize=(10,7))
ax.plot([0,2],[0,4],color=blue,lw=3);ax.plot([2,3],[4,4],color=blue,lw=3)
ax.plot([0,2,3],[0,4,4],'o',color=red)
ax.set(xlim=(-.1,3.2),ylim=(-.2,5),xlabel='Position x (m)',ylabel='Force along motion (N)',
       xticks=[0,1,2,3],yticks=[0,2,4])
ax.grid(alpha=.2);fig.tight_layout();save(fig,14,48)

f,a=board('Block floating at equilibrium')
a.add_patch(Rectangle((1.4,1.1),7.2,3.25,ec=blue,fc='#e5f2fa'))
a.add_patch(Rectangle((3.9,2.55),2.2,3.0,ec=ink,fc='#e4d4ae',lw=2))
segment(a,1.1,4.35,8.9,4.35)
label(a,7.2,4.7,'waterline',14);label(a,5,5.85,'block: 600 kg/m³',16)
label(a,7.1,1.7,'water: 1000 kg/m³',15)
save(f,14,51)

f,a=board('Equal positive charges on one axis')
segment(a,1,3.5,9,3.5,ink)
for x,caption in [(3,'+q at −a'),(7,'+q at +a')]:
    a.add_patch(Circle((x,3.5),.31,ec=ink,fc='#f3e3d9',lw=2))
    label(a,x,4.45,caption)
label(a,5,2.8,'0',15)
label(a,9,3.9,'x',16)
save(f,14,53)

f,a=board('Converging lens and near object')
segment(a,1,3.3,9,3.3,ink);segment(a,6,1.1,6,5.6,blue,3)
for x,caption in [(3,'F'),(9,'F')]:
    a.add_patch(Circle((x,3.3),.06,color=ink));label(a,x,2.9,caption,15)
arrow(a,(4.5,3.3),(4.5,4.7))
label(a,4.5,5.15,'object',15);label(a,6.65,5.65,'lens',15)
label(a,5.25,1.15,'object distance 5 cm; focal length 10 cm',14)
save(f,14,57)

# Test 15
f,a=board('Frog heart: return pathways')
for x,y,name in [(3.35,4.3,'Right atrium'),(6.65,4.3,'Left atrium'),(5,2.35,'Ventricle')]:
    a.add_patch(Ellipse((x,y),2.4,1.3,fc='#e6eef0',ec=ink,lw=2));label(a,x,y,name,13)
arrow(a,(3.5,3.6),(4.4,2.85));arrow(a,(6.5,3.6),(5.6,2.85))
arrow(a,(8.2,5.8),(7.2,4.7),'from lungs')
arrow(a,(1.8,5.8),(2.75,4.7),'systemic return')
save(f,15,2)

f,a=board('Leaf: vascular bundle and surrounding cells')
a.add_patch(Circle((5,3.45),.7,fc='#d5d1c7',ec=ink,lw=2))
label(a,5,3.45,'vascular\nbundle',11)
for radius,caption,shade in [(1.65,'bundle sheath','#94bc83'),(2.8,'mesophyll','#cfe2c5')]:
    a.add_patch(Circle((5,3.45),radius,fill=False,ec=blue,lw=2))
    for k in range(10 if radius<2 else 15):
        angle=2*np.pi*k/(10 if radius<2 else 15)
        x,y=5+radius*np.cos(angle),3.45+radius*np.sin(angle)
        a.add_patch(Circle((x,y),.35,fc=shade,ec=ink,lw=.8))
label(a,8,5.3,'mesophyll',13);label(a,8,4.7,'bundle sheath',13)
save(f,15,4)

f,a=board('Octahedral donor-site comparison')
for x,title,body in [(2.7,'Complex I','six separate\nmonodentate donors'),(7.3,'Complex II','three bidentate\nligands')]:
    a.add_patch(Circle((x,3.7),.38,fc='#e9eeee',ec=ink))
    label(a,x,3.7,'M',18)
    for dx,dy in [(-1.45,0),(1.45,0),(0,-1.35),(0,1.35),(-.8,-.8),(.8,.8)]:
        segment(a,x+.3*np.sign(dx),3.7+.3*np.sign(dy),x+dx*.8,3.7+dy*.8)
        a.add_patch(Circle((x+dx,3.7+dy),.21,fc='#ead9be',ec=ink))
    if x>5:
        for (u,v) in [((-1.45,0),(0,1.35)),((1.45,0),(.8,.8)),((0,-1.35),(-.8,-.8))]:
            segment(a,x+u[0],3.7+u[1],x+v[0],3.7+v[1],red,1.5)
    label(a,x,5.95,title);label(a,x,1.05,body,13)
save(f,15,17)

f,a=board('Aniline substitution sequence')
for x,name in [(1.35,'Aniline'),(4.0,'Acetanilide'),(6.7,'para-bromo\nacetanilide'),(9.1,'para-bromo\naniline')]:
    label(a,x,3.85,name,13)
for x,y,cap in [(2.25,3.8,'acetylate'),(5.0,3.8,'brominate'),(7.9,3.8,'hydrolyse')]:
    arrow(a,(x,y),(x+.7,y),cap)
label(a,5,1.7,'Aniline with bromine water: 2,4,6-tribromo product',15)
save(f,15,24)

fig,ax=plt.subplots(figsize=(10,7))
x=np.linspace(.0008,.0031,100)
ax.plot(x,-6000*x+24,color=red,lw=3,label='X: slope −6000 K')
ax.plot(x,-3000*x+15,color=blue,lw=3,label='Y: slope −3000 K')
ax.set(xlabel='Reciprocal temperature 1/T (K⁻¹)',ylabel='ln k',
       xlim=(0,.0034),xticks=[0,.001,.002,.003])
ax.legend();ax.grid(alpha=.2);fig.tight_layout();save(fig,15,27)

f,a=board('Open tank accelerating right')
a.add_patch(Rectangle((1.6,1.35),6.7,4.5,fill=False,ec=ink,lw=2))
a.add_patch(Polygon([(1.62,1.37),(8.28,1.37),(8.28,3.1),(1.62,4.8)],
                    fc='#e3f1f8',ec='none'))
segment(a,1.62,4.8,8.28,3.1,blue,3)
arrow(a,(6.0,.7),(8.3,.7),'acceleration +a')
save(f,15,48)

f,a=board('Glass-to-air interface')
a.add_patch(Rectangle((.7,.8),8.6,2.6,fc='#dfeef3',ec='none'))
segment(a,.7,3.4,9.3,3.4,ink,2.6)
segment(a,5,1.1,5,5.9,blue,1.4)
a.plot([5,5],[3.4,5.9],ls='--',color=blue)
arrow(a,(2.26,1.1),(5,3.4))
a.add_patch(Arc((5,3.4),1.65,1.65,theta1=220,theta2=270,ec=red,lw=2))
label(a,4.48,2.75,'50°',16);label(a,8,4.5,'air n=1.0',15)
label(a,8,2.1,'glass n=1.5',15)
save(f,15,57)

f,a=board('Two-slit geometry with a thin sheet')
segment(a,2.7,1.1,2.7,2.4,ink,4);segment(a,2.7,2.7,2.7,4.05,ink,4)
segment(a,2.7,4.35,2.7,5.7,ink,4)
a.add_patch(Rectangle((3.0,4.05),.3,.35,fc='#ddd4be',ec=ink))
segment(a,8.5,1,8.5,5.8,ink,3)
label(a,1.3,3.38,'two slits',14);label(a,4.5,4.9,'thin sheet',13)
arrow(a,(3.7,1.1),(7.9,1.1),'screen distance D')
label(a,8.9,3.4,'screen',14)
save(f,15,60)
