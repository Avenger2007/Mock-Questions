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

### A2 Genetics and Plant Breeding

| Test | Answer facts |
|---|---|
| T1 | mitochondria atp, ribosome protein synthesis, chloroplast photosynthesis, golgi packaging secretion, mitosis stage order, mendel no linkage different chromosomes, vernalization not breeding method |

### A3 Biochemistry

| Test | Answer facts |
|---|---|
| T1 | vitamin a night blindness, vitamin d rickets, vitamin c scurvy, thiamine beriberi, neutral ph 7, sucrose glucose fructose |

### A4 Microbiology

| Test | Answer facts |
|---|---|
| T1 | bacteria prokaryote no nucleus, actinomycetes earthy smell geosmin, fungi acid soils decomposers, yeast ethanol co2, blue green algae rice n fixing |

### A5 Seed Science

| Test | Answer facts |
|---|---|
| T1 | nucleus breeder foundation certified chain, scutellum monocot cotyledon |

### L1 Livestock: Scope, Importance and Breeds

| Test | Answer facts |
|---|---|
| T1 | sahiwal milch, murrah buffalo haryana, jamunapari goat not sheep, kadaknath indigenous mp, verghese kurien white revolution, hallikar draught |

### L2 Livestock: Care, Management and Diseases

| Test | Answer facts |
|---|---|
| T1 | eimeria coccidiosis, clostridium chauvoei bq, pasteurella hs, paramyxovirus ranikhet, colostrum antibodies passive immunity, balanced ration definition 24 hours, mastitis udder |

### L3 Artificial Insemination and Livestock Products

| Test | Answer facts |
|---|---|
| T1 | ai collection artificial vagina, semen dilution extender, frozen semen liquid nitrogen, htst 72c 15 s |

### L4 Fisheries

| Test | Answer facts |
|---|---|
| T1 | rohu indian major carp |

### C1 Crop Production: Introduction and Modern Agriculture

| Test | Answer facts |
|---|---|
| T1 | conservation agriculture three principles, precision agriculture gps vrt, organic no synthetic fertilizer, ndvi remote sensing crop health, berseem forage crop, sesame oilseed not pulse |

### C2 Soil, Soil Fertility, Fertilizers and Manures

| Test | Answer facts |
|---|---|
| T1 | urea 46 n, dap 18-46, mop 60 k2o, ssp 16 p2o5, soil separates size order, urea calculation 92 n 200, zinc khaira rice |

### C3 Irrigation and Drainage

| Test | Answer facts |
|---|---|
| T1 | field capacity definition, pwp no recovery, available water fc minus pwp, cri stage wheat, sar sodium hazard |

### C4 Weed Control

| Test | Answer facts |
|---|---|
| T1 | phalaris minor wheat, orobanche mustard, echinochloa rice, cuscuta berseem, glyphosate non-selective |

### C5 Field Crops: Cultivation, Protection and Post-harvest

| Test | Answer facts |
|---|---|
| T1 | puddling reduces percolation, sri young seedlings 8-12 days, brown planthopper hopper burn, rice 20x15 spacing 33 hills, sri moist not flooded saves water |

### H1 Horticulture: Importance, Orchards, Gardens and Propagation

| Test | Answer facts |
|---|---|
| T1 | mango softwood grafting, banana suckers, guava air layering, grape hardwood cuttings, annual one season, quincunx extra plant centre |

### H2 Cultivation of Fruits, Vegetables and Flowers

| Test | Answer facts |
|---|---|
| T1 | papain papaya latex, buttoning overaged seedlings, potato stem tuber not root |

### H3 Fruit and Vegetable Preservation

| Test | Answer facts |
|---|---|
| T1 | kms not for coloured fruits, sugar preserves osmosis, pectin jelly set |
