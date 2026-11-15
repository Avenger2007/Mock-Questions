# NEST 25-test plan

Written 15 November 2026. **Status: plan only; no NEST test is written yet.** The slot table is [NEST_25_Test_Plan.csv](NEST_25_Test_Plan.csv) (2,000 rows). It is built and checked by `tools/nest/plan_25_tests.py`. The rules for writing the tests are in [NISER_Test_Instructions.md](NISER_Test_Instructions.md) and the syllabus is in [Syllabus.md](Syllabus.md).

## What the plan fixes

- **25 tests × 80 questions = 2,000 slots**, 500 per subject. Each test has Biology Q1–20, Chemistry Q21–40, Mathematics Q41–60, Physics Q61–80.
- **Fixed IDs** `NEST27-TNN-QNN`.
- **Difficulty:** 3 easy, 13 medium, 4 hard in every section of every test. Each chapter gets about 15% easy and 20% hard of its own slots.
- **Coverage:** every chapter of the official syllabus has slots, spread evenly over the 25 tests, and every focus line is used at least once.
- **No repetition by design:** every slot has a different (chapter, focus, angle). The focus is the syllabus sub-topic; the angle is the kind of task. A focus that returns later in the series returns with a different task.

## How it was built (and its limits)

- Method taken from the IAT plan (`docs/blueprints/iat_25_test_plan.md` and `.csv`): fixed slots, a chapter taxonomy from the official syllabus, a stated difficulty mix, and a record per question that is updated when the test is written.
- Changes from the IAT plan, made because of the IAT audit: uniqueness of (chapter, focus, angle) is enforced by the checker; the plan and the tests are reconciled in the same commit; chapters not in the syllabus have no slots.
- **Chapter weights follow syllabus breadth. They are not yet calibrated against NEST previous-year papers.** The official papers with answers are on `https://www.nestexam.in`. Calibrate before Test 1: change the slot numbers in the script, regenerate, and re-check.
- The NEST 2027 syllabus was not published on 15 November 2026; the plan uses the NEST 2026 syllabus.
- The `angle` is a brief, not a format label. The question `format` (numerical, conceptual, graph, data, diagram, experiment) is set when the question is written.

## CSV columns

| Column | Meaning |
|---|---|
| `test`, `question`, `id` | fixed position and ID |
| `section`, `subject` | B, C, M or P |
| `chapter_code`, `chapter`, `class_level` | chapter from `Syllabus.md` |
| `focus` | the syllabus sub-topic the question must test |
| `angle` | the kind of task |
| `difficulty_target` | easy, medium or hard |
| `state` | `planned`, then `authored`, then `audited` |
| `source_json`, `question_sha256` | filled when the question exists |
| `notes` | reason for any change to the slot |

## Task angles

- **Biology:** mechanism or reason; experiment or observation to interpret; data, table or graph to read; compare two structures or processes; applied case (disorder, mutation, changed condition); quantitative (ratio, count, rate, probability); order of steps or pathway logic.
- **Chemistry:** concept with reason; numerical, multi-step; structure or mechanism; trend or ordering with reason; experiment or laboratory observation; data or graph to read; two linked reactions or ideas.
- **Mathematics:** multi-step computation; condition on a parameter; counting or existence of solutions; geometric interpretation; behaviour or graph of a function; inverse problem (find the data); special or limiting case.
- **Physics:** numerical, multi-step; conceptual, qualitative; graph to read or to choose; scaling or limiting case; experiment or measurement; compare two situations; conservation-law approach.

## Chapter allocation

### Biology (500 slots; Class 11: 255, Class 12: 245)

| Code | Chapter | Class | Slots | Easy / Medium / Hard | Focus lines |
|---|---|---:|---:|---:|---:|
| `B-LIVCLS` | The Living World; Biological Classification | 11 | 15 | 3 / 9 / 3 | 6 |
| `B-PLANTK` | Plant Kingdom | 11 | 10 | 2 / 6 / 2 | 4 |
| `B-ANIMK` | Animal Kingdom | 11 | 15 | 2 / 10 / 3 | 5 |
| `B-MORPH` | Morphology of Flowering Plants | 11 | 10 | 1 / 7 / 2 | 4 |
| `B-ANAT` | Anatomy of Flowering Plants | 11 | 10 | 1 / 7 / 2 | 4 |
| `B-FROG` | Structural Organisation in Animals (frog) | 11 | 5 | 0 / 4 / 1 | 3 |
| `B-CELL` | Cell: The Unit of Life | 11 | 20 | 3 / 13 / 4 | 7 |
| `B-BIOMOL` | Biomolecules | 11 | 20 | 3 / 13 / 4 | 6 |
| `B-CYCLE` | Cell Cycle and Cell Division | 11 | 15 | 2 / 10 / 3 | 5 |
| `B-PHOTO` | Photosynthesis in Higher Plants | 11 | 20 | 3 / 13 / 4 | 6 |
| `B-RESP` | Respiration in Plants | 11 | 15 | 2 / 10 / 3 | 5 |
| `B-PGR` | Plant Growth and Development | 11 | 10 | 1 / 7 / 2 | 4 |
| `B-BREATH` | Breathing and Exchange of Gases | 11 | 10 | 2 / 6 / 2 | 4 |
| `B-CIRC` | Body Fluids and Circulation | 11 | 15 | 2 / 10 / 3 | 5 |
| `B-DIGEST` | Digestion and Absorption | 11 | 10 | 2 / 6 / 2 | 4 |
| `B-EXCR` | Excretory Products and their Elimination | 11 | 15 | 3 / 9 / 3 | 5 |
| `B-LOCO` | Locomotion and Movement | 11 | 10 | 1 / 7 / 2 | 4 |
| `B-NEURAL` | Neural Control and Coordination | 11 | 15 | 2 / 10 / 3 | 5 |
| `B-ENDO` | Chemical Coordination and Integration | 11 | 15 | 2 / 10 / 3 | 6 |
| `B-REPFL` | Sexual Reproduction in Flowering Plants | 12 | 15 | 2 / 10 / 3 | 6 |
| `B-HUMREP` | Human Reproduction | 12 | 15 | 2 / 10 / 3 | 5 |
| `B-REPH` | Reproductive Health | 12 | 5 | 1 / 4 / 0 | 3 |
| `B-INHER` | Principles of Inheritance and Variation | 12 | 35 | 5 / 23 / 7 | 11 |
| `B-MOLB` | Molecular Basis of Inheritance | 12 | 35 | 5 / 23 / 7 | 11 |
| `B-EVOL` | Evolution | 12 | 20 | 3 / 13 / 4 | 6 |
| `B-HEALTH` | Human Health and Diseases | 12 | 20 | 3 / 12 / 5 | 7 |
| `B-MICRO` | Microbes in Human Welfare | 12 | 10 | 1 / 7 / 2 | 4 |
| `B-BTP` | Biotechnology: Principles and Processes | 12 | 25 | 4 / 16 / 5 | 7 |
| `B-BTA` | Biotechnology and its Applications | 12 | 15 | 3 / 9 / 3 | 5 |
| `B-POP` | Organisms and Populations | 12 | 20 | 3 / 13 / 4 | 5 |
| `B-ECO` | Ecosystem | 12 | 15 | 3 / 9 / 3 | 5 |
| `B-BIODIV` | Biodiversity and its Conservation | 12 | 15 | 3 / 9 / 3 | 5 |

### Chemistry (500 slots; Class 11: 270, Class 12: 230)

| Code | Chapter | Class | Slots | Easy / Medium / Hard | Focus lines |
|---|---|---:|---:|---:|---:|
| `C-MOLE` | Some Basic Concepts of Chemistry | 11 | 20 | 3 / 13 / 4 | 5 |
| `C-ATOM` | Structure of Atom | 11 | 25 | 4 / 16 / 5 | 7 |
| `C-PERIOD` | Classification of Elements and Periodicity; s and p block trends | 11 | 30 | 5 / 19 / 6 | 8 |
| `C-BOND` | Chemical Bonding and Molecular Structure | 11 | 35 | 5 / 23 / 7 | 9 |
| `C-THERMO` | Chemical Thermodynamics; The Gaseous State | 11 | 35 | 5 / 23 / 7 | 9 |
| `C-EQUIL` | Equilibrium | 11 | 40 | 6 / 26 / 8 | 10 |
| `C-REDOX` | Redox Reactions | 11 | 15 | 2 / 10 / 3 | 3 |
| `C-GOC` | Organic Chemistry: Basic Principles and Techniques | 11 | 35 | 5 / 23 / 7 | 9 |
| `C-HC` | Hydrocarbons | 11 | 35 | 5 / 23 / 7 | 9 |
| `C-SOLN` | Solutions | 12 | 25 | 4 / 16 / 5 | 7 |
| `C-ELECTRO` | Electrochemistry | 12 | 30 | 5 / 19 / 6 | 7 |
| `C-KIN` | Chemical Kinetics | 12 | 30 | 5 / 19 / 6 | 7 |
| `C-DF` | d and f Block Elements | 12 | 25 | 4 / 16 / 5 | 7 |
| `C-COORD` | Coordination Compounds | 12 | 30 | 4 / 20 / 6 | 7 |
| `C-HALO` | Haloalkanes and Haloarenes | 12 | 20 | 3 / 13 / 4 | 6 |
| `C-ALC` | Alcohols, Phenols and Ethers | 12 | 20 | 3 / 13 / 4 | 6 |
| `C-CARB` | Aldehydes, Ketones and Carboxylic Acids | 12 | 25 | 4 / 16 / 5 | 6 |
| `C-AMINE` | Amines | 12 | 15 | 2 / 10 / 3 | 4 |
| `C-BIOM` | Biomolecules | 12 | 10 | 1 / 7 / 2 | 4 |

### Mathematics (500 slots; Class 11: 285, Class 12: 215)

| Code | Chapter | Class | Slots | Easy / Medium / Hard | Focus lines |
|---|---|---:|---:|---:|---:|
| `M-SETS` | Sets | 11 | 10 | 1 / 8 / 1 | 3 |
| `M-RELFUN` | Relations and Functions | 11 | 30 | 5 / 19 / 6 | 7 |
| `M-TRIG` | Trigonometric Functions | 11 | 25 | 4 / 16 / 5 | 5 |
| `M-PMI` | Principle of Mathematical Induction | 11 | 5 | 0 / 4 / 1 | 2 |
| `M-CMPLX` | Complex Numbers and Quadratic Equations | 11 | 25 | 4 / 16 / 5 | 5 |
| `M-INEQ` | Linear Inequalities | 11 | 10 | 2 / 6 / 2 | 3 |
| `M-PNC` | Permutations and Combinations | 11 | 25 | 4 / 16 / 5 | 5 |
| `M-BINOM` | Binomial Theorem | 11 | 15 | 2 / 10 / 3 | 3 |
| `M-SEQ` | Sequence and Series | 11 | 20 | 3 / 13 / 4 | 5 |
| `M-LINES` | Straight Lines | 11 | 20 | 3 / 13 / 4 | 4 |
| `M-CONIC` | Conic Sections | 11 | 30 | 5 / 19 / 6 | 5 |
| `M-LIMDER` | Limits and Derivatives | 11 | 20 | 3 / 13 / 4 | 5 |
| `M-STAT` | Statistics | 11 | 15 | 2 / 10 / 3 | 3 |
| `M-PROB` | Probability | 11 | 35 | 5 / 23 / 7 | 7 |
| `M-INVTRIG` | Inverse Trigonometric Functions | 12 | 15 | 2 / 10 / 3 | 3 |
| `M-MATDET` | Matrices and Determinants | 12 | 35 | 5 / 22 / 8 | 8 |
| `M-CONTDIFF` | Continuity and Differentiability | 12 | 25 | 4 / 16 / 5 | 6 |
| `M-AOD` | Applications of Derivatives | 12 | 30 | 5 / 19 / 6 | 5 |
| `M-INTEG` | Integrals | 12 | 35 | 6 / 22 / 7 | 7 |
| `M-AREA` | Applications of the Integrals | 12 | 10 | 1 / 7 / 2 | 2 |
| `M-DE` | Differential Equations | 12 | 20 | 3 / 13 / 4 | 4 |
| `M-VEC` | Vectors | 12 | 20 | 3 / 13 / 4 | 4 |
| `M-3D` | Three-dimensional Geometry | 12 | 15 | 2 / 10 / 3 | 3 |
| `M-LPP` | Linear Programming | 12 | 10 | 1 / 7 / 2 | 2 |

### Physics (500 slots; Class 11: 260, Class 12: 240)

| Code | Chapter | Class | Slots | Easy / Medium / Hard | Focus lines |
|---|---|---:|---:|---:|---:|
| `P-UNITS` | Units and Measurements | 11 | 10 | 1 / 7 / 2 | 3 |
| `P-KIN1D` | Motion in a Straight Line | 11 | 15 | 2 / 10 / 3 | 3 |
| `P-KIN2D` | Motion in a Plane | 11 | 20 | 3 / 13 / 4 | 4 |
| `P-NLM` | Laws of Motion | 11 | 25 | 4 / 16 / 5 | 5 |
| `P-WEP` | Work, Energy and Power | 11 | 25 | 4 / 16 / 5 | 5 |
| `P-ROT` | System of Particles and Rotational Motion | 11 | 25 | 4 / 16 / 5 | 5 |
| `P-GRAV` | Gravitation | 11 | 20 | 3 / 13 / 4 | 4 |
| `P-SOLIDS` | Mechanical Properties of Solids | 11 | 10 | 1 / 7 / 2 | 3 |
| `P-FLUIDS` | Mechanical Properties of Fluids | 11 | 20 | 3 / 13 / 4 | 4 |
| `P-THERMAL` | Thermal Properties of Matter | 11 | 15 | 3 / 9 / 3 | 4 |
| `P-THERMO` | Thermodynamics | 11 | 20 | 3 / 13 / 4 | 4 |
| `P-KTG` | Kinetic Theory of Gases | 11 | 15 | 2 / 9 / 4 | 4 |
| `P-SHM` | Oscillations | 11 | 20 | 3 / 12 / 5 | 4 |
| `P-WAVES` | Waves | 11 | 20 | 3 / 13 / 4 | 5 |
| `P-EFIELD` | Electric Charges and Fields | 12 | 25 | 4 / 16 / 5 | 5 |
| `P-EPOT` | Electrostatic Potential and Capacitance | 12 | 25 | 4 / 16 / 5 | 5 |
| `P-CURR` | Current Electricity | 12 | 25 | 4 / 16 / 5 | 5 |
| `P-MAGMOV` | Moving Charges and Magnetism | 12 | 25 | 4 / 16 / 5 | 6 |
| `P-MAGMAT` | Magnetism and Matter | 12 | 10 | 1 / 8 / 1 | 3 |
| `P-EMI` | Electromagnetic Induction | 12 | 15 | 3 / 9 / 3 | 3 |
| `P-AC` | Alternating Current | 12 | 20 | 3 / 13 / 4 | 5 |
| `P-EMW` | Electromagnetic Waves | 12 | 10 | 1 / 8 / 1 | 3 |
| `P-RAY` | Ray Optics | 12 | 25 | 4 / 16 / 5 | 6 |
| `P-WAVEOPT` | Wave Optics | 12 | 15 | 2 / 10 / 3 | 4 |
| `P-DUAL` | Dual Nature of Radiation and Matter | 12 | 15 | 2 / 10 / 3 | 3 |
| `P-ATOMS` | Atoms | 12 | 10 | 1 / 7 / 2 | 3 |
| `P-NUCLEI` | Nuclei | 12 | 10 | 1 / 7 / 2 | 3 |
| `P-SEMI` | Semiconductor Electronics | 12 | 10 | 2 / 6 / 2 | 3 |

## Focus lines by chapter

### Biology

- **The Living World; Biological Classification** (`B-LIVCLS`): three domains, taxonomic hierarchy and binomial nomenclature; concept of species; taxonomy and systematics; five kingdom classification: criteria; Monera and Protista: major groups; Fungi: major groups and life cycles; lichens, viruses and viroids.
- **Plant Kingdom** (`B-PLANTK`): algae: groups and distinguishing features; bryophytes and pteridophytes: dominant generation; gymnosperms and angiosperms: distinguishing features; comparing major plant groups.
- **Animal Kingdom** (`B-ANIMK`): basis of classification: symmetry, coelom, germ layers; non-chordate phyla: Porifera to Aschelminthes; non-chordate phyla: Annelida to Hemichordata; chordate classes: fishes and amphibians; chordate classes: reptiles, birds and mammals.
- **Morphology of Flowering Plants** (`B-MORPH`): root, stem and leaf modifications; inflorescence and flower: parts, symmetry, aestivation, placentation; fruit and seed structure; floral formula and family Solanaceae.
- **Anatomy of Flowering Plants** (`B-ANAT`): tissue systems: epidermal, ground, vascular; dicot and monocot root; dicot and monocot stem; dicot and monocot leaf.
- **Structural Organisation in Animals (frog)** (`B-FROG`): frog: digestive and respiratory systems; frog: circulatory and nervous systems; frog: reproductive system and morphology.
- **Cell: The Unit of Life** (`B-CELL`): prokaryotic and eukaryotic cells; cell theory; cell membrane and cell wall; endomembrane system: ER, Golgi, lysosomes, vacuoles; mitochondria, plastids and ribosomes; cytoskeleton, cilia, flagella, centrioles; nucleus and chromosomes; plant cell and animal cell compared.
- **Biomolecules** (`B-BIOMOL`): metabolites and chemical composition of cells; proteins: levels of structure and function; carbohydrates and lipids; nucleic acids: structure; enzymes: properties and types; enzyme action: kinetics, inhibition, temperature and pH.
- **Cell Cycle and Cell Division** (`B-CYCLE`): phases of the cell cycle and DNA content; mitosis: stages and significance; meiosis I: prophase I events and segregation; meiosis II and significance of meiosis; mitosis and meiosis compared.
- **Photosynthesis in Higher Plants** (`B-PHOTO`): site of photosynthesis and pigments; light reaction and electron transport; cyclic and non-cyclic photophosphorylation; chemiosmosis; Calvin cycle: use of ATP and NADPH; photorespiration and the C4 pathway; factors affecting photosynthesis.
- **Respiration in Plants** (`B-RESP`): glycolysis and fermentation; TCA cycle; electron transport system and oxidative phosphorylation; respiratory balance sheet and ATP count; amphibolic pathway and respiratory quotient.
- **Plant Growth and Development** (`B-PGR`): seed germination, growth phases and growth rate; differentiation, dedifferentiation, redifferentiation; auxin, gibberellin and cytokinin; ethylene and abscisic acid.
- **Breathing and Exchange of Gases** (`B-BREATH`): respiratory system and mechanism of breathing; respiratory volumes and capacities; exchange and transport of gases; regulation of respiration and disorders.
- **Body Fluids and Circulation** (`B-CIRC`): blood: composition, groups and coagulation; heart structure and double circulation; cardiac cycle and cardiac output; ECG and regulation of cardiac activity; lymph and circulatory disorders.
- **Digestion and Absorption** (`B-DIGEST`): alimentary canal and digestive glands; digestive enzymes and gastrointestinal hormones; absorption and assimilation; calorific values; nutritional and digestive disorders.
- **Excretory Products and their Elimination** (`B-EXCR`): modes of excretion; nephron structure and urine formation; concentration of filtrate: counter-current mechanism; regulation: RAAS, ANF, ADH; micturition; excretory disorders, dialysis and other organs.
- **Locomotion and Movement** (`B-LOCO`): types of movement and muscle types; contractile proteins and sliding filament mechanism; skeletal system and joints; muscular and skeletal disorders.
- **Neural Control and Coordination** (`B-NEURAL`): neuron structure and types; resting potential and generation of nerve impulse; conduction and synaptic transmission; central neural system: brain regions; peripheral and visceral nervous systems.
- **Chemical Coordination and Integration** (`B-ENDO`): hypothalamus and pituitary; thyroid, parathyroid and pineal; adrenal and pancreas; gonads; hormones of heart, kidney and gut; mechanism of hormone action; hypo- and hyperactivity disorders.
- **Sexual Reproduction in Flowering Plants** (`B-REPFL`): microsporogenesis and male gametophyte; megasporogenesis and embryo sac; pollination and outbreeding devices; pollen-pistil interaction and double fertilization; endosperm, embryo, seed and fruit; apomixis, parthenocarpy, polyembryony.
- **Human Reproduction** (`B-HUMREP`): male reproductive system and spermatogenesis; female reproductive system and oogenesis; menstrual cycle and its hormones; fertilisation, cleavage and implantation; pregnancy, placenta, parturition and lactation.
- **Reproductive Health** (`B-REPH`): contraception and MTP; STDs and amniocentesis; infertility and assisted reproductive technologies.
- **Principles of Inheritance and Variation** (`B-INHER`): law of dominance and segregation: monohybrid ratios; inheritance of two genes: dihybrid ratios; incomplete dominance and co-dominance; multiple alleles and blood groups; pleiotropy; polygenic inheritance; chromosome theory; linkage and recombination; sex determination in humans, birds and honey bee; pedigree analysis; sex-linked disorders: haemophilia, colour blindness; autosomal disorders: sickle-cell, thalassemia, PKU; chromosomal disorders: Down, Turner, Klinefelter.
- **Molecular Basis of Inheritance** (`B-MOLB`): search for genetic material: Griffith, Avery, Hershey-Chase; structure of DNA and RNA; base pairing rules; DNA packaging; DNA replication: Meselson-Stahl and the machinery; transcription in prokaryotes and eukaryotes; genetic code and mutations; translation; lac operon; Human and rice genome projects; DNA fingerprinting; RNA world and Central Dogma.
- **Evolution** (`B-EVOL`): origin of life; evidences of evolution; Darwin, natural selection and its types; Hardy-Weinberg principle; gene flow, genetic drift and mutation; adaptive radiation and human evolution.
- **Human Health and Diseases** (`B-HEALTH`): bacterial and viral diseases; protozoan, helminth and fungal diseases; malaria life cycle; innate and acquired immunity; antibodies; active and passive immunity; vaccines; allergy; autoimmunity; HIV and AIDS; cancer; drug and alcohol abuse.
- **Microbes in Human Welfare** (`B-MICRO`): food processing and industrial products; sewage treatment and biogas; biocontrol agents and biofertilizers; antibiotics.
- **Biotechnology: Principles and Processes** (`B-BTP`): restriction enzymes and ligase; cloning vectors and selectable markers; competent host and transformation methods; PCR; gel electrophoresis and isolation of DNA; screening recombinants: insertional inactivation; bioreactors and downstream processing.
- **Biotechnology and its Applications** (`B-BTA`): Bt crops and RNA interference; human insulin and vaccine production; gene therapy and stem cells; transgenic animals; tissue culture; biosafety, biopiracy and patents.
- **Organisms and Populations** (`B-POP`): population attributes: birth rate, death rate, age distribution; exponential and logistic growth; mutualism and commensalism; competition; predation and parasitism.
- **Ecosystem** (`B-ECO`): components and patterns of an ecosystem; productivity; decomposition; energy flow and food chains; ecological pyramids.
- **Biodiversity and its Conservation** (`B-BIODIV`): levels and patterns of biodiversity; species-area relation; importance of biodiversity; loss of biodiversity and extinction; in situ conservation: hotspots, reserves, parks, sacred groves; ex situ conservation; Red Data Book; Ramsar sites.

### Chemistry

- **Some Basic Concepts of Chemistry** (`C-MOLE`): laws of chemical combination; mole concept and molar mass; percentage composition; empirical and molecular formula; stoichiometry and limiting reagent; concentration terms in stoichiometry.
- **Structure of Atom** (`C-ATOM`): discovery of subatomic particles; isotopes and isobars; Thomson and Rutherford models; Bohr model and hydrogen spectrum; dual nature, de Broglie relation and uncertainty principle; quantum numbers and shapes of orbitals; Aufbau, Pauli and Hund rules; electronic configuration; stability of half-filled and filled subshells.
- **Classification of Elements and Periodicity; s and p block trends** (`C-PERIOD`): modern periodic law and the periodic table; IUPAC names for Z > 100; atomic, ionic and inert gas radii; ionization enthalpy; electron gain enthalpy and electronegativity; valency and oxidation state trends; s-block trends: radii, hydration enthalpy, reactivity; p-block trends across periods and down groups; unique behaviour of the first element of a group.
- **Chemical Bonding and Molecular Structure** (`C-BOND`): ionic bond and lattice considerations; Lewis structures and formal charge; bond parameters: length, angle, enthalpy, order; polarity, dipole moment and Fajans rules; valence bond theory and resonance; VSEPR and molecular geometry; hybridization with s, p and d orbitals; molecular orbital theory of homonuclear diatomics; hydrogen bond.
- **Chemical Thermodynamics; The Gaseous State** (`C-THERMO`): system, state functions, work and heat; first law: internal energy and enthalpy; heat capacity and measurement of ΔU and ΔH; Hess law and enthalpies of reaction; bond, combustion, formation, atomization and solution enthalpies; entropy and the second law; Gibbs energy and spontaneity; criteria for equilibrium; gas laws and the ideal gas equation; deviations from ideal behaviour.
- **Equilibrium** (`C-EQUIL`): dynamic nature; law of mass action; Kc and Kp; Le Chatelier principle; degree of dissociation in gaseous equilibria; ionization of weak acids and bases; degree of ionization; pH of acids, bases and mixtures; polybasic acids and acid strength; hydrolysis of salts; buffer solutions and Henderson equation; solubility product; common ion effect.
- **Redox Reactions** (`C-REDOX`): oxidation number; balancing redox reactions; types and applications of redox reactions; redox titration idea.
- **Organic Chemistry: Basic Principles and Techniques** (`C-GOC`): classification and IUPAC nomenclature; isomerism; inductive and electromeric effects; resonance and hyperconjugation; carbocations, carbanions and free radicals: stability; electrophiles, nucleophiles and types of organic reactions; methods of purification; qualitative analysis of elements; quantitative analysis.
- **Hydrocarbons** (`C-HC`): alkanes: conformations of ethane and free-radical halogenation; alkanes: combustion, pyrolysis and preparation; alkenes: geometrical isomerism and preparation; alkenes: electrophilic addition; Markovnikov and peroxide effect; alkenes: ozonolysis and oxidation; alkynes: acidic character and addition reactions; benzene: resonance and aromaticity; electrophilic aromatic substitution: mechanism; directive influence in monosubstituted benzene.
- **Solutions** (`C-SOLN`): concentration terms; solubility of gases: Henry law; Raoult law; ideal and non-ideal solutions; relative lowering of vapour pressure; elevation of boiling point and depression of freezing point; osmotic pressure; van't Hoff factor and abnormal molar mass.
- **Electrochemistry** (`C-ELECTRO`): galvanic cells and standard electrode potential; Nernst equation; Gibbs energy, EMF and equilibrium constant; conductance, conductivity and molar conductivity; Kohlrausch law; electrolysis and Faraday laws; batteries, fuel cells and corrosion.
- **Chemical Kinetics** (`C-KIN`): average and instantaneous rate; rate law, order and molecularity; zero order: integrated equation and half-life; first order: integrated equation and half-life; finding order from data; Arrhenius equation and activation energy; collision theory and catalysts.
- **d and f Block Elements** (`C-DF`): electronic configuration and oxidation states of 3d metals; ionization enthalpy, radii and metallic character; colour and magnetic properties; catalytic property, interstitial compounds and alloys; K2Cr2O7 and KMnO4: preparation and properties; lanthanides and lanthanide contraction; actinides compared with lanthanides.
- **Coordination Compounds** (`C-COORD`): Werner theory; ligands and coordination number; IUPAC nomenclature; structural isomerism; stereoisomerism; valence bond theory: hybridization and magnetism; crystal field theory: splitting, colour and magnetism; importance of coordination compounds.
- **Haloalkanes and Haloarenes** (`C-HALO`): nature of the C–X bond and physical properties; SN1 and SN2 mechanisms; optical rotation and stereochemistry of substitution; elimination versus substitution; other reactions; haloarenes: reactivity and directive influence; polyhalogen compounds: uses and environmental effects.
- **Alcohols, Phenols and Ethers** (`C-ALC`): alcohols: preparation; alcohols: reactions and mechanism of dehydration; identification of primary, secondary and tertiary alcohols; phenols: acidity; phenols: electrophilic substitution and named reactions; ethers: preparation and cleavage.
- **Aldehydes, Ketones and Carboxylic Acids** (`C-CARB`): preparation of aldehydes and ketones; nucleophilic addition: mechanism and reactivity; reactions of alpha hydrogen: aldol; oxidation, reduction and distinguishing tests; carboxylic acids: acidity and substituent effects; carboxylic acids: preparation and reactions.
- **Amines** (`C-AMINE`): classification, structure and basicity; preparation of amines; reactions and identification of primary, secondary and tertiary amines; diazonium salts.
- **Biomolecules** (`C-BIOM`): monosaccharides: glucose, fructose and D–L configuration; oligosaccharides and polysaccharides; amino acids, peptide bond and protein structure; denaturation; enzymes, hormones, vitamins and nucleic acids.

### Mathematics

- **Sets** (`M-SETS`): subsets, intervals and power set; union, intersection, difference and complement; counting with Venn diagrams.
- **Relations and Functions** (`M-RELFUN`): Cartesian product; domain and range of a relation; domain and range of real functions; modulus, signum and greatest integer functions; exponential and logarithmic functions and their graphs; algebra and composition of functions; reflexive, symmetric, transitive and equivalence relations; one-one and onto functions.
- **Trigonometric Functions** (`M-TRIG`): radian measure; signs, domain, range and graphs; sum and difference formulae; multiple angle identities: 2x and 3x; sum-to-product and product-to-sum; general solution of trigonometric equations.
- **Principle of Mathematical Induction** (`M-PMI`): the induction step and simple applications; divisibility and sum statements by induction.
- **Complex Numbers and Quadratic Equations** (`M-CMPLX`): algebra of complex numbers; conjugate and modulus; Argand plane and polar form; loci in the Argand plane; quadratic equations with real coefficients: complex roots; nature and relations of roots.
- **Linear Inequalities** (`M-INEQ`): inequalities in one variable; graphical solution in two variables; systems of linear inequalities.
- **Permutations and Combinations** (`M-PNC`): fundamental principle of counting; permutations with restrictions; permutations with repeated objects; combinations and selection problems; relations between nPr and nCr.
- **Binomial Theorem** (`M-BINOM`): general and middle term; coefficient extraction; sums of binomial coefficients and Pascal triangle.
- **Sequence and Series** (`M-SEQ`): arithmetic mean and its use; G.P.: general term and sum of n terms; infinite G.P.; A.M.–G.M. relation; special sums: Σk, Σk², Σk³.
- **Straight Lines** (`M-LINES`): slope and angle between two lines; forms of the equation of a line; distance of a point from a line; normal form; families of lines, concurrency and reflection.
- **Conic Sections** (`M-CONIC`): circle: standard equation; parabola: standard equation, focus, directrix, latus rectum; ellipse: standard equation and eccentricity; hyperbola: standard equation and eccentricity; degenerate conics and identifying a conic.
- **Limits and Derivatives** (`M-LIMDER`): limits of polynomial and rational functions; trigonometric limits; exponential and logarithmic limits; derivative from first principles and as a rate; product, quotient and chain rule.
- **Statistics** (`M-STAT`): range and mean deviation; variance and standard deviation of ungrouped data; variance and standard deviation of grouped data; effect of change of scale.
- **Probability** (`M-PROB`): sample space and events; addition rule; mutually exclusive and exhaustive events; classical probability with counting; conditional probability; multiplication theorem and independent events; total probability; Bayes theorem.
- **Inverse Trigonometric Functions** (`M-INVTRIG`): domain, range and principal values; graphs of inverse trigonometric functions; equations and compositions with principal values.
- **Matrices and Determinants** (`M-MATDET`): matrix operations and transpose; symmetric and skew-symmetric matrices; non-commutativity and zero divisors (order 2); determinants up to 3 × 3: minors and cofactors; area of a triangle by determinants; adjoint and inverse; consistency and number of solutions of a linear system; solving a system using the inverse.
- **Continuity and Differentiability** (`M-CONTDIFF`): continuity of a function; differentiability and its relation to continuity; implicit and inverse trigonometric derivatives; logarithmic differentiation; parametric derivatives; second order derivatives.
- **Applications of Derivatives** (`M-AOD`): rate of change of quantities; increasing and decreasing functions; local maxima and minima: first and second derivative tests; absolute maxima and minima on an interval; optimisation in real-life situations.
- **Integrals** (`M-INTEG`): integration by substitution; integration by partial fractions; integration by parts; standard quadratic-denominator and square-root forms; Fundamental Theorem of Calculus; properties of definite integrals; evaluation of definite integrals.
- **Applications of the Integrals** (`M-AREA`): area under lines and parabolas; area of circles and ellipses and regions bounded with a line.
- **Differential Equations** (`M-DE`): order and degree; general and particular solutions; separation of variables; homogeneous equations; linear equations dy/dx + py = q and dx/dy + px = q.
- **Vectors** (`M-VEC`): direction cosines; position vector; section formula; scalar product and projections; vector product and areas; combined use of dot and cross products.
- **Three-dimensional Geometry** (`M-3D`): distance and section formula in space; direction cosines and equation of a line; angle between lines; skew lines and shortest distance.
- **Linear Programming** (`M-LPP`): feasible region and corner points; optimal value in bounded and unbounded regions.

### Physics

- **Units and Measurements** (`P-UNITS`): SI units; fundamental and derived units; significant figures; dimensional analysis and its applications.
- **Motion in a Straight Line** (`P-KIN1D`): average and instantaneous velocity; uniformly accelerated motion; graphs of rectilinear motion.
- **Motion in a Plane** (`P-KIN2D`): vectors: components, dot and cross product; motion in a plane with uniform acceleration; projectile motion; uniform circular motion.
- **Laws of Motion** (`P-NLM`): Newton laws and free-body analysis; impulse and conservation of momentum; equilibrium of concurrent forces; static, kinetic and rolling friction; dynamics of circular motion.
- **Work, Energy and Power** (`P-WEP`): work by constant and variable forces; work-energy theorem; potential energy and springs; conservative and non-conservative forces; power; motion in a vertical circle; collisions in one and two dimensions.
- **System of Particles and Rotational Motion** (`P-ROT`): centre of mass and its motion; torque and equilibrium of a rigid body; moment of inertia and radius of gyration; angular momentum and its conservation; rotational kinematics and dynamics compared with linear motion.
- **Gravitation** (`P-GRAV`): Kepler laws and the law of gravitation; variation of g with altitude and depth; gravitational potential energy and escape speed; orbital velocity and energy of a satellite.
- **Mechanical Properties of Solids** (`P-SOLIDS`): stress, strain and Hooke law; Young modulus; bulk and shear modulus; Poisson ratio; elastic energy and stress-strain curve.
- **Mechanical Properties of Fluids** (`P-FLUIDS`): pressure in a fluid column and Pascal law; Bernoulli theorem and Torricelli law; viscosity, Stokes law and terminal velocity; surface tension, excess pressure and capillary rise.
- **Thermal Properties of Matter** (`P-THERMAL`): thermal expansion; calorimetry and latent heat; conduction and thermal conductivity; radiation: Stefan and Wien laws; Newton law of cooling.
- **Thermodynamics** (`P-THERMO`): first law; heat, work and internal energy; isothermal and adiabatic processes; cyclic processes and P–V diagrams; second law and the Carnot engine.
- **Kinetic Theory of Gases** (`P-KTG`): ideal gas equation and pressure from kinetic theory; rms speed and kinetic interpretation of temperature; degrees of freedom, equipartition and specific heats; mean free path.
- **Oscillations** (`P-SHM`): displacement, velocity, acceleration and phase in SHM; energy in SHM; spring-mass systems; simple pendulum.
- **Waves** (`P-WAVES`): progressive wave equation and wave speed; superposition and reflection; standing waves in strings; standing waves in organ pipes; beats.
- **Electric Charges and Fields** (`P-EFIELD`): Coulomb law and superposition; electric field of point and continuous charges; electric dipole: field and torque; electric flux and Gauss theorem; field of charged line, sheet and shell.
- **Electrostatic Potential and Capacitance** (`P-EPOT`): potential of point charges and a dipole; equipotential surfaces; potential energy of a system; electrostatics of conductors; capacitors in series and parallel; dielectrics and energy stored in a capacitor.
- **Current Electricity** (`P-CURR`): drift velocity, mobility and Ohm law; resistivity and temperature dependence; electrical energy and power; cells: emf, internal resistance and combinations; Kirchhoff rules and Wheatstone bridge.
- **Moving Charges and Magnetism** (`P-MAGMOV`): Biot-Savart law; Ampere law and the solenoid; force on a moving charge in E and B fields; force on and between current-carrying conductors; torque on a current loop; magnetic dipole moment; moving coil galvanometer: sensitivity and conversion.
- **Magnetism and Matter** (`P-MAGMAT`): bar magnet as a dipole; torque; Gauss law for magnetism; magnetisation and magnetic intensity; dia-, para- and ferromagnetism; effect of temperature.
- **Electromagnetic Induction** (`P-EMI`): Faraday laws and Lenz law; motional emf; self and mutual induction.
- **Alternating Current** (`P-AC`): peak and rms values; phasors; R, L and C separately; reactance; series LR, LC and LCR circuits; impedance; resonance; power and power factor; AC generator and transformer.
- **Electromagnetic Waves** (`P-EMW`): displacement current; properties of electromagnetic waves; electromagnetic spectrum: sources and uses.
- **Ray Optics** (`P-RAY`): spherical mirrors; refraction and total internal reflection; refraction at spherical surfaces; thin lenses and lens maker formula; combination of lenses and power; prism.
- **Wave Optics** (`P-WAVEOPT`): Huygens principle: reflection and refraction; Young double slit experiment; coherence and sustained interference; single-slit diffraction.
- **Dual Nature of Radiation and Matter** (`P-DUAL`): photoelectric effect: observations; Einstein photoelectric equation; de Broglie relation.
- **Atoms** (`P-ATOMS`): alpha scattering and the Rutherford model; Bohr model: radius, velocity and energy; hydrogen line spectra.
- **Nuclei** (`P-NUCLEI`): size and composition of the nucleus; nuclear force; mass defect and binding energy per nucleon; fission and fusion.
- **Semiconductor Electronics** (`P-SEMI`): intrinsic and extrinsic semiconductors; p-n junction and diode I–V characteristics; diode as a rectifier.

## Using the plan

1. Print the 80 rows of the test you are about to write.
2. Write each question to its row. If a row cannot be met (for example the focus does not give a good hard question), edit the row and give the reason in `notes`; keep the chapter total.
3. After the test is written, set `state`, `source_json` and `question_sha256` for its 80 rows in the same commit.
4. Run `python3 tools/nest/plan_25_tests.py --check`. It fails if a (chapter, focus, angle) is used twice, if a section is not 20 questions with 3/13/4, or if a focus line has no slot.
5. The script refuses to regenerate the CSV once any row is no longer `planned`, so authored tests cannot be overwritten.

## Checks passed on 15 November 2026

- 2,000 slots, 2,000 different IDs.
- 2,000 different (chapter, focus, angle) tasks.
- Every one of the 100 sections has 20 slots with 3 easy, 13 medium, 4 hard.
- All 103 chapters and all 522 focus lines have at least one slot.
- No chapter appears more than twice in one section.
