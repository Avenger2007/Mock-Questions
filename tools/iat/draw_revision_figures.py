"""Exact figures for manually authored revision questions; preserves prior six PNGs."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'IISER/images'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 17})
fig, ax = plt.subplots(figsize=(8,6), dpi=150)
fig.subplots_adjust(left=.18, right=.95, bottom=.2, top=.88)
ax.plot([0,1,2,3,4], [0,.01,.01,.03,.03], color='black', lw=2.4)
ax.set(xlim=(0,4.2), ylim=(0,.035), xlabel='Progress of experiment (schematic)',
       ylabel='Cumulative nitrogen (mol)', yticks=[0,.01,.02,.03])
ax.set_yticklabels(['0','0.010','0.020','0.030'])
ax.set_xticks([1,3]); ax.set_xticklabels(['Cold stage, 0-5 °C','After warming'])
ax.axvline(2, color='gray', ls='--', lw=1)
ax.spines[['top','right']].set_visible(False)
ax.set_title('Gas collected from the same mixture', pad=17, fontsize=18)
fig.savefig(OUT/'IAT_T01_Q21.png', dpi=150, facecolor='white'); plt.close(fig)
fig, ax = plt.subplots(figsize=(8,6), dpi=150)
ax.set(xlim=(0,10), ylim=(0,7.5));ax.axis('off')
ax.text(5,6.8,'Alkene connectivity',ha='center',fontsize=23)
for y,label,formula in [(5.3,'P',r'CH$_2$=CH-CH$_2$-CH$_3$'),
                        (3.6,'Q',r'CH$_3$-CH=CH-CH$_3$'),
                        (1.9,'R',r'CH$_2$=C(CH$_3$)$_2$')]:
    ax.text(1,y,label,ha='center',va='center',fontsize=25,fontweight='bold')
    ax.text(5.6,y,formula,ha='center',va='center',fontsize=26)
ax.text(5,.55,'Connectivity only; no E/Z configuration assigned',ha='center',fontsize=15)
fig.savefig(OUT/'IAT_T01_Q25.png', dpi=150, facecolor='white'); plt.close(fig)
