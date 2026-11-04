"""Recompute selected changed answers from transcribed inputs, without reading keys to solve.

These author-side probes supplement, and never replace, hidden-key subject review.
"""
import hashlib,itertools,json,math
from pathlib import Path
from fractions import Fraction as F
import sympy as s
R=Path(__file__).resolve().parents[2]
papers={t: R/('IISER/IAT TEST 1.json' if t==1 else f'IISER/IAT NEW TEST {t}.json') for t in range(1,16)}
data={t:json.loads(p.read_text()) for t,p in papers.items()};rows=[]
def check(t,n,value,expected,selected,method):
 q=data[t]['questions'][n-1];option=q['options']['ABCD'.index(q['correct_option'])][3:]
 values=value if isinstance(value,tuple) else (value,)
 targets=expected if isinstance(expected,tuple) else (expected,)
 passed=len(values)==len(targets) and all(s.simplify(s.sympify(a)-s.sympify(b))==0 for a,b in zip(values,targets)) and option==selected
 rows.append(dict(id=q['id'],calculated=str(value),expected=str(expected),selected_option=option,method=method,passed=passed))
x,k=s.symbols('x k',real=True)
check(3,43,s.sqrt(F(125,5)-4**2),3,'3','Population variance = sum(x²)/5 minus mean²; sum(x²)=125, mean=4.')
check(4,12,(F(4,9)*F(3,4))/(1-F(4,9)*F(1,4))*F(1,4),F(3,32),'3/32','Bayes update on an unaffected first child, before next-child recessive risk.')
seq=[a for a in itertools.product('HT',repeat=6) if a.count('H')==3]
check(4,38,F(sum(sum(a[i:i+2]==('H','H') for i in range(5))==1 for a in seq),len(seq)),F(3,5),'3/5','Exhaust all 20 equally likely toss sequences conditional on three heads; count exactly one adjacent HH.')
check(4,55,s.sqrt((F(1,2)*F(50,10**6)*100**2-F(1,2)*2*F(4,10)**2)*2/F(50,10**6)),60,'60 V','Lossless LC: subtract inductor energy from initial capacitor energy.')
check(5,21,F(15-10,1000)*44,F(22,100),'0.22 g','First 10 mmol H+ converts carbonate to bicarbonate; remaining 5 mmol releases CO2.')
check(5,28,(F(2*4825,2*96500)*F(635,10),F(2*4825,2*96500)),(F(3175,1000),F(5,100)),'3.175 g and 0.050 mol','Faraday charge/(2F) gives both Cu deposition and Cl2 evolution.')
check(6,41,F(7,1+F(1,2)+F(1,4))/(1-F(1,2)),8,'8','Adjacent three-term block ratio is r³=1/8; recover first term and geometric sum.')
check(7,13,(F(12,6),F(12*100,6*50)),(2,4),'2 and 4','Cardiac output ratio, then multiply by arterial-venous oxygen difference.')
check(7,34,s.integrate(-x,(x,-1,0))+s.integrate(x,(x,0,1)),1,'1','Split absolute-value integral at zero.')
check(8,25,s.sqrt(s.Rational(1,10**10)*10**8),F(1,10),'0.10 M','Ksp with dominant Ag(NH3)2+ and fixed free NH3=1 M: s²=beta*Ksp.')
check(8,34,2+2*min(3*2,3*1,2*1),6,'6','Initial equivalence classes sizes 3,2,1; 2 missing reverse pairs then merge cheapest two classes.')
check(9,21,F(176,100)/44*100/10,F(2,5),'0.40','CO2 moles equal CaCO3 moles; recover carbonate mass and divide by initial 10 g.')
check(9,38,s.Rational(sum(abs(a-1) for a in [1,1,4]),3),1,'1','Median is 1; average absolute distance from median, not mean.')
y=x*s.sqrt(1+2*s.log(x))
assert s.simplify(s.diff(y,x)-(x*x+y*y)/(x*y))==0 and y.subs(x,1)==1
check(9,42,y.subs(x,s.E),s.E*s.sqrt(3),'e√3','Verify solution by substitution into original ODE and initial value, then evaluate at e.')
check(9,44,F((2*2)*(2*3),2),12,'12','Positive intercept constraint 2/a+3/b=1; AM-GM gives minimizing intercepts a=4,b=6.')
check(9,60,1-(1-F(1,2))**2,F(3,4),r'\(3MI_0/(4R)\)','Integrated induced charge uses M*(Iinitial-Ifinal)/R; final current is I0/4.')
check(10,32,s.solve(s.Eq(4/s.sqrt(1+k*k),2),k)[1],s.sqrt(3),'±√3','Length of origin chord in x²+y²=4x equals 4/sqrt(1+k²); both signs have this magnitude.')
check(10,38,s.binomial(6,4)*2**4,240,'240','Recover n=6 from binomial ratio, then evaluate coefficient of x^4.')
check(10,39,sum(n*n for n in range(1,11)),385,'385','Telescoping odd increments yields a_n=n²; independently sum first ten squares.')
check(10,52,F(3,4)-F(1,2),F(1,4),r'\(GMm/(4r)\); bound','Fixed-radius kinetic-energy increase; final total energy = 3/4-1=-1/4 GMm/r, hence bound.')
check(10,57,(F(100**2*30,30**2+40**2),F(100**2*30,30**2+10**2)),(120,300),'120 W; 300 W','Real power V²R/(R²+X²) before and after added capacitive reactance -30 ohm.')
t=s.symbols('t',positive=True);xp=t*t+1;yp=t**3-3*t
check(11,32,(yp.subs(t,1),s.simplify(s.diff(s.diff(yp,t)/s.diff(xp,t),t)/s.diff(xp,t)).subs(t,1)),(-2,F(3,2)),r'\(y=-2;\ 3/2\)','Parametric first and second derivatives, evaluated at horizontal tangent t=1.')
check(11,38,sum(j*j*s.binomial(6,j) for j in range(7)),672,'672','Explicit enumeration of weighted binomial sum, independent of derivative identity.')
check(11,45,s.asin(F(1,2))+s.acos(-F(1,2)),5*s.pi/6,'5π/6','Use principal ranges for inverse sine and cosine.')
check(11,47,max(s.solve(50*x*x+2*x-14,x),key=lambda v:float(v)),(-1+s.sqrt(701))/50,'50x²+2x=14, x≈0.51 m','Positive energy root; friction consumes 2x and spring stores 50x² of initial 14 J.')
check(11,52,(1/F(1,2)**2*F(1,2)-1,2),(1,2),'1; 2mg','Pendulum period squared ratio = length ratio times g/(g+a); then support force m(g+a).')
check(11,59,(F(200-150,100),F(100,150)),(F(1,2),F(2,3)),'1/2; 2/3','Direct branch gives one photon, cascade two; photon energy sums to 100 E42.')
check(12,11,F(1,4)-F(39,100)**2,F(979,10000),'979/10000','Intercross: P(aa)-P(aabb), with coupling gamete ab frequency 0.39.')
check(12,25,-s.log(s.sqrt(s.Rational(1,10**14)/s.Rational(1,10**5)*s.Rational(1,10)),10),5,'5','Weak conjugate acid Ka=Kw/Kb and [H+]=sqrt(Ka*C).')
check(12,32,sum(sum(n%d==0 for d in [2,3,5])==2 for n in range(1,121)),28,'28','Enumerate integers 1..120 satisfying exactly two divisibility conditions.')
check(12,43,((2**2-3)/2,F(2**2,4)),(F(1,2),1),r'\(1/2\le k\le1\)','Root sum=2, sum squares=4-2k<=3; real roots require k<=1 and positivity holds.')
check(12,49,((2**2*(2-1))/(1**2*(3-1)),2*2**2),(2,8),'2 and 8','Stokes terminal speed scales r²(rho_s-rho_f); drag power scales r*v².')
check(12,54,(F(1,2)-1-(-1),-1),(F(1,2),-1),r'\(+U/2;\ -U\)','Battery-fixed V: final field U/2, battery work -U, external work = delta U - Wbattery.')
check(13,21,F(2,3)*(30-5),F(50,3),r'\(50/3\) mL','After steam condenses, 5 mL O2 remains; reacted H2:O2 volume ratio is 2:1.')
check(13,34,s.integrate(x*s.exp(x),(x,0,1)),1,'1','Independent symbolic integration by parts check.')
check(13,37,(F(1,10)*F(8,10)*F(2,10))/(F(1,10)*F(8,10)*F(2,10)+F(9,10)*F(1,10)*F(9,10)),F(16,97),'16/97','Bayes over conditionally independent positive-then-negative observations.')
check(13,39,F(10*(1+512),2)-sum(2**j for j in range(10)),1542,'1542','Ten-term AP and GP with identical endpoints 1,512; subtract finite sums.')
check(13,44,s.integrate(x*s.log(x)-(x-1),(x,1,s.E)),(4*s.E-s.E**2-1)/4,r'\((4e-e^2-1)/4\)','Solve y/x=ln x and integrate above tangent x-1 on [1,e]; convexity proves ordering.')
check(13,57,1/(F(1,20)-F(1,60)),30,'30 cm on the object side','First lens image 60 cm meets mirror plane; return object for lens is 60 cm on incident side.')
check(13,58,F(2*4,4**2+1),F(8,17),'8/17','Initial contrast implies amplitude ratio2; quarter weaker intensity doubles ratio to4; visibility 2r/(1+r²).')
check(14,10,F((600*F(1,2)+300*F(2,3))*F(8,10)-250,6000),F(1,40),'1/40','NPP=6000; prey productions600,300; predator production from consumed500 gives150.')
check(14,15,F(3,4)*4**s.Rational(1,4),3*s.sqrt(2)/4,r'\(3\sqrt2/4\)','Fit z=1/4 from doubling over 16x area; apply 0.75 habitat coefficient and 4x area.')
check(14,26,2*(1-F(1,F(3,2))),F(2,3),'2/3','For dimerisation i=1-alpha/2; measured apparent/true mass=1/i=1.5.')
check(14,27,F(4,F(3,2)),F(8,3),'8/3 mol','Combined S+1.5 O2 -> SO3 limited by 4 mol O2; 3 mol S is excess.')
check(14,35,s.sqrt(s.exp(s.log(3))+1),2,r'\(2;\ \mathbb R\)','Solve e^y=x²-1 on x>1: positive inverse; logarithm covers all real y.')
check(14,37,tuple(s.solve(s.Eq(2*x/(x*x-1),1),x)),(1-s.sqrt(2),1+s.sqrt(2)),r'\(1\pm\sqrt2\)','Trace of inverse 2t/(t²-1)=1; both roots avoid singular ±1.')
check(14,41,sum(3**j for j in range(5)),121,'121','Positive GP product27 fixes middle3; sum13 gives increasing ratio3; finite five-term sum.')
check(14,48,s.sqrt(s.Rational(2*(4+4+4),2)),2*s.sqrt(3),'2√3 m s⁻¹','Integrate force graph: triangle4+rectangle4 J, add initial kinetic4 J, mass2 kg.')
check(14,60,(900-100)*F(1,2)**3*F(1,2)+100,150,'150 counts min⁻¹','Subtract electronic background; infer 4 h half-life, decay12h, halve source only, restore background.')
check(15,7,F(2*3,16)/F(15,16),F(2,5),'2/5','Enumerate independent 3:1 dominant phenotypes; condition removes only double recessive.')
check(15,28,-F(1000,2)*3/F(1,100)/1000-F(249,100),-F(15249,100),'−152.5 kJ mol⁻¹','Bomb heat capacity500 J/K gives delta U=-150 kJ/mol; subtract RT=2.49 kJ/mol and round to one decimal.')
yy=s.sqrt(5);tx,ty=s.symbols('tx ty')
meet=s.solve([-2*(tx-1)+yy*(ty-yy),-2*(tx-1)-yy*(ty+yy)],[tx,ty])
check(15,31,abs(meet[tx]),F(3,2),'3/2','Tangents to circle (x-3)^2+y²=9 at x=1,y=±sqrt5; solve intersection equations.')
check(15,40,(2+1,F(3,1)/s.sqrt(6)),(3,s.sqrt(6)/2),r'\(3;\ \sqrt6/2\)','Parallel direction normal-dot-product2-k+1=0; point-to-plane distance3/sqrt6.')
check(15,42,(-F(5,3),s.sqrt(F(25,9)-1)),(-F(5,3),F(4,3)),r'\((-5/3,0);\ 4/3\)','Expand distance-ratio equation and complete the square for centre and radius.')
check(15,43,((1+F(2,1))/2,(F(2,3)+3)/2),(F(3,2),F(11,6)),r'\((3/2,11/6)\)','Positive root product2; if other root in (2,3), smaller root is in (2/3,1); evaluate monotone parameter endpoints.')
check(15,45,sum(4+3*j for j in [1,2,3]),30,'30','Five-term AP from4 to16 has difference3; inserted terms7,10,13.')
check(15,50,((800*F(2,5)+800*F(3,5)*F(1,3)-40)/800*100,800*F(3,5)*F(2,3)),(55,320),'55%; 320 J','Cascade heat engine balances; subtract parasitic40 J from total work, keep final rejected heat320 J.')
check(15,55,900-(300*F(1,4)+600*F(1,2)),525,'525','Equal activities give parent counts300:600 for half-lives2:4 h; after4 h parents375 remain.')
check(15,60,(F(1,2),F(3,4)*2/F(1,2)),(F(1,2),3),r'\(\beta/2;\ 3\lambda\)','Double slit separation halves fringe width; sheet shift 3/4 old beta gives path1.5 lambda and thickness3 lambda.')
out=R/'IISER/review/milestone15_fixes/arithmetic_checks.json'
out.write_text(json.dumps(dict(scope='Author-side recomputation of transcribed changed-item inputs; not independent academic approval.',source_sha256={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in papers.values()},checks=rows,passed=sum(r['passed'] for r in rows),total=len(rows)),indent=2)+'\n')
print(f"{sum(r['passed'] for r in rows)}/{len(rows)} passed")
for row in rows:
 if not row['passed']:print(row)
assert all(r['passed'] for r in rows)
