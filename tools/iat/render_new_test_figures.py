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

def t03():
    fig, ax = axis();ax.axis('off')
    ax.annotate('Promoter / transcription',xy=(.15,.81),xytext=(.83,.81),xycoords='axes fraction',textcoords='axes fraction',fontsize=24,ha='right',arrowprops=dict(arrowstyle='->',lw=3))
    ax.text(.5,.60,"5′  TTA CGA CAT  3′",fontsize=37,ha='center',transform=ax.transAxes,color=INK)
    ax.text(.5,.43,"3′  AAT GCT GTA  5′",fontsize=37,ha='center',transform=ax.transAxes,color=INK)
    ax.text(.5,.23,'DNA duplex',fontsize=24,ha='center',transform=ax.transAxes)
    finish(fig,'IAT_T03_Q07.png')

    fig, ax = axis();ax.set_xlim(0,5);ax.set_ylim(105,195);ax.set_xticks([1,2,3,4],['M','C','P','Q']);ax.set_yticks([120,150,160,180],['120','150','160','180']);ax.set_ylabel('Fragment length (units)',fontsize=25);ax.set_xlabel('Gel lane',fontsize=25)
    for x,levels in [(1,[120,150]),(2,[120,180]),(3,[160,180]),(4,[120,160])]:
        ax.add_patch(plt.Rectangle((x-.35,110),.7,78,facecolor='#e9eef1',edgecolor='#c5d1d7'))
        for level in levels:ax.plot([x-.28,x+.28],[level,level],lw=9,color=INK,solid_capstyle='butt')
    finish(fig,'IAT_T03_Q15.png')

    fig, axs = plt.subplots(1,2,figsize=(12,9))
    for ax,title,lower,upper,gap in [(axs[0],'X: Δ < P',.34,.54,'small'),(axs[1],'Y: Δ > P',.22,.76,'large')]:
        ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off');ax.text(.5,.92,title,ha='center',fontsize=28,color=INK)
        for cx in [.31,.5,.69]:ax.plot([cx-.07,cx+.07],[lower,lower],lw=4,color=INK)
        for cx in [.4,.6]:ax.plot([cx-.07,cx+.07],[upper,upper],lw=4,color=INK)
        ax.text(.83,lower,'t₂g',fontsize=22,va='center');ax.text(.83,upper,'e_g',fontsize=22,va='center')
        ax.annotate('',xy=(.14,upper),xytext=(.14,lower),arrowprops=dict(arrowstyle='<->',lw=2));ax.text(.03,(upper+lower)/2,'Δ',fontsize=23)
        ax.annotate('Energy',xy=(.04,.82),xytext=(.04,.12),rotation=90,fontsize=20,arrowprops=dict(arrowstyle='->',lw=2))
    finish(fig,'IAT_T03_Q17.png')

    fig,ax=axis();ax.axis('off');ax.text(.5,.78,'Reductive ozonolysis products',fontsize=28,ha='center',transform=ax.transAxes)
    ax.text(.5,.57,'H–C(=O)–H    +    CH₃–C(=O)–H',fontsize=38,ha='center',transform=ax.transAxes,color=INK)
    ax.text(.5,.37,'one molecule of each',fontsize=25,ha='center',transform=ax.transAxes)
    finish(fig,'IAT_T03_Q23.png')

    fig,ax=axis();ax.add_patch(Circle((0,0),2.6,fill=False,lw=5,color=INK));ax.add_patch(Circle((1.3,0),1.3,facecolor='white',edgecolor=INK,lw=4))
    ax.plot([0,1.3],[0,0],'--',lw=2,color='#657b86');ax.plot(0,0,'o',color=INK);ax.plot(1.3,0,'o',color=INK)
    ax.text(-.58,-.28,'O',fontsize=30);ax.text(1.4,-.27,'H',fontsize=30);ax.text(.20,-1.70,'OH = R/2',fontsize=28)
    ax.annotate('R',xy=(-1.85,1.85),xytext=(-.8,.8),fontsize=30,arrowprops=dict(arrowstyle='->',lw=2));ax.annotate('R/2',xy=(2.35,.73),xytext=(2.05,1.63),fontsize=28,arrowprops=dict(arrowstyle='->',lw=2))
    ax.set_xlim(-3.4,3.5);ax.set_ylim(-3.1,3.1);ax.set_aspect('equal');ax.axis('off');finish(fig,'IAT_T03_Q48.png')

    fig,ax=axis();ax.set_xlim(-1.6,4.6);ax.set_ylim(-1.3,1.7);ax.axis('off');ax.annotate('',xy=(4.35,0),xytext=(-1.35,0),arrowprops=dict(arrowstyle='->',lw=3,color=INK))
    ax.plot([0,3],[0,0],'o',ms=11,color=INK);ax.text(-.28,.27,'+q',fontsize=32);ax.text(2.62,.27,'−4q',fontsize=32)
    ax.text(-.1,-.38,'0',fontsize=25);ax.text(2.8,-.38,'3a',fontsize=25);ax.text(4.15,-.36,'x',fontsize=26)
    ax.annotate('',xy=(3,-.68),xytext=(0,-.68),arrowprops=dict(arrowstyle='<->',lw=2));ax.text(1.23,-1.05,'3a',fontsize=25)
    finish(fig,'IAT_T03_Q53.png')

if __name__ == '__main__':
    t02()
    t03()
