"""Transcribed-input arithmetic probes, not a question generator or academic certification."""
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
paper = ROOT / 'IISER/IAT TEST 1.json'
data = json.loads(paper.read_text())
checks = []
def record(n, method, result, expected):
    ok = math.isclose(float(result), float(expected), rel_tol=1e-8, abs_tol=1e-7)
    q = data['questions'][n-1]
    checks.append({'question': n, 'method': method, 'computed': str(result),
                   'expected_value': str(expected), 'passed': ok,
                   'stored_selected_content': q['options'][ord(q['correct_option'])-65]})
    assert ok, (n, result, expected)

record(4,'Gamete-frequency product, percent',F(80,1000)**2*100,F(16,25))
record(6,'Net secondary production / NPP, percent',F(180-120,2400-900)*100,4)
record(11,'Uncut DNA mass / total DNA mass',F(900,900+600+300),F(1,2))
record(13,'Conditional family carrier × conditional HW carrier × recessive union',F(2,3)*(2*F(1,5)*F(4,5)/(1-F(1,5)**2))*F(1,4),F(1,18))
record(18,'Gibbs energy at 200 K, kJ/mol',24-200*.08,8)
record(18,'Gibbs energy at 400 K, kJ/mol',24-400*.08,-8)
record(19,'Assay mole fraction',(3.94/394)/((3.94/394)+(2.16/108/2)),.5)
record(20,'Ksp then Nernst equation, V',1.10-.060/2*math.log10(1/(1e-20/(1e-4)**2)),.74)
record(22,'Charge-balance Fe(III) fraction',F(8-2*3,3),F(2,3))
record(23,'Additional first-order interval, min',1.099/(.288/10),38.1597222222)
record(24,'Two independent chiral centres; no E/Z multiplicity',2**2,4)
record(26,'Osmolarity difference, mol/L',.060*(1+2*.75)-.10,.05)
record(27,'Bicarbonate recovered from lost volatile mass, g',(.31)*168/62,.84)
record(27,'Initial bicarbonate mass percent',(.31)*168/62/1.90*100,44.21052631578947)
record(30,'Final buffer after both acid additions',14-(5+math.log10((.01+.02)/(.04-.01-.02))),8.52287874528)
record(31,'Numerical inverse trace',np.trace(np.linalg.inv([[3,1],[1,1]])),2)
record(32,'Exhaustive six-folder arrangements',sum(p.index('B')-p.index('A')==2 for p in itertools.permutations('ABCDEF')),96)
x=np.linspace(-1,2,10001)
record(33,'Eliminated polynomial minimum including endpoints',np.min((x*x-4*x+2)/3),F(-2,3))
record(34,'Circle-line imaginary-coordinate product',(2+math.sqrt(5))*(2-math.sqrt(5)),-1)
x=np.linspace(0,math.pi,100001)
record(35,'Numerical quadrature of original integral',np.trapezoid(x*np.sin(x)/(1+np.cos(x)**2),x),math.pi**2/4)
r=np.array([1.,2.,3.]); normal=np.ones(3)
ref=r-2*(r@normal-3)/(normal@normal)*normal
record(36,'Direct vector reflection norm',np.linalg.norm(ref),math.sqrt(2))
record(38,'Second moments minus combined mean squared',((1+2**2)+(9+6**2))/2-4**2,9)
record(39,'Conjugate form near zero',4/(math.sqrt(1+3e-9)+math.sqrt(1-1e-9)),2)
record(40,'Enumerate 6! assignments with exactly two fixed points',F(sum(sum(i==v for i,v in enumerate(p))==2 for p in itertools.permutations(range(6))),math.factorial(6)),F(3,16))
record(41,'Direct inverse tangent sum',math.atan(2)+math.atan(3),3*math.pi/4)
record(42,'Initial-value solution at x=3',4*3/(1+3),3)
t1,t2=1+math.sqrt(2),1-math.sqrt(2)
P=np.array([t1*t1,2*t1]); Q=np.array([t2*t2,2*t2]); T=np.linalg.solve([[1,-t1],[1,-t2]],[-t1*t1,-t2*t2])
record(44,'Parabola endpoints satisfy focal chord P',P[1]-P[0]+1,0)
record(44,'Parabola endpoints satisfy focal chord Q',Q[1]-Q[0]+1,0)
record(44,'Independently solved tangent intersection x',T[0],-1)
record(44,'Independently solved tangent intersection y',T[1],2)
record(44,'Determinant area of triangle PQT',abs(np.linalg.det(np.array([Q-P,T-P])))/2,8*math.sqrt(2))
a=np.array([1.,0.,0.]); b=np.array([.5,math.sqrt(3)/2,0.])
record(45,'Direct adjacent-vector cross product',np.linalg.norm(np.cross(a+2*b,a-b)),3*math.sqrt(3)/2)
t=np.linspace(0,6,60001); v=np.interp(t,[0,2,4,6],[0,4,-4,0])
record(46,'Integral of speed / time',np.trapezoid(np.abs(v),t)/6,2)
record(46,'Signed velocity integral / time',np.trapezoid(v,t)/6,0)
record(48,'Bernoulli coefficient in density × v² units',F(1,2)*(4**2-1),F(15,2))
Ii=F(3); If=F(9,4); wf=Ii/If
record(49,'Angular momentum ratio',wf,F(4,3))
record(49,'Kinetic-energy increase in mR²ω² units',If*wf**2/2-Ii/2,F(1,2))
record(50,'Reservoir entropy change, J/K',F(500,300)-F(800,500),F(1,15))
record(51,'Maximum/equilibrium extension',F(15,10),F(3,2))
record(51,'Amplitude from displacement and initial speed divided by omega',math.hypot(.03,.04),.05)
record(52,'String frequency after tension change',512*math.sqrt((255/256)**2),510)
record(52,'Candidate satisfying both beat frequencies',[f for f in (508,516) if abs(f-510)==2][0],508)
record(52,'Zero-beat tension fraction',(508/512)**2,F(127,128)**2)
record(53,'Turning-point coordinate / a',1+(F(5,4)-F(1,2)),F(7,4))
Vmid=F(12)*(F(1,2)+F(1,3))/(F(1,2)+F(1,3)+F(1,4)+F(1,3))
record(54,'Connected-node KCL excess at A, amperes',(12-Vmid)/2-Vmid/4,F(12,17))
record(55,'Final mass number',238-4,234)
record(55,'Final atomic number',92-2+2,92)
record(57,'Layer depth/index sum, cm',F(6)/F(3,2)+F(4)/F(4,3),7)
record(58,'Source rms phasor magnitude, V',math.hypot(8,10-4),10)
record(58,'Resistor real power, W',2*8,16)
phase=np.linspace(0,2*math.pi,100001); sine=np.sin(phase)
record(59,'Half-wave / full-wave mean squared voltage',np.trapezoid(np.maximum(sine,0)**2,phase)/np.trapezoid(sine**2,phase),.5)
delta=next(d for d in range(1,15001) if d%300==0 and d%500==0 and (d//300)%2==1 and (d//500)%2==1)
record(60,'Smallest shared odd half-wave path → thickness, μm',delta/.5/1000,3)
record(5,'Daily osmole excretion before',2*300,600)
record(5,'Daily osmole excretion after',.75*800,600)
record(8,'Reduced female gamete chromosomes',24/2,12)
record(8,'Reduced male gamete chromosomes',48/2,24)
record(8,'Zygote chromosomes',12+24,36)
record(8,'Primary endosperm nucleus chromosomes',12+12+24,48)
record(8,'Zygote maternal to paternal ratio',F(12,24),F(1,2))
record(8,'Endosperm maternal to paternal ratio',F(24,24),1)
record(12,'Preparation B bypass response relative to basal',8/2,4)
record(14,'External oxygen ratio at equal diffusion geometry',8/4,2)
record(14,'Measured cutaneous uptake ratio',4/2,2)
record(21,'Warm-stage nitrogen by cumulative difference',.030-.010,.020)
record(21,'Total amines from final nitrogen plateau',.010+.020,.030)
record(27,'Residue mass reconstructed from both initial components',1.06+.84*106/168,1.59)
record(51,'Linear-amplitude distractor force in mg units',1+(.03+.04)/.10,1.7)
record(52,'Rejected upper fork candidate beat after string change',abs(516-510),6)
report={'paper_sha256':hashlib.sha256(paper.read_bytes()).hexdigest(),
        'checks':checks,'passed':sum(c['passed'] for c in checks),
        'limitations':'Inputs transcribed from stems. These arithmetic probes do not independently certify conceptual correctness, answer uniqueness, timing or syllabus fit. No questions are generated or modified.'}
(ROOT/'IISER/review/IAT_TEST_1_arithmetic_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Passed {len(checks)} arithmetic/enumeration probes.')
