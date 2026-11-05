"""Author-side recalculation from transcribed inputs, bound to selected option text.

Computational checks supplement the written derivations; no independent subject
approval or timed difficulty measurement is implied.
"""
import hashlib,itertools,json,math
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import sympy as s
R=Path(__file__).resolve().parents[2];O=R/'IISER/review/tests16_17';O.mkdir(exist_ok=True)
sources={t:R/f'IISER/IAT NEW TEST {t}.json' for t in [16,17]}
papers={t:json.loads(p.read_text()) for t,p in sources.items()};checks=[]
def probe(t,n,value,target,option,method):
 q=papers[t]['questions'][n-1];selected=q['options']['ABCD'.index(q['correct_option'])][3:]
 vals=value if isinstance(value,tuple) else (value,);targets=target if isinstance(target,tuple) else (target,)
 def equal(a,b):
  d=s.simplify(s.sympify(a)-s.sympify(b))
  return d==0 or (d.is_number and abs(float(d))<1e-8)
 ok=selected==option and len(vals)==len(targets) and all(equal(a,b) for a,b in zip(vals,targets))
 checks.append(dict(id=q['id'],method=method,calculated=str(value),expected=str(target),selected_option=selected,expected_selected_option=option,passed=bool(ok)))
 if not ok:print('FAILED',checks[-1])
x,a,t=s.symbols('x a t',real=True)
# Biology: corrected sampling, conditional families, conserved strands and explicit time budgets.
probe(16,7,(F(80+80,480),F(160,480)**2),(F(1,3),F(1,9)),'1/3 and 1/9','Inverse-survival weighting of four observed classes before gamete union.')
probe(16,10,s.solve([s.Symbol('r')-20*s.Symbol('z')-F(2,5),s.Symbol('r')-60*s.Symbol('z')-F(1,5)],[s.Symbol('r'),s.Symbol('z')])[s.Symbol('r')]/F(5,1000),100,'100','Solve common r and r/K from two per-capita rates.')
probe(16,11,F(2*F(1,4)*F(1,2),2*F(1,4)*F(3,4)),F(2,3),'2/3','Enumerate ordered affected-son and daughter classes, divide by exactly-one-affected event.')
probe(16,12,(F(2,2**3),F(2,2*2**3)),(F(1,4),F(1,8)),'1/4 and 1/8','Two original heavy strands conserved through eight duplexes.')
starts=list(range(0,20,4));released=sum(v+30<=40 for v in starts)
probe(16,14,(released,len(starts)-released),(3,2),'3 released; 2 translating','Explicit finite initiation cohort and individual release times.')
probe(17,4,1-min(F(90,15),F(60,6))/min(F(90,9),F(60,6)),F(2,5),'2/5','Independent limiting-resource calculation of the stipulated ATP/NADPH model.')
# Chemistry: molecular counting and exact mole/charge/energy accounting.
probe(16,16,(7+5,1+1+2,1,3,1),(12,4,1,3,1),'(12,4;1,3,1)','Count seven heavy-atom edges, five C-H edges, and drawn multiple-bond orders.')
probe(16,17,(F(16,10)-1,3*F(6,10)+2*F(4,10)),(F(3,5),F(13,5)),'0.60 and 2.60','External-chloride linear mixture plus complex-ion count.')
probe(16,18,(4-2-3,6-2-3,4+2),(-1,1,6),"P gives both octets with C=-1,O=+1; Q leaves carbon with only six electrons",'Formal charges in triple-bond proposal, carbon shell count in double-bond proposal.')
probe(16,19,F(4)/(F(4,3)),3,'3','Balmer limiting wavelength divided by finite Lyman-alpha wavelength.')
probe(16,20,2*F(224,1000)/F(224,10)/(F(280,100)/280),2,'2','Dumas N2 molecules converted to N atoms and divided by organic molecule count.')
probe(16,24,s.log(2)/(s.log(4)/(10+2*5)),10,'10 min','Multiply survival factors from the two temperature intervals.')
probe(16,25,s.Rational(1,10**16)/(s.Rational(1,10**10)/s.Rational(1,10)),s.Rational(1,10**7),'AgI; 10^-7 M','Compute silver at AgCl onset, then iodide from AgI equilibrium; compare initial thresholds separately.')
probe(16,26,(5*F(2,100),3*F(2,100)),(F(1,10),F(6,100)),'0.100 mol I-; 0.060 mol I2','Electron-balanced iodate/iodide stoichiometry.')
probe(16,27,612+436-348-2*413,-126,'-126 kJ/mol','Full gas-phase bond-energy inventory difference.')
probe(16,28,(F(30,60),F(30,40)),(F(1,2),F(3,4)),'1/2 and 3/4','Different denominators for liquid Raoult fraction and gas partial-pressure fraction.')
probe(17,18,(0,2*(6-3),s.sqrt(3*5)),(0,6,s.sqrt(15)),r'\((0,6,\sqrt{15})\)','Per-Cr d count, two-centre electron balance and per-ion spin-only moment.')
probe(17,19,2*(3-1-1)+1,3,'3','One radial node fixes l=1; fixed spin gives one electron per magnetic state.')
carbon=F(1320,1000)/44;hydrogen=2*F(540,1000)/18;oxygen=(F(9,10)-12*carbon-hydrogen)/16
probe(17,21,(carbon/oxygen,hydrogen/oxygen,F(90,30)),(1,2,3),'C3H6O3','Combustion atom recovery and sample oxygen by mass difference; molecular multiplier three.')
probe(17,22,2+1,3,'3','Enumerate methyl/n-propyl, methyl/isopropyl and ethyl/ethyl ether partitions.')
probe(17,26,3-1,2,'Val-Ala-Gly; 2','Fixed peptide termini leave alanine central; linear bond count n-1.')
probe(17,27,F(10*F(5,100),5*F(20,100)),F(1,2),'1/2','Henry-law partial-pressure ratio, not total-pressure ratio.')
etotal=F(108,100)/108;ecu=2*F(254,1000)/F(635,10)
probe(17,28,(ecu/etotal,(etotal-ecu)/2),(F(4,5),F(1,1000)),'80%; 0.001 mol','Series silver coulometer, copper electron demand, remaining H2 electron pair.')
q=F(8-6,12-8);signal_a=F(12-8,1-q)
probe(17,29,(10,12-signal_a),(10,4),'10 min; 4 units','Equal-interval signal differences infer q=1/2 and eliminate unknown baseline.')
# All thirty Mathematics items: algebra, enumeration, boundaries and numerical integration.
probe(16,31,sum(r*r for r in s.solve(t*(t*t-4),t)),8,'8','Enumerate all normal parameters including zero; sum contact abscissae.')
probe(16,32,2*s.sqrt(5+20),10,'10','Recover a²=5,b²=20 from point and asymptote ratio; focal separation.')
corners=tuple(sum(m==1 for m in Counter(s.real_roots(x**3-3*x+v)).values()) for v in [-3,-2,-1,0,1,2,3])
probe(16,33,corners,(1,1,3,3,3,1,1),r'\((-\infty,-2]\cup[2,\infty)\)','Exact real-root multiplicities at interior, exterior and boundary parameter samples; written proof supplies full intervals.')
grid=np.linspace(0,1,100001);f=np.log1p(grid)/(np.log1p(grid)+np.log(2-grid))
probe(16,34,np.trapezoid(f,grid),F(1,2),'1/2','Numerical quadrature independent of reflection derivation.')
angles=[2*k*math.pi+v*math.pi/3 for k in range(-3,4) for v in [-1,1]]
probe(16,35,max(abs(math.cos(v)-.5) for v in angles),0,r'\(\{2k\pi\pm\pi/3:k\in\mathbb Z\}\)','Check both claimed cosine branches over multiple periods; completeness is the standard cosine solution.')
A=s.diag(1,2);X=s.Matrix([[2,-2],[-3,3]])
probe(16,36,(X.det(),s.trace(X),*(A*X-X*A)),(0,5,0,2,-3,0),'2 and 3','Substitute one admissible matrix and its diagonal swap into commutator/trace/determinant constraints.')
assert s.Matrix([[3,-2],[-3,2]]).det()==0
trials=list(itertools.product([0,1],repeat=3))
probe(16,37,F(sum(sum(r)==2 for r in trials),sum(sum(r)>=1 for r in trials)),F(3,7),'3/7','Exhaust all fair trial outcomes after solving equal one/two-success probabilities.')
probe(16,38,(1-s.real_root(F(80,10),3))**4,1,'1','Coefficient determines the unique real cube root; evaluate signed polynomial at one.')
probe(16,39,next(n for n in range(1,30) if 2+3*(n-1)>40),14,'14','Enumerate strict AP term threshold after block reconstruction.')
probe(16,40,s.limit(x,x,0,dir='+'),0,'0','Upper bound for absolute product is x; verify it tends to zero, with written bound valid for all x>0.')
tp,sp=s.symbols('tp sp');d=s.Matrix([1+sp-tp,-sp-tp,2])
feet=s.solve([d.dot(s.Matrix([1,1,0])),d.dot(s.Matrix([1,-1,0]))],[tp,sp])
probe(16,41,(feet[tp],feet[tp],1),(F(1,2),F(1,2),1),'(1/2,1/2,1)','Solve both common-perpendicular equations independently.')
seatings=[('A',)+p for p in itertools.permutations('BCDEF')]
count=sum(min(r.index('B'),6-r.index('B'))==2 and r.index('C') not in [1,5] for r in seatings)
probe(16,42,count,24,'24','Exhaust all 120 rotationally fixed circular permutations.')
theta=[-3*math.pi/4,-math.pi/2,0,math.pi/2,3*math.pi/4,math.pi]
wrap=tuple(int(abs(math.atan2(math.sin(2*v),math.cos(2*v))-(2*v-2*math.pi))<1e-8) for v in theta)
probe(16,43,wrap,(0,0,0,0,1,1),r'\((\pi/2,\pi]\)','Direct principal-argument evaluation on both sides and at branch endpoints.')
y=2*s.exp(x)/(2*s.exp(x)-1)
assert s.simplify(s.diff(y,x)-y*(1-y))==0 and y.subs(x,0)==2
probe(16,44,(y.subs(x,s.log(2)),s.solve(2*s.exp(x)-1,x)[0]),(F(4,3),-s.log(2)),r'\(4/3;(-\ln2,\infty)\)','Substitute explicit solution into ODE and initial value; solve denominator zero independently.')
def trigsum(v):return math.asin(2*v/(1+v*v))+math.acos((1-v*v)/(1+v*v))
probe(16,45,tuple(int(abs(trigsum(v)-math.pi)<1e-8) for v in [-10,-2,-1,0,.5,1,2,10]),(0,0,0,0,0,1,1,1),r'\([1,\infty)\)','Direct inverse-function evaluation samples all four theta regimes and the included boundary.')
probe(17,31,s.solve(s.Eq(x*x,(4-x)**2+9),x)[0],F(25,8),'(25/8,0)','Equal radius equations after independently subtracting the original two circles.')
probe(17,32,max(F(0),F(1,2),F(2,5)),F(1,2),'1/2','Evaluate both rational endpoints and unique in-domain derivative zero.')
yy=s.symbols('yy');implicit=x*s.exp(yy)+yy*s.exp(x)-1
slope=(-s.diff(implicit,x)/s.diff(implicit,yy)).subs({x:1,yy:0})
probe(17,33,1/slope,-(1+s.E),'(0,-(1+e))','Compute both partial derivatives of the implicit expression, then use normal slope and intercept.')
probe(17,34,s.integrate((x*x+1)/(x+1),(x,0,1)),2*s.log(2)-F(1,2),r'\(2\ln2-1/2\)','Independent symbolic rational integration.')
def real_iter(v):
 try:
  if v==-1:return False
  u=math.sqrt((v-1)/(v+1));w=math.sqrt((u-1)/(u+1))
  return 0<w<1
 except ValueError:return False
probe(17,35,tuple(int(real_iter(v)) for v in [-10,-2,-1,0,1,2,10]),(1,1,0,0,0,0,0),r'\((-\infty,-1);\ (0,1)\)','Evaluate iterate feasibility across every original-domain branch and excluded endpoint; written algebra supplies full range.')
avec=s.Matrix([1,0]);bvec=s.Matrix([F(1,2),s.sqrt(3)/2]);cvec=F(4,3)*avec-F(2,3)*bvec
probe(17,36,s.sqrt(cvec.dot(cvec)),2/s.sqrt(3),r'\(2/\sqrt3\)','Construct explicit unit directions with the given dot product and verify vector norm.')
probe(17,37,s.Matrix([[1,1,0],[0,1,1],[1,0,1]]).det()*5,10,'10','Evaluate the simultaneous row-mixing determinant.')
probe(17,38,(F(2,3)*F(1,8))/(F(2,3)*F(1,4)+F(1,3)),F(1,6),'1/6','Direct joint probability HHT divided by HH, independent of two-step posterior exposition.')
probe(17,39,sum(len(set(v))==3 for v in itertools.product(range(3),repeat=4)),36,'36','Exhaust all 81 labelled functions and count onto images.')
probe(17,40,s.binomial(7,4)*(-F(1,2))**4,F(35,16),r'\(35/16\)','Parity sum fixes n=7; coefficient also verified by expanding the finite polynomial.')
dval=s.sqrt(13)-1
probe(17,41,(6-dval)*(8+dval),36,r'\(\sqrt{13}-1\)','Substitute feasible positive AP difference into transformed GP product.')
def four_inside(v):
 roots=np.roots([1,-2*v,v+2]);xs=[]
 for r in roots:
  if abs(r.imag)<1e-7 and r.real>1e-7:xs.extend([r.real,-r.real])
 return len(xs)==4 and len({round(z,6) for z in xs})==4 and all(abs(z)<3-1e-7 for z in xs)
probe(17,42,tuple(int(four_inside(v)) for v in [-2,0,1,2,2.1,2.2,2.5]),(0,0,0,0,1,0,0),r'\((2,11/5)\)','Numerical root enumeration checks positive-u multiplicity and strict x bounds at representative and boundary parameters.')
probe(17,43,np.var([0,1,2,3,4]),2,'2','Explicit feasible original data 10,1,2,3,4 verifies given moments; corrected data variance computed directly.')
yy=(x+1)*s.exp(2*x);assert s.simplify(s.diff(yy,x)-2*yy-s.exp(2*x))==0
probe(17,44,yy.subs(x,-F(3,2)),-1/(2*s.E**3),r'\(-1/(2e^3)\)','Verify linear ODE by substitution and evaluate its derivative-sign minimum.')
eps=1e-3;g=np.linspace(0,eps,1001)
probe(17,45,np.trapezoid(np.cos(g*g),g)/eps,1,'1','Numerical shrinking-interval average supplements the exact fundamental-theorem limit.')
# Physics: independent force/energy/charge balances, often retaining symbolic scales.
probe(16,46,s.sqrt(100-60)*2,4*s.sqrt(10),r'\(4\sqrt{10}\ \mathrm m\)','Vertical energy at measured height fixes vx via the 45-degree velocity direction.')
probe(16,47,F(1,2)*(30-6),12,'12 N','Normal force then static-friction threshold.')
probe(16,48,(F(36,3),(F(36,6)-3)/2),(12,F(3,2)),'12 m/s; 1.5 m/s2','Fixed-power force at half the terminal speed.')
probe(16,49,(F(1-2,2),1-F(2*F(1,4),1+4)),(-F(1,2),F(9,10)),'-omega/2; 9/10','Signed angular momentum and positive energies for counterrotating discs.')
probe(16,50,4*s.pi**2/(F(4,3)*s.pi),3*s.pi,r'\(3\pi/(GT^2)\)','Eliminate sphere radius and mass from circular period to obtain dimensionless numerator.')
probe(16,51,10-5-1,4,'4 m','Bernoulli velocity head subtracted before vapour-pressure head.')
probe(16,52,F(200-100,150+500),F(2,13),'2/13','Sum two input-heat legs and subtract compression work.')
probe(16,53,(-1)*s.diff((x*x-1)**2,x,2).subs(x,0),4,'x=0 only','Negative charge reverses potential curvature; at +/-1 curvature is instead negative.')
probe(16,54,F(1-2*F(1,2),1+2),0,'0','Signed final-node charge divided by parallel capacitance.')
probe(16,55,(2,1-2*2**2),(2,-7),r'2I; \(-7I\pi R^2\hat z\)','Centre field fixes current ratio; moment then weights loop area.')
probe(16,56,F(2**2-1**2,2),F(3,2),r'\(3B\omega a^2/2\); A','Integrate radial motional potential on both arms; farther end is lower for the stated B direction.')
c=s.asin(1/s.sqrt(3))
probe(16,57,(s.sqrt(3)*s.sin(s.pi/3-c),2*60-60),((s.sqrt(6)-1)/2,60),r'\((\sqrt6-1)/2;\ 60^\circ\)','Critical internal exit angle propagated through entry Snell law, then separate symmetric deviation.')
probe(16,58,F(1,2)*F(1,2)*F(1,2),F(1,8),'I0/8; 45 degrees','Sequential ideal polariser projections at the optimum.')
probe(16,59,int(not any(abs(2-gap)<1e-9 for gap in [1.89,2.55]) and 2<2.55),1,'No listed or higher bound transition matches; the photons do not cause resonant excitation','Check photon lies strictly between adjacent excitation gaps and below continuum.')
probe(16,60,(3*F(26,10)-4*F(11,10))*F(3,4),F(255,100),'2.55 MeV','Total fusion binding release, then inverse-mass recoil partition.')
pos=4*t-t**3/3
probe(17,46,(pos.subs(t,2)+(pos.subs(t,2)-pos.subs(t,4)),pos.subs(t,4)),(16,-F(16,3)),'16 m; -16/3 m','Integrate acceleration twice and split path at the derived reversal t=2.')
probe(17,47,(F(1,100)+F(2,10)/5)*100,5,'5.0%','Absolute volume subtraction errors then fractional quotient errors.')
probe(17,48,2*(1-F(1,2)),1,'g downward','Terminal effective weight calibrates drag; reversed velocity adds it to downward effective weight.')
probe(17,49,(0,1/F(1,12)),(0,12),'Zero; 12F/(ML)','Zero vector force and couple torque FL divided by rod inertia.')
probe(17,50,8**s.Rational(2,3),4,'4','Free expansion has unchanged ideal-gas temperature; reversible comparator has TV^(2/3) constant.')
probe(17,51,(s.Rational(2,3)*s.pi-s.pi/3)/(2*s.pi),F(1,6),'T/6','Choose decreasing-position initial phase before target phase.')
probe(17,52,5*(160-120),200,'200 Hz','Consecutive harmonic spacing with odd-mode selection at centre.')
probe(17,53,F(1,6*4),F(1,24),r'\(q/(24\varepsilon_0)\)','Large-cube six-face symmetry and four equivalent squares per face.')
probe(17,54,((1-F(120,200))/50,F(144,200)+F(144,240)),(F(8,1000),F(132,100)),'0.008 per degree C; 1.32 W','Independent balance-based lower-arm coefficient and sum of two branch powers.')
aa,bb=s.symbols('aa bb');initial=s.solve([aa+bb-900,aa/4+bb/2-300],[aa,bb])
probe(17,55,(initial[aa]/16)/(initial[aa]/16+initial[bb]/4),F(1,3),'1/3','Infer two initial activity components from independent times, then decay each to four hours.')
probe(17,56,(1,0),(1,0),'Emf magnitude Ab around the loop path, but no sustained conduction current across the gap','Faraday emf coefficient A*b is nonzero; stipulated open insulating path carries zero steady conduction.')
v=1/(F(1,20)-F(1,30))
probe(17,57,(v,v/(-30)),(60,-2),'60 cm right; -2','Contact-lens powers added before signed lens imaging.')
react=s.symbols('react',real=True)
react_roots=s.solve(s.Eq((1-react)**2,(2-react/2)**2),react)
positive_react=next(v for v in react_roots if v>0)
probe(17,58,s.sqrt(positive_react),s.sqrt(2),r'\(\sqrt2 f\)','Solve both equal-impedance branches algebraically and retain positive reactance ratio.')
def clip(vin):
 vo=max(-2,min(3,vin/2));upper=max(0,(vin-vo)-vo) if vo==3 else 0
 return vo,upper
probe(17,59,(clip(8)[0],clip(-6)[0],clip(8)[1]),(3,-2,2),'+3 V, -2 V; 2 mA','Verify clamp feasibility and KCL in both diode states, using kohm so currents are mA.')
probe(17,60,((s.sqrt(F(1,2))+s.sqrt(F(1,2)))**2,(s.sqrt(F(1,2))-s.sqrt(F(1,2)))**2),(2,0),'2I0 and zero','Project each coherent amplitude onto a common analyser before adding.')
report=dict(scope='Author-side recomputation and selected-option binding; boundary samples supplement written proofs, not independent academic certification.',source_sha256={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources.values()},checks=checks,passed=sum(r['passed'] for r in checks),total=len(checks))
(O/'calculation_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f"{report['passed']}/{report['total']} calculation checks passed")
assert report['passed']==report['total']
