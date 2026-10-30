"""Deterministic, exact diagrams for the manually authored IAT pilot."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'IISER/images'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 17,
                     'axes.linewidth': 1.4, 'savefig.facecolor': 'white'})

def canvas():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
    ax.set(xlim=(0, 10), ylim=(0, 7.5))
    ax.axis('off')
    return fig, ax

def save(fig, n):
    fig.savefig(OUT / f'IAT_T01_Q{n:02}.png', dpi=150)
    plt.close(fig)

fig, ax = canvas()
ax.add_patch(Ellipse((4.8, 3.4), 6.5, 3.8, fill=False, lw=2.5))
ax.add_patch(Ellipse((4.8, 3.4), 6.25, 3.55, fill=False, lw=1.2))
ax.text(4.5, 3.65, 'Thylakoid lumen', ha='center')
ax.text(4.5, 2.9, 'pH 5', ha='center', fontsize=22)
ax.plot([7.75, 8.3], [3.4, 3.4], color='black', lw=5)
ax.add_patch(Circle((8.65, 3.4), .42, fill=False, lw=2))
ax.annotate('ATP synthase', xy=(8.65, 3.85), xytext=(7.0, 5.4),
            arrowprops={'arrowstyle':'-', 'lw':1.3}, ha='center')
ax.text(4.5, 6.4, 'Outside: pH 8; ADP + inorganic phosphate', ha='center')
ax.text(5, .65, 'Darkness • sealed, proton-tight membrane', ha='center', fontsize=16)
save(fig, 9)

fig, ax = canvas()
ax.text(5, 6.7, 'Completely digested PCR sample', ha='center', fontsize=20)
ax.add_patch(Rectangle((3.0, 1.0), 4.1, 4.9, fill=False, lw=1.6))
ax.add_patch(Rectangle((4.35, 5.5), 1.4, .18, fill=False, lw=1.5))
for y, size in [(4.7, 900), (3.5, 600), (2.0, 300)]:
    ax.plot([4.35, 5.75], [y, y], color='black', lw=5, solid_capstyle='butt')
    ax.text(7.45, y, f'{size} bp', va='center')
ax.text(5, .45, 'Band positions only; intensity is not to scale', ha='center', fontsize=15)
save(fig, 11)

fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
fig.subplots_adjust(left=.16, right=.94, bottom=.17, top=.92)
ax.plot([0, 2, 4, 6], [0, 4, -4, 0], color='black', lw=2.5)
ax.scatter([0, 2, 4, 6], [0, 4, -4, 0], color='black', s=30)
ax.axhline(0, color='black', lw=1); ax.axvline(0, color='black', lw=1)
ax.set(xlim=(-.3, 6.4), ylim=(-5, 5), xticks=range(7), yticks=[-4, -2, 0, 2, 4],
       xlabel='Time, t (s)', ylabel='Velocity, v (m/s)')
ax.spines[['top', 'right']].set_visible(False)
save(fig, 46)

fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
fig.subplots_adjust(left=.2, right=.94, bottom=.18, top=.92)
ax.plot([0, 1, 2], [0, -1, -1], color='black', lw=2.8)
ax.axhline(0, color='black', lw=1); ax.axvline(0, color='black', lw=1)
ax.plot([1,1], [0,-1], 'k--', lw=1)
ax.set(xlim=(-.05,2.2), ylim=(-1.4,.25), xticks=[0,1,2], xticklabels=['0','a','2a'],
       yticks=[-1,0], yticklabels=['−E₀','0'], xlabel='Position, x', ylabel='Electric field, Eₓ')
ax.spines[['top','right','bottom','left']].set_visible(False)
save(fig, 53)

fig, ax = canvas()
top, mid, bottom = 6.4, 3.8, 1.2
left, right, supply = 4, 7.6, 1.5
ax.plot([supply,right],[top,top],'k',lw=2)
ax.plot([supply,right],[bottom,bottom],'k',lw=2)
ax.plot([supply,supply],[bottom,3.3],'k',lw=2)
ax.plot([supply,supply],[4.1,top],'k',lw=2)
ax.plot([.9,2.1],[4.1,4.1],'k',lw=2.4)
ax.plot([1.15,1.85],[3.3,3.3],'k',lw=2.4)
ax.text(.45,4.25,'+',fontsize=18); ax.text(.45,3.1,'−',fontsize=18)
ax.text(1.5,.5,'12 V',ha='center')
def resistor(x, y1, y2, label, labelx):
    c=(y1+y2)/2
    ax.plot([x,x],[y1,c+.45],'k',lw=2)
    ax.plot([x,x],[c-.45,y2],'k',lw=2)
    ax.add_patch(Rectangle((x-.2,c-.45),.4,.9,fill=False,lw=2))
    ax.text(labelx,c,label,va='center',ha='center')
resistor(left,top,mid,'2 Ω',3.0)
resistor(left,mid,bottom,'4 Ω',3.0)
resistor(right,top,mid,'3 Ω',8.7)
resistor(right,mid,bottom,'3 Ω',8.7)
ax.plot([left,5.4],[mid,mid],'k',lw=2)
ax.plot([6.2,right],[mid,mid],'k',lw=2)
ax.add_patch(Circle((5.8,mid),.4,fill=False,lw=2))
ax.text(5.8,mid,'A',ha='center',va='center',fontsize=16)
ax.text(5.8,4.55,'Ideal ammeter',ha='center',fontsize=15)
for x,name in [(left,'A'),(right,'B')]:
    ax.plot(x,mid,'ko',ms=5)
    ax.text(x+(-.4 if name=='A' else .4),mid+.15,name,ha='center',va='bottom')
save(fig, 54)

fig, ax = canvas()
ax.text(5,6.75,'Viewed from air, close to the normal',ha='center',fontsize=18)
ax.plot([1,9],[5.8,5.8],'k',lw=2)
ax.plot([1,9],[3.25,3.25],'k',lw=1.8)
ax.plot([1,9],[1.35,1.35],'k',lw=2)
ax.plot([1,1],[1.35,5.8],'k',lw=1.5); ax.plot([9,9],[1.35,5.8],'k',lw=1.5)
ax.text(4.5,4.5,'n = 3/2',ha='center',fontsize=22)
ax.text(4.5,2.2,'n = 4/3',ha='center',fontsize=22)
for y1,y2,label in [(3.25,5.8,'6 cm'),(1.35,3.25,'4 cm')]:
    ax.annotate('',xy=(8,y1),xytext=(8,y2),arrowprops={'arrowstyle':'<->','lw':1.4})
    ax.text(7.4,(y1+y2)/2,label,ha='right',va='center')
ax.add_patch(Ellipse((4.5,1.45),.75,.18,color='black'))
ax.text(4.5,.7,'Coin',ha='center')
save(fig, 57)
print('Wrote six exact diagrams at 1200 × 900 pixels.')
