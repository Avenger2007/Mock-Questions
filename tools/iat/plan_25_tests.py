"""Assemble and audit an editorial slot plan; never writes mock questions."""
from collections import Counter, defaultdict
from pathlib import Path
import csv, json, re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs/blueprints/iat_25_test_slots.tsv'
BLUE = (ROOT / 'docs/blueprints/iat.md').read_text()
TAX = json.loads((ROOT / 'docs/blueprints/iat_taxonomy.json').read_text())
P1 = json.loads((ROOT / 'IISER/IAT TEST 1.json').read_text())

# Editorial subtopic rotations, not question stems. Slash separates different
# syllabus mechanisms within a chapter; no numeric substitution is encoded here.
ROTATIONS = {
 'B': {
  'DIV':'algal pigment and reserve product/bryophyte sporophyte dependence/pteridophyte spore type/gymnosperm ovule exposure/angiosperm seed character/taxonomic hierarchy',
  'STR':'root vascular arrangement/stem cambium origin/leaf mesophyll distribution/flower whorl position/floral formula inference/frog circulatory structure',
  'CELL':'membrane transport control/organelle fractionation/enzyme inhibition/ribosome translation context/chromosome versus DNA content/mitotic checkpoint/biomolecule linkage',
  'PLANT':'light-response limiting factor/Calvin-cycle carbon tracing/photorespiration contrast/C3 versus C4 anatomy/respiratory quotient/stomatal exchange/chemiosmotic gradient',
  'HUMAN':'cardiac output and pressure/gas transport and dissociation/nephron clearance and reabsorption/neural synapse and receptor/endocrine feedback/skeletal muscle contraction/immune-related physiology',
  'REPRO':'pollen compatibility and outbreeding/embryo-sac development/double-fertilisation ploidy/seed and fruit development/human gametogenesis/menstrual hormone sequence',
  'GEN':'Mendelian two-locus segregation/conditional pedigree risk/linkage test-cross interpretation/sex-linked transmission/molecular replication direction/transcription regulation/genetic-code reading/mutation and disorder/Hardy-Weinberg assumption/evolutionary selection evidence',
  'WELFARE':'vaccination response timing/antibody versus cellular defence/cancer and cell-cycle link/pathogen life-cycle stage/microbe product identification/antibiotic resistance selection',
  'BIOTECH':'restriction recognition and ends/vector selection and marker/PCR primer orientation/gel fragment interpretation/recombinant selection control/biotechnology application evidence',
  'ECO':'population growth regime/competition and resource/primary versus secondary productivity/food-web energy accounting/species-area relationship/biodiversity conservation evidence'
 },
 'C': {
  'STO':'limiting reagent in stages/empirical formula from composition/solution dilution and reaction yield/gas stoichiometry under stated conditions',
  'ATOM':'spectral series limit/quantum-number exclusions/orbital occupancy and energy/hydrogen transition wavelength',
  'PERIOD':'ionisation anomaly/electron-affinity comparison/isoelectronic-radius constraint/effective nuclear charge trend',
  'BOND':'VSEPR angle with lone pair/bond polarity versus molecular dipole/resonance contributor validity/hybridisation and sigma-pi count/formal-charge minimisation',
  'DF':'variable oxidation-state stability/colour and d-electron count/lanthanoid contraction trend/spin-only moment',
  'COORD':'ionisation isomer wet test/geometrical isomer count/ligand-field high-low spin/coordination number and charge/chelate stability comparison',
  'THERM':'Hess-cycle route/enthalpy versus entropy sign/Gibbs-temperature boundary/calorimetric heat balance',
  'EQ':'reaction quotient shift/buffer before and after neutralisation/weak-acid dissociation/common-ion solubility',
  'REDOX':'half-reaction electron balance/disproportionation assessment/oxidation-number constraints/redox titration equivalence',
  'SOL':'Raoult deviation/colligative-property comparison/van Hoff factor inference/partial-vapour-pressure table',
  'ELEC':'cell polarity from quotient/concentration-cell potential/Faraday deposition/electrolysis discharge order/conductivity dilution',
  'KIN':'initial-rate order table/integrated half-life relation/Arrhenius temperature comparison/rate graph and activation barrier',
  'GOC':'resonance versus inductive acidity/isomer classification/electrophile nucleophile selectivity/stability of reactive intermediates',
  'HC':'addition regioselectivity/ozonolysis reconstruction/aromatic substitution orientation/combustion composition',
  'HALO':'SN1 versus SN2 outcome/competing elimination/aryl versus alkyl reactivity/stereochemical substitution',
  'ALCO':'alcohol oxidation selectivity/phenol acidity/ether cleavage/sodium versus neutral reagent response',
  'CARB':'Tollens versus iodoform evidence/carbonyl addition selectivity/aldol eligibility/acid derivative transformation/esterification equilibrium',
  'AMINE':'basicity in solvent/diazonium cold-warm response/amine-class test/aniline substitution control',
  'BIO':'reducing sugar before-after hydrolysis/peptide hydrolysis products/amino acid charge/nucleic-acid base pairing'
 },
 'M': {
  'SET':'composition domain/inverse restriction/injection versus surjection/equivalence relation test',
  'COUNT':'circular arrangement with forbidden pair/inclusion-exclusion count/path count avoiding a point/identical-item grouping',
  'BINOM':'signed coefficient extraction/middle-term ratio/term independent of variable/neighboring-coefficient identity',
  'COMPLEX':'modulus locus/argument branch/roots-of-unity geometry/conjugate polynomial condition',
  'QUAD':'strict interval root test/discriminant and parameter/sign of roots/common-root condition',
  'TRIG':'inverse-value branch/trig equation endpoints/compound-angle identity/periodic solution count',
  'VECTOR':'scalar triple product/dot-product projection/cross-product orientation/collinearity test',
  'MATRIX':'determinant row transform/inverse existence/adjoint identity/matrix equation',
  'COORD':'circle tangency/chord distance/ellipse focus-directrix/parabola normal/hyperbola asymptote/line family intersection',
  '3D':'skew-line distance/plane intersection/foot of perpendicular/line-plane angle',
  'SEQ':'telescoping rational sum/arithmetic-geometric progression/series convergence under stated condition/partial-sum inversion',
  'LIMIT':'one-sided absolute-value limit/removable singularity/continuity parameter/exponential limit',
  'DIFF':'implicit tangent/monotonicity interval/parameterised differentiability/extreme value with endpoints',
  'INT':'area between curves/substitution and bounds/symmetry of definite integral/partial fractions with limits',
  'DE':'separable initial-value problem/first-order linear solution/homogeneous substitution/formation from curve family',
  'STAT':'affine variance transform/combined-group variance/mean deviation of grouped observations/standard-deviation constraint',
  'PROB':'Bayes with unequal priors/without-replacement conditional event/independent versus exclusive events/binomial probability event'
 },
 'P': {
  'UNITS':'dimension of coefficient/error propagation/significant-digit inference/unit conversion trap',
  'KIN':'relative motion with shared origin/projectile interception/piecewise acceleration graph/vertical-motion turning time',
  'FORCE':'coupled tension with support acceleration/limiting friction and impending slip/normal force under noninertial motion/constraint acceleration',
  'WORK':'position-dependent work/power at instant/energy with dissipative stage/spring-gravity conversion',
  'ROT':'drilled-body inertia/angular momentum with changing radius/torque versus angular acceleration/rolling energy partition',
  'GRAV':'escape speed ratio/orbital energy transfer/gravity inside uniform sphere/satellite period under radius change',
  'SOLID':'stress-strain two regimes/series wire extension/elastic-energy density/Poisson-ratio response',
  'FLUID':'pressure in accelerating vessel/Bernoulli with elevation/viscosity terminal speed/buoyancy under partial immersion',
  'THERMAL':'calorimetry with phase plateau/thermal-expansion constraint/conduction thermal resistance/cooling comparison',
  'THERMO':'engine-cycle energy bookkeeping/entropy in mixing/adiabatic process inference/first-law sign convention',
  'KTG':'rms speed for gas mixtures/equipartition heat capacity/mean free path trend/pressure from molecular impacts',
  'SHM':'spring-combination period/phase and energy at given displacement/pendulum length change/velocity-acceleration relation',
  'WAVE':'interference with source phase/standing-wave node shift/beat ambiguity with reference change/reflection phase at boundary',
  'ELECTRO':'flux of multi-charge surface/field cancellation locus/dipole torque and energy/electric potential from field region',
  'CAP':'dielectric with battery disconnected/capacitor energy after reconnection/series-capacitor charge/plate-separation change',
  'CURRENT':'bridge balance with temperature/internal resistance terminal voltage/resistor network node reduction/drift versus current density',
  'MAG':'force with vector field components/field of current loop/magnetic dipole energy/parallel-wire force',
  'EMI':'rotating rod motional emf/Lenz direction under flux change/inductor energy from current/mutual induction sign',
  'AC':'phasor phase and impedance/rms real power/resonance bandwidth concept/inductor-capacitor voltage cancellation',
  'EMW':'field orientation and propagation/energy flux comparison/spectrum wavelength and frequency/polarisation implication',
  'RAY':'lens-mirror combination/real-virtual image sign/critical angle through layers/prism deviation',
  'WAVEOPT':'slit separation and fringe shift/thin-film phase reversal/coherence and visibility/diffraction central width',
  'DUAL':'stopping potential from two frequencies/de Broglie acceleration comparison/threshold frequency and work function/photocurrent saturation',
  'ATOM':'Bohr transition ratio/line-series limit/energy-level absorption/emission selection',
  'NUC':'multi-stage decay bookkeeping/binding-energy per nucleon/half-life mixture/radioactivity count rate',
  'SEMI':'diode I-V inference/half-wave output power/p-n junction bias/rectifier ripple comparison'
 }
}

LENSES = [
 'infer the missing cause from two independent observations',
 'predict the outcome when one control is changed',
 'compare two models under the same boundary condition',
 'read a signed graph or a labelled representation',
 'detect an assumption that changes the conclusion',
 'reconstruct an initial state from a final measurement',
 'interpret a small experimental table and a control',
 'identify which common shortcut gives a wrong result',
 'check the limiting case before choosing an equation',
 'combine an ordering constraint with a quantitative result',
 'separate a total quantity from its marginal change',
 'compare the same system before and after a perturbation',
 'use a counterexample to reject an overstrong claim',
 'derive a ratio while an unmeasured scale cancels',
 'join a structural clue with a measured response',
 'distinguish two mechanisms with a second test',
 'track conservation across two linked stages',
 'reason backwards from an observed equality',
 'identify the first point where a threshold is crossed',
 'test competing explanations using a negative control',
 'connect a verbal condition with a mathematical bound',
 'compare a microscopic rule with a macroscopic reading',
 'resolve an apparent contradiction between two measurements',
 'combine a qualitative trend with an exact numerical condition',
 'decide whether a result persists after a stated reversal'
]
SPECIFIC = {
 (2,'B'): 'seed-plant diagnostic characters|floral whorl and ovary position|organelle fraction contamination control|light versus carbon dioxide limitation|cardiac output from rate and stroke volume|meiosis-I nondisjunction in gametes|codominance versus incomplete dominance in offspring|antiserum versus vaccine response timing|sticky-end ligation compatibility|density-dependent growth from interval data|conditional pedigree segregation|translation reading frame after insertion|clearance versus tubular reabsorption|mitotic arrest and chromosome count|girdling with transport control'.split('|'),
 (2,'C'): 'lone-pair angle ordering|coordination ionisation isomer wet test|hydrogen series convergence|carbocation stability and rearrangement|alkene addition regiochemistry|SN1 versus SN2 stereochemistry|alcohol oxidation versus phenol test|two-test aldehyde ketone identification|amine basicity from solvation and resonance|osmotic pressure of mixed nonelectrolytes|concentration-cell polarity|initial-rate law inference|Hess cycle sign accounting|titration across equivalence|ligand-field spin and moment'.split('|'),
 (2,'M'): 'circle tangent to both axes|conic focus-directrix eccentricity|piecewise monotonicity|definite-integral bound substitution|restricted inverse domain|matrix determinant condition|two-stage conditional sampling|signed binomial coefficient|series from partial sums|one-sided absolute-value limit|skew-line distance|circular forbidden-adjacency count|complex locus with argument|separable differential equation with boundary|closed-interval trig roots'.split('|'),
 (2,'P'): 'coupled tension with accelerating support|work against position-dependent friction|escape-speed radius comparison|two-slope stress-strain energy|heat exchange with phase plateau|mean versus rms energies in gas mixture|period after spring recombination|disconnected capacitor dielectric insertion|force vector under two magnetic components|potential from piecewise field table|variable-resistance bridge balance|lens-mirror sequence|stopping potential at two light frequencies|Bohr wavelength ratio|flux-change induced-current direction'.split('|'),
 (3,'B'): 'algal generation from ploidy|plant tissue from walls and arrangement|coupled membrane transport control|stomatal humidity response|oxygen dissociation and blood transport|pollen viability and outbreeding|linked-locus recombinant test-cross|primary versus secondary immune response|PCR primer strand orientation|energy pyramid with detrital branch|two-gene enzyme pathway interaction|operator mutation and inducer control|synaptic release versus receptor blockade|meiosis-II segregation consequence|DNA fingerprint band discrimination'.split('|'),
 (3,'C'): 'bond versus molecule polarity|high-low spin ligand field|d-electron colour versus oxidation state|first-ionisation anomaly|de Broglie mass-charge comparison|two-stage yield limiting reagent|substituent effects on aromatic acid|ozonolysis product reconstruction|aryl versus alkyl halide condition|phenol versus alcohol base response|peptide hydrolysis and charge|common-ion solubility|Raoult deviation from pressure data|aqueous electrolysis selectivity|calorimetric enthalpy and limit'.split('|'),
 (3,'M'): 'parameterised line-circle tangency|implicit vertical-tangent condition|parameterised monotonicity interval|area between intersecting curves|one-to-one counterexample|scalar triple-product coplanarity|determinant row transform|Bayes with unequal priors|lattice path avoiding a point|binomial adjacent-term ratio|telescoping rational sum|strict interval root condition|variance after affine transform|first-order linear DE|one-sided limit under parameter'.split('|'),
 (3,'P'): 'projectile relative motion|instantaneous power and accumulated work|inertia of drilled disc|pressure in accelerating liquid|entropy of irreversible thermal mixing|interference with phase offset|satellite energy across radii|zero-potential locus|capacitor dielectric energy comparison|temperature-dependent bridge resistance|charge trajectory across field regions|phasor phase from impedance|optical path through two media|EM field orientation and energy flux|multi-emission decay chain'.split('|')
}
assert all(len(v)==15 for v in SPECIFIC.values())
STYLES = {'B':list('CCCDDTGENCCDDCC'), 'C':list('CCDNDNCDGNCCDNC'),
          'M':list('NNNCNNNCNNNCNNN'), 'P':list('NDDNNCNDDGNCNND')}
STYLE_NAME={'R':'recall','C':'conceptual','N':'numerical','D':'diagram/structure',
            'G':'graph','T':'table/match','E':'experiment'}

def profiles(subject):
    block = BLUE.split('### '+{'B':'Biology','C':'Chemistry','M':'Mathematics','P':'Physics'}[subject]+'\n',1)[1].split('\n### ',1)[0]
    if subject=='B':
        additions=dict(re.findall(r'^\| ([A-E]) \| ([A-Z ]+) \|$',block,re.M))
        return {k:('DIV STR CELL PLANT HUMAN REPRO GEN WELFARE BIOTECH ECO '+v).split() for k,v in additions.items()}
    return {k:v.split() for k,v in re.findall(r'^\| ([A-E]) \| ([A-Z0-9 ]+) \|$',block,re.M)}

table=BLUE.split('## Reservation by test',1)[1].split('## Review',1)[0]
reservations=[]
for line in table.splitlines():
    m=re.match(r'^\| (\d+) \| ([A-E]) \| ([A-E]) \| ([A-E]) \| ([A-E]) \|',line)
    if m: reservations.append((int(m[1]),dict(zip('BCMP',m.groups()[1:]))))
assert len(reservations)==25
for s in 'BCMP':
    assert len(ROTATIONS[s])==len([c for c in TAX[s] if not c.startswith('X')])
    assert len(STYLES[s])==15

usage=defaultdict(int)
rows=[]
for test,assignment in reservations:
    for si,subject in enumerate('BCMP'):
        codes=profiles(subject)[assignment[subject]]
        if test==1:
            # Preserve the already committed paper as the authoritative 15-slot plan.
            qs=P1['questions'][15*si:15*(si+1)]
            canonical={
              'B':'DIV STR CELL GEN HUMAN ECO CELL REPRO PLANT WELFARE BIOTECH HUMAN GEN STR GEN',
              'C':'BOND COORD THERM CARB ELEC AMINE REDOX KIN CARB GOC SOL STO PERIOD BIO EQ',
              'M':'MATRIX COUNT SET COMPLEX INT 3D DIFF STAT LIMIT PROB TRIG DE QUAD COORD VECTOR',
              'P':'KIN UNITS FLUID ROT THERMO SHM WAVE ELECTRO CURRENT NUC EMI RAY AC SEMI WAVEOPT'
            }
            codes=canonical[subject].split()
            assert all(codes),(subject,codes)
        assert len(codes)==15,(test,subject,codes)
        for j,code in enumerate(codes):
            qn=15*si+j+1
            rank=usage[subject,code];usage[subject,code]+=1
            seeds=ROTATIONS[subject][code].split('/')
            focus=seeds[rank%len(seeds)]
            lens=LENSES[(rank//len(seeds)+sum(map(ord,code)))%len(LENSES)]
            if test==1:
                q=qs[j]
                focus=q['sub_topic']; angle='Existing authored Test 1: '+q['question'].split('.')[0][:110]
                tier=q['difficulty'];style=q['format'];state='authored'
            else:
                easy=3 if si==(test-1)%4 else 2
                hard=3 if si==test%4 else 2
                order=sorted(range(15),key=lambda k:(k*7+test*3+si*5)%17)
                tier='easy' if j in order[:easy] else 'hard' if j in order[easy:easy+hard] else 'medium'
                style=STYLE_NAME[STYLES[subject][(j+test)%15]]
                angle=SPECIFIC[(test,subject)][j] if (test,subject) in SPECIFIC else focus+'; '+lens
                state='reserved, must be authored and reviewed'
            rows.append({'test':test,'question':qn,'id':f'IAT27-T{test:02}-Q{qn:02}',
              'subject':subject,'chapter_code':code,'chapter':TAX[subject][code][0],
              'class_level':TAX[subject][code][1],'focus':focus,'angle_seed':angle,
              'dominant_style_target':style,'difficulty_target':tier,'state':state})
assert len(rows)==1500
assert len({r['id'] for r in rows})==1500
for test in range(1,26):
    paper=[r for r in rows if r['test']==test]
    assert len(paper)==60 and Counter(r['subject'] for r in paper)==dict.fromkeys('BCMP',15)
    assert Counter(r['difficulty_target'] for r in paper)=={'easy':9,'medium':42,'hard':9},(test,Counter(r['difficulty_target'] for r in paper))
for s in 'BCMP':
    current=[c for c in TAX[s] if not c.startswith('X')]
    assert all(usage[s,c]>0 for c in current)
with OUT.open('w') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print('Wrote',len(rows),'slots to',OUT)
for s in 'BCMP':print(s,dict(sorted((c,usage[s,c]) for c in ROTATIONS[s])))
