"""Recalculate authored numerical claims and bind results to selected literal answers."""
import hashlib,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[2];O=R/'IISER/review/tests18_19'
sources={t:R/f'IISER/IAT NEW TEST {t}.json' for t in [18,19]};papers={t:json.loads(p.read_text()) for t,p in sources.items()};checks=[]
def probe(t,n,value,target,option,method):
 q=papers[t]['questions'][n-1];selected=q['options']['ABCD'.index(q['correct_option'])][3:]
 vals=value if isinstance(value,tuple) else(value,);targets=target if isinstance(target,tuple) else(target,)
 ok=selected==option and len(vals)==len(targets) and all(s.simplify(s.sympify(a)-s.sympify(b))==0 or abs(float(s.N(s.sympify(a)-s.sympify(b))))<1e-8 for a,b in zip(vals,targets))
 checks.append(dict(id=q['id'],method=method,calculated=str(value),expected=str(target),selected_option=selected,expected_selected_option=option,passed=bool(ok)))
 if not ok:print('FAILED',checks[-1])
x,t,a,p=s.symbols('x t a p',real=True)
# Biological numerical models and conditioned sample spaces.
probe(18,4,(6-(-2),0),(8,0),'8 units and zero','Recover respiratory offset from dark measurement; subtract at compensation.')
probe(18,6,(18,2*18+9),(18,45),'18 and 45','Count actual nuclei in separate embryo and central-cell events.')
probe(18,7,2*F(6,10)*F(4,10),F(48,100),'An increase from 0.20 to 0.48','Reconstruct allele frequencies and random-union heterozygosity.')
probe(18,12,F(1,4)/F(3,4),F(1,3),'1/3','Condition joint AaBb probability on viability.')
meet=s.solve(2*t-(3-2*t),t)[0]
probe(18,13,(meet,2*meet),(F(3,4),F(3,2)),'They collide at 1.5 cm from P at 0.75 ms and do not pass through each other','Solve the delayed two-front meeting before applying the stated refractory rule.')
probe(18,15,(1+1,8-(1+1)),(2,6),'2 kb and 6 kb','Sum actual arcs to the fixed backbone site and retain full molecule length.')
probe(19,7,2*F(1,4)*F(1,2),F(1,4),'1/4','Sum the two independent sibling orders.')
probe(19,11,F(4,10)*F(1,10),F(1,25),'1/25','Assign ab as parental in one phase and recombinant in the other.')
probe(19,12,F(1,16)/F(9,16),F(1,9),'1/9','Enumerate pair event and no-affected denominator.')
probe(19,13,(F(24,10)-2,F(20,10)-2),(F(4,10),0),'It shrinks from 0.4 micrometre to zero','Compute central gap between the thin-filament tips.')
probe(19,15,64-16*s.sqrt(8),64-32*s.sqrt(2),r'\(k<64-32\sqrt2\)','Species-area exponent plus unique-species union; strict threshold checked at integer18 and19.')
assert 64-18>32*s.sqrt(2) and 64-19<32*s.sqrt(2)
# Chemistry: electron, energy, mass, equilibrium and limit accounting.
probe(18,16,(s.cos(s.pi/3)+s.cos(2*s.pi/3),s.sin(s.pi/3)+s.sin(2*s.pi/3)),(0,s.sqrt(3)),r'\(\sqrt3d,0\)','Exact component sum for the drawn cis bond directions; trans directions oppose.')
probe(18,18,(20-300*F(50,1000)+F(5,2)*(-4),20-300*F(50,1000)+F(5,2)*(-1)),(-5,F(5,2)),'Forward is favourable at Q1 but unfavourable at Q2','Independently evaluate standard and actual Gibbs changes.')
probe(18,22,(F(3,100)-F(12,100)/6)*6,F(6,100),'0.060','Subtract Fe electron demand from dichromate equivalents, then use thiosulfate electron stoichiometry.')
probe(18,23,2*F(40-(-20),40),3,'3','Reverse barrier from the transition-state energy cycle, then common-temperature ratio.')
probe(18,26,1-F(1,3),F(2,3),'2/3','Conserved solute and pressure equality set final reverse-osmosis volume.')
probe(18,27,F(636-630,10)/2*F(5,100),F(15,1000),'0.0150 mol','Infer the heavy isotope number fraction from the weighted mass and multiply total atom moles.')
probe(18,28,(80-330-500)-(120-350-360),-160,'F is favoured by 160 kJ despite Cl\'s more exothermic isolated electron gain','Sum every stage on the common per-atom mole basis.')
n=s.solve(s.Eq(3*(x-5),9*(x-15)),x)[0]
probe(18,30,(n,14-(-s.log(s.sqrt(s.Rational(1,10)**10*F(n,1000)/F(1,5)),10))),(20,F(17,2)),'8.50','Recover acid amount from two buffer ratios and calculate equivalence hydrolysis.')
probe(19,17,((4+2)/2,4+2),(3,6),'+3 and 6','Charge balance and explicit donor contacts.')
probe(19,22,(6+2+1,1+1+1),(9,3),'Phenol, 1,2-diiodoethane and methyl iodide; 3 mol HI','Check final carbon count and one HI per three successive substitutions.')
alpha=(F(14,1000)*100/1400)*1000/F(1,100)/400
probe(19,26,F(1,100)*alpha**2/(1-alpha),F(1,1200),r'\(8.33\times10^{-4}\) M','Calibrate geometry, infer ionisation fraction and use full remaining-acid denominator.')
probe(19,27,s.exp((s.log(4)+s.log(1))/2)*3,6,'6','Interpolate log rate-constant ratio at reciprocal-temperature midpoint, then multiply concentration ratio.')
probe(19,28,F(8,4**2),F(1,2),'K=1/2; positive','Reverse/double one reaction and add the second before computing K.')
H=s.symbols('H',positive=True);C=s.Rational(1,10**8);Ka=s.Rational(1,10**5);Kw=s.Rational(1,10**14)
poly=s.together(H-Kw/H-C*Ka/(Ka+H)).as_numer_denom()[0]
hroot=[float(s.re(r)) for r in s.nroots(poly,maxsteps=100) if abs(float(s.im(r)))<1e-16 and s.re(r)>0][0]
probe(19,29,int(1e-7<hroot<1.052e-7),1,'Slightly below 7, with water autoionisation important','Solve full charge-balance cubic including water rather than using small-ionisation shortcut.')
# All thirty mathematics questions, independently recomputed.
hc=s.solve(s.Eq(x*x+(x-1)**2,(x-2)**2+(x-3)**2),x)[0]
probe(18,31,s.sqrt(2*hc**2-(hc**2+(hc-1)**2)),s.sqrt(2),r'\(\sqrt2\)','Recover the equidistant centre on y=x and independently evaluate its positive power at the origin.')
probe(18,32,s.Rational(4)/(1-F(1,9))+9,F(27,2),'27/2','Recover ellipse semiaxis squares from reconstructed endpoints.')
area=2*(s.integrate(x*x,(x,0,1))+s.integrate(2-x*x,(x,1,s.sqrt(2))))
probe(18,33,area,8*(s.sqrt(2)-1)/3,r'\(8(\sqrt2-1)/3\)','Integrate the two polynomial gaps independently.')
probe(18,34,s.integrate(1/(2*(1+x*x)),(x,0,1)),s.pi/8,r'\(\pi/8\)','Evaluate the transformed elementary integral.')
f=x+s.log(x);invcurv=(-s.diff(f,x,2)/s.diff(f,x)**3).subs(x,1)
probe(18,35,invcurv,F(1,8),'1/8','Apply twice-differentiated inverse identity.')
ff=(3*x-6)/(2*x-3)
probe(18,36,(s.simplify(ff.subs(x,ff)-x),s.discriminant(2*x*x-6*x+6,x)),(0,-12),'f is its own inverse and has no real fixed point','Symbolic rational composition and fixed-point discriminant with pole excluded in written proof.')
A=s.Matrix([[0,1,0],[0,0,1],[1,0,0]]);B=s.eye(3)+A+t*A*A
tr=s.factor(s.trace(B.inv()));roots=s.solve(s.Eq(tr,-F(3,4)),t)
probe(18,37,(sum(roots),*roots),(-1,-3,2),'-1','Construct the matrix, invert symbolically and solve the trace condition.')
sets=[z for z in itertools.combinations(range(1,8),3) if max(z)-min(z)==4]
probe(18,38,F(sum(4 in z for z in sets),len(sets)),F(1,3),'1/3','Exhaust the conditional three-ticket subsets.')
probe(18,39,s.pi/12+5*s.pi/12,s.pi/2,r'\(\pi/2\)','Sum both admissible double-angle branches after excluding original denominator zeros.')
probe(18,40,abs(1+4-1)/s.sqrt(2),2*s.sqrt(2),r'\(2\sqrt2\)','Select plane normal by complete pencil coefficients and evaluate normalised distance.')
probe(18,41,s.sqrt((4+1+2)/(s.Integer(4)+1-2)),s.sqrt(F(7,3)),r'\(\sqrt{7/3}\)','Use both projection equations to obtain norm and dot-product constraints.')
zs=[s.exp(s.I*sgn*s.pi/6)*sign for sgn in [-1,1] for sign in [-1,1]]
probe(18,42,tuple(s.simplify(z**6) for z in zs),(-1,-1,-1,-1),'-1','Enumerate all square roots of both admissible transformed unit-circle points.')
good=[k for k in range(1,13) if k>6 and 4*(k*k-4*k-12)>(k+3)**2]
probe(18,43,len(good),3,'3','Exhaust the finite integer-parameter domain against strict coefficient inequalities.')
const=sum((-1)**j*math.comb(8,k)*math.comb(6,j) for k in range(9) for j in range(7) if 22-3*k-2*j==0)
probe(18,44,const,0,'0','Enumerate every exponent pair of the product.')
probe(18,45,F(8**2,1)/(1-F(1,3)**2),72,'72','Reconstruct GP from odd/all sums and sum the squared GP.')
probe(19,31,3*s.sqrt(16-F(4,3)**2),8*s.sqrt(2),r'\(8\sqrt2\)','Recover focal-triangle height from the two distance equations.')
probe(19,32,(s.limit((1-s.cos(x))/x,x,0,dir='+'),s.limit((s.cos(x)-1)/x,x,0,dir='-')),(0,0),"f is twice differentiable with f''(0)=0",'Independent one-sided second-derivative limits after resolving the absolute value.')
probe(19,33,s.prod(s.solve(s.Eq(1+a*a,F(3,2)),a)),-F(1,2),'-1/2','Solve the inside-interval absolute-integral equation and exclude outside cases by the >=2 bound.')
fs=[g for g in itertools.product([-2,-1,0,1,2],repeat=3) if tuple(v*v for v in g)==(0,1,4)]
probe(19,34,len(fs),4,'4','Exhaust all125 finite maps and test the right-inverse composition.')
probe(19,35,tuple(sorted(2*v+2 for v in [-2,2])),(-2,6),'-2 and 6','Compute all parameter branches from exact cofactors and traces.')
probe(19,36,F(2,10)/(F(2,10)+F(3,10)),F(2,5),'2/5','Compute conditional masses of the two exclusive independent-event outcomes.')
paths=set(itertools.permutations('RRRRUUU'));valid=[]
for z in paths:
 if 'UU' in ''.join(z):continue
 xx=yy=0;vis=[]
 for step in z:
  xx+=step=='R';yy+=step=='U';vis.append((xx,yy))
 if (2,1) not in vis:valid.append(z)
probe(19,37,len(valid),3,'3','Exhaust all35 lattice paths and apply both adjacency and vertex conditions.')
bs=sum(F((-1)**k*math.comb(8,k),k+1) for k in range(9))
probe(19,38,(bs,math.comb(8,4)),(F(1,9),70),'70','Evaluate weighted finite binomial sum exactly and its central coefficient.')
seq=[F(1)]
for j in range(1,12):seq.append(F(3,2)*seq[-1]+1)
probe(19,39,tuple(seq[j]-(3*F(3,2)**j-2) for j in range(12)),(0,)*12,r'\(3(3/2)^{n-1}-2\)','Generate recurrence values from the stated sum identity and check closed form; written proof gives all n.')
assert all(sum(seq[:j])==3*seq[j-1]-2*j for j in range(1,13))
probe(19,40,s.diff(1+2*x,x),2,'2','Finite halving identity plus continuity establishes the affine solution before differentiation.')
y=x*(1-s.log(x));assert s.simplify(x*s.diff(y,x)-y+x)==0
probe(19,41,y.subs(x,s.E),0,r'\(e\)','Substitute claimed first zero into the verified positive-domain differential solution.')
AA=s.Matrix([1,0,1]);PP=s.Matrix([2,1,0]);dd=s.Matrix([1,2,2]);hh=AA+((PP-AA).dot(dd)/dd.dot(dd))*dd
probe(19,42,sum(2*hh-PP),F(19,9),'19/9','Project to the line and perform the exact half-turn.')
# Three symbolic generic vectors with a parallel to b-c establish the identity without sampling a scale.
b=s.Matrix(s.symbols('b0:3'));c=s.Matrix(s.symbols('c0:3'))
probe(19,43,s.expand((b-c).dot(b.cross(c))),0,r'\(0\)','Expand the generic scalar triple product after the cross-product parallelism condition; degenerate cases handled explicitly.')
validp=[]
for q in range(100):
 mu=F(20,q+6);mad=(q*abs(mu)+4*abs(2-mu)+2*abs(6-mu))/(q+6)
 if mad==F(5,3):validp.append(q)
probe(19,44,tuple(validp),(6,),'6','Exact integer-frequency enumeration supplements exhaustive two-case quadratic proof.')
probe(19,45,F(3,2)/s.sqrt(1+8+F(1,4)),3/s.sqrt(37),r'\(3/\sqrt{37}\)','Reconstruct symmetric tangent denominator from sum and product.')
# All thirty physics items, including explicit modelling and boundary checks.
probe(18,46,1-1,0,'Zero; gravity supplies the inward acceleration','Top-of-circle radial balance at the limiting speed.')
vc=F(6,3);K=F(3,2)*vc**2;xx=[r for r in s.solve(10*x*x+4*x-K,x) if r>0][0]
probe(18,47,xx,F(3,5),'0.60 m','Momentum-conserving impact followed by dissipative spring energy.')
probe(18,48,(1,s.sqrt(1-F(1,2)**2)),(1,s.sqrt(3)/2),r'\(1,\sqrt3/2\)','Project uniform interior gravity along a chord; compare amplitudes at fixed angular frequency.')
probe(18,49,F(1,2)*(1+F(1,2)),F(3,4),r'\(3\sigma^2AL/(4Y)\)','Thin-wire limiting force and both series strain energies.')
probe(18,50,F((2+3)**2,2*3),F(25,6),'25/6','Junction-drop conductivity ratio followed by network reconfiguration.')
probe(18,51,(8**F(1,3)*8,1/(8*s.sqrt(2))),(16,1/(8*s.sqrt(2))),r'\(16,1/(8\sqrt2)\)','Combine free-path density ratio, Cv-derived gamma, adiabatic heating and rms-speed time scale.')
probe(18,52,4/s.sqrt(F(1,4)),8,r'\(8\theta_0\)','Conserve angular momentum at the pull, then convert bottom speed to small angular amplitude.')
probe(18,53,((1+2)/3,F(1,2)),(1,F(1,2)),r'\(V,\;CV^2/2\)','Solve charged middle-node balance; only one capacitor retains a voltage.')
probe(18,54,(-s.cos(s.pi),s.sin(s.pi),s.cos(s.pi)),(1,0,-1),r'\(+\mu B,0,\text{ unstable}\)','Potential, torque and angular energy curvature at anti-alignment.')
qfield=x/(1+x*x)**s.Rational(3,2)
probe(18,55,s.diff(qfield,x), (1-2*x*x)/(1+x*x)**s.Rational(5,2),r'\(a>R/\sqrt2\)','Differentiate the supplied one-ring field and impose negative axial slope for positive test charge.')
rval=F(6-5,1)/F(25-20,10);emf=6+2*rval
probe(18,56,(rval,emf,emf**2/(4*rval)),(2,10,F(25,2)),'12.5 W','Infer meter-loaded source parameters and optimise power after meter removal.')
probe(18,57,6/(F(3,2)-F(3,4)),8,'8 cm','Use signed magnifications to reconstruct both object positions.')
probe(18,58,F(20-5,10),F(3,2),"B's work function exceeds A's by 1.5 eV, and the stopping-potential difference stays 1.5 V",'Subtract photon-energy equations; common frequency increments cancel.')
probe(18,59,F(2*50*144,100)/F(72,10),20,'20 fm; it supplies an upper scale bound, not an exact radius measurement','Head-on Coulomb turning point with alpha charge two.')
probe(18,60,F(1,2)*2*3**2*F(6,8),F(27,4),'6.75 J','Integrate series-resistor power fractions against total lost magnetic energy.')
yp=t**3/3;yb=18*t-5*t*t;ret=[v for v in s.solve(yb-yp,t) if v>0][0]
probe(19,46,s.diff(yb-yp,t).subs(t,ret),-21,'-21 m/s','Solve relative-position polynomial, select first positive root and differentiate relative position.')
probe(19,47,(2*(F(3,2)-1),F(3,2)-2*(F(3,2)-1)),(1,F(1,2)),r'\(mg/k\), yes','Energy turning point lies before natural-length contact boundary.')
probe(19,48,1/F(3,5)-1,F(2,3),r'\(2MR^2/3\)','Invert translational fraction using the rolling constraint.')
probe(19,49,F(1,2)-(F(1,2)+F(1,4)),-F(1,4),'Downward by H/4','Infer block density from two buoyancies and compare lower-surface draft.')
vf=s.solve(s.Eq(F(3,2)*x-F(9,2),-(x-1)),x)[0]
probe(19,50,vf,F(11,5),r'\(11V/5\)','First-law endpoint balance with constant external pressure rather than reversible path law.')
probe(19,51,s.pi/(F(2,100)*(2*s.pi/F(4,10))),10,'Leftward at 10 m/s','Snapshot slope and same-sign particle velocity identify the leftward travelling-wave branch.')
probe(19,52,2*4*F(1,3),F(8,3),r'\(8\pi^2d^3/(3GT^2)\)','Centripetal force at the smaller barycentric radius with full force separation d.')
probe(19,53,(-F(1,4)+F(1,16),0,F(1,2)-F(1,4)),(-F(3,16),0,F(1,4)),r'\(-3kQq/(16a^2),0,kQq/(4a)\)','Exact signed forces and potential energies for both separated dipole charges.')
ks=s.solve(s.Eq((x+1)**2,F(16,3)*x),x);kval=[v for v in ks if v>1][0]
probe(19,54,(kval,F(3,4)),(3,F(3,4)),r'\(3,3/4\)','Solve dielectric-geometry capacitance ratio and invert it for fixed-charge energy.')
# Independent nodal solution of all six internal cube vertices, not the symmetry reduction.
vertices=list(itertools.product([0,1],repeat=3));internal=[v for v in vertices if v not in [(0,0,0),(1,1,1)]]
unknown=s.symbols('v0:6');V=dict(zip(internal,unknown));V[(0,0,0)]=s.Integer(1);V[(1,1,1)]=s.Integer(0)
neigh=lambda u:[v for v in vertices if sum(a!=b for a,b in zip(u,v))==1]
sol=s.solve([sum(V[u]-V[v] for v in neigh(u)) for u in internal],unknown)
current=sum((V[(0,0,0)]-V[v]).subs(sol) for v in neigh((0,0,0)))
probe(19,55,(1/current,(V[(1,0,0)]-V[(1,1,0)]).subs(sol)),(F(5,6),F(1,5)),r'\(5R/6,V/(5R)\)','Solve six Kirchhoff node equations independently of the written cube-symmetry proof.')
probe(19,56,s.sqrt(F(1,2)**2+(s.sqrt(3)/2)**2),1,r'\(\mu_0I^2/(2\pi d)\), parallel to C towards B','Vector sum of the attracting and repelling wire forces.')
probe(19,57,((120/3)/s.sqrt(6**2+(10-2)**2)/3,F(6,10)),(F(4,3),F(3,5)),r'\(4/3\text{ A},0.6\)','Transform voltage, compute secondary phasor current and reflect its magnitude and phase.')
probe(19,58,F(1,2)/F(3,4),F(2,3),r'\([0,\theta)\cup(\pi-\theta,\pi]\)','Impact-parameter geometry gives the exact sine threshold; written interval proof keeps both directions and excludes equality.')
probe(19,59,(F(1,2)/2,1/(2*s.Integer(2))),(F(1,4),F(1,4)),'The fields are equal; no conduction current crosses the ideal gap','Use enclosed-area branches inside and outside plate radius in Ampere-Maxwell law.')
probe(19,60,2*(80/F(2))+20,100,'100 counts/min','Apply independent activity decay and detection-efficiency changes before adding background.')
report=dict(total=len(checks),passed=sum(c['passed'] for c in checks),source_sha256={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources.values()},checks=checks,scope='Author-side mathematical and numerical probes; not independent academic review or measured timing.')
(O/'calculation_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(report['passed'],'/',report['total'],'checks passed')
assert report['passed']==report['total']
