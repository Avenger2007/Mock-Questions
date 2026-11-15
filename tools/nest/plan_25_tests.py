"""Build the NEST (NISER/CEBS) 25-test slot plan.

Chapter slot counts: 60% syllabus breadth + 40% share in the NEST 2024 (two sessions), 2025 and 2026 papers
(docs/blueprints/nest_pyq_analysis.md), rounded to 5, minimum 5.

usage:  python3 tools/nest/plan_25_tests.py            write NISER/NEST_25_Test_Plan.csv and print the count tables
        python3 tools/nest/plan_25_tests.py --check    verify the CSV on disk without rewriting it

Planning metadata only: it never writes question text, options, numbers or answers.
Every slot is one question ID with a chapter, one syllabus focus, one task angle and a difficulty target.
No two slots share the same (chapter, focus, angle), so two questions can never be planned on the same task.
Once a test is authored, its rows are frozen: change 'state' and the hash columns, not the slot.
"""
import csv, sys, os, collections

OUT = 'NISER/NEST_25_Test_Plan.csv'
TESTS, PER_SECTION = 25, 20
SUBJECTS = [('B', 'Biology', 1), ('C', 'Chemistry', 21), ('M', 'Mathematics', 41), ('P', 'Physics', 61)]

ANGLES = {
 'B': ['mechanism or reason', 'experiment or observation to interpret', 'data, table or graph to read',
       'compare two structures or processes', 'applied case (disorder, mutation, changed condition)',
       'quantitative (ratio, count, rate, probability)', 'order of steps or pathway logic'],
 'C': ['concept with reason', 'numerical, multi-step', 'structure or mechanism', 'trend or ordering with reason',
       'experiment or laboratory observation', 'data or graph to read', 'two linked reactions or ideas'],
 'M': ['multi-step computation', 'condition on a parameter', 'counting or existence of solutions',
       'geometric interpretation', 'behaviour or graph of a function', 'inverse problem (find the data)',
       'special or limiting case'],
 'P': ['numerical, multi-step', 'conceptual, qualitative', 'graph to read or to choose', 'scaling or limiting case',
       'experiment or measurement', 'compare two situations', 'conservation-law approach'],
}

# (code, chapter, class, slots, [focus, ...])   focus wording follows NISER/Syllabus.md
CH = {
'B': [
 ('LIVCLS','The Living World; Biological Classification',11,25,['three domains, taxonomic hierarchy and binomial nomenclature','concept of species; taxonomy and systematics','five kingdom classification: criteria','Monera and Protista: major groups','Fungi: major groups and life cycles','lichens, viruses and viroids']),
 ('PLANTK','Plant Kingdom',11,5,['algae: groups and distinguishing features','bryophytes and pteridophytes: dominant generation','gymnosperms and angiosperms: distinguishing features','comparing major plant groups']),
 ('ANIMK','Animal Kingdom',11,10,['basis of classification: symmetry, coelom, germ layers','non-chordate phyla: Porifera to Aschelminthes','non-chordate phyla: Annelida to Hemichordata','chordate classes: fishes and amphibians','chordate classes: reptiles, birds and mammals']),
 ('MORPH','Morphology of Flowering Plants',11,5,['root, stem and leaf modifications','inflorescence and flower: parts, symmetry, aestivation, placentation','fruit and seed structure','floral formula and family Solanaceae']),
 ('ANAT','Anatomy of Flowering Plants',11,15,['tissue systems: epidermal, ground, vascular','dicot and monocot root','dicot and monocot stem','dicot and monocot leaf']),
 ('FROG','Structural Organisation in Animals (frog)',11,5,['frog: digestive and respiratory systems','frog: circulatory and nervous systems','frog: reproductive system and morphology']),
 ('CELL','Cell: The Unit of Life',11,25,['prokaryotic and eukaryotic cells; cell theory','cell membrane and cell wall','endomembrane system: ER, Golgi, lysosomes, vacuoles','mitochondria, plastids and ribosomes','cytoskeleton, cilia, flagella, centrioles','nucleus and chromosomes','plant cell and animal cell compared']),
 ('BIOMOL','Biomolecules',11,30,['metabolites and chemical composition of cells','proteins: levels of structure and function','carbohydrates and lipids','nucleic acids: structure','enzymes: properties and types','enzyme action: kinetics, inhibition, temperature and pH']),
 ('CYCLE','Cell Cycle and Cell Division',11,15,['phases of the cell cycle and DNA content','mitosis: stages and significance','meiosis I: prophase I events and segregation','meiosis II and significance of meiosis','mitosis and meiosis compared']),
 ('PHOTO','Photosynthesis in Higher Plants',11,25,['site of photosynthesis and pigments','light reaction and electron transport','cyclic and non-cyclic photophosphorylation; chemiosmosis','Calvin cycle: use of ATP and NADPH','photorespiration and the C4 pathway','factors affecting photosynthesis']),
 ('RESP','Respiration in Plants',11,15,['glycolysis and fermentation','TCA cycle','electron transport system and oxidative phosphorylation','respiratory balance sheet and ATP count','amphibolic pathway and respiratory quotient']),
 ('PGR','Plant Growth and Development',11,10,['seed germination, growth phases and growth rate','differentiation, dedifferentiation, redifferentiation','auxin, gibberellin and cytokinin','ethylene and abscisic acid']),
 ('BREATH','Breathing and Exchange of Gases',11,10,['respiratory system and mechanism of breathing','respiratory volumes and capacities','exchange and transport of gases','regulation of respiration and disorders']),
 ('CIRC','Body Fluids and Circulation',11,10,['blood: composition, groups and coagulation','heart structure and double circulation','cardiac cycle and cardiac output','ECG and regulation of cardiac activity','lymph and circulatory disorders']),
 ('DIGEST','Digestion and Absorption',11,5,['alimentary canal and digestive glands','digestive enzymes and gastrointestinal hormones','absorption and assimilation; calorific values','nutritional and digestive disorders']),
 ('EXCR','Excretory Products and their Elimination',11,10,['modes of excretion','nephron structure and urine formation','concentration of filtrate: counter-current mechanism','regulation: RAAS, ANF, ADH; micturition','excretory disorders, dialysis and other organs']),
 ('LOCO','Locomotion and Movement',11,5,['types of movement and muscle types','contractile proteins and sliding filament mechanism','skeletal system and joints','muscular and skeletal disorders']),
 ('NEURAL','Neural Control and Coordination',11,15,['neuron structure and types','resting potential and generation of nerve impulse','conduction and synaptic transmission','central neural system: brain regions','peripheral and visceral nervous systems']),
 ('ENDO','Chemical Coordination and Integration',11,10,['hypothalamus and pituitary','thyroid, parathyroid and pineal','adrenal and pancreas','gonads; hormones of heart, kidney and gut','mechanism of hormone action','hypo- and hyperactivity disorders']),
 ('REPFL','Sexual Reproduction in Flowering Plants',12,10,['microsporogenesis and male gametophyte','megasporogenesis and embryo sac','pollination and outbreeding devices','pollen-pistil interaction and double fertilization','endosperm, embryo, seed and fruit','apomixis, parthenocarpy, polyembryony']),
 ('HUMREP','Human Reproduction',12,10,['male reproductive system and spermatogenesis','female reproductive system and oogenesis','menstrual cycle and its hormones','fertilisation, cleavage and implantation','pregnancy, placenta, parturition and lactation']),
 ('REPH','Reproductive Health',12,5,['contraception and MTP','STDs and amniocentesis','infertility and assisted reproductive technologies']),
 ('INHER','Principles of Inheritance and Variation',12,40,['law of dominance and segregation: monohybrid ratios','inheritance of two genes: dihybrid ratios','incomplete dominance and co-dominance','multiple alleles and blood groups; pleiotropy','polygenic inheritance','chromosome theory; linkage and recombination','sex determination in humans, birds and honey bee','pedigree analysis','sex-linked disorders: haemophilia, colour blindness','autosomal disorders: sickle-cell, thalassemia, PKU','chromosomal disorders: Down, Turner, Klinefelter']),
 ('MOLB','Molecular Basis of Inheritance',12,40,['search for genetic material: Griffith, Avery, Hershey-Chase','structure of DNA and RNA; base pairing rules','DNA packaging','DNA replication: Meselson-Stahl and the machinery','transcription in prokaryotes and eukaryotes','genetic code and mutations','translation','lac operon','Human and rice genome projects','DNA fingerprinting','RNA world and Central Dogma']),
 ('EVOL','Evolution',12,30,['origin of life','evidences of evolution','Darwin, natural selection and its types','Hardy-Weinberg principle','gene flow, genetic drift and mutation','adaptive radiation and human evolution']),
 ('HEALTH','Human Health and Diseases',12,20,['bacterial and viral diseases','protozoan, helminth and fungal diseases; malaria life cycle','innate and acquired immunity; antibodies','active and passive immunity; vaccines; allergy; autoimmunity','HIV and AIDS','cancer','drug and alcohol abuse']),
 ('MICRO','Microbes in Human Welfare',12,5,['food processing and industrial products','sewage treatment and biogas','biocontrol agents and biofertilizers','antibiotics']),
 ('BTP','Biotechnology: Principles and Processes',12,25,['restriction enzymes and ligase','cloning vectors and selectable markers','competent host and transformation methods','PCR','gel electrophoresis and isolation of DNA','screening recombinants: insertional inactivation','bioreactors and downstream processing']),
 ('BTA','Biotechnology and its Applications',12,10,['Bt crops and RNA interference','human insulin and vaccine production','gene therapy and stem cells','transgenic animals; tissue culture','biosafety, biopiracy and patents']),
 ('POP','Organisms and Populations',12,25,['population attributes: birth rate, death rate, age distribution','exponential and logistic growth','mutualism and commensalism','competition','predation and parasitism']),
 ('ECO','Ecosystem',12,15,['components and patterns of an ecosystem','productivity','decomposition','energy flow and food chains','ecological pyramids']),
 ('BIODIV','Biodiversity and its Conservation',12,15,['levels and patterns of biodiversity; species-area relation','importance of biodiversity','loss of biodiversity and extinction','in situ conservation: hotspots, reserves, parks, sacred groves','ex situ conservation; Red Data Book; Ramsar sites']),
],
'C': [
 ('MOLE','Some Basic Concepts of Chemistry',11,15,['laws of chemical combination','mole concept and molar mass','percentage composition; empirical and molecular formula','stoichiometry and limiting reagent','concentration terms in stoichiometry']),
 ('ATOM','Structure of Atom',11,20,['discovery of subatomic particles; isotopes and isobars','Thomson and Rutherford models','Bohr model and hydrogen spectrum','dual nature, de Broglie relation and uncertainty principle','quantum numbers and shapes of orbitals','Aufbau, Pauli and Hund rules; electronic configuration','stability of half-filled and filled subshells']),
 ('PERIOD','Classification of Elements and Periodicity; s and p block trends',11,25,['modern periodic law and the periodic table; IUPAC names for Z > 100','atomic, ionic and inert gas radii','ionization enthalpy','electron gain enthalpy and electronegativity','valency and oxidation state trends','s-block trends: radii, hydration enthalpy, reactivity','p-block trends across periods and down groups','unique behaviour of the first element of a group']),
 ('BOND','Chemical Bonding and Molecular Structure',11,35,['ionic bond and lattice considerations','Lewis structures and formal charge','bond parameters: length, angle, enthalpy, order','polarity, dipole moment and Fajans rules','valence bond theory and resonance','VSEPR and molecular geometry','hybridization with s, p and d orbitals','molecular orbital theory of homonuclear diatomics','hydrogen bond']),
 ('THERMO','Chemical Thermodynamics; The Gaseous State',11,35,['system, state functions, work and heat','first law: internal energy and enthalpy','heat capacity and measurement of ΔU and ΔH','Hess law and enthalpies of reaction','bond, combustion, formation, atomization and solution enthalpies','entropy and the second law','Gibbs energy and spontaneity; criteria for equilibrium','gas laws and the ideal gas equation','deviations from ideal behaviour']),
 ('EQUIL','Equilibrium',11,40,['dynamic nature; law of mass action; Kc and Kp','Le Chatelier principle','degree of dissociation in gaseous equilibria','ionization of weak acids and bases; degree of ionization','pH of acids, bases and mixtures','polybasic acids and acid strength','hydrolysis of salts','buffer solutions and Henderson equation','solubility product','common ion effect']),
 ('REDOX','Redox Reactions',11,15,['oxidation number','balancing redox reactions','types and applications of redox reactions; redox titration idea']),
 ('GOC','Organic Chemistry: Basic Principles and Techniques',11,25,['classification and IUPAC nomenclature','isomerism','inductive and electromeric effects','resonance and hyperconjugation','carbocations, carbanions and free radicals: stability','electrophiles, nucleophiles and types of organic reactions','methods of purification','qualitative analysis of elements','quantitative analysis']),
 ('HC','Hydrocarbons',11,40,['alkanes: conformations of ethane and free-radical halogenation','alkanes: combustion, pyrolysis and preparation','alkenes: geometrical isomerism and preparation','alkenes: electrophilic addition; Markovnikov and peroxide effect','alkenes: ozonolysis and oxidation','alkynes: acidic character and addition reactions','benzene: resonance and aromaticity','electrophilic aromatic substitution: mechanism','directive influence in monosubstituted benzene']),
 ('SOLN','Solutions',12,20,['concentration terms','solubility of gases: Henry law','Raoult law; ideal and non-ideal solutions','relative lowering of vapour pressure','elevation of boiling point and depression of freezing point','osmotic pressure','van\'t Hoff factor and abnormal molar mass']),
 ('ELECTRO','Electrochemistry',12,25,['galvanic cells and standard electrode potential','Nernst equation','Gibbs energy, EMF and equilibrium constant','conductance, conductivity and molar conductivity','Kohlrausch law','electrolysis and Faraday laws','batteries, fuel cells and corrosion']),
 ('KIN','Chemical Kinetics',12,30,['average and instantaneous rate','rate law, order and molecularity','zero order: integrated equation and half-life','first order: integrated equation and half-life','finding order from data','Arrhenius equation and activation energy','collision theory and catalysts']),
 ('DF','d and f Block Elements',12,30,['electronic configuration and oxidation states of 3d metals','ionization enthalpy, radii and metallic character','colour and magnetic properties','catalytic property, interstitial compounds and alloys','K2Cr2O7 and KMnO4: preparation and properties','lanthanides and lanthanide contraction','actinides compared with lanthanides']),
 ('COORD','Coordination Compounds',12,40,['Werner theory; ligands and coordination number','IUPAC nomenclature','structural isomerism','stereoisomerism','valence bond theory: hybridization and magnetism','crystal field theory: splitting, colour and magnetism','importance of coordination compounds']),
 ('HALO','Haloalkanes and Haloarenes',12,15,['nature of the C–X bond and physical properties','SN1 and SN2 mechanisms','optical rotation and stereochemistry of substitution','elimination versus substitution; other reactions','haloarenes: reactivity and directive influence','polyhalogen compounds: uses and environmental effects']),
 ('ALC','Alcohols, Phenols and Ethers',12,30,['alcohols: preparation','alcohols: reactions and mechanism of dehydration','identification of primary, secondary and tertiary alcohols','phenols: acidity','phenols: electrophilic substitution and named reactions','ethers: preparation and cleavage']),
 ('CARB','Aldehydes, Ketones and Carboxylic Acids',12,30,['preparation of aldehydes and ketones','nucleophilic addition: mechanism and reactivity','reactions of alpha hydrogen: aldol','oxidation, reduction and distinguishing tests','carboxylic acids: acidity and substituent effects','carboxylic acids: preparation and reactions']),
 ('AMINE','Amines',12,15,['classification, structure and basicity','preparation of amines','reactions and identification of primary, secondary and tertiary amines','diazonium salts']),
 ('BIOM','Biomolecules',12,15,['monosaccharides: glucose, fructose and D–L configuration','oligosaccharides and polysaccharides','amino acids, peptide bond and protein structure; denaturation','enzymes, hormones, vitamins and nucleic acids']),
],
'M': [
 ('SETS','Sets',11,10,['subsets, intervals and power set','union, intersection, difference and complement','counting with Venn diagrams']),
 ('RELFUN','Relations and Functions',11,40,['Cartesian product; domain and range of a relation','domain and range of real functions','modulus, signum and greatest integer functions','exponential and logarithmic functions and their graphs','algebra and composition of functions','reflexive, symmetric, transitive and equivalence relations','one-one and onto functions','functional equations and counting functions']),
 ('TRIG','Trigonometric Functions',11,25,['radian measure; signs, domain, range and graphs','sum and difference formulae','multiple angle identities: 2x and 3x','sum-to-product and product-to-sum','general solution of trigonometric equations']),
 ('PMI','Principle of Mathematical Induction',11,5,['the induction step and simple applications','divisibility and sum statements by induction']),
 ('CMPLX','Complex Numbers and Quadratic Equations',11,35,['algebra of complex numbers; conjugate and modulus','Argand plane and polar form','loci in the Argand plane','quadratic equations with real coefficients: complex roots','nature and relations of roots','polynomial equations: number of real roots','conditions on coefficients for rational or integer roots']),
 ('INEQ','Linear Inequalities',11,5,['inequalities in one variable','graphical solution in two variables','systems of linear inequalities']),
 ('PNC','Permutations and Combinations',11,20,['fundamental principle of counting','permutations with restrictions','permutations with repeated objects','combinations and selection problems','relations between nPr and nCr']),
 ('BINOM','Binomial Theorem',11,10,['general and middle term','coefficient extraction','sums of binomial coefficients and Pascal triangle']),
 ('SEQ','Sequence and Series',11,15,['arithmetic mean and its use','G.P.: general term and sum of n terms','infinite G.P.','A.M.–G.M. relation','special sums: Σk, Σk², Σk³']),
 ('LINES','Straight Lines',11,15,['slope and angle between two lines','forms of the equation of a line','distance of a point from a line; normal form','families of lines, concurrency and reflection']),
 ('CONIC','Conic Sections',11,40,['circle: standard equation','parabola: standard equation, focus, directrix, latus rectum','ellipse: standard equation and eccentricity','hyperbola: standard equation and eccentricity','degenerate conics and identifying a conic','circles touching lines and each other']),
 ('LIMDER','Limits and Derivatives',11,20,['limits of polynomial and rational functions','trigonometric limits','exponential and logarithmic limits','derivative from first principles and as a rate','product, quotient and chain rule']),
 ('STAT','Statistics',11,10,['range and mean deviation','variance and standard deviation of ungrouped data','variance and standard deviation of grouped data; effect of change of scale']),
 ('PROB','Probability',11,35,['sample space and events','addition rule; mutually exclusive and exhaustive events','classical probability with counting','conditional probability','multiplication theorem and independent events','total probability','Bayes theorem']),
 ('INVTRIG','Inverse Trigonometric Functions',12,15,['domain, range and principal values','graphs of inverse trigonometric functions','equations and compositions with principal values']),
 ('MATDET','Matrices and Determinants',12,35,['matrix operations and transpose','symmetric and skew-symmetric matrices','non-commutativity and zero divisors (order 2)','determinants up to 3 × 3: minors and cofactors','area of a triangle by determinants','adjoint and inverse','consistency and number of solutions of a linear system','solving a system using the inverse']),
 ('CONTDIFF','Continuity and Differentiability',12,35,['continuity of a function','differentiability and its relation to continuity','implicit and inverse trigonometric derivatives','logarithmic differentiation','parametric derivatives','second order derivatives']),
 ('AOD','Applications of Derivatives',12,25,['rate of change of quantities','increasing and decreasing functions','local maxima and minima: first and second derivative tests','absolute maxima and minima on an interval','optimisation in real-life situations']),
 ('INTEG','Integrals',12,40,['integration by substitution','integration by partial fractions','integration by parts','standard quadratic-denominator and square-root forms','Fundamental Theorem of Calculus','properties of definite integrals','evaluation of definite integrals']),
 ('AREA','Applications of the Integrals',12,10,['area under lines and parabolas','area of circles and ellipses and regions bounded with a line']),
 ('DE','Differential Equations',12,20,['order and degree; general and particular solutions','separation of variables','homogeneous equations','linear equations dy/dx + py = q and dx/dy + px = q']),
 ('VEC','Vectors',12,15,['direction cosines; position vector; section formula','scalar product and projections','vector product and areas','combined use of dot and cross products']),
 ('3D','Three-dimensional Geometry',12,15,['distance and section formula in space','direction cosines and equation of a line','angle between lines; skew lines and shortest distance']),
 ('LPP','Linear Programming',12,5,['feasible region and corner points','optimal value in bounded and unbounded regions']),
],
'P': [
 ('UNITS','Units and Measurements',11,20,['SI units; fundamental and derived units','significant figures','dimensional analysis and its applications']),
 ('KIN1D','Motion in a Straight Line',11,10,['average and instantaneous velocity','uniformly accelerated motion','graphs of rectilinear motion']),
 ('KIN2D','Motion in a Plane',11,15,['vectors: components, dot and cross product','motion in a plane with uniform acceleration','projectile motion','uniform circular motion']),
 ('NLM','Laws of Motion',11,20,['Newton laws and free-body analysis','impulse and conservation of momentum','equilibrium of concurrent forces','static, kinetic and rolling friction','dynamics of circular motion']),
 ('WEP','Work, Energy and Power',11,25,['work by constant and variable forces; work-energy theorem','potential energy and springs','conservative and non-conservative forces; power','motion in a vertical circle','collisions in one and two dimensions']),
 ('ROT','System of Particles and Rotational Motion',11,20,['centre of mass and its motion','torque and equilibrium of a rigid body','moment of inertia and radius of gyration','angular momentum and its conservation','rotational kinematics and dynamics compared with linear motion']),
 ('GRAV','Gravitation',11,20,['Kepler laws and the law of gravitation','variation of g with altitude and depth','gravitational potential energy and escape speed','orbital velocity and energy of a satellite']),
 ('SOLIDS','Mechanical Properties of Solids',11,5,['stress, strain and Hooke law; Young modulus','bulk and shear modulus; Poisson ratio','elastic energy and stress-strain curve']),
 ('FLUIDS','Mechanical Properties of Fluids',11,20,['pressure in a fluid column and Pascal law','Bernoulli theorem and Torricelli law','viscosity, Stokes law and terminal velocity','surface tension, excess pressure and capillary rise']),
 ('THERMAL','Thermal Properties of Matter',11,20,['thermal expansion','calorimetry and latent heat','conduction and thermal conductivity','radiation: Stefan and Wien laws; Newton law of cooling']),
 ('THERMO','Thermodynamics',11,25,['first law; heat, work and internal energy','isothermal and adiabatic processes','cyclic processes and P–V diagrams','second law and the Carnot engine']),
 ('KTG','Kinetic Theory of Gases',11,15,['ideal gas equation and pressure from kinetic theory','rms speed and kinetic interpretation of temperature','degrees of freedom, equipartition and specific heats','mean free path']),
 ('SHM','Oscillations',11,25,['displacement, velocity, acceleration and phase in SHM','energy in SHM','spring-mass systems','simple pendulum']),
 ('WAVES','Waves',11,20,['progressive wave equation and wave speed','superposition and reflection','standing waves in strings','standing waves in organ pipes','beats']),
 ('EFIELD','Electric Charges and Fields',12,25,['Coulomb law and superposition','electric field of point and continuous charges','electric dipole: field and torque','electric flux and Gauss theorem','field of charged line, sheet and shell']),
 ('EPOT','Electrostatic Potential and Capacitance',12,25,['potential of point charges and a dipole','equipotential surfaces; potential energy of a system','electrostatics of conductors','capacitors in series and parallel','dielectrics and energy stored in a capacitor']),
 ('CURR','Current Electricity',12,20,['drift velocity, mobility and Ohm law','resistivity and temperature dependence','electrical energy and power','cells: emf, internal resistance and combinations','Kirchhoff rules and Wheatstone bridge']),
 ('MAGMOV','Moving Charges and Magnetism',12,25,['Biot-Savart law','Ampere law and the solenoid','force on a moving charge in E and B fields','force on and between current-carrying conductors','torque on a current loop; magnetic dipole moment','moving coil galvanometer: sensitivity and conversion']),
 ('MAGMAT','Magnetism and Matter',12,5,['bar magnet as a dipole; torque; Gauss law for magnetism','magnetisation and magnetic intensity','dia-, para- and ferromagnetism; effect of temperature']),
 ('EMI','Electromagnetic Induction',12,10,['Faraday laws and Lenz law','motional emf','self and mutual induction']),
 ('AC','Alternating Current',12,10,['peak and rms values; phasors','R, L and C separately; reactance','series LR, LC and LCR circuits; impedance','resonance; power and power factor','AC generator and transformer']),
 ('EMW','Electromagnetic Waves',12,15,['displacement current','properties of electromagnetic waves','electromagnetic spectrum: sources and uses']),
 ('RAY','Ray Optics',12,30,['spherical mirrors','refraction and total internal reflection','refraction at spherical surfaces','thin lenses and lens maker formula','combination of lenses and power','prism']),
 ('WAVEOPT','Wave Optics',12,15,['Huygens principle: reflection and refraction','Young double slit experiment','coherence and sustained interference','single-slit diffraction']),
 ('DUAL','Dual Nature of Radiation and Matter',12,10,['photoelectric effect: observations','Einstein photoelectric equation','de Broglie relation']),
 ('ATOMS','Atoms',12,20,['alpha scattering and the Rutherford model','Bohr model: radius, velocity and energy','hydrogen line spectra']),
 ('NUCLEI','Nuclei',12,20,['size and composition of the nucleus; nuclear force','mass defect and binding energy per nucleon','fission and fusion']),
 ('SEMI','Semiconductor Electronics',12,10,['intrinsic and extrinsic semiconductors','p-n junction and diode I–V characteristics','diode as a rectifier']),
],
}



def build():
    rows = []
    for s, sname, first in SUBJECTS:
        chs = CH[s]
        assert sum(c[3] for c in chs) == TESTS * PER_SECTION, (s, sum(c[3] for c in chs))
        tokens = []
        for ci, (code, name, cls, n, foci) in enumerate(chs):
            assert n <= 7 * len(foci), (s, code, 'needs more focus lines')
            for j in range(n):
                f, r = j % len(foci), j // len(foci)
                tokens.append(((j + 0.5) / n, ci, code, name, cls, foci[f], ANGLES[s][(f + r + ci) % 7]))
        tokens.sort()
        # difficulty: 3 easy / 13 medium / 4 hard in every section, shared between chapters in proportion to their slots
        need = {c[0]: {'hard': c[3] * 0.20, 'easy': c[3] * 0.15} for c in chs}
        for t in range(TESTS):
            block = tokens[t * PER_SECTION:(t + 1) * PER_SECTION]
            block.sort(key=lambda x: ((x[1] + 5 * t) % len(chs), x[0]))
            diff = ['medium'] * PER_SECTION
            for level, k in (('hard', 4), ('easy', 3)):
                free = [i for i in range(PER_SECTION) if diff[i] == 'medium']
                free.sort(key=lambda i: (-need[block[i][2]][level], (i + 7 * t) % PER_SECTION))
                used = set()
                for i in free:
                    if len(used) == k: break
                    if block[i][2] in used and len(free) - free.index(i) > k - len(used): continue
                    diff[i] = level; need[block[i][2]][level] -= 1; used.add(block[i][2])
            for i, (_, ci, code, name, cls, focus, angle) in enumerate(block):
                q = first + i
                rows.append(dict(test=t + 1, question=q, id=f'NEST27-T{t+1:02}-Q{q:02}', section=s, subject=sname,
                                 chapter_code=f'{s}-{code}', chapter=name, class_level=cls, focus=focus, angle=angle,
                                 difficulty_target=diff[i], state='planned', source_json='', question_sha256='', notes=''))
    return rows


def check(rows):
    assert len(rows) == TESTS * 4 * PER_SECTION
    assert len({r['id'] for r in rows}) == len(rows)
    trip = collections.Counter((r['chapter_code'], r['focus'], r['angle']) for r in rows)
    assert max(trip.values()) == 1, 'a (chapter, focus, angle) task is planned twice'
    for t in range(1, TESTS + 1):
        for s, _, _ in SUBJECTS:
            sec = [r for r in rows if int(r['test']) == t and r['section'] == s]
            d = collections.Counter(r['difficulty_target'] for r in sec)
            assert len(sec) == 20 and (d['easy'], d['medium'], d['hard']) == (3, 13, 4), (t, s, d)
    planned = {(r['chapter_code'], r['focus']) for r in rows}
    for s, _, _ in SUBJECTS:
        for code, _, _, _, foci in CH[s]:
            for f in foci:
                assert (f'{s}-{code}', f) in planned, ('focus never planned', code, f)
    return True


if __name__ == '__main__':
    if '--check' in sys.argv:
        rows = list(csv.DictReader(open(OUT, encoding='utf-8')))
        check(rows); print('plan OK:', len(rows), 'slots')
    else:
        rows = build(); check(rows)
        if os.path.exists(OUT) and any(r['state'] != 'planned' for r in csv.DictReader(open(OUT, encoding='utf-8'))):
            sys.exit('refusing to overwrite: some slots are already authored. Edit the CSV rows instead.')
        with open(OUT, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
        print('wrote', OUT, len(rows), 'slots')
    for s, sname, _ in SUBJECTS:
        c11 = sum(c[3] for c in CH[s] if c[2] == 11)
        print(f'\n{sname}: Class 11 {c11} / Class 12 {500 - c11}; chapters {len(CH[s])}; focus lines {sum(len(c[4]) for c in CH[s])}')
        print(' | '.join(f'{c[0]} {c[3]}' for c in CH[s]))
