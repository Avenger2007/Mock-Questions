"""Draw fixed, question-bearing diagrams for IAT New Tests 6 and 7."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Polygon, Rectangle

OUT = Path(__file__).resolve().parents[2] / 'IISER/images'
OUT.mkdir(parents=True, exist_ok=True)
INK = '#193442'
TEAL = '#347b77'
RED = '#b75e53'

def canvas():
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_xlim(0, 12); ax.set_ylim(0, 9); ax.set_aspect('equal'); ax.axis('off')
    return fig, ax

def label(ax, x, y, s, size=23, **kw):
    kw.setdefault('ha', 'center'); kw.setdefault('va', 'center')
    ax.text(x, y, s, fontsize=size, color=INK, **kw)

def save(fig, t, n):
    fig.tight_layout(pad=1.5)
    fig.savefig(OUT / f'IAT_T{t:02d}_Q{n:02d}.png', dpi=100, facecolor='white')
    plt.close(fig)

def root_sections():
    fig, ax = canvas()
    for cx, title in [(3.25, 'Section I'), (8.75, 'Section II')]:
        ax.add_patch(Circle((cx, 4.5), 2.35, fill=False, linewidth=3, edgecolor=INK))
        ax.add_patch(Circle((cx, 4.5), 1.65, fill=False, linewidth=2, edgecolor=TEAL))
        label(ax, cx, 7.5, title, 28)
    # Section I: central xylem star and alternating phloem.
    points=[]
    for j in range(16):
        theta=np.pi*j/8
        r=1.38 if j%4==0 else (0.55 if j%2 else 0.78)
        points.append((3.25+r*np.cos(theta),4.5+r*np.sin(theta)))
    ax.add_patch(Polygon(points,closed=True,facecolor='#d4e8e7',edgecolor=TEAL,linewidth=2))
    for theta in np.pi/4+np.arange(4)*np.pi/2:
        ax.add_patch(Ellipse((3.25+1.1*np.cos(theta),4.5+1.1*np.sin(theta)),.46,.32,
                             angle=np.degrees(theta),facecolor='#eac4b5',edgecolor=RED))
    label(ax,3.25,1.45,'small/absent pith',20)
    # Section II: pith and alternating radial vascular units.
    ax.add_patch(Circle((8.75,4.5),.85,facecolor='#f6e9cd',edgecolor=INK,linewidth=2))
    label(ax,8.75,4.5,'pith',19)
    for j in range(12):
        theta=2*np.pi*j/12
        col=TEAL if j%2==0 else RED
        ax.add_patch(Ellipse((8.75+1.25*np.cos(theta),4.5+1.25*np.sin(theta)),.52,.32,
                             angle=np.degrees(theta),facecolor=col,alpha=.7,edgecolor=INK))
    label(ax,8.75,1.45,'many radial units',20)
    save(fig,6,2)

def pollen():
    fig,ax=canvas()
    for cx,name in [(3.2,'P self stigma'),(8.8,'Other plant stigma')]:
        ax.add_patch(Rectangle((cx-1.5,5.3),3,.8,facecolor='#e8c6d6',edgecolor=INK,linewidth=2))
        ax.add_patch(Rectangle((cx-.65,2.0),1.3,3.3,facecolor='#f7e9ee',edgecolor=INK,linewidth=2))
        for dx in (-.6,.6):ax.add_patch(Circle((cx+dx,6.3),.26,facecolor='#f5d38b',edgecolor=INK))
        label(ax,cx,7.5,name,24)
        label(ax,cx,1.5,'hydrated grains',19)
    for dx in (-.6,.6):
        ax.plot([8.8+dx,8.8+dx*.5],[6.05,3.0],color=TEAL,lw=5)
    label(ax,3.2,3.3,'no tubes',21);label(ax,8.8,2.5,'tubes in style',21)
    save(fig,6,6)

def wet_tests():
    fig,ax=canvas()
    for cx, reagent, result in [(3.1,'BaCl₂','white precipitate'),(8.9,'AgNO₃','clear solution')]:
        label(ax,cx,7.5,'Add '+reagent,27)
        ax.plot([cx-1,cx-1,cx+1,cx+1],[6.5,2.8,2.8,6.5],color=INK,lw=4)
        ax.add_patch(Rectangle((cx-.95,2.85),1.9,2,facecolor='#dceef0',edgecolor='none'))
        if cx<6:
            for xx in np.linspace(cx-.72,cx+.72,7):ax.add_patch(Circle((xx,3.05),.09,color='#e9e6df'))
        label(ax,cx,1.8,result,24)
    label(ax,6,8.35,'Immediate ion tests on aliquots',26)
    save(fig,6,17)

def rate_table():
    fig,ax=canvas();label(ax,6,8,'Initial-rate measurements',29)
    columns=['Trial','[A] / M','[B] / M','Rate / units']
    rows=[['1','0.10','0.10','2'],['2','0.20','0.10','8'],['3','0.20','0.20','16']]
    xs=[2.0,4.6,7.2,10]
    for x,s in zip(xs,columns):label(ax,x,6.65,s,23)
    for i,row in enumerate(rows):
        y=5.25-1.3*i
        ax.add_patch(Rectangle((.65,y-.52),10.7,1.04,facecolor='#e7f2f0' if i%2==0 else '#f4f7f7',edgecolor='none'))
        for x,s in zip(xs,row):label(ax,x,y,s,27)
    ax.plot([.65,11.35],[6.0,6.0],color=INK,lw=2)
    save(fig,6,27)

def charges():
    fig,ax=canvas();ax.annotate('',(10.8,4.5),(1.1,4.5),arrowprops=dict(arrowstyle='->',lw=3,color=INK))
    for x,text in [(3,'+q'),(9,'+4q')]:
        ax.add_patch(Circle((x,4.5),.38,facecolor='#dceeea',edgecolor=TEAL,lw=3));label(ax,x,5.45,text,29)
    label(ax,3,3.8,'0');label(ax,9,3.8,'3a');label(ax,10.8,3.8,'x')
    ax.annotate('',(9,2.7),(3,2.7),arrowprops=dict(arrowstyle='<->',lw=2,color=INK));label(ax,6,2.25,'3a',25)
    save(fig,6,53)

def diffraction():
    fig,ax=canvas();x=np.linspace(-10,10,800);y=np.sinc(x/6)**2
    ax.set_aspect('auto');ax.plot(x,y,color=TEAL,lw=4);ax.axvline(0,color=INK,lw=1);ax.axhline(0,color=INK,lw=1)
    for x0,s in [(-6,'−6 mm'),(0,'0'),(6,'+6 mm')]:
        ax.plot([x0,x0],[0,-.06],color=INK,lw=2);ax.text(x0,-.15,s,ha='center',fontsize=22,color=INK)
    ax.text(0,1.1,'Single-slit intensity',ha='center',fontsize=27,color=INK)
    ax.text(0,-.35,'Screen coordinate y',ha='center',fontsize=23,color=INK)
    ax.set_xlim(-10,10);ax.set_ylim(-.42,1.2);ax.axis('off');save(fig,6,58)

def leaf():
    fig,ax=canvas();label(ax,6,8.1,'Upper surface',25)
    ax.add_patch(Rectangle((1.5,7.2),9,.45,facecolor='#e0e9e0',edgecolor=INK,lw=2))
    for x in np.arange(2,10.5,.8):
        ax.add_patch(Rectangle((x,4.7),.6,2.3,facecolor='#a3c9a3',edgecolor=TEAL,lw=1.5))
        for y in (5.2,6,6.7):ax.add_patch(Circle((x+.3,y),.07,color='#3f8565'))
    rng=np.random.default_rng(7)
    for x,y in zip(rng.uniform(2,10,24),rng.uniform(2.4,4.5,24)):
        ax.add_patch(Ellipse((x,y),.62,.38,angle=20,facecolor='#b9d8b5',edgecolor=TEAL,alpha=.9))
    ax.add_patch(Rectangle((1.5,1.75),9,.45,facecolor='#e0e9e0',edgecolor=INK,lw=2))
    label(ax,6,.9,'Lower surface',25)
    save(fig,7,2)

def embryo():
    fig,ax=canvas();label(ax,6,8,'Megaspore lineage',27)
    for i,x in enumerate((1.9,4.5,7.1,9.7)):
        ax.add_patch(Circle((x,6),.5,facecolor='#dceeea' if i==3 else '#eadbdb',edgecolor=INK,lw=2))
        label(ax,x,4.9,'functional' if i==3 else 'degenerates',19)
    ax.annotate('',(9.7,3.3),(9.7,4.4),arrowprops=dict(arrowstyle='->',lw=2,color=INK))
    for y,count in ((3.2,2),(2.3,4),(1.4,8)):
        label(ax,9.7,y,f'{count} nuclei',23)
    label(ax,4.6,3.2,'three successive mitoses',23)
    save(fig,7,6)

def platinum():
    fig,ax=canvas()
    for cx,title,ligands in [(3,'X',['Cl','NH₃','NH₃','Cl']),(9,'Y',['Cl','NH₃','Cl','NH₃'])]:
        label(ax,cx,7.6,title,27);label(ax,cx,4.5,'Pt',31)
        pts=[(cx,6.25),(cx+1.7,4.5),(cx,2.75),(cx-1.7,4.5)]
        for (x,y),s in zip(pts,ligands):
            ax.plot([cx,x],[4.5,y],lw=3,color=INK);label(ax,x,y,s,25,bbox=dict(facecolor='white',edgecolor='none',pad=2))
    save(fig,7,17)

def quantum():
    fig,ax=canvas();label(ax,6,8,'Candidate quantum-number sets',28)
    label(ax,6.6,6.9,'(n, l, mₗ, mₛ)',25)
    for j,(name,values) in enumerate([('A','(3, 2, −2, +1/2)'),('B','(2, 1, 0, −1/2)'),('C','(3, 3, 0, +1/2)'),('D','(4, 0, 0, −1/2)')]):
        y=5.8-j*1.25;ax.add_patch(Rectangle((2,y-.45),8,.9,facecolor='#ecf4f3' if j%2==0 else '#f5f7f7',edgecolor='none'))
        label(ax,3,y,name,27);label(ax,6.7,y,values,25)
    save(fig,7,20)

def lenz():
    fig,ax=canvas();ax.add_patch(Circle((6,4.6),2.25,fill=False,lw=5,edgecolor=TEAL))
    for x in np.arange(3.7,8.5,1.2):
        for y in np.arange(2.4,7.1,1.2):
            ax.plot(x,y,marker='x',ms=11,mew=2,color=INK)
    label(ax,6,8,'External B into page',26)
    label(ax,6,1.15,'Magnitude decreasing with time',24)
    save(fig,7,56)

def fringes():
    fig,ax=canvas();ax.plot([2,10],[4.5,4.5],lw=2,color=INK);ax.plot([10,10],[1,8],lw=4,color=INK)
    ax.add_patch(Rectangle((2,3.5),.16,2,facecolor=INK))
    for y in (4.2,4.8):ax.add_patch(Rectangle((1.99,y),.2,.14,facecolor='white'))
    ax.plot([2.2,10],[4.2,6.5],'--',color=TEAL,lw=2);ax.plot([2.2,10],[4.8,6.5],'--',color=TEAL,lw=2)
    ax.plot([9.75,10.25],[6.5,6.5],lw=5,color=RED)
    label(ax,10.5,6.55,'4th bright: +4 mm',21,ha='left')
    label(ax,2.5,6.5,'slit gap d',22);label(ax,6,2.4,'screen distance D',22)
    label(ax,10.5,4.5,'centre',19,ha='left')
    save(fig,7,58)

if __name__=='__main__':
    for fn in (root_sections,pollen,wet_tests,rate_table,charges,diffraction,leaf,embryo,platinum,quantum,lenz,fringes):fn()
