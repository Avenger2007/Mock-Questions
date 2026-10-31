"""Render manually specified, exact IAT review diagrams; never author question content."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

OUT = Path(__file__).resolve().parents[2] / 'IISER/images'
OUT.mkdir(parents=True, exist_ok=True)
INK = '#172d3b'

def finish(fig, name):
    fig.tight_layout(pad=2)
    fig.savefig(OUT / name, dpi=100, facecolor='white')
    plt.close(fig)

def axis(figsize=(12,9)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.spines[['top','right']].set_visible(False)
    ax.tick_params(labelsize=22, width=1.5)
    return fig, ax

def t02():
    fig, ax = axis()
    labels = ['P','Q','R']; x=np.arange(3); w=.23
    for offset, values, label, color in [(-w,[9,1,1],'Chlorophyll','#4e8d70'),(0,[1,9,1],'Ribosomal RNA','#5677aa'),(w,[1,1,9],'Catalase','#bc745a')]:
        ax.bar(x+offset,values,width=w,label=label,color=color)
    ax.set_xticks(x,labels);ax.set_ylim(0,10);ax.set_yticks([0,2,4,6,8,10]);ax.set_ylabel('Relative marker enrichment',fontsize=25);ax.set_xlabel('Cell fraction',fontsize=25)
    ax.legend(fontsize=19,loc='upper center',ncol=3,bbox_to_anchor=(.5,1.15));finish(fig,'IAT_T02_Q03.png')

    fig, ax = axis();x=np.array([0,1,2,3,4]);ax.plot(x,[0,2.4,3,3,3],'-o',lw=4,ms=10,label='Low CO₂',color='#a64c45');ax.plot(x,[0,3,6,8,9],'-s',lw=4,ms=10,label='High CO₂',color='#327664')
    ax.set_xlim(0,4);ax.set_ylim(0,10);ax.set_xticks(x);ax.set_yticks([0,2,4,6,8,10]);ax.set_xlabel('Light intensity (relative units)',fontsize=25);ax.set_ylabel('Net photosynthesis (relative units)',fontsize=25);ax.legend(fontsize=24);finish(fig,'IAT_T02_Q04.png')

    fig, ax = axis();ax.axis('off')
    ax.text(.5,.78,'P',fontsize=30,ha='center',transform=ax.transAxes,color=INK)
    ax.text(.5,.64,'[Co(NH₃)₅Br]  SO₄',fontsize=40,ha='center',transform=ax.transAxes,color=INK)
    ax.text(.5,.40,'Q',fontsize=30,ha='center',transform=ax.transAxes,color=INK)
    ax.text(.5,.26,'[Co(NH₃)₅SO₄]  Br',fontsize=40,ha='center',transform=ax.transAxes,color=INK)
    finish(fig,'IAT_T02_Q17.png')

    fig, ax = axis();ax.bar([1,2,3],[2,4,16],width=.5,color='#487f9b')
    ax.set_xticks([1,2,3],['1\nA .10, B .10','2\nA .20, B .10','3\nA .20, B .20']);ax.set_ylim(0,18);ax.set_yticks([0,4,8,12,16]);ax.set_ylabel('Initial rate (10⁻³ M/s)',fontsize=24);ax.set_xlabel('Trial and concentrations (M)',fontsize=24)
    finish(fig,'IAT_T02_Q27.png')

    fig, ax = axis();ax.plot([0,1,1,3],[2,2,-1,-1],lw=4,color=INK)
    ax.axhline(0,lw=1.5,color=INK);ax.axvline(0,lw=1.5,color=INK);ax.set_xlim(-.2,3.35);ax.set_ylim(-1.5,2.6)
    ax.set_xticks([0,1,3],['0','a','3a']);ax.set_yticks([-1,0,2],['−E₀','0','+2E₀']);ax.set_xlabel('Position x',fontsize=25);ax.set_ylabel('Eₓ',fontsize=27);finish(fig,'IAT_T02_Q55.png')

    fig, ax = axis();ax.set_xlim(-35,25);ax.set_ylim(-2,4);ax.axis('off');ax.plot([-35,23],[0,0],lw=2,color=INK)
    ax.annotate('',xy=(-30,2.6),xytext=(-30,0),arrowprops=dict(arrowstyle='->',lw=3,color=INK));ax.text(-33,2.9,'Object',fontsize=23)
    ax.plot([0,0],[-1.8,2.2],lw=4,color='#327664');ax.text(-5,-1.55,'Lens  f=10 cm',fontsize=21)
    ax.plot([20,20],[-1.8,2.2],lw=5,color=INK);ax.text(13,2.5,'Plane mirror',fontsize=21)
    ax.annotate('',xy=(0,-.55),xytext=(-30,-.55),arrowprops=dict(arrowstyle='<->',lw=2));ax.text(-21,-.95,'30 cm',fontsize=23)
    ax.annotate('',xy=(20,-.55),xytext=(0,-.55),arrowprops=dict(arrowstyle='<->',lw=2));ax.text(6,-.95,'20 cm',fontsize=23)
    finish(fig,'IAT_T02_Q57.png')

if __name__ == '__main__':
    t02()
