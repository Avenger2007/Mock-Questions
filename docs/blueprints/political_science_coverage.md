# Coverage map — CUET Political Science, Tests 1–15

This map was written **before** any test, so that repeats are prevented rather than fixed. Rules:

- Every passage theme in §A is used **once** in the series.
- Each **answer fact** is a short key such as `kamaraj plan 1963`, `shimla agreement 1972` or `kyoto protocol 1997`.
  - An answer fact is the fact a question turns on. Each correct pair in a match item, and each event in a sequence, is its own fact.
  - A key may be used **at most twice in the series**, in different tests and different formats.
  - Before a test ships, its keys are checked against the ledgers in §C (`pol_check.py`, flag `REPEAT-TARGET`) and then added to them (`mark_pol.py`).
  - Distractors may repeat.
- Every test covers all sixteen units in the quotas set in the blueprint (§3).

## A. Passage per test (5 linked questions)

| Test | Unit | Theme (original summary) |
|---|---|---|
| 1 | I6 | The declaration of the Emergency in 1975: its context and constitutional basis |
| 2 | W6 | The global commons and common property resources |
| 3 | I2 | The integration of the princely states (Hyderabad, Manipur, Junagadh) |
| 4 | W1 | Shock therapy in the post-communist states |
| 5 | I7 | The Punjab crisis and the Rajiv Gandhi–Longowal Accord |
| 6 | W2 | The European Union from economic union to political actor |
| 7 | I4 | Nehru's foreign policy and non-alignment |
| 8 | W3 | The ethnic conflict in Sri Lanka |
| 9 | I8 | The Mandal issue and the coalition era |
| 10 | W4 | Reform of the UN Security Council and India's claim |
| 11 | I1 | The first general election, 1951–52 |
| 12 | W7 | Resistance to globalisation and the World Social Forum |
| 13 | I5 | The Congress split of 1969 |
| 14 | W5 | Human security and cooperative security |
| 15 | I3 | The Planning Commission and the first two Five Year Plans |

## B. Slot rotation (keeps each unit's questions moving across the series)

- **I1:** the 1952, 1957 and 1962 elections; the Election Commission and Sukumar Sen; ballot methods; Kerala 1957 and its dismissal in 1959; Congress as a social and ideological coalition; factions; opposition parties (Socialists, CPI, Jana Sangh, Swatantra) and their leaders.
- **I2:** the challenges of nation-building; Partition and refugees; integration of princely states (Patel, Hyderabad, Manipur, Junagadh, the Instrument of Accession); the Kashmir question as the syllabus words it; the States Reorganisation Commission (1953) and Act (1956); Potti Sriramulu and Andhra; linguistic states; the new states (Gujarat, Maharashtra, Haryana, Nagaland and others).
- **I3:** the Planning Commission (1950); the first plan (agriculture; K.N. Raj); the second plan (heavy industry; Mahalanobis); the Bombay Plan; the public sector; the Kerala model; J.C. Kumarappa; land reforms and the Green Revolution; Operation Flood (Verghese Kurien); the NITI Aayog (2015).
- **I4:** non-alignment; Panchsheel (1954); Bandung (1955); Belgrade (1961); Tibet and the Dalai Lama; the 1962 war and Krishna Menon; the 1965 war and Tashkent; 1971, the Indo-Soviet Treaty and the Shimla Agreement; nuclear policy (Pokhran 1974 and 1998, the NPT, the CTBT).
- **I5:** succession after Nehru (Shastri, Indira Gandhi); the Kamaraj Plan; the Syndicate; Lohia's non-Congressism; 1967 and the SVD governments; defection, "Aya Ram Gaya Ram"; the 1969 presidential election (V.V. Giri vs Sanjeeva Reddy); bank nationalisation; the Congress split; the "grand alliance"; the 1971 election and "Garibi Hatao".
- **I6:** committed judiciary and bureaucracy (the A.N. Ray supersession, 1973); the Gujarat (Navnirman) and Bihar movements; JP and "Total Revolution"; the 1974 railway strike (George Fernandes); the Allahabad High Court verdict (Raj Narain); Article 352 and "internal disturbance"; the 42nd Amendment; Shah Commission; 1977 and the Janata Party; Morarji Desai and Charan Singh; the PUCL and the rise of civil liberties groups.
- **I7:** regional parties; Punjab (Anandpur Sahib Resolution 1973, Operation Blue Star 1984, the anti-Sikh riots, the Rajiv–Longowal Accord 1985); Kashmir as the syllabus words it; the North-East (Mizo National Front and Laldenga, Nagaland and Phizo, the Assam movement and the Assam Accord 1985, AASU); the Dravidian movement and Periyar.
- **I8:** participatory upsurge in the 1990s; the rise of the Janata Dal and the BJP; the Mandal Commission (B.P. Mandal) and its implementation (1990); the National Front, United Front, NDA and UPA governments; Prime Ministers and their terms; the 2004, 2009, 2014 and 2019 elections; the "lessons" of the coalition era.
- **I9:** the new economic policy (1991); its opposition; the rise of OBCs in North Indian politics; Dalit politics (Kanshi Ram, BAMCEF, the BSP); the Ayodhya issue as NCERT words it; communalism and secularism.
- **W1:** Gorbachev and his reforms (glasnost, perestroika); the end of the USSR (1991); the CIS; the 15 successor states; shock therapy; the Balkans (Yugoslavia, Chechnya); Central Asia; India's ties with Russia and other post-communist countries.
- **W2:** China's rise (the 1978 open-door policy, SEZs, WTO entry 2001); India–China ties; the European Union (Maastricht 1992, the Euro, enlargement); ASEAN (1967, the ASEAN Way, ARF, AEC, Vision 2020); Japan and South Korea and India's ties with them.
- **W3:** Pakistan (army rule, democracy in turn); Nepal (monarchy to republic, the Maoists, the SPA); Sri Lanka (Tamil conflict, LTTE, IPKF); Bangladesh (1971, Mujib); Bhutan and the Maldives; SAARC (1985) and SAFTA (2004); India's disputes and agreements with its neighbours.
- **W4:** the UN (1945, organs, secretaries-general, the Security Council and the veto); reform debates and India's claim to permanent membership; the IMF, the World Bank, the WTO and the IAEA; NGOs such as Amnesty International and Human Rights Watch; accountability of new global institutions.
- **W5:** traditional security (deterrence, defence, the balance of power, alliances); arms control and disarmament (the BWC, the CWC, the NPT, START); non-traditional security (terrorism, human rights, poverty, health, migration, epidemics); cooperative security; India's security strategy.
- **W6:** the Earth Summit (Rio, 1992) and Agenda 21; the Kyoto Protocol (1997); common but differentiated responsibilities; the global commons (Antarctica, the Montreal Protocol 1987); common property resources (sacred groves); indigenous peoples; India's stand and its programmes.
- **W7:** the meaning of globalisation; its economic, political and cultural sides (McDonaldisation, the "jeans" example); its critics (left and right); the World Social Forum (Porto Alegre 2001; Mumbai 2004); India and globalisation (the 1991 reforms); resistance in India.

## C. Ledgers (filled as tests are shipped)

### I1 Era of one-party dominance

| Test | Answer facts |
|---|---|
| T1 | acharya narendra dev socialist, rajagopalachari swatantra, deen dayal upadhyaya jana sangh, ak gopalan cpi, kerala 1957 ems namboodiripad, congress 364 of 489 fptp |
| T2 | election commission 1950 sukumar sen, ballot box per candidate, evm 2004, jana sangh 1951 sp mukherjee, congress factions |

### I2 Nation-building and its problems

| Test | Answer facts |
|---|---|
| T1 | src 1953 act 1956 14 states, potti sriramulu andhra, gujarat maharashtra 1960, manipur 1948 universal franchise, razakars nizam hyderabad |
| T2 | nagaland 1963, gujarat maharashtra 1960, haryana 1966, meghalaya 1972, patel princely states integration, partition religious majorities |

### I3 Politics of planned development

| Test | Answer facts |
|---|---|
| T1 | first plan agriculture, bombay plan 1944 |
| T2 | planning commission 1950 resolution, kerala model education health |

### I4 India's external relations

| Test | Answer facts |
|---|---|
| T1 | panchsheel 1954, bandung 1955, tashkent 1966, shimla 1972, krishna menon resigned 1962, indo soviet treaty 1971 reason |
| T2 | nam belgrade 1961, dalai lama asylum 1959, panchsheel peaceful coexistence, tashkent kosygin mediated, pokhran 1974 |

### I5 Challenge to and restoration of the Congress system

| Test | Answer facts |
|---|---|
| T1 | kamaraj plan 1963, indira pm 1966, 1967 congress lok sabha majority, shastri pm 1964, fourth general election 1967, bank nationalisation 1969, 1971 election garibi hatao, aya ram gaya ram gaya lal haryana |
| T2 | kamaraj kingmaker, lohia non congressism, vv giri independent president 1969, sanjeeva reddy official candidate, syndicate congress leaders, grand alliance 1971 no positive programme |

### I6 Crises of the constitutional order

| Test | Answer facts |
|---|---|
| T1 | article 352 internal disturbance, emergency declared 25 june 1975, raj narain election petition, shah commission emergency excesses, emergency press censorship preventive detention, lok sabha term extended |
| T2 | navnirman gujarat 1974, jp total revolution, supersession judges 1973, railway strike george fernandes, morarji desai first non congress pm, pucl civil liberties |

### I7 Regional aspirations and conflicts

| Test | Answer facts |
|---|---|
| T1 | anandpur sahib 1973, operation blue star 1984, rajiv longowal accord 1985, mizo accord 1986, states carved out of assam, aasu assam movement |
| T2 | nagaland 1963, sikkim merger 1975, assam accord 1985, mizoram state 1987, phizo naga national council, dmk annadurai 1949 |

### I8 Democratic upsurge and coalition politics

| Test | Answer facts |
|---|---|
| T1 | mandal commission janata government, 27 percent obc reservation, mandal implemented vp singh 1990, national front 1989, united front 1996, nda 1998, upa 2004 |
| T2 | vp singh national front, deve gowda united front, chandra shekhar congress support, vajpayee nda, 2014 bjp majority own, coalition era regional parties role |

### I9 Recent issues and challenges

| Test | Answer facts |
|---|---|
| T1 | new economic policy 1991 rao |
| T2 | bamcef 1978, bsp 1984, mandal implemented vp singh 1990, new economic policy 1991 rao, ayodhya december 1992 |

### W1 Collapse of bipolarity

| Test | Answer facts |
|---|---|
| T1 | ussr 15 republics, cis formed 1991, russia inherited security council seat, shock therapy rapid imf, gorbachev general secretary 1985, berlin wall fell 1989, lithuania independence 1990, ussr dissolved 1991, glasnost openness, central asian republics |
| T2 | perestroika restructuring, second world socialist bloc, shock therapy rapid imf, warsaw pact military alliance, berlin wall built 1961, soviet afghanistan 1979, gorbachev general secretary 1985, german unification 1990, chechnya dagestan secessionist, russia military hardware india |

### W2 Alternative centres of power

| Test | Answer facts |
|---|---|
| T1 | asean 1967, asean regional forum 1994, maastricht treaty 1992, china wto 2001, asean founding members, asean way informal cooperative, japan g7 nuclear |
| T2 | eu flag anthem currency, eec 1957, maastricht created eu, china special economic zones, rajiv gandhi china 1988 |

### W3 South Asia after the Cold War

| Test | Answer facts |
|---|---|
| T1 | saarc 1985, safta 2004, maldives multiparty 2005, nepal monarchy abolished 2008, ipkf 1987 accord, bhutan flushed out militants, musharraf 1999 |
| T2 | mujib bangladesh, bhutto pakistan, gyanendra nepal, ltte sri lanka, bangladesh independence 1971, saarc 1985, pakistan nuclear test 1998, safta in force 2006, saarc members myanmar not, pakistan army clergy landowners |

### W4 International organisations

| Test | Answer facts |
|---|---|
| T1 | imf financial regulation, world bank loans development, wto global trade rules, iaea peaceful nuclear energy, security council 15 members, kofi annan ghana, amnesty international ngo human rights |
| T2 | un founded 1945, five permanent veto, general assembly one vote, india non permanent member, guterres portugal, wto 1995 successor gatt |

### W5 Security in the contemporary world

| Test | Answer facts |
|---|---|
| T1 | npt 1968, bwc 1972, start i 1991, cwc 1992, human security freedom from want fear, internally displaced persons |
| T2 | traditional security military threat, terrorism non traditional, global poverty threat, hiv aids epidemic threat, balance of power meaning |

### W6 Environment and natural resources

| Test | Answer facts |
|---|---|
| T1 | earth summit rio 1992, kyoto protocol 1997, montreal protocol 1987, antarctic treaty 1959, cbdr rio declaration, sacred groves common property |
| T2 | global commons four areas, montreal protocol ozone, global commons cooperation difficult north south, outer space technology north south, common property community rules |

### W7 Globalisation and its critics

| Test | Answer facts |
|---|---|
| T1 | globalisation flows four kinds, mcdonaldisation homogenisation, wsf porto alegre 2001, india reforms 1991, wsf mumbai 2004, cultural heterogenisation jeans kurta |
| T2 | left critics capitalism phase, right critics traditional culture, advocates prosperity, wsf neo liberal opposition, minimalist state welfare, right wing valentines day |
