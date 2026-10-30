"""Build two source-backed PDF reports; never modifies the authored IAT paper."""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/pdf'
ASSETS = ROOT / 'output/iat_reports/assets'
OUT.mkdir(parents=True, exist_ok=True)
ASSETS.mkdir(parents=True, exist_ok=True)
PAPER = ROOT / 'IISER/review/baseline/IAT_TEST_1_before_revision.json'
test = json.loads(PAPER.read_text())
questions = test['questions']
ledger = json.loads((ROOT/'docs/blueprints/iat_pyq_ledger.json').read_text())
metrics = json.loads((ROOT/'docs/blueprints/iat_pyq_metrics.json').read_text())
taxonomy = json.loads((ROOT/'docs/blueprints/iat_taxonomy.json').read_text())
plan = list(csv.DictReader((ROOT/'IISER/review/baseline/iat_test_01_plan_before_revision.tsv').open(), delimiter='\t'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
tracked = [PAPER, ROOT/'IISER/review/baseline/IAT_TEST_1_before_revision.pdf'] + [(ROOT/'IISER/images'/f'IAT_T01_Q{n:02}.png') for n in [9,11,46,53,54,57]]
before = {str(p.relative_to(ROOT)):sha(p) for p in tracked}

SUBJECTS = dict(zip('BCMP',['Biology','Chemistry','Mathematics','Physics']))
SHORT = {
 'B': {'DIV':'Diversity','STR':'Plant/animal structure','CELL':'Cells and biomolecules','PLANT':'Plant physiology','HUMAN':'Human physiology','REPRO':'Reproduction','GEN':'Genetics and evolution','WELFARE':'Human welfare','BIOTECH':'Biotechnology','ECO':'Ecology'},
 'C': {'STO':'Mole concept / stoichiometry','ATOM':'Atomic structure','PERIOD':'Periodicity','BOND':'Chemical bonding','DF':'d- and f-block','COORD':'Coordination compounds','THERM':'Thermodynamics','EQ':'Equilibrium','REDOX':'Redox','SOL':'Solutions','ELEC':'Electrochemistry','KIN':'Kinetics','GOC':'Organic principles','HC':'Hydrocarbons','HALO':'Halo compounds','ALCO':'Alcohols / phenols / ethers','CARB':'Carbonyls / carboxylic acids','AMINE':'Nitrogen compounds','BIO':'Biomolecules'},
 'M': {'SET':'Relations / functions','COUNT':'Permutations / combinations','BINOM':'Binomial theorem','COMPLEX':'Complex numbers','QUAD':'Quadratic equations','TRIG':'Trigonometry','VECTOR':'Vectors','MATRIX':'Matrices / determinants','COORD':'Coordinate geometry','3D':'3D geometry','SEQ':'Sequences / series','LIMIT':'Limits / continuity','DIFF':'Differentiation','INT':'Integration','DE':'Differential equations','STAT':'Statistics','PROB':'Probability'},
 'P': {'UNITS':'Units / dimensions','KIN':'Kinematics','FORCE':'Laws of motion','WORK':'Work / energy / power','ROT':'Rotation / centre of mass','GRAV':'Gravitation','SOLID':'Elasticity of solids','FLUID':'Fluid mechanics','THERMAL':'Thermal properties','THERMO':'Thermodynamics','KTG':'Kinetic theory','SHM':'Oscillations','WAVE':'Waves','ELECTRO':'Electric field / potential','CAP':'Capacitance / potential','CURRENT':'Current electricity','MAG':'Magnetism','EMI':'Electromagnetic induction','AC':'Alternating current','EMW':'Electromagnetic waves','RAY':'Ray optics','WAVEOPT':'Wave optics','DUAL':'Photons / matter waves','ATOM':'Atoms','NUC':'Nuclei','SEMI':'Semiconductors'}
}

# Manual audit recoding. Same mutually exclusive dominant-task rules as the PYQ ledger.
# No tier is silently changed in the test JSON.
TASKS = {
 'B':'C C E N C N C C D C D E N C E'.split(),
 'C':'C C N N N E N N D C N N C N N'.split(),
 'M':'N N N N N N N N N N N N C N N'.split(),
 'P':'G C N N C N N G D C N D N N N'.split()
}
EASIER = {5,8,12,14,21,27,29,51,52}
HARD_TO_MEDIUM = {4,33}
NOTES = [
 'Keep. Generation and independence must be read together; introductory item.',
 'Keep. Cambium and bundle position support the stated ordinary-growth prediction.',
 'Keep. Substrate rescue is consistent with inhibition; wording avoids claiming proof.',
 'Review tier: medium. The measured ab frequency can simply be squared; phase inference is not required.',
 'Strengthen. Controlled conditions leave a familiar direct ADH response; likely easy.',
 'Keep. Correctly separates plant respiration, assimilation and consumer respiration.',
 'Keep. Explicit centromere convention removes chromosome/chromatid ambiguity.',
 'Review tier: easy. The two fertilisation outcomes are direct; no endosperm calculation is needed.',
 'Keep figure. Proton gradient and ATP-synthase orientation are correct; trim absolute distractors.',
 'Keep. Active/passive distinction is sound; shorten the unusually long correct option.',
 'Keep figure. Complete digestion and equal recovery justify band-mass inference; not equal band brightness.',
 'Strengthen. Binding assay directly identifies the receptor defect, leaving little inference.',
 'Keep. Both unaffected-person conditions are necessary; 1/18 follows.',
 'Strengthen. Photosynthetic skin and a four-chambered frog heart are weak distractors; likely easy.',
 'Keep. Opposite directions in replicate small populations support drift; a table would improve scanning.',
 'Keep. Resonance is represented correctly; revise option-length cue.',
 'Keep. Co charge balance and wavelength relation are consistent with the stipulated transition.',
 'Keep. Correct unit conversion and temperature sign change; one short calculation chain.',
 'Keep. Identical portions and independent assays remove mixture-scale ambiguity.',
 'Keep. Ksp-controlled copper concentration and the two-electron Nernst factor are both needed.',
 'Strengthen. The stem supplies the cold/warm rules, so the answer mainly copies the two amounts; likely easy.',
 'Keep. Integer charge balance correctly interprets mixed valence; appropriate easy item.',
 'Keep. Additional time is correctly distinguished from total time; supplied logarithms are adequate.',
 'Keep with scope review. Formula tracking and two stereocentres are sound; explicitly map geometric/optical isomerism.',
 'Replace one of Q24/Q25 at its stable ID: consecutive ketone/alcohol chirality contexts narrow organic coverage.',
 'Clarify initial equal hydrostatic pressures. The osmotic result is correct under that standard assumption.',
 'Review tier: easy. Final residue is already pure carbonate; the initial mixture mass is not needed.',
 'Keep. Isoelectronic trend is unambiguous; use charge superscripts in all displayed options.',
 'Strengthen. Both products and the two-silver stoichiometry are supplied; the remaining arithmetic is very short.',
 'Keep. Strong-acid stoichiometry precedes the buffer ratio; approximation and final pH are sound.',
 'Keep. Determinant and inverse trace are correct; appropriate short starter.',
 'Keep. Ordered spacing and arrangements are counted once; enumeration confirms 96.',
 'Review tier: medium. Two substitutions and completing the square give the endpoint minimum.',
 'Keep. Intersecting loci and the signed product require interpretation rather than modulus alone.',
 'Keep. Reflection symmetry plus substitution is valid; usable medium calculus item.',
 'Keep. Plane reflection and origin distance are distinct; vector check agrees.',
 'Keep. Both cusp locations must be cancelled; a=b=-2 is sufficient.',
 'Keep. Population-variance convention is explicit; between-group variation is included.',
 'Keep. Rationalisation is short and unambiguous; appropriate easy item.',
 'Keep. Exactly two fixed points requires the four-key derangement count; exhaustive check agrees.',
 'Keep. Principal-value quadrant is correctly enforced; option D needs proper inverse-tangent typography.',
 'Keep. Separation, partial fractions and initial condition are valid; lower-medium demand.',
 'Keep. Strict root location needs f(1)<0, not just the discriminant.',
 'Keep. Split point moves with the parameter; optimisation and endpoints are correct.',
 'Keep. Bilinear cross product gives the correct area; no picture is necessary.',
 'Keep graph. Signed and absolute areas differ; zero crossing and scale are correct.',
 'Keep. Dimensions of b follow term-by-term consistency; correct easy classification.',
 'Keep. Radius-to-area factor is squared before Bernoulli is used.',
 'Keep. Internal powered work is clearly distinguished from external axial torque; long stem merits timed review.',
 'Keep. First-law balance and Carnot limit agree; no impossible engine is implied.',
 'Review tier: easy. Maximum extension follows directly from equilibrium extension plus amplitude.',
 'Review tier: easy. Two trial frequencies resolve the beat ambiguity quickly.',
 'Keep graph. Negative field area decreases positive-charge kinetic energy; turning point lies within the plot.',
 'Keep circuit. Meter shorts the midpoints; connected-node KCL confirms 12/17 A from A to B.',
 'Keep. Alpha/beta-minus bookkeeping is correct and deliberately easy.',
 'Clarify that the bar spans the rails perpendicular to them. The standard motional-emf result is correct.',
 'Keep as useful setup sketch. Paraxial depth sum is correct and layer-order independent.',
 'Keep. Reactive voltages oppose; 10 V rms and 16 W real power are correct.',
 'Keep. Mean-square voltage, not mean voltage squared, gives the half-wave power ratio.',
 'Keep. Initial pi reversal changes integer-wave conditions to odd half waves; 3 micrometres is consistent.'
]
assert len(NOTES)==60
audit_rows=[]
for i,(q,p) in enumerate(zip(questions,plan),1):
    s=q['section']; matches=[code for code,label in taxonomy[s].items() if label[0]==p['chapter']]
    if s=='P' and i==46: matches=['KIN']
    if s=='P' and i==53: matches=['ELECTRO']
    if s=='P' and i==59: matches=['SEMI']
    assert len(matches)==1,(i,p['chapter'],matches)
    tier='easy' if i in EASIER else 'medium' if i in HARD_TO_MEDIUM else q['difficulty']
    audit_rows.append({'question':i,'id':q['id'],'subject':s,'chapter_code':matches[0],
        'dominant_task':TASKS[s][(i-1)%15],'stored_difficulty':q['difficulty'],
        'review_difficulty':tier,'key':q['correct_option'],'note':NOTES[i-1],
        'action':'revise' if i in EASIER|HARD_TO_MEDIUM|{9,10,14,16,24,25,26,28,41,49,56} else 'keep'})

BLUE='#315d7d'; INK='#202a32'; GRAY='#929aa0'; ORANGE='#9b582e'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.labelsize':10,
 'xtick.labelsize':9,'ytick.labelsize':10,'axes.spines.top':False,'axes.spines.right':False,
 'axes.edgecolor':'#899096','text.color':INK,'axes.labelcolor':INK,
 'xtick.color':INK,'ytick.color':INK,'savefig.facecolor':'white'})

def finish(fig,name):
    p=ASSETS/(name+'.png');fig.savefig(p,dpi=210,bbox_inches='tight',pad_inches=.10);plt.close(fig);return p

def chapter_chart(s, codes=None, audit=False):
    rows=[r for r in metrics['chapter_counts'][s] if not r['code'].startswith('X') and (codes is None or r['code'] in codes)]
    if codes is None: rows=sorted(rows,key=lambda r:(-r['recent_n'],r['chapter']))
    den=metrics['by_subject'][s]['recent_current_n'];n=len(rows)
    row_height=.175 if audit and n>22 else .23
    fig,ax=plt.subplots(figsize=(7.0,row_height*n+1.05))
    y=np.arange(n)
    if audit:
        actual=Counter(r['chapter_code'] for r in audit_rows if r['subject']==s)
        expected=[15*r['recent_n']/den for r in rows]
        ax.barh(y-.17,expected,height=.31,facecolor='white',edgecolor=GRAY,lw=1.1,label='Recent share × 15 (reference)')
        ax.barh(y+.17,[actual[r['code']] for r in rows],height=.31,color=BLUE,label='Test 1')
        ax.set_xlim(0,max(4,max(expected)+.7));ax.set_xlabel('Questions in a 15-question section')
        for j,r in enumerate(rows):ax.text(actual[r['code']]+.04,j+.17,str(actual[r['code']]),va='center',fontsize=9)
    else:
        ax.barh(y,[r['recent_n'] for r in rows],color=BLUE,height=.58)
        ax.set_xlim(0,max(r['recent_n'] for r in rows)*(1.48 if s=='B' else 2.05)+.8)
        ax.set_xlabel('Questions in 2023–2026 (current-scope families)')
        for j,r in enumerate(rows):
            label=f"{r['recent_n']}  ({100*r['recent_n']/den:.1f}%)"+(f" [{r['all_n']}]" if s!='B' else '')
            ax.text(r['recent_n']+.12,j,label,va='center',fontsize=9)
    ax.set_yticks(y,[SHORT[s][r['code']] for r in rows]);ax.invert_yaxis()
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=not audit,nbins=6))
    ax.grid(axis='x',color='#e1e3e5',lw=.6);ax.set_axisbelow(True)
    fig.tight_layout()
    return finish(fig,('audit_' if audit else 'chapter_')+s+('_'+codes[0] if codes else ''))

TASK_MAP={'recall':'Recall','conceptual':'Concept','numerical':'Numerical','table/match':'Visual/data','graph':'Visual/data','diagram/structure':'Visual/data','experiment':'Experiment'}
TASK_LETTER={'R':'Recall','C':'Concept','N':'Numerical','T':'Visual/data','G':'Visual/data','D':'Visual/data','E':'Experiment'}
CATS=['Recall','Concept','Numerical','Visual/data','Experiment']
PALETTE={'Recall':'#c6cbd0','Concept':'#7b8b99','Numerical':BLUE,'Visual/data':ORANGE,'Experiment':'#c1a57b'}

def recent_mix(s):
    c=Counter()
    for k,v in metrics['by_subject'][s]['recent_tasks'].items():c[TASK_MAP[k]]+=v
    return c

def mix_chart(audit=False):
    fig,ax=plt.subplots(figsize=(7.0,4.1 if audit else 3.2))
    series=[]
    for s in 'BCMP':
        series.append((SUBJECTS[s]+' / PYQ',recent_mix(s),metrics['by_subject'][s]['recent_n']))
        if audit:series.append((SUBJECTS[s]+' / Test 1',Counter(TASK_LETTER[r['dominant_task']] for r in audit_rows if r['subject']==s),15))
    for y,(name,counts,den) in enumerate(series):
        left=0
        for cat in CATS:
            v=100*counts[cat]/den
            ax.barh(y,v,left=left,color=PALETTE[cat],height=.6,edgecolor='white',linewidth=.5)
            if v>=9:ax.text(left+v/2,y,f'{v:.0f}%',ha='center',va='center',fontsize=8.5,color='white' if cat in ['Concept','Numerical','Visual/data'] else INK)
            left+=v
    ax.set_yticks(range(len(series)),[x[0].replace(' / PYQ','') if not audit else x[0] for x in series]);ax.invert_yaxis()
    ax.set_xlim(0,100);ax.set_xlabel('Share of questions (%)');ax.set_xticks([0,25,50,75,100])
    handles=[plt.Rectangle((0,0),1,1,color=PALETTE[c]) for c in CATS]
    ax.legend(handles,CATS,ncol=3,loc='upper center',bbox_to_anchor=(.46,-.17),frameon=False,fontsize=8.5)
    fig.tight_layout();return finish(fig,'audit_style' if audit else 'styles')

def difficulty_chart(audit=False):
    if audit:
        fig,ax=plt.subplots(figsize=(7,3.1));y=np.arange(4);width=.24
        for j,(kind,color) in enumerate([('stored_difficulty',GRAY),('review_difficulty',BLUE)]):
            hard=[sum(r[kind]=='hard' for r in audit_rows if r['subject']==s) for s in 'BCMP']
            ax.bar(y+(j-.5)*width,hard,width,color=color,label='Stored hard' if j==0 else 'Audit-proposed hard')
        ax.set_xticks(y,SUBJECTS.values());ax.set_ylim(0,4);ax.set_yticks(range(5));ax.set_ylabel('Hard questions out of 15');ax.legend(frameon=False,fontsize=9)
    else:
        fig,ax=plt.subplots(figsize=(7,3.0));years=metrics['years'];bottom=np.zeros(len(years))
        for tier,color in [('easy','#c6cbd0'),('medium',BLUE),('hard',ORANGE)]:
            vals=np.array([metrics['by_year'][str(y)]['tiers'].get(tier,0)/metrics['by_year'][str(y)]['n']*100 for y in years])
            ax.bar([str(y) for y in years],vals,bottom=bottom,color=color,label=tier.capitalize(),width=.65);bottom+=vals
        ax.set_ylim(0,100);ax.set_yticks([0,25,50,75,100]);ax.set_ylabel('Editorial tier share (%)');ax.legend(ncol=3,frameon=False,loc='upper center',bbox_to_anchor=(.5,1.18),fontsize=9)
    fig.tight_layout();return finish(fig,'audit_difficulty' if audit else 'difficulty')

def coverage_chart():
    years=list(range(2017,2027));fig,ax=plt.subplots(figsize=(7,2.65))
    for j,y in enumerate(years):
        n=metrics['by_year'].get(str(y),{}).get('n')
        if n is not None:ax.bar(j,n,color=BLUE if y>=2023 else GRAY,width=.65);ax.text(j,n+1,str(n),ha='center',fontsize=9)
        else:ax.text(j,8,'Not\nrecovered',ha='center',fontsize=8.5)
    ax.set_xticks(range(10),[str(y) for y in years]);ax.set_ylim(0,70);ax.set_ylabel('English questions acquired');ax.set_yticks([0,15,30,45,60]);fig.tight_layout();return finish(fig,'coverage')

def recurrence_chart():
    labels=[];arr=[]
    for s in 'BCMP':
        top=sorted([r for r in metrics['chapter_counts'][s] if not r['code'].startswith('X')],key=lambda r:(-r['recent_n'],r['chapter']))[:5]
        for r in top:
            labels.append(s+' | '+SHORT[s][r['code']]);arr.append([sum(x['year']==y and x['subject']==s and x['chapter_code']==r['code'] for x in ledger) for y in range(2023,2027)])
    fig,ax=plt.subplots(figsize=(7,6.0));a=np.array(arr);im=ax.imshow(a,cmap='Blues',vmin=0,vmax=max(a.flatten()),aspect='auto')
    for i in range(len(labels)):
        for j in range(4):ax.text(j,i,str(a[i,j]),ha='center',va='center',color='white' if a[i,j]>=3 else INK,fontsize=9)
    ax.set_yticks(range(len(labels)),labels,fontsize=9);ax.set_xticks(range(4),range(2023,2027));ax.tick_params(length=0)
    for i in [4.5,9.5,14.5]:ax.axhline(i,color='white',lw=3)
    fig.tight_layout();return finish(fig,'recurrence')

def classes_chart():
    fig,ax=plt.subplots(figsize=(7,2.7))
    for i,s in enumerate('BCMP'):
        c=metrics['by_subject'][s]['recent_primary_classes'];n=sum(c.values());v=100*c.get('11',0)/n
        ax.barh(i,v,color=BLUE,height=.55);ax.barh(i,100-v,left=v,color='#d0d5d9',height=.55)
        ax.text(v/2,i,f"11: {c.get('11',0)}",ha='center',va='center',color='white',fontsize=9)
        ax.text(v+(100-v)/2,i,f"12: {c.get('12',0)}",ha='center',va='center',fontsize=9)
    ax.set_yticks(range(4),SUBJECTS.values());ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xticks([0,25,50,75,100]);ax.set_xlabel('Approximate primary-class share (%)');fig.tight_layout();return finish(fig,'classes')

for font,file in [('Body','DejaVuSans.ttf'),('BodyB','DejaVuSans-Bold.ttf'),('Title','DejaVuSerif.ttf')]:
    pdfmetrics.registerFont(TTFont(font,'/usr/share/fonts/truetype/dejavu/'+file))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyB',italic='Body',boldItalic='BodyB')
W,H=A4;M=45;CW=W-2*M
BASE_STYLE=ParagraphStyle('body',fontName='Body',fontSize=10.4,leading=15,textColor=colors.HexColor(INK),spaceAfter=7)

class Report:
    def __init__(self,name,label,total):
        self.path=OUT/name;self.c=canvas.Canvas(str(self.path),pagesize=A4)
        self.c.setTitle(label);self.c.setAuthor('OurMocks');self.c.setSubject('Source-backed IAT study and review; 29 October 2026')
        self.label=label;self.total=total;self.page=0;self.y=0
    def start(self,title,sub=''):
        if self.page:self.c.showPage()
        self.page+=1;c=self.c
        c.setFillColor(colors.HexColor('#53616b'));c.setFont('Body',8)
        c.drawString(M,H-27,'OURMOCKS  /  '+self.label.upper())
        c.setStrokeColor(colors.HexColor('#a5adb3'));c.setLineWidth(.5);c.line(M,H-35,W-M,H-35)
        c.setFillColor(colors.HexColor(INK));c.setFont('Title',20)
        self.y=H-66
        self.para(title,size=20,leading=25,font='Title',after=10)
        if sub:self.para(sub,size=9.2,leading=13,color='#52616b',after=13)
        c.setFont('Body',8);c.setFillColor(colors.HexColor('#53616b'))
        c.drawString(M,22,'29 October 2026  |  OurMocks research notes')
        c.drawRightString(W-M,22,f'{self.page} / {self.total}')
    def para(self,text,size=10.4,leading=15,font='Body',after=7,color=INK):
        style=ParagraphStyle('local',parent=BASE_STYLE,fontName=font,fontSize=size,leading=leading,textColor=colors.HexColor(color))
        p=Paragraph(text,style);_,h=p.wrap(CW,1000)
        if self.y-h<43:raise ValueError(f'Page overflow: {self.label} p{self.page}: {text[:70]} at {self.y:.0f}, height {h:.0f}')
        p.drawOn(self.c,M,self.y-h);self.y-=h+after
    def heading(self,text):self.para(text,size=12,leading=17,font='BodyB',after=6)
    def bullet(self,text):self.para('• '+text,after=5)
    def chart(self,p,height):
        from PIL import Image
        im=Image.open(p);w,h=im.size;scale=min(CW/w,height/h);dw=w*scale;dh=h*scale
        if self.y-dh<43:raise ValueError(f'Chart overflow {self.label} p{self.page}')
        self.c.drawImage(str(p),M+(CW-dw)/2,self.y-dh,dw,dh,mask='auto');self.y-=dh+8
    def note(self,text):self.para(text,size=8.4,leading=11.7,color='#52616b',after=9)
    def table(self,headers,rows,widths=None,size=9.2,leading=12.6):
        sty=ParagraphStyle('cell',parent=BASE_STYLE,fontSize=size,leading=leading)
        hdr=ParagraphStyle('header',parent=sty,fontName='BodyB')
        vals=[[Paragraph(escape(str(x)),hdr) for x in headers]]+[[Paragraph(escape(str(x)),sty) for x in row] for row in rows]
        t=Table(vals,colWidths=widths or [CW/len(headers)]*len(headers),hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#edf0f2')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,0),(-1,0),.65,colors.HexColor('#8a959d')),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor('#ccd2d6'))]))
        _,h=t.wrap(CW,1000)
        if self.y-h<43:raise ValueError(f'Table overflow {self.label} p{self.page}: {h:.0f} at {self.y:.0f}')
        t.drawOn(self.c,M,self.y-h);self.y-=h+12
    def end(self):
        assert self.page==self.total,(self.label,self.page,self.total)
        self.c.save()

def source_note(s):
    den=metrics['by_subject'][s]['recent_current_n']
    extra=' Bracketed counts [ ] show all acquired years for that family.' if s!='B' else ''
    return f'Source: manual PYQ chapter ledger [S2]. Recent = 2023–2026. Shares use {den} current-scope questions in {SUBJECTS[s]}; each question has one primary chapter.'+extra

def all_count_table(s,codes=None):
    rows=[r for r in metrics['chapter_counts'][s] if not r['code'].startswith('X') and (codes is None or r['code'] in codes)]
    return [[SHORT[s][r['code']],r['all_n'],r['recent_n']] for r in rows]

def make_student():
    r=Report('IAT_PYQ_Analysis_Student_Guide.pdf','IAT PYQ analysis',14)
    r.start('What IAT papers ask you to do','A visual guide for Class 12 students | Nine acquired English papers, 2017–2026')
    r.para('The main lesson is to prepare for <b>reasoning across all four sciences</b>. Repeated topics deserve extra practice, but a chapter with fewer recent questions is still part of your syllabus.')
    r.heading('Four findings to use in your preparation')
    for t in [
      '<b>Biology:</b> genetics/evolution and human physiology account for 22 of the 58 recent current-scope questions. Practise mechanisms, crosses and observations, not only definitions.',
      '<b>Chemistry:</b> bonding, organic principles, coordination and carbonyl/carboxyl chemistry together account for 23 of 55 recent current-scope questions. Connect structures with reactions and reasons.',
      '<b>Mathematics:</b> coordinate geometry, differentiation and integration each contribute 6 of 59 recent current-scope questions. Questions also test domains, cases and branch choices.',
      '<b>Physics:</b> field/potential reasoning and work/energy lead this sample. Choosing a model, reading a graph and keeping signs correct often matter before arithmetic.'
    ]:r.bullet(t)
    r.heading('How to read the numbers')
    r.para('A weightage is a share of the questions we counted. For example, 12 genetics questions out of 58 recent Biology questions gives 20.7%. It does <b>not</b> promise that the next paper will repeat this share.')
    r.table(['Where to go','What you will find'],[
      ['Pages 2–3','The papers included, exam pattern and scoring'],['Pages 4–8','Every retained chapter family, shown subject by subject'],['Pages 9–12','Repeated areas, question styles, difficulty and syllabus changes'],['Pages 13–14','Study priorities, an error log and sources']],widths=[90,CW-90])
    r.note('The verified exam rules here are for 2026. This report supports 2027 preparation, but does not claim a verified 2027 notification. Sources and limits are listed on page 14.')

    r.start('Which papers are included?','Count the evidence before treating a pattern as reliable.')
    r.chart(coverage_chart(),220)
    r.note('English question counts from the acquired archive [S1–S2]. Grey bars are older papers; blue bars are the recent comparison window. No bar is drawn for the unrecovered 2020 paper.')
    r.table(['Set','Questions','Why it matters'],[
      ['All acquired English papers','539','Nine papers; useful for breadth and style'],['Recent papers: 2023–2026','239','Closer to the retained syllabus; four papers only'],['Recent, current-scope families','231','58 Biology + 55 Chemistry + 59 Maths + 59 Physics']],widths=[195,65,CW-260])
    r.heading('Three gaps to remember')
    r.bullet('The acquired 2025 English copy has 59 labelled questions, ending at Physics Q14. We did not invent a replacement.')
    r.bullet('The 2026 source is a provisional answer-key document. Its first-option answer convention is not evidence about live-exam answer letters.')
    r.bullet('Hindi copies support access but are not counted again. Mirror sources and OCR errors are recorded; check the original page if a formula looks wrong.')

    r.start('Know the pattern and count marks correctly','Verified IAT 2026 rules [S3]. Recheck the target-year notification before the exam.')
    r.table(['Rule','What it means'],[
      ['60 single-correct MCQs','15 each in Biology, Chemistry, Mathematics and Physics'],['180 minutes','An overall average of 3 minutes per question; individual items can take less or more'],['+4 / -1 / 0','Correct / incorrect / unanswered'],['240 maximum marks','All four subjects contribute; there is no best-three rule'],['Calculator','On-screen non-programmable scientific calculator; personal calculators are not allowed']],widths=[155,CW-155],size=10)
    r.heading('A simple score example')
    r.para('Suppose you get <b>35 correct, 15 wrong and leave 10 unanswered</b>. Your score is (35 × 4) - (15 × 1) = <b>125 out of 240</b>. This is an illustration, not a result measured from the PYQs.')
    r.heading('Use the time for decisions, not just calculations')
    r.bullet('Start with questions where you can identify a method. A long stem is not automatically hard, and a short stem is not automatically easy.')
    r.bullet('For a graph, read both axes and signs. For a reaction, track each functional group. For a probability, check what information is already given.')
    r.bullet('If you cannot see a productive next step, mark the question for a later pass. Return with time to check units, cases and option wording.')
    r.note('No score-to-rank estimate, cut-off forecast or fixed attempt target is justified by this chapter-count study. Actual scores depend on the paper and the candidate group.')

    r.start('Biology: genetics and physiology recur','Current-scope recent sample: 58 questions. Broad units are not all the same size.')
    r.chart(chapter_chart('B'),270);r.note(source_note('B'))
    r.table(['Family','All years','Recent'],all_count_table('B'),widths=[CW-140,75,65],size=9.2,leading=11.6)
    r.para('<b>Practise:</b> inheritance probabilities, cell processes, hormone effects and experimental controls. In a cross, distinguish a gamete frequency from an offspring probability.',size=9.7,leading=13)

    r.start('Chemistry: connect structure, reason and reaction','Current-scope recent sample: 55 questions. The chart lists all 19 retained families.')
    r.chart(chapter_chart('C'),390);r.note(source_note('C'))
    r.para('<b>The main cluster:</b> bonding 7; organic principles 6; coordination 5; carbonyl/carboxyl chemistry 5. These are 23 of 55 questions, or 41.8%. Other families together still contribute 58.2%.')
    r.para('<b>Practise:</b> interpreting molecular structures, comparing reagents and using equilibrium before a calculation. Physical chemistry remains important even when its questions are split across several chapters.')
    r.note('All-year / recent counts for the remaining detail are preserved in the companion chapter-count appendix [S2]. Historical topics such as solid state and surface chemistry are not silently included in this current-scope chart.')

    r.start('Mathematics: calculus, functions and geometry','Current-scope recent sample: 59 questions. A single method will not cover this range.')
    r.chart(chapter_chart('M'),375);r.note(source_note('M'))
    r.para('<b>Three joint leaders:</b> coordinate geometry, differentiation and integration have 6 questions each. Together they contribute 18 of 59 questions (30.5%); the rest of the syllabus contributes the other 69.5%.')
    r.para('<b>Practise:</b> domain restrictions, principal values, symmetry, root location and exact counting. In calculus, decide whether a transformation or a graph can simplify the problem before expanding algebra.')
    r.note('Limits, functions and probability span material taught across both school years. A chapter-family label is not a precise item-by-item Class 11/12 classification.')

    p11=[c for c,v in taxonomy['P'].items() if v[1]==11 and not c.startswith('X')]
    p12=[c for c,v in taxonomy['P'].items() if v[1]==12 and not c.startswith('X')]
    r.start('Physics: mechanics, heat and waves','Part 1 of 2 | Same denominator as the next page: 59 recent current-scope Physics questions.')
    r.chart(chapter_chart('P',p11),310);r.note(source_note('P'))
    r.para('<b>What repeats:</b> work/energy has 5 questions, oscillations 4, and rotation, thermodynamics and waves 3 each. Energy conservation and force reasoning also appear as secondary tools in other chapters.')
    r.heading('Do not confuse a zero with an excluded chapter')
    r.para('No recent question was assigned primarily to Laws of Motion in this four-paper window. That does not remove Newton’s laws from the syllabus or mean they were never used inside another problem.')
    r.para('<b>Practise:</b> drawing a force model, choosing a conservation law, distinguishing distance from displacement and linking an equation to a graph.')

    r.start('Physics: electricity, optics and modern topics','Part 2 of 2 | The shares on both Physics pages add to 100%, apart from rounding.')
    r.chart(chapter_chart('P',p12),310);r.note(source_note('P'))
    r.para('<b>What repeats:</b> electric field/potential reasoning has 6 questions; ray optics 4; induction 3. Atoms, nuclei, matter waves and electronics appear across the window even when each has a smaller count.')
    r.heading('Treat figures as data')
    r.para('In a circuit, identify which nodes are connected before using a formula. In optics, check the medium, viewing direction and approximation. For a field graph, the sign of an area can decide whether kinetic energy rises or falls.')
    r.note('Electric field/potential and capacitance/potential are separate primary families in this taxonomy. Each question is placed in only one, so their displayed counts do not double-count items.')

    r.start('A frequent topic can still vary by year','Five leading families per subject, selected by recent count; ties use alphabetical chapter order.')
    r.chart(recurrence_chart(),425)
    r.note('Each cell is an actual primary-topic count in that year [S2]. B/C/M/P mean Biology/Chemistry/Mathematics/Physics. The 2025 Physics source has 14 questions. Zero means no acquired item was tagged to that family that year.')
    r.para('Read across a row to see repetition and gaps. A chapter can lead the four-year total without being equally common every year. The dark cells show concentration in this sample, not a higher probability for next year.')
    r.para('<b>Preparation rule:</b> revisit recurring families, then rotate through the remaining syllabus. Do not try to turn a four-year heatmap into an exact next-paper forecast.')

    r.start('IAT asks for more than recall','Dominant task = the main kind of thinking needed. One question receives one task label.')
    r.chart(mix_chart(),250)
    r.note('Recent unfiltered window: B/C/M n=60 each; P n=59. Visual/data combines diagrams/structures, graphs and tables. These task categories include scope-review items; chapter charts use filtered denominators.')
    r.table(['Subject','What the pattern suggests'],[
      ['Biology','Compare explanations, interpret a cross or experiment, and use data to test a mechanism.'],['Chemistry','Read structures as well as words. A formula typed in a stem is not automatically a structure-reading task.'],['Mathematics','Work through cases and constraints, not only routine substitution. The numerical/concept boundary is editorial.'],['Physics','Model the situation and read figures, then calculate with signs and units.']],widths=[95,CW-95],size=9.7,leading=13)
    r.para('<b>Figure task totals:</b> 23/60 Biology, 25/60 Chemistry, 1/60 Mathematics and 20/59 Physics. These include tables and molecular structures, not just separate image files.',size=9.6,leading=13)

    r.start('Difficulty is an estimate, not a measured result','The labels below are editorial judgements about steps and reasoning, not student success rates.')
    r.chart(difficulty_chart(),245)
    r.note('All nine acquired papers; the 2025 denominator is 59. The years are separate categories: the missing 2020 paper is not interpolated. Source: manual difficulty tags [S2].')
    r.table(['Recent window','Easy','Medium','Hard'],[[SUBJECTS[s]]+[metrics['by_subject'][s]['recent_tiers'].get(t,0) for t in ['easy','medium','hard']] for s in 'BCMP'],widths=[CW-195,65,65,65])
    r.para('Physics has more hard tags under this rubric. That is a signal to practise modelling and longer reasoning, not evidence that a future paper must be harder or that a particular score will earn a rank.')
    r.table(['Working label','A useful way to recognise it'],[['Easy','One familiar idea and a short route'],['Medium','Linked ideas, cases or two to three substantive steps'],['Hard','Integration, a less obvious route or a longer derivation']],widths=[95,CW-95],size=9.5,leading=12.4)
    r.note('The mock-series target of 9 easy / 39 medium / 12 hard is an OurMocks design rule. It is not an official IAT quota or a fit to every paper.')

    r.start('Prepare both school years; check the current syllabus','The Class 11/12 split below is approximate because labels are assigned at family level.')
    r.chart(classes_chart(),220)
    r.note('Recent, unfiltered questions. Numbers inside bars are counts. Some Maths families span both years, so do not use these bars as exact chapter quotas. Source: taxonomy-derived primary-class tags [S2].')
    r.heading('Old papers are valuable, but old scope can differ')
    r.para('Across all years, <b>22 questions</b> are flagged as historical or needing scope review. Eight of these are in the recent window, all in 2023. The chapter charts exclude those recent review flags.')
    r.table(['Subject','Examples that need scope checking'],[
      ['Biology','Transport/mineral nutrition, digestion and environmental issues; some nitrogen-fixation content can overlap retained microbes topics.'],['Chemistry','Detailed p-block, gases, solid state, polymers, metallurgy and surface chemistry.'],['Mathematics','Mathematical induction; linear programming is named only in an umbrella heading in the stored syllabus.'],['Physics','Logic gates and Zener-diode detail.']],widths=[95,CW-95],size=9.5,leading=12.8)
    r.para('<b>Use the latest official list:</b> a question appearing in an old paper is not enough to prove it belongs in the target-year mock. Conversely, a low recent count does not exclude a listed topic.')

    r.start('Turn the patterns into a study plan','These are preparation priorities, not predicted questions or guaranteed chapter counts.')
    r.table(['Subject','Revisit often','Keep in rotation'],[
      ['Biology','Genetics, cells, human physiology, biotechnology','Diversity, structural biology, plants, reproduction, ecology, welfare'],['Chemistry','Bonding, organic principles, coordination, carbonyl chemistry','All physical families plus retained inorganic and organic chapters'],['Mathematics','Calculus, functions, coordinate geometry, matrices, probability','Counting, binomial, sequences, complex numbers, vectors, 3D, statistics, trigonometry'],['Physics','Energy, electrostatics, oscillations, optics','Remaining mechanics, thermal, electricity, magnetism and modern topics']],widths=[75,190,CW-265],size=9.7,leading=13.4)
    r.heading('A repeatable practice cycle')
    r.bullet('<b>Learn:</b> revise the NCERT idea and the conditions under which it applies.')
    r.bullet('<b>Apply:</b> solve a mix of conceptual, numerical and visual questions without looking at the explanation first.')
    r.bullet('<b>Review:</b> write down whether the error came from a concept, representation, calculation, assumption or time decision.')
    r.bullet('<b>Return:</b> solve a different problem on the same idea after a gap; do not rely on remembering the option letter.')
    r.para('During mock review, explain why the other three options fail. If you guessed correctly, still record the missing reasoning. A correct mark can hide a weak method.')
    r.note('No reliable probability forecast, cut-off or rank model is built here. Such claims would need cleaner complete data, independent tagging and testing on unseen papers.')

    r.start('Keep an error log and know the sources','Use the evidence to guide practice, not to narrow your preparation to a few chapters.')
    r.table(['Question / topic','What went wrong?','What I will change'],[['Example: field graph','Used unsigned area','Write the field sign before integration'],['________________','________________','________________'],['________________','________________','________________']],widths=[150,165,CW-315],size=9.4)
    r.heading('Small glossary')
    r.para('<b>PYQ:</b> previous-year question. <b>Weightage:</b> counted share of a defined set. <b>n:</b> number of questions. <b>Primary chapter:</b> the one main family assigned to an item. <b>Editorial difficulty:</b> a reviewer’s estimate, not a measured pass rate.',size=9.8,leading=14)
    r.heading('Sources and reproducibility')
    r.para('[S1] Acquired reference collection: PYQ/IAT/manifest.json and SOURCES.md. Stored PDFs are labelled mirror copies; original pages remain authoritative when OCR is unclear.',size=9.3,leading=13)
    r.para('[S2] Manual ledger, tags, taxonomy and metrics in docs/blueprints/iat_pyq_*.json / .txt; complete all-year and recent chapter counts in iat_pyq_chapter_counts.md. Counts are reproducible with tools/iat/analyse_pyq.py. Chapter labels, styles and tiers can be reviewed and changed transparently.',size=9.3,leading=13)
    r.para('[S3] Official 2026 exam page: <link href="https://www.iiseradmission.in/pages/admission/iat.html" color="#315d7d">iiseradmission.in/pages/admission/iat.html</link>. Official Information Brochure: <link href="https://app.iiseradmission.in/assets/pdfs/IB_IAT_2026_ENG.pdf" color="#315d7d">app.iiseradmission.in/assets/pdfs/IB_IAT_2026_ENG.pdf</link>, sections 19 and 23; checked 29 October 2026. Rules are paraphrased, not reproduced as an official document.',size=9.1,leading=13)
    r.para('[S4] Stored official syllabus: IISER/IISER_Aptitude_Test_Syllabus_2026.md, extracted from the accompanying PDF. No 2027 brochure is verified in this report.',size=9.3,leading=13)
    r.note('Prepared with AI assistance from the project’s evidence. Human review is appropriate for item-level chapter and difficulty judgements. Figures show counted data, not invented trends or student-performance statistics.')
    r.end();return r.path

def stem_words(q):
    text=re.sub(r'\\\([\s\S]*?\\\)',' formula ',q['question'])
    return len(re.findall(r'[A-Za-z]+',text))

def length_chart():
    fig,ax=plt.subplots(figsize=(7,2.5))
    values=[[stem_words(q) for q in questions if q['section']==s] for s in 'BCMP']
    b=ax.boxplot(values,tick_labels=SUBJECTS.values(),patch_artist=True,widths=.45,
       medianprops={'color':INK,'linewidth':1.6},flierprops={'marker':'o','markerfacecolor':'white','markeredgecolor':GRAY})
    for p in b['boxes']:p.set(facecolor='#d5e0e7',edgecolor=BLUE)
    ax.set_ylabel('Prose words in the stem');ax.set_ylim(bottom=0);ax.grid(axis='y',color='#e3e5e7',lw=.6);fig.tight_layout();return finish(fig,'audit_reading')

def image_pair(r,n1,n2):
    details={
     9:('Thylakoid gradient','pH 5 in the lumen, pH 8 outside, and an outward catalytic head are consistent with transient ATP synthesis. There is no proton-flow arrow revealing the answer.','Useful setup sketch. The two pH values and sidedness could be stated compactly in text; the sketch aids orientation rather than adding a new measured observation.'),
     11:('Restriction-digest gel','The 900/600/300 bp bands match complete digestion of the heterozygous product. Band positions and sizes are legible. The caption explicitly says intensity is not to scale.','Genuine band-reading task. The equal-looking drawn bands must not be read as equal fluorescence. Keep the mass-proportionality assumption and non-quantitative-intensity caption.'),
     46:('Velocity-time graph','Straight segments pass through (0,0), (2,4), (4,-4) and (6,0), so the central zero crossing is 3 s. Units and ticks are present; no area is shaded as an answer.','Essential to the intended graph-reading skill. Signed areas cancel; absolute area gives 12 m, hence average speed 2 m/s and average velocity zero.'),
     53:('Electric-field graph','The field goes from zero to -E0 at a, then remains -E0 to 2a. The horizontal zero line and negative sign are correct. No stopping coordinate is marked.','Essential to the intended area-reading skill. Work to a is -qE0a/2; the remaining 3qE0a/4 stops the charge at 7a/4, inside the drawn region.'),
     54:('Connected resistor bridge','Supply polarity is top-positive; left resistors are 2/4 ohm, right resistors 3/3 ohm. Dots identify junctions A/B and the ideal meter connects them. The 12 V label no longer overlaps a resistor value.','Essential topology diagram. The meter makes the midpoint potentials equal, but permits current. Connected-node KCL confirms 12/17 A from A to B, not zero.'),
     57:('Two parallel liquid layers','The upper layer is 6 cm at index 3/2; the lower layer is 4 cm at index 4/3; air is above and the coin is at the bottom. Dimension arrows delimit the correct layers.','Useful setup sketch. The same data fit in two short text lines. No ray or virtual-image marker gives away the 7 cm apparent depth or its order invariance.')
    }
    for n in [n1,n2]:
        title,accuracy,purpose=details[n]
        r.heading(f'Q{n}: {title}')
        r.chart(ROOT/f'IISER/images/IAT_T01_Q{n:02}.png',216)
        r.para('<b>Accuracy:</b> '+accuracy,size=9.7,leading=13.4,after=6)
        r.para('<b>Purpose:</b> '+purpose,size=9.7,leading=13.4,after=10)

def make_audit():
    r=Report('IAT_Test_1_Full_Audit.pdf','Test 1 audit',19)
    r.start('A usable pilot, but not yet a final PYQ-matched mock','Decision: revise before student release | Audit of the unchanged Test 1 snapshot')
    r.para('The paper meets its formal structure and has relevant, scientifically consistent diagrams. The main weaknesses are <b>style balance, difficulty calibration and a few weak distractors</b>. No definite wrong key was found under the stated assumptions in this review; that is not independent academic certification.')
    r.table(['Parameter','Finding','Decision'],[
      ['Exam structure','60 questions; 15 per subject; 180 minutes; +4/-1/0','Pass for 2026 scheme'],
      ['Syllabus mapping','All 60 map to retained families; combined subtopics need editorial sign-off','Broad fit; review detail'],
      ['Chapter balance','Maths has 0 coordinate geometry versus 6/59 recent items','Revise'],
      ['Question style','Chemistry is 9/15 numerical; PYQ coding is 12/60','Revise'],
      ['Difficulty','Stored 9/39/12; this review suggests 18/32/10','Recalibrate content'],
      ['Images','All six match their questions; four representation tasks, two setup sketches','Relevant; none clearly random'],
      ['Keys and solutions','45 arithmetic probes pass; 60 explanations inspected','Pass checks; human review pending'],
      ['Release readiness','No timed student trial or verified 2027 brochure','Not established']],widths=[105,270,CW-375],size=9.3,leading=12.7)
    r.para('<b>What to keep:</b> strong linked reasoning in B13, C20, M40/M44 and P49/P54/P60; fixed IDs; separate solutions; exact graph and circuit drawing.',size=9.7,leading=13.8)
    r.note('This is an AI-assisted self-audit by the assistant that authored the pilot, not an independent examiner’s certification. Difficulty and distractor quality are reasoned judgements; counts and checks are separately labelled.')

    r.start('What was compared, and against which standard?','Three different tests: official structure, project design rules and observed PYQ characteristics.')
    r.table(['Benchmark','Evidence','How it is used'],[
      ['Official 2026 rules','Brochure sections 19/23 and official exam page','Counts, marking, time and calculator policy'],
      ['OurMocks blueprint','Stored 2026 syllabus, fixed-order rule, 9/39/12 design mix','Internal authoring standard; not an official quota'],
      ['Observed PYQ sample','539 items overall; recent 239; recent current-scope 231','Chapter, style and editorial difficulty comparisons'],
      ['Current pilot','60 JSON items, six PNGs, 49-page review PDF','Item-level and image-level checks']],widths=[125,175,CW-300],size=9.5,leading=13)
    r.heading('How to interpret the comparisons')
    r.bullet('Chapter reference counts are recent current-scope shares multiplied by 15. They can be fractional because they are a reference average, not a rule for one paper.')
    r.bullet('Question-style comparisons use the same mutually exclusive dominant-task categories. The pilot was manually recoded, rather than treating its broad JSON format labels as equivalent.')
    r.bullet('The audit proposes tiers from the reasoning actually left after the stem supplies its facts. These labels are not candidate pass rates and have not been validated by a student trial.')
    r.heading('Snapshot identity')
    r.para('Canonical file: IISER/IAT TEST 1.json<br/>Test ID: IAT27_TEST_01<br/>SHA-256: '+sha(PAPER),size=9.0,leading=13)
    r.note('The audit does not rewrite, shuffle or renumber Test 1. Sources: repository ledger, taxonomy, plan, validator results, arithmetic probe results and render-check checksums. Full references and release actions appear on page 19.')

    chapter_findings={
     'B':('Biology covers all ten broad units','All ten retained Biology families appear. Genetics has 3 questions; cell, human physiology and structure have 2 each; other units have 1. This is broad coverage, not proof that each large unit is covered deeply.',
          'Recent-share references would put human physiology near 2.6 and genetics near 3.1 questions. Test 1 has 2 and 3. Structural organisation has 2 versus about 1.3; this is a modest one-paper variation. The bigger issue is that several Biology questions are easier than their labels.'),
     'C':('Chemistry needs more variety in representation','Fourteen of 19 retained primary families appear. Carbonyl chemistry has 2 questions; every other selected family has 1. Atomic structure, d/f-block, hydrocarbons, halo compounds and alcohols/phenols/ethers have no primary slot.',
          'Omitting five families in a 15-item section is not automatically a failure. However, organic principles are important in recent PYQs, and the adjacent Q24/Q25 ketone-to-alcohol chirality contexts narrow the range of organic thinking. Add structural interpretation by replacing or strengthening content at stable IDs.'),
     'M':('Mathematics omits a recent leading family','Fourteen of 17 primary families appear. Integration has 2 questions. Coordinate geometry, binomial theorem and sequences/series have no primary slot. Vectors and 3D geometry do not replace the missing plane-coordinate/conics family.',
          'Coordinate geometry has 6/59 recent current-scope items, tied with differentiation and integration. Replace an existing repeated or lower-priority slot with an original coordinate/conic problem at the same ID. The absence is a sample-balance concern, not a violation of an official chapter quota.'),
     'P':('Physics is broad, with clear rotating omissions','Fifteen of 26 primary families appear, each once. Seven Class 11 and eight Class 12 primary topics are represented. A 15-item section cannot exhaust 26 families.',
          'Work/energy, capacitance, magnetism, gravitation, thermal properties, kinetic theory, matter waves and atoms lack primary slots, among others. Energy reasoning is still used in Q49/Q53/Q59. Count these as secondary connections, not full primary-chapter coverage. Retain a series-wide rotation.')
    }
    for s in 'BCMP':
        title,p1,p2=chapter_findings[s];r.start(title,f'{SUBJECTS[s]} | Filled bars: Test 1. Open bars: recent current-scope share × 15.')
        r.chart(chapter_chart(s,audit=True),360 if s in 'CM' else 300 if s=='B' else 395)
        r.note('Denominator: '+str(metrics['by_subject'][s]['recent_current_n'])+' recent current-scope questions. Fractional references are not prescribed quotas. Each item counts once by its primary family.')
        r.para(p1,size=10,leading=14)
        r.para(p2,size=10,leading=14)

    r.start('The style gap is larger than the chapter-count gap','Manual recoding uses the same task definitions as the recent PYQ ledger.')
    r.chart(mix_chart(audit=True),310)
    r.note('PYQ denominators: 60/60/60/59 in B/C/M/P, including scope-review items. Test 1: 15 each. Visual/data combines structures, diagrams, graphs and tables; it is not an image-file count.')
    r.table(['Comparison','PYQ recent','Test 1','Audit implication'],[
      ['Chemistry numerical','12/60 (20.0%)','9/15 (60.0%)','Add structure/reagent interpretation; do not only add decorative PNGs'],
      ['Maths numerical','37/60 (61.7%)','14/15 (93.3%)','Add conceptual domain/case/geometry reasoning'],
      ['Biology visual/data','23/60 (38.3%)','2/15 (13.3%)','Use a real table, pedigree or labelled biological observation'],
      ['Physics visual/data','20/59 (33.9%)','4/15 (26.7%)','Broadly closer; keep the meaningful graphs and circuit']],widths=[115,90,90,CW-295],size=9,leading=12.1)
    r.note('The categories are editorial. Q24 is coded as structure reasoning, while its JSON format is conceptual. Printed chemical formulae alone are not automatically counted as visual tasks.')

    r.start('Difficulty labels currently overstate some items','Stored labels pass the project count rule; the content does not yet justify every label.')
    r.chart(difficulty_chart(audit=True),200)
    r.table(['Set','Easy','Medium','Hard'],[
      ['Stored Test 1',9,39,12],['Audit proposal',18,32,10],['Recent PYQ tags, n=239',35,146,58]],widths=[CW-180,60,60,60],size=9.5)
    r.para('<b>Medium to easy:</b> Q5, Q8, Q12, Q14, Q21, Q27, Q29, Q51 and Q52. Their stems either directly supply the mechanism or leave a short familiar calculation.',size=9.8,leading=13.5)
    r.para('<b>Hard to medium:</b> Q4 and Q33. Q4 can use the supplied ab frequency directly; Q33 is elimination followed by completing the square. Both are useful questions, but the hard labels are debatable.',size=9.8,leading=13.5)
    r.para('Do not simply change labels and claim compliance. If the fixed 9/39/12 mix is required, strengthen the affected content or replace selected items, solve them again and recheck the mix. The proposed 18/32/10 split is a review judgement, not a measured outcome.',size=9.8,leading=13.5)

    r.start('Readability, distractors and avoidable cues','Long wording can explain assumptions, but should not substitute for reasoning difficulty.')
    r.chart(length_chart(),200)
    r.note('Prose-word counts replace each delimited formula by one placeholder and count alphabetic words; mathematical reading time is not measured. Each box summarises 15 stems: middle line = median, box = middle half, points = outlying counts.')
    r.para('<b>Option-length cue:</b> among 15 prose-heavy questions with no delimited mathematics in any option and at least one 8-word option, the correct choice is uniquely longest in <b>8</b>: Q3, Q8, Q9, Q10, Q12, Q14, Q16 and Q25. This is a screening signal, not proof that a student can infer answers from length.',size=9.8,leading=13.5)
    r.table(['Item','What weakens it','What to improve'],[
      ['Q12','The binding assay explicitly states the defect that the answer repeats','Ask students to distinguish competing evidence patterns'],
      ['Q14','Photosynthetic frog skin and a four-chambered heart are implausible alternatives','Use credible errors about ventilation and diffusion'],
      ['Q21 / Q29','The relevant reaction rules or quantitative response are supplied','Leave a real chemical identification step'],
      ['Q27','1.90 g is unnecessary once pure final carbonate mass is given','Require mixture inference, or classify it as easy']],widths=[65,215,CW-280],size=9.3,leading=12.6)
    r.note('Keep useful assumptions in Q4/Q11/Q20/Q49/Q60. Removing necessary controls merely to shorten stems would create ambiguity.')

    r.start('Are the six images random?','No: each is tied to the question data or physical setup. Their cognitive roles differ.')
    r.table(['Q','Correct content checked','Purpose','Verdict'],[
      [9,'pH values, membrane and ATP-synthase sidedness','Orient a chemiosmotic setup','Relevant setup sketch'],
      [11,'900/600/300 bp bands and non-quantitative intensity','Read the observed digest pattern','Genuine representation task'],
      [46,'Exact v–t points, zero crossing, axes and units','Read signed versus absolute area','Genuine graph task'],
      [53,'Negative field, break at a and constant segment','Read work from a field graph','Genuine graph task'],
      [54,'Rail polarity, four resistors, junctions and meter','Understand connected topology','Genuine circuit task'],
      [57,'Two depths, two indices, coin and viewing medium','Organise the layered setup','Relevant setup sketch']],widths=[28,200,160,CW-388],size=9.3,leading=12.7)
    r.heading('Two different questions about necessity')
    r.para('<b>If the image and its alt text disappear, does the current stem lose data?</b> Yes for all six: the pH values, observed bands, graph shape, resistor topology or layer values are not fully repeated in the main stem.')
    r.para('<b>Does the diagram itself test a representation skill?</b> Most clearly Q11/Q46/Q53/Q54. Q9/Q57 are helpful setup sketches whose data could be stated in one or two short sentences. They are relevant, but should not be counted as equivalent to a demanding graph-reading problem.')
    r.note('All six filenames match stable question IDs; all have alt text and register entries. No generated decorative illustration, answer-revealing result annotation or scientific mismatch was found. Detailed reproductions follow on pages 11–13.')

    r.start('Biology figures: correct, with a key reading limit','Reproductions from the unchanged pilot PNG files; the report adds no new question data.')
    image_pair(r,9,11)
    r.start('Graphs: the shape is part of the problem','Axes, signs and key coordinates were checked against the stems and solutions.')
    image_pair(r,46,53)
    r.start('Circuit and optics: keep the setup precise','The circuit carries topology; the layered diagram organises values that could also be stated in text.')
    image_pair(r,54,57)

    r.start('Keys and worked solutions: what the checks establish','No definite wrong key found in this review; checks are conditional on stated idealisations.')
    r.table(['Item','Re-derived result','Main reasoning checked'],[
      ['B13','1/18','(2/3) family carrier × (1/3) unaffected population carrier × (1/4)'],
      ['C20','0.74 V','Copper concentration 10^-12 M, then Nernst with n=2'],
      ['C24','C8H14O2; 4 isomers','Reduction adds H2; acylation adds C2H2O; two centres, no terminal E/Z'],
      ['M40','3/16','Choose two fixed points and derange the other four'],
      ['M44','1/4','Split at sqrt(a); optimise at a=1/4 and compare endpoints'],
      ['P49','4ω/3; work = mR²ω²/2','Conserve angular momentum, not kinetic energy'],
      ['P54','12/17 A, A to B','Connected-node KCL; midpoint potential 120/17 V'],
      ['P60','3 micrometres','Smallest shared odd half-wave path is 1500 nm']],widths=[45,145,CW-190],size=9.3,leading=12.6)
    r.heading('Measured checks versus academic judgement')
    r.para('The validator finds 60 four-option items, key/explanation agreement, no duplicate normalised stems and no identical option texts within an item. Keys total 15 A, 15 B, 15 C and 15 D; no letter runs more than three times. The 45 computational probes pass, and all 328 delimited expressions render.',size=9.8,leading=13.5)
    r.para('These do not prove semantic originality, optimal distractors, exact NCERT scope or real student timing. For example, Q26 should state initially equal hydrostatic pressures; Q56 should explicitly say the bar spans the rails perpendicular to them. Both stored results are consistent with the standard intended setup.',size=9.8,leading=13.5)
    r.note('The 49-page review PDF matches its source/diagram checksums and contains 60 question headings and 60 solution headings. This audit does not reproduce every full solution; those remain in the pilot review PDF.')

    for s in 'BCMP':
        r.start(SUBJECTS[s]+': all 15 items reviewed','E/M/H below are the audit’s proposed tiers. Keys shown are the stored answers, not a revised answer key.')
        rows=[a for a in audit_rows if a['subject']==s]
        r.table(['Q','Key','Tier','Finding / action'],[[a['question'],a['key'],a['review_difficulty'][0].upper(),a['note']] for a in rows],widths=[28,36,34,CW-98],size=9.05,leading=12.2)
        counts=Counter(a['review_difficulty'] for a in rows)
        r.note(f"Proposed tier count: {counts['easy']} easy / {counts['medium']} medium / {counts['hard']} hard. 'Keep' means no specific correction was identified here; it does not replace human academic sign-off. Primary families are shown in the chapter comparison, pages 3–6.")

    r.start('What must happen before release?','Keep the same IDs and image links. This report audits the draft; it does not silently revise it.')
    r.table(['Priority','Concrete action','Completion evidence'],[
      ['1. Content calibration','Strengthen the nine medium-to-easy items; review hard labels Q4/Q33','Fresh solutions and a justified 9/39/12 split, if that policy is retained'],
      ['2. Maths coverage','Use an existing slot, such as one repeated integration slot, for coordinate/conic reasoning','Coordinate family represented without expanding past 60'],
      ['3. Style and distractors','Add real structure/table interpretation; address Q12/Q14/Q21/Q27/Q29 and Q24/Q25 overlap','Reasoning survives option elimination; no decorative image quota'],
      ['4. Setup clarity','Add initial-pressure condition to Q26 and bar orientation to Q56','One clear intended model per question'],
      ['5. Human trial','Obtain subject review plus a timed student attempt','Recorded correctness, ambiguity, timing and difficulty feedback'],
      ['6. Target-year rules','Verify the 2027 syllabus and brochure before claiming compliance','Official source and date recorded']],widths=[90,235,CW-325],size=9.1,leading=12.4)
    r.heading('Sources and limitations')
    r.para('Official 2026 sources: <link href="https://www.iiseradmission.in/pages/admission/iat.html" color="#315d7d">IAT examination page</link> and <link href="https://app.iiseradmission.in/assets/pdfs/IB_IAT_2026_ENG.pdf" color="#315d7d">Information Brochure, sections 19/23</link>, rechecked 29 October 2026. Project sources: canonical JSON, six PNGs, stored syllabus, 60-slot plan, PYQ ledger/metrics, validator, arithmetic and render reports.',size=8.9,leading=12.3)
    r.para('PYQ limits: no recovered 2020 paper; 2025 English has 59 questions; 2026 is a provisional reordered key. Difficulty/style labels are editorial. No score/rank, causal trend, forecast accuracy or measured discrimination is established.',size=8.9,leading=12.3)
    r.note('Audit calculations and all 60 item comments are saved in output/iat_reports/IAT_Test_1_Audit_Data.json. The audited source hash is on page 2. Final verdict: structurally sound pilot; revise for PYQ-style realism, then obtain human release approval.')
    r.end();return r.path

if __name__=='__main__':
    student=make_student()
    audit=make_audit()
    assert before=={str(p.relative_to(ROOT)):sha(p) for p in tracked},'Audited test was modified'
    report={'audited_files_sha256':before,'test_unchanged':True,'items':audit_rows,
            'stored_tiers':dict(Counter(q['difficulty'] for q in questions)),
            'review_tiers':dict(Counter(a['review_difficulty'] for a in audit_rows)),
            'outputs':[str(p.relative_to(ROOT)) for p in [student,audit]],
            'method_note':'AI-assisted self-audit; chapter and task tags and proposed tiers are editorial. Reference counts are recent current-scope shares × 15, not quotas.'}
    (ROOT/'output/iat_reports/IAT_Test_1_Audit_Data.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'pdfs':[str(student),str(audit)],'proposed_tiers':report['review_tiers'],'test_unchanged':True},indent=2))
