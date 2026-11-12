# Coverage map — CUET Agriculture, Tests 1–15

This map was written **before** any test, so that repeats are prevented rather than fixed.

**Rules**
- Every passage theme in §A is used **once** in the series.
- Each **answer fact** is a short key such as `striga sorghum`, `vertisols black soil` or `rinderpest virus`.
  - It is the fact a question turns on. Each correct pair in a match item, and each step in a sequence, is its own fact.
  - A key may be used **at most twice in the series**, in different tests and different formats.
  - Before a test ships, its keys are checked against the ledgers in §C (`agri_check.py`, flag `REPEAT-TARGET`) and then added to them (`mark_agri.py`).
  - Distractors may repeat.
- Every test covers all seventeen sub-units in the quotas set in the blueprint (§3).

## A. Passage per test (5 linked questions)

| Test | Sub-unit | Theme (original text) |
|---|---|---|
| 1 | C5 | Growing rice: nursery, puddling, transplanting and water management |
| 2 | L1 | Indigenous cattle breeds and the White Revolution |
| 3 | H3 | Making jam and jelly at home: pectin, acid, sugar and the end point |
| 4 | A2 | Hybridization and the semi-dwarf wheats of the Green Revolution |
| 5 | C2 | The Soil Health Card and integrated nutrient management |
| 6 | L2 | Managing a commercial layer flock |
| 7 | C3 | Drip and sprinkler irrigation |
| 8 | A1 | The Indian monsoon and agromet advisories |
| 9 | H2 | Mango cultivation: varieties, propagation and problems |
| 10 | C5 | Millets: nutri-cereals and why they matter |
| 11 | A4 | Soil microbes and biofertilizers |
| 12 | L3 | From the farm to the packet: processing market milk |
| 13 | C4 | *Phalaris minor* and herbicide resistance in rice–wheat systems |
| 14 | L4 | Composite fish culture in village ponds |
| 15 | C1 | Conservation and precision agriculture |

Odd tests have a key of 13 / 12 / 13 / 12 (A / B / C / D); even tests have 12 / 13 / 12 / 13.

## B. Slot rotation (keeps each sub-unit's questions moving across the series)

- **A1:** weather vs climate; rainfall, temperature, humidity, wind and sunshine, with the instruments that measure them (rain gauge, thermometer, hygrometer, anemometer and wind vane, sunshine recorder); forecasts (nowcast, short, medium, long range); IMD and agromet advisories; climate change (CO₂, CH₄, N₂O, effects on crops); Köppen and Thornthwaite classification; the monsoon (onset in Kerala, SW and NE monsoon, break, withdrawal, El Niño).
- **A2:** cell organelles; mitosis and meiosis (phases, significance); DNA, RNA, chromosomes and the double helix; Mendel's laws, the reasons for his success and the absence of linkage; monohybrid and dihybrid ratios; quantitative and polygenic inheritance; continuous and discontinuous variation; self- and cross-pollinated crops; introduction, selection (pure line, mass), hybridization, mutation breeding, polyploidy, aneuploidy; tissue culture, totipotency, somatic hybrids; Bt cotton and GM crops; the history of plant breeding (Borlaug, Swaminathan).
- **A3:** pH and buffers; carbohydrates (monosaccharides to polysaccharides); amino acids and proteins; lipids and fatty acids; vitamins and deficiency diseases; enzymes (classes, co-factors, the lock and key model); nucleic acids and nucleotides.
- **A4:** prokaryotic cell structure; algae, bacteria, fungi, actinomycetes, protozoa, viruses; respiration and fermentation; decomposition of organic matter and C:N; soil flora and fauna (earthworms); Rhizobium, Azotobacter, Azospirillum, BGA, Azolla, PSB, mycorrhiza; *Trichoderma*.
- **A5:** monocot vs dicot seed structure; sexual, asexual and apomictic reproduction; self- and cross-pollination and their agents; double fertilization; dormancy (causes, breaking it); classes of seed (nucleus, breeder, foundation, certified) and tag colours.
- **L1:** livestock in the economy; Operation Flood and Verghese Kurien; NDDB, Amul; cattle breeds (milch, draught, dual), buffalo breeds, goat and sheep breeds, poultry breeds (Indian and exotic), and their home tracts.
- **L2:** loose and stanchion housing; deep litter, cage, battery and free-range poultry; feeding principles; roughage vs concentrate; balanced ration; colostrum and calf care; care of pregnant and milch animals, bullocks, chicks, layers and broilers; signs of sickness; Rinderpest, BQ, FMD, mastitis, HS, coccidiosis, fowl pox, Ranikhet disease (causal agents, signs, vaccines).
- **L3:** male and female reproductive organs; semen collection (artificial vagina), dilution, frozen semen at −196 °C in liquid nitrogen; the role of AI; heat detection; milk composition; filtration, clarification, pasteurisation (LTLT, HTST, UHT), homogenisation; products (butter, ghee, paneer, curd, khoa, ice cream); cooperatives and marketing.
- **L4:** definitions of fish, fisheries and aquaculture; characteristics of fish (gills, fins, scales, cold-blooded); Indian major carps; exotic carps; composite fish culture; freshwater, brackish and marine fisheries; the Blue Revolution.
- **C1:** foodgrain production since 1950–51; the Green Revolution; projections; sustainable agriculture; commercialisation; crop groups (cereals, pulses, oilseeds, fibre, sugar, forage); conservation agriculture; precision agriculture (GPS, GIS, VRT); natural farming (jeevamrit, beejamrit); organic farming and certification; remote sensing (NDVI, satellites).
- **C2:** soil pH; texture classes and the textural triangle; soil structure; tilth; soil organisms; fertility vs productivity; soil health; the 17 essential nutrients (macro, secondary, micro) and their functions and deficiency symptoms; soil types of India (alluvial, black, red, laterite, desert, saline-alkaline); FYM, compost, vermicompost, green manure; straight, complex and mixed fertilizers (urea 46% N, DAP 18-46-0, MOP 60% K₂O, SSP 16% P₂O₅); INM; acid, saline and sodic soils and their amendments (lime, gypsum); erosion; soil testing.
- **C3:** sources of irrigation; scheduling by critical stage, IW/CPE, soil moisture and depletion; field capacity, PWP, available water; crop water requirement and consumptive use; surface, sprinkler and drip methods; surface and subsurface drainage; watershed management; water quality (EC, SAR, RSC).
- **C4:** what makes a plant a weed; weed classes (by life span, habitat, leaf form); crop–weed competition and the critical period; parasitic weeds (*Striga*, *Orobanche*, *Cuscuta*); cultural, mechanical, chemical (selective, non-selective, pre-emergence, post-emergence) and biological control (*Zygogramma*, *Neochetina*, *Cactoblastis*); IWM; important weeds (*Parthenium*, *Phalaris minor*, *Echinochloa*, *Cyperus rotundus*, *Eichhornia*).
- **C5:** rice, wheat, maize, sorghum, pearl millet, groundnut, mustard, pigeon pea, gram, sugarcane, cotton and berseem: season, seed rate, spacing, fertilizer, critical stages, key pests (stem borer, BPH, pink bollworm, aphid, pod borer) and diseases (blast, rust, smut, wilt, red rot, tikka, downy mildew, ergot); IPM; harvesting, threshing, storage (moisture %), processing and marketing; millets.
- **H1:** fruits and vegetables in the diet; diversification; the processing industry; orchard location and layout systems (square, rectangular, triangular, quincunx, hexagonal, contour); ornamental and kitchen gardens; training (open centre, central leader, modified leader) and pruning; intercropping; frost and sunscald protection; trees, shrubs, climbers, annuals and perennials; seed, cutting, layering (air, ground), budding (T, patch) and grafting (veneer, cleft, approach).
- **H2:** mango, papaya, banana, guava, citrus and grapes; radish, carrot, potato, onion, cauliflower, brinjal, tomato, spinach and cabbage; gladiolus, canna, chrysanthemum, rose and marigold: varieties, propagation, spacing, disorders and physiological problems (mango malformation, black tip, spongy tissue, buttoning, whiptail, browning), harvest and marketing.
- **H3:** the principles of preservation (removal of microbes, inhibition, killing); methods (heat, cold, drying, chemicals such as KMS and sodium benzoate, sugar, salt, acid, fermentation, irradiation); jam, jelly and marmalade (pectin, 65–68% TSS, the sheet test); ketchup and sauce; chips; packing (cans, bottles, laminates).

## C. Ledgers (filled as tests are shipped)

### A1 Agrometeorology

| Test | Answer facts |
|---|---|
| T1 | sw monsoon kerala 1 june, ne monsoon tamil nadu oct-dec, el nino weak monsoon, hygrometer humidity, methane flooded paddy |
| T2 | anemometer wind speed, wind vane direction, campbell stokes sunshine, rain gauge rainfall, climate long term average, koppen temperature precipitation |
| T3 | short range up to 3 days, medium range 3-10 days, long range beyond 10 days, rainfall millimetres, clouds trap long wave radiation frost |
| T4 | co2 fossil fuel deforestation, ch4 ruminants, n2o nitrogen fertilizer, cfc refrigerants, sw monsoon june september, terminal heat grain filling shortened |
| T5 | co2 fertilisation c3 crops, heat shortens crop duration, extreme events frequency, sea level salinity coast, imd national weather service, rh highest before sunrise |
| T6 | photoperiod flowering, humidity fungal disease, wind lodging evaporation, max min thermometer, el nino pacific warming |
| T7 | koppen a tropical humid, koppen b dry, koppen c warm temperate, koppen d cold snow, relative humidity definition, monsoon withdrawal northwest |
| T8 | agromet advisory twice weekly, postpone spray before rain washoff, late monsoon short duration varieties, advance harvest forecast rain, dry spell mulch light irrigation |
| T9 | open pan evaporation, soil thermometer, pyranometer solar radiation, barometer air pressure, monsoon advance order, rainy day 2.5 mm |
| T10 | frost below zero, hailstorm cumulonimbus ice, heat wave above normal, drought rainfall deficit, max temperature early afternoon, temperature falls altitude, cold wave crop damage, isohyets equal rainfall |

### A2 Genetics and Plant Breeding

| Test | Answer facts |
|---|---|
| T1 | mitochondria atp, ribosome protein synthesis, chloroplast photosynthesis, golgi packaging secretion, mitosis stage order, mendel no linkage different chromosomes, vernalization not breeding method |
| T2 | quantitative traits continuous variation, polygenic many genes small effect, discontinuous distinct classes, meiosis halves chromosome number, pure line selection self pollinated johannsen, aabbcc 8 gametes 2 power n, wheat self pollinated |
| T3 | heterosis f1 superiority, emasculation removal anthers, polyploidy more than two sets, mutation heritable change, prophase i substages order, colchicine polyploidy, totipotency tissue culture, uracil not in dna |
| T4 | semi dwarf short stiff straw no lodging, bagging prevents stray pollen, kalyan sona sonalika, f2 segregation select true breeding, borlaug nobel peace 1970, norin 10 dwarfing genes |
| T5 | monohybrid f2 3 1, monohybrid genotypic 1 2 1, dihybrid 9 3 3 1, test cross 1 1, tissue culture steps, gamma rays physical mutagen, bt cotton bacillus thuringiensis, mendel success reasons |
| T6 | mendel laws inheritance, watson crick double helix, de vries mutation theory, johannsen pure line theory, dna double stranded, dna in nucleus chromosomes, hybrid seed f2 segregation, somatic hybridisation protoplast fusion, rice 2n 24 gamete 12 |
| T7 | chiasma crossover point, centromere joins chromatids, spindle fibres, synapsis pairing, transgenic plant steps, male sterility hybrid seed no emasculation, triticale wheat rye, crop rotation not biotechnology |
| T8 | mitosis two identical cells, meiosis four haploid cells, sharbati sonora mutation, plant introduction definition, wheat seed not vegetative |
| T9 | polyploids larger organs, mutation source variation, mendel father genetics, heterosis maximum f1, mass selection bulk seed, quantitative trait not single gene |
| T10 | linkage genes inherited together, crossing over prophase i, non sister chromatids, distance more recombination, phenotype, backcross f1 parent, synthetic variety cross pollinated, locus gene position |

### A3 Biochemistry

| Test | Answer facts |
|---|---|
| T1 | vitamin a night blindness, vitamin d rickets, vitamin c scurvy, thiamine beriberi, neutral ph 7, sucrose glucose fructose |
| T2 | ribose pentose rna, starch plant storage, glycogen animal storage, cellulose cell wall, protein structure levels order, enzymes proteins |
| T3 | fats glycerol fatty acids, unsaturated double bonds, lipids insoluble water, saturated fats solid, buffer resists ph change, vitamin k fat soluble |
| T4 | protein amino acids, starch glucose monomer, nucleic acid nucleotides, fat glycerol fatty acids, peptide bond, enzyme denaturation heat |
| T5 | enzymes lower activation energy, enzymes not used up, optimum temperature ph, lock and key, ph 5.2 acidic, nucleotide sugar phosphate base |
| T6 | glucose fructose monosaccharides, lactose disaccharide, starch polysaccharide, glucose monosaccharide, vitamin d sunlight skin |
| T7 | essential amino acids diet, pulses rich protein, heat denatures protein, dna hydrogen bonds bases, vitamin k blood clotting |
| T8 | amylase starch, lipase fats, pepsin proteins, cellulase cellulose, oil lipid, carrot beta carotene vitamin a |
| T9 | vitamin c water soluble, fat soluble stored not excreted, enzyme substrate complex steps, hydrolases |
| T10 | iodine starch blue black, benedict reducing sugar, biuret protein violet, sudan fat red, cofactor non protein helper, nucleic acids phosphate acidic |

### A4 Microbiology

| Test | Answer facts |
|---|---|
| T1 | bacteria prokaryote no nucleus, actinomycetes earthy smell geosmin, fungi acid soils decomposers, yeast ethanol co2, blue green algae rice n fixing |
| T2 | lactobacillus curd, yeast eukaryote, wide cn ratio n immobilisation |
| T3 | aspergillus fungus, streptomyces actinomycete, amoeba protozoan, tmv virus, virus nucleic acid protein coat, earthworms aerate casts enrich |
| T4 | aerobic more energy than fermentation, fermentation without oxygen, decomposition releases co2 nutrients, ammonification nitrification order, trichoderma biocontrol |
| T5 | nitrosomonas ammonium nitrite, azotobacter free living n, mycorrhiza phosphorus uptake, trichoderma biocontrol, humus definition, methanogens biogas |
| T6 | bacterial growth curve phases, silage lactic acid bacteria, penicillium eukaryote not prokaryote |
| T7 | bread yeast, vinegar acetobacter, roquefort penicillium, jute retting bacteria, actinomycetes antibiotics streptomycin, soil protozoa feed bacteria |
| T8 | virus obligate parasite, tmv rna, insect vectors plant viruses, waterlogged slow decomposition oxygen, penicillin penicillium notatum |
| T9 | earthworm burrows casts, root knot nematode galls, termite woody matter, mycorrhiza p uptake roots, viruses smallest electron microscope, nitrobacter nitrite nitrate |
| T10 | gram stain steps, pathogens disease causing, mushroom fungi |

### A5 Seed Science

| Test | Answer facts |
|---|---|
| T1 | nucleus breeder foundation certified chain, scutellum monocot cotyledon |
| T2 | hard seed coat dormancy, scarification, ga breaks dormancy, double fertilisation zygote pen |
| T3 | germination events order, anemophily wind maize |
| T4 | breeder tag golden yellow, foundation tag white, certified tag azure blue, apomixis definition |
| T5 | self pollination same flower, cross pollination another plant, bees pollinate mustard, epigeal germination cotton |
| T6 | endosperm stored food, radicle embryonic root, plumule embryonic shoot, testa seed coat, tetrazolium viability test |
| T7 | monocot one cotyledon, bean dicot, maize endosperm food, wheat caryopsis |
| T8 | seed processing steps, isolation distance pollen contamination |
| T9 | sexual gamete fusion, potato sugarcane asexual, ovule becomes seed |
| T10 | hypogeal pea, good seed quality weed free |

### L1 Livestock: Scope, Importance and Breeds

| Test | Answer facts |
|---|---|
| T1 | sahiwal milch, murrah buffalo haryana, jamunapari goat not sheep, kadaknath indigenous mp, verghese kurien white revolution, hallikar draught |
| T2 | bos indicus zebu, tharparkar dual purpose, anand pattern three tier, crossbred more milk less heat tolerant, operation flood 1970 nddb, rashtriya gokul mission 2014 |
| T3 | gir gujarat, ongole andhra pradesh, kangayam tamil nadu, rathi rajasthan, india first milk production, rhode island red dual purpose exotic |
| T4 | nddb 1965 anand, amul gujarat cooperative, holstein friesian highest yield, merino fine wool |
| T5 | white leghorn egg type, aseel game, cornish meat type, kadaknath black flesh, surti buffalo, black bengal goat |
| T6 | cow ruminant four chambers, national milk day kurien |
| T7 | murrah haryana, jaffarabadi gujarat, nili ravi punjab, bhadawari high fat, jersey island origin, up first milk state |
| T8 | barbari goat, sirohi goat rajasthan, merino exotic sheep, beetal goat, large white yorkshire pig, pashmina changthangi goat |
| T9 | livestock products draught, dung manure fuel, livestock regular income, sheep wool, india first buffalo population |
| T10 | red sindhi dairy, hariana dual purpose, kankrej dual purpose gujarat, deoni dual purpose maharashtra, heifer, nellore deccani chokla sheep |

### L2 Livestock: Care, Management and Diseases

| Test | Answer facts |
|---|---|
| T1 | eimeria coccidiosis, clostridium chauvoei bq, pasteurella hs, paramyxovirus ranikhet, colostrum antibodies passive immunity, balanced ration definition 24 hours, mastitis udder |
| T2 | deep litter husk floor, battery cage tiers, free range outdoors, loose housing cattle, fmd virus blisters, healthy signs moist muzzle bright eyes |
| T3 | dry off before calving, pregnant separate calving, extra concentrate late pregnancy, navel iodine, coccidiosis damp litter oocysts, layers calcium eggshell, bq bacterial not viral |
| T4 | hs throat swelling fever, mastitis clots milk, fowl pox comb scabs, ranikhet twisted neck, rinderpest eradicated, groundnut cake concentrate not roughage, lasota vaccine ranikhet |
| T5 | maize grain energy concentrate, mustard cake protein, mineral mixture, stover dry roughage, newborn calf care steps, shed long axis east west, california mastitis test |
| T6 | pullets lay 18-20 weeks, layers 16 hours light, cull non layers feed cost, layer feed 110 g calculation, short days reduce laying |
| T7 | rumen microbes digest cellulose, green fodder carotene, clean water always, cow body temperature 38.5, deworming calves internal parasites, wet hand milking bad practice |
| T8 | chicks brooder heat, bullocks concentrate work days, pregnant cow dry period, newborn calf colostrum, broilers 5-6 weeks, fowl pox mosquito, good housing ventilation dry |
| T9 | fmd vaccination, mastitis teat dip, coccidiostat feed, deworming roundworms, heat sign standing mounted, hay dried fodder, urea treated straw protein |
| T10 | anthrax bacterium, rabies virus, ringworm fungus, babesiosis protozoan tick, silage making steps, dehorning young calves, shed floor slope drain |

### L3 Artificial Insemination and Livestock Products

| Test | Answer facts |
|---|---|
| T1 | ai collection artificial vagina, semen dilution extender, frozen semen liquid nitrogen, htst 72c 15 s |
| T2 | buffalo milk higher fat, paneer acid coagulation |
| T3 | ai one bull thousands cows, ai prevents reproductive disease, frozen semen after bull death, am pm rule insemination |
| T4 | lactose milk sugar, ghee from butter |
| T5 | casein main milk protein, milk poor in iron, cow gestation 280 days |
| T6 | butter churning cream, khoa evaporation, dahi lactic fermentation, ice cream freezing whipping, oestrous cycle 21 days |
| T7 | pasteurisation kills pathogens, pasteurised milk cooled, uht above 130, thawing semen 37c |
| T8 | milk plant steps order, standardisation milk fat |
| T9 | butter making steps, lactometer milk density |
| T10 | cream rises fat lighter, milk 87 water, skim milk fat removed, toned milk smp water, sweetened condensed milk |

### L4 Fisheries

| Test | Answer facts |
|---|---|
| T1 | rohu indian major carp |
| T2 | fish gills, fish cold blooded, fins locomotion |
| T3 | aquaculture definition |
| T4 | blue revolution fisheries |
| T5 | pomfret marine fish |
| T6 | prawn not fish |
| T7 | fish seed stages order |
| T8 | silver carp exotic |
| T9 | pisciculture |
| T10 | fish rich protein |

### C1 Crop Production: Introduction and Modern Agriculture

| Test | Answer facts |
|---|---|
| T1 | conservation agriculture three principles, precision agriculture gps vrt, organic no synthetic fertilizer, ndvi remote sensing crop health, berseem forage crop, sesame oilseed not pulse |
| T2 | green revolution wheat, castor oilseed not fibre, jeevamrit microbial culture |
| T3 | foodgrain 1950-51 about 51 mt, foodgrain above 300 mt, sugar beet sugar crop, sustainable agriculture future generations |
| T4 | precision vrt gps, remote sensing satellite area, conservation agriculture happy seeder, natural farming beejamrit, sorghum cereal, modern agriculture challenges |
| T5 | groundnut oilseed, npop organic certification, foodgrains cereals pulses |
| T6 | cereals wheat rice maize, jute cotton fibre, sorghum grain fodder, oats berseem fodder, lentil pulse, ndvi red nir |
| T7 | maize queen cereals, zero tillage wheat after rice, synthetic insecticide not organic |
| T8 | green revolution foodgrains, white revolution milk, blue revolution fish, yellow revolution oilseeds, lucerne forage legume, gps global positioning system |
| T9 | soybean oilseed, sunn hemp fibre, sorghum cereal, moong pulse, rice not rabi, zbnf zero budget natural farming |
| T10 | ager field cultura, branches agriculture ornithology, mixed farming crops livestock |

### C2 Soil, Soil Fertility, Fertilizers and Manures

| Test | Answer facts |
|---|---|
| T1 | urea 46 n, dap 18-46, mop 60 k2o, ssp 16 p2o5, soil separates size order, urea calculation 92 n 200, zinc khaira rice |
| T2 | alluvial indo gangetic, black soil swells cracks cotton, red soil iron oxide, laterite leaching, soil sampling steps, gypsum sodic soil, phosphorus purple leaves |
| T3 | fym bulky organic manure, dhaincha green manure, inm combines sources, green manuring steps, magnesium chlorophyll, npk complex fertilizer |
| T4 | c h o from air water, ca mg s secondary, nickel micronutrient, optimum ph 6.5-7.5, tilth physical condition, dap calculation 46 p2o5 18 n |
| T5 | shc twelve parameters, shc ph ec oc, urea cheap npk imbalance, shc grid 2.5 ha irrigated, inm organic plus fertilizer roles |
| T6 | n older leaf yellowing, k leaf margin scorch, fe young leaf interveinal chlorosis, b growing point death, soil horizons order, soil texture proportions, lime acid soil |
| T7 | fym dung urine litter, vermicompost casts, green manure undecomposed, oilcake concentrated, mop calculation 60 k2o, ammonia volatilisation urea |
| T8 | water erosion bare slopes, sodic soil exchangeable sodium, pit compost steps, saline soil leaching drainage, ssp supplies sulphur |
| T9 | soil test steps, fym 0.5 n calculation, clay highest water holding, azolla anabaena |
| T10 | splash raindrop impact, sheet thin layer, gully deep channels, rill small channels tillage, vermicompost steps, furrow slice weight calculation, potassium primary nutrient |

### C3 Irrigation and Drainage

| Test | Answer facts |
|---|---|
| T1 | field capacity definition, pwp no recovery, available water fc minus pwp, cri stage wheat, sar sodium hazard |
| T2 | border strip wheat, furrow row crops, wild flooding low efficiency, sprinkler unsuited windy, wheat stage order cri tillering jointing flowering, iw cpe cumulative pan evaporation |
| T3 | surface drains open ditches, tile drains perforated pipes, mole drains bullet plough, vertical drainage pumping wells, watershed common outlet, irrigation volume 1 ha 5 cm 500 m3 |
| T4 | schedule critical stages, schedule soil moisture depletion, irrigation efficiency order drip sprinkler furrow flooding, tubewells wells largest source |
| T5 | evapotranspiration definition, effective rainfall, irrigation requirement, delta crop, irrigation requirement calculation, waterlogging roots lack oxygen |
| T6 | ridge to valley, contour bunds reduce runoff, maize tasselling silking critical, tank surface water |
| T7 | drip filters clogging, sprinkler sandy undulating land, fertigation definition, drip emitter discharge calculation, sprinkler wind drift |
| T8 | canal surface water, tank stored runoff, tube well deep groundwater, open well shallow groundwater, irrigation time calculation 50 lps, saline water osmotic stress |
| T9 | drainage removes excess water, poor drainage waterlogging salinity, soil moisture instruments, evening irrigation less evaporation |
| T10 | crop water requirement components, rice more water than wheat, sandy soil light frequent irrigation, water use efficiency yield per water, farm pond runoff life saving irrigation |

### C4 Weed Control

| Test | Answer facts |
|---|---|
| T1 | phalaris minor wheat, orobanche mustard, echinochloa rice, cuscuta berseem, glyphosate non-selective |
| T2 | weeds prolific seed, weed seed dormancy, weeds compete light water nutrients, weeds alternate hosts, zygogramma parthenium |
| T3 | eichhornia aquatic weed, cyperus rotundus tubers |
| T4 | herbicide timing order, critical period first third |
| T5 | stale seedbed cultural, insects biological control, 2 4 d broadleaf weeds |
| T6 | neochetina water hyacinth, zygogramma parthenium, cactoblastis prickly pear, grass carp submerged weeds, atrazine maize sorghum |
| T7 | pre emergence before weeds, selective herbicide spares crop, herbicide dose area, herbicide resistance repeated use, stale seedbed flush weeds |
| T8 | cuscuta stem parasite, orobanche root parasite, striga root parasite sorghum, striga trap crops, parthenium congress grass |
| T9 | hand weeding mechanical, crop rotation breaks weed cycle |
| T10 | weed plant out of place |

### C5 Field Crops: Cultivation, Protection and Post-harvest

| Test | Answer facts |
|---|---|
| T1 | puddling reduces percolation, sri young seedlings 8-12 days, brown planthopper hopper burn, rice 20x15 spacing 33 hills, sri moist not flooded saves water |
| T2 | blast pyricularia, red rot colletotrichum, tikka cercospora, wilt fusarium udum, pink bollworm cotton, wheat storage moisture 10-12 |
| T3 | cajanus cajan pigeon pea, cicer arietinum gram, pennisetum glaucum pearl millet, sorghum bicolor, wheat post harvest order, ergot pearl millet sclerotia |
| T4 | yellow stem borer rice, helicoverpa gram pod borer, mustard aphid, early shoot borer sugarcane, sugarcane sets, groundnut peg underground pods, gram nipping branching |
| T5 | sugarcane growth phases, wheat rabi, puccinia wheat rust |
| T6 | wheat sowing operations order, cotton lint seed hairs, white rust mustard albugo, maize 60x20 plant population |
| T7 | rice growth stages order, chickpea wilt fusarium ciceris, groundnut king oilseeds |
| T8 | hd 2967 wheat, pusa basmati 1121 rice, pusa bold mustard, icpl 87 pigeon pea, groundnut stages order, pearl millet drought tolerant |
| T9 | loose smut ustilago, blb xanthomonas, alternaria blight mustard, green ear sclerospora, ragi calcium, bt cotton bollworm control |
| T10 | international year millets 2023, minor millets kodo, millets c4 drought rainfed, millet rice water saving calculation, millets gluten free fertilizer shelf life |

### H1 Horticulture: Importance, Orchards, Gardens and Propagation

| Test | Answer facts |
|---|---|
| T1 | mango softwood grafting, banana suckers, guava air layering, grape hardwood cuttings, annual one season, quincunx extra plant centre |
| T2 | training framework, pruning dead shoots, grapes pruned annually, shrub definition, kitchen garden perennials one side |
| T3 | climbers need support, air layering gootee |
| T4 | square system, contour planting slopes, rectangular row spacing wider, triangular equilateral, t budding steps, irrigation frost protection |
| T5 | mango seedlings not true to type, vegetative identical parent, rootstock resistance, rootstock definition, hedge living fence |
| T6 | air layering steps, doob lawn grass, whitewash trunk sunscald |
| T7 | edging path borders, topiary clipped shapes, rockery stones, bonsai dwarf pots, hibiscus stem cuttings, secateurs pruning tool |
| T8 | kitchen garden fresh vegetables, kitchen waste water, kitchen garden rotation, mango perennial, budding single bud scion |
| T9 | stooling earthed up, inarching own roots, patch budding rectangle, cleft grafting wedge, thinning out whole branch |
| T10 | mist chamber rooting cuttings, polyhouse plastic film, shade net reduces light, hot bed heated early seedlings, fruit planting steps, windbreak shelter belt wind |

### H2 Cultivation of Fruits, Vegetables and Flowers

| Test | Answer facts |
|---|---|
| T1 | papain papaya latex, buttoning overaged seedlings, potato stem tuber not root |
| T2 | gladiolus corms, rose t budding, canna rhizomes, chrysanthemum terminal cuttings suckers, alphonso mango, black tip brick kiln fumes |
| T3 | carrot apiaceae, onion alliaceae, spinach chenopodiaceae, brinjal solanaceae, panama wilt banana |
| T4 | dashehari mango not grape, whiptail molybdenum, marigold seed propagation |
| T5 | grand naine banana, allahabad safeda guava, coorg honey dew papaya, anab-e-shahi grape, spinach leaves, blossom end rot calcium |
| T6 | papaya seed, papaya male female bisexual, cauliflower curd, potato seed tubers |
| T7 | onion seed sets, tomato nursery transplant, carrot direct sown, radish direct sown, onion bulb, bunchy top aphid |
| T8 | radish root, cabbage head leaves, tomato fruit, potato stem tuber, gladiolus cut flower, guava vitamin c |
| T9 | mango anacardiaceae, amrapali dashehari neelum, mango seedlings not true type late, mango high density 5x5 calculation, alternate bearing biennial |
| T10 | okra malvaceae, tomato solanaceae, cucumber cucurbit, garlic cloves, cabbage cool season, staking tomato |

### H3 Fruit and Vegetable Preservation

| Test | Answer facts |
|---|---|
| T1 | kms not for coloured fruits, sugar preserves osmosis, pectin jelly set |
| T2 | potato chips steps, sodium benzoate ketchup |
| T3 | pectin acid sugar balance, guava rich pectin, marmalade citrus peel shreds, jelly fails low acid pectin, jelly end point 5-6 above boiling |
| T4 | drying lowers water activity, salt pickles, irradiation preservation, canning heat seal, squash 25 percent juice |
| T5 | tomato ketchup steps, blanching inactivates enzymes |
| T6 | drying removes moisture, canning heat sealed, refrigeration low temperature, irradiation kills microbes, chips nitrogen flushed laminate |
| T7 | squash steps, raisins drying grapes |
| T8 | pickles salt oil acid, refractometer tss brix |
| T9 | dehydration reduces bulk, frozen kept frozen, sulphuring colour drying, murabba sugar syrup |
| T10 | pasteurisation below 100, sterilisation all microbes, fermentation sugar acid alcohol, osmotic dehydration syrup, aam papad mango |
