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
| T3 | election commission 1950, jana sangh 1951 sp mukherjee, swatantra 1959, third general election 1962, congress socialist party 1934 |
| T4 | first general election 1952, second general election 1957, third general election 1962, fourth general election 1967, jana sangh akhand bharat, cpi abandoned violent revolution 1951 |
| T5 | congress 1885 pressure group, congress accommodated radicals conservatives, congress 45 percent votes 1952, congress ideological coalition, cpi 16 seats largest opposition, congress dominance reason legacy organisation |
| T6 | kerala government dismissed 1959 article 356, 17 crore voters first election, mexico pri one party |
| T7 | congress socialist party formed 1934, socialists left congress 1948, first general election completed 1952, cpi government kerala 1957, rajagopalachari first indian governor general |
| T8 | swatantra free economy land ceilings, jana sangh hindi national language, socialists criticised congress capitalists, cpi russian revolution inspired, ambedkar scheduled castes federation, opposition parties role check |
| T9 | jana sangh one culture one nation, socialist party splits ssp psp, swatantra against planning nationalisation, cpi founded 1920s, swatantra masani ranga munshi |
| T10 | dange cpi leader, balraj madhok jana sangh, lohia socialist leader, kripalani kmpp, socialist second votes 1952, jana sangh atomic weapons |
| T11 | first election oct 1951 feb 1952, first election postponed twice, literacy 15 percent first election, first election results accepted, first election proved critics wrong |
| T12 | cpi organised cadre, jana sangh urban north base, swatantra support industrialists landlords, csp formed within congress false, congress social coalition classes, cpi support regions |

### I2 Nation-building and its problems

| Test | Answer facts |
|---|---|
| T1 | src 1953 act 1956 14 states, potti sriramulu andhra, gujarat maharashtra 1960, manipur 1948 universal franchise, razakars nizam hyderabad |
| T2 | nagaland 1963, gujarat maharashtra 1960, haryana 1966, meghalaya 1972, patel princely states integration, partition religious majorities |
| T3 | 565 princely states, instrument of accession, hyderabad army september 1948, manipur merger 1949 assembly not consulted, government approach princely states considerations |
| T4 | partition 80 lakh migrated, punjab bengal divided, ghaffar khan opposed partition, princely states not all joined by august 1947, andhra first linguistic state, hari singh accession october 1947 |
| T5 | uttarakhand from up, chhattisgarh from mp, jharkhand from bihar, telangana from andhra 2014, linguistic reorganisation postponed partition fear, tryst with destiny nehru |
| T6 | three challenges nation building, potti sriramulu fast 56 days, partition division of assets, nehru not keen linguistic states, andhra state 1953, states reorganisation act 1956, maharashtra gujarat 1960, punjab haryana 1966, travancore refused to join |
| T7 | two nation theory meaning, linguistic state meaning, princely state meaning, refugee meaning, andhra telugu, src appointed 1953 |
| T8 | gandhi kolkata 15 august 1947, gandhi assassination godse, rss banned after assassination, hyderabad not acceded 1947, east pakistan bangladesh, linguistic states strengthened unity |
| T9 | fazl ali src chairman, bodhachandra singh manipur, nizam osman ali khan, jinnah pakistan demand, partition problems minorities both sides, telangana peasant movement communists |
| T10 | paramountcy lapse princely choice, patel deputy pm home minister, bombay bilingual state, hyderabad largest princely state, vishalandhra telugu madras, four difficult princely states |
| T11 | hari singh accession 1947 order, manipur merger 1949 order, three states created 2000, telangana state 2014, partition deaths 5 to 10 lakh, punjabi suba movement |
| T12 | vishalandhra telugu state, mahagujarat gujarati state, samyukta maharashtra marathi, punjabi suba punjabi state, india secular state minorities, hyderabad standstill agreement |

### I3 Politics of planned development

| Test | Answer facts |
|---|---|
| T1 | first plan agriculture, bombay plan 1944 |
| T2 | planning commission 1950 resolution, kerala model education health |
| T3 | mahalanobis second plan, kumarappa gandhian economist, kurien operation flood, kn raj first plan, green revolution middle peasants |
| T4 | planning commission chaired pm, niti aayog 2015, second plan heavy industry, planning commission not constitutional, mixed economy |
| T5 | planning commission 1950, second plan 1956, bank nationalisation 1969, niti aayog 2015, second plan neglect agriculture criticism |
| T6 | land ceiling meaning, green revolution hyv seeds, operation flood milk cooperatives, zamindari abolition meaning, soviet model five year plans |
| T7 | second plan tariffs protection, first plan not heavy industry, bhakra nangal foundations, state control inefficiency corruption, green revolution punjab haryana west up |
| T8 | first plan 1951, second plan 1956, plan holiday 1966, operation flood 1970, odisha iron ore tribals displacement |
| T9 | charan singh agriculture planning, land ceiling poorly implemented false, green revolution disparity, bihar food crisis 1960s, kerala peoples plan campaign decentralised |
| T10 | bombay plan industrialists, anand amul cooperative, bhilai steel plant, zamindari abolition intermediaries, green revolution subsidised inputs price support |
| T11 | first plan cycle of poverty, public sector heavy industries, private sector agriculture trade, green revolution mid 1960s not 1950s, white revolution milk |
| T12 | second plan quick structural transformation, planning commission not abolished 1977 false, liberalisation away from planning, operation flood rural urban link, planning state role remove poverty |

### I4 India's external relations

| Test | Answer facts |
|---|---|
| T1 | panchsheel 1954, bandung 1955, tashkent 1966, shimla 1972, krishna menon resigned 1962, indo soviet treaty 1971 reason |
| T2 | nam belgrade 1961, dalai lama asylum 1959, panchsheel peaceful coexistence, tashkent kosygin mediated, pokhran 1974 |
| T3 | bandung 1955, chinese aggression 1962, pokhran ii 1998, kargil 1999, nam founders zhou not, no first use doctrine |
| T4 | pm 1962 nehru, pm 1965 shastri, pm 1971 indira, pm 1998 vajpayee, dhaka surrender 1971, nonalignment reason independent policy |
| T5 | india recognise prc early, china tibet 1950, 1962 war both sectors, cpi split 1964 china, homi bhabha nuclear programme, npt discriminatory reason |
| T6 | panchsheel 1954, dalai lama asylum 1959, nam belgrade 1961, indo soviet treaty 1971, kashmir referred un 1948, nehru foreign minister |
| T7 | nehru three foreign policy aims, asian relations conference 1947, indonesia freedom conference 1949, nonalignment not isolation neutrality, nonalignment aid both blocs |
| T8 | hindi chini bhai bhai, mcmahon line, aksai chin, nefa arunachal, credible minimum deterrence, us china pakistan axis 1971 |
| T9 | indus treaty nehru ayub 1960, 1965 war rann of kutch, shimla indira bhutto 1972, india did not sign npt, 1956 hungary not condemned, 1971 refugees east pakistan |
| T10 | first kashmir war 1947 48, china nuclear test 1964, pokhran peaceful explosion 1974, kargil conflict 1999, first no confidence motion 1963, india opposed apartheid |
| T11 | nehru nuclear disarmament, janata genuine nonalignment |
| T12 | krishna menon defence minister 1962, kosygin soviet pm tashkent, zhou enlai chinese premier, bhabha led nuclear programme, 1965 indian army lahore, tibetan refugees india |

### I5 Challenge to and restoration of the Congress system

| Test | Answer facts |
|---|---|
| T1 | kamaraj plan 1963, indira pm 1966, 1967 congress lok sabha majority, shastri pm 1964, fourth general election 1967, bank nationalisation 1969, 1971 election garibi hatao, aya ram gaya ram gaya lal haryana |
| T2 | kamaraj kingmaker, lohia non congressism, vv giri independent president 1969, sanjeeva reddy official candidate, syndicate congress leaders, grand alliance 1971 no positive programme |
| T3 | congress split 1969 o and r, privy purses abolished, 1971 congress two thirds, jai jawan jai kisan, nijalingappa expelled indira |
| T4 | nehru died 1964, shastri died tashkent 1966, congress split 1969 o and r, 1971 election garibi hatao, samyukt vidhayak dal, privy purse meaning |
| T5 | 1967 political earthquake, goongi gudia |
| T6 | defection meaning, coalition meaning, non congressism meaning, conscience vote 1969, shastri succeeded nehru 1964, ten point programme 1967 |
| T7 | indira hatao slogan, congress r 352 seats 1971, 1971 election held early, grand alliance lost 1971, charan singh up cm 1967, pl 480 food imports |
| T8 | devaluation 1966, fourth general election 1967, bank nationalisation july 1969, giri elected president august 1969, congress o syndicate faction, split ideological framing |
| T9 | morarji lost leadership 1966, sk patil syndicate bombay, giri won 1969 independent, sanjiva reddy official nominee 1969, congress lost nine states 1967, indira left turn not us pact |
| T10 | 1967 first election without nehru, congress r minority cpi dmk support, syndicate backed reddy not giri, grand alliance members, bangladesh victory boosted indira 1972, kamaraj madras cm |
| T11 | atulya ghosh syndicate bengal, annadurai dmk madras 1967, gaya lal defections haryana, charan singh left congress up 1967, congress restored dependent on leader, syndicate thought indira dependent |
| T12 | congress r requisitionists, congress o syndicate faction split, kamaraj plan leaders resign, svd non congress coalitions, 1967 background economic crisis, garibi hatao social groups |

### I6 Crises of the constitutional order

| Test | Answer facts |
|---|---|
| T1 | article 352 internal disturbance, emergency declared 25 june 1975, raj narain election petition, shah commission emergency excesses, emergency press censorship preventive detention, lok sabha term extended |
| T2 | navnirman gujarat 1974, jp total revolution, supersession judges 1973, railway strike george fernandes, morarji desai first non congress pm, pucl civil liberties |
| T3 | 42nd amendment lok sabha six years, turkman gate demolition, compulsory sterilisation, committed bureaucracy, congress for democracy jagjivan ram |
| T4 | 1977 congress lost north, janata government fell, charan singh pm 1979, congress won 1980, bihar movement students jp, elections march 1977 |
| T5 | preventive detention meaning, habeas corpus meaning, press censorship meaning, total revolution meaning, kesavananda 1973, gujarat agitation january 1974, allahabad verdict june 1975, janata party formed january 1977, indian express blank space censorship |
| T6 | emergency internal disturbance, 1977 elections not court ordered, 44th amendment armed rebellion, right to move courts suspended, fakhruddin ali ahmed, rss jamaat banned emergency |
| T7 | committed judiciary meaning, basic structure doctrine meaning, misa detention law, twenty point programme emergency, janata party won 1977, 42nd amendment six years |
| T8 | emergency weaknesses strengths, 1977 referendum on emergency, congress held south 1977, opposition merged janata, morarji first non congress pm, 111000 arrested preventive detention |
| T9 | bihar movement march 1974, jp march parliament 1975, elections announced january 1977, shah commission appointed may 1977, cpi supported emergency |
| T10 | an ray chief justice supersession, raj narain defeated indira 1977, jc shah inquiry, sanjay gandhi no official post, janata 295 seats 1977, writers returned awards emergency |
| T11 | cabinet informed after emergency, elections postponed 1976 emergency, fundamental rights not enforceable false, 1977 congress lost centre first, jp appeal army police, janata components bld |
| T12 | supersession judges 1973 order, allahabad verdict 1975 order, 42nd amendment passed 1976, 44th amendment 1978, 39th amendment pm election court, janata infighting leadership |

### I7 Regional aspirations and conflicts

| Test | Answer facts |
|---|---|
| T1 | anandpur sahib 1973, operation blue star 1984, rajiv longowal accord 1985, mizo accord 1986, states carved out of assam, aasu assam movement |
| T2 | nagaland 1963, sikkim merger 1975, assam accord 1985, mizoram state 1987, phizo naga national council, dmk annadurai 1949 |
| T3 | indira assassinated october 1984, anti sikh violence 1984, punjab militancy continued after accord, mnf famine 1959, article 370 august 2019 |
| T4 | laldenga mizoram, longowal punjab, sheikh abdullah kashmir, mahanta assam, anandpur sahib autonomy, seven sisters north east |
| T5 | akali dal 1920 political wing, operation blue star june 1984, punjab accord chandigarh transfer, accord provisions tribunal afspa withdrawal, punjab 1992 low turnout |
| T6 | periyar dravidian movement, anti hindi agitation 1965, assam movement 1979 1985, goa portuguese 1961, sheikh abdullah dismissed 1953, indira sheikh accord 1974, kashmir militancy 1989, article 370 abrogated 2019, agp 1985 assam |
| T7 | goa opinion poll 1967, sikkim became state 1975, bodo autonomy demand, dmk power madras 1967, ladakh buddhists muslims, regional aspirations democratic approach not |
| T8 | nagaland statehood 1963, mnf armed campaign 1966, manipur tripura states 1972, assam accord 1985, chandigarh shared capital, kashmiriyat |
| T9 | karbi dimasa autonomy, kazi lhendup dorji sikkim, mgp goa merger maharashtra, farooq abdullah cm, assam movement illegal migrants bangladesh, goa statehood 1987 |
| T10 | sikkim referendum 1975, naga independence 1951, akali coalition governments 1967 1977, mizo accord rajiv not indira, 1987 elections jk rigging, chogyal ruler sikkim |
| T11 | dmk founded 1949 order, goa liberated 1961 order, anti hindi agitation 1965 order, dmk government madras 1967, siliguri corridor 22 km |
| T12 | arunachal state 1987 nefa, tripura indigenous minority migration, meghalaya carved assam 1972, goa opinion poll rejected merger, khalistan demand militants, sikkim 22nd state |

### I8 Democratic upsurge and coalition politics

| Test | Answer facts |
|---|---|
| T1 | mandal commission janata government, 27 percent obc reservation, mandal implemented vp singh 1990, national front 1989, united front 1996, nda 1998, upa 2004 |
| T2 | vp singh national front, deve gowda united front, chandra shekhar congress support, vajpayee nda, 2014 bjp majority own, coalition era regional parties role |
| T3 | bjp formed 1980, janata dal 1988, 1989 no single party majority, 1991 congress minority government, rajiv gandhi assassinated 1991, upa left outside support |
| T4 | chandra shekhar 1990, rao 1991, deve gowda 1996, gujral 1997, bjp 2 seats 1984, nda 1999 2004 full term |
| T5 | 2019 nda returned, consensus economic policy, consensus backward castes claims, pragmatism over ideology, congress 145 seats 2004 |
| T6 | bjp 85 seats 1989, bjp 120 seats 1991, bjp 182 seats 1998, bjp 282 seats 2014, vajpayee 13 days 1996, uf congress outside support |
| T7 | upa formed 2004, upa second term 2009, bjp majority own 2014, nda returned 2019, vp singh national front pm |
| T8 | coalitions norm after 1989, obc leaders north india, janata dal splits, bjp no majority 1998, congress 197 seats 1989, 2014 first majority since 1984 |
| T9 | second backward classes commission, mandal task identify sebc, anti mandal protests 1990, 1989 congress not restored, coalition era alliances necessary inference |
| T10 | bjp founded 1980 order, janata dal formed 1988, rajiv assassinated 1991 order, manmohan pm 2004, bjp withdrew support nf 1990, congress decline social base |
| T11 | 1991 congress minority government, 1996 bjp largest 13 days, 1999 nda full term, 2009 upa second term, nf supported by bjp and left, bipolar coalition competition |
| T12 | rao after rajiv, janata dal vp singh leader, no majority 1989 2014, uf not vajpayee, 1984 sympathy wave, five developments 1990s |

### I9 Recent issues and challenges

| Test | Answer facts |
|---|---|
| T1 | new economic policy 1991 rao |
| T2 | bamcef 1978, bsp 1984, mandal implemented vp singh 1990, new economic policy 1991 rao, ayodhya december 1992 |
| T3 | kanshi ram bsp founder, manmohan singh finance minister 1991, mayawati up cm, advani rath yatra 1990, faizabad 1986 unlocking |
| T4 | bamcef employees federation, obc parties up bihar, bsp dalit support, nep opposition left, bsp first government up 1995 |
| T5 | babri masjid mir baqi, demolition december 1992, faizabad locks 1986, bjp state governments dismissed, south states backward reservation early |
| T6 | obc full form, rath yatra somnath 1990 |
| T7 | economic crisis 1991, supreme court upheld obc reservation, obc 27 percent, mandal not rajiv, ayodhya secularism debate |
| T8 | kar sevaks, hindutva savarkar, bahujan meaning, liberalisation meaning, mandal commission appointed janata 1978 |
| T9 | shah bano 1985, national front government fell 1990, mandal report submitted 1980, bsp founded 1984, vhp ayodhya movement |
| T10 | nep not vp singh false, bsp broadened support, advani arrested bihar 1990, hindutva hinduness, muslim women act 1986 |
| T11 | ram janmabhoomi belief, dalit meaning oppressed, reservation meaning quota, rath yatra mobilisation, bjp hindutva after 1986 |
| T12 | bamcef formed 1978 order, muslim women act passed 1986, bsp up government 1995 order, mandal report 1980 order, demolition communal riots aftermath |

### W1 Collapse of bipolarity

| Test | Answer facts |
|---|---|
| T1 | ussr 15 republics, cis formed 1991, russia inherited security council seat, shock therapy rapid imf, gorbachev general secretary 1985, berlin wall fell 1989, lithuania independence 1990, ussr dissolved 1991, glasnost openness, central asian republics |
| T2 | perestroika restructuring, second world socialist bloc, shock therapy rapid imf, warsaw pact military alliance, berlin wall built 1961, soviet afghanistan 1979, gorbachev general secretary 1985, german unification 1990, chechnya dagestan secessionist, russia military hardware india |
| T3 | soviet planned economy state ownership, soviet afghanistan 1979, yeltsin president russia, nationalism republics, yugoslavia breakup balkans, tajikistan civil war 2001, india russia multipolar world |
| T4 | shock therapy world bank imf model, largest garage sale, rouble fell inflation savings, oligarchs inequality welfare dismantled, strong executive president weak parliament |
| T5 | lenin 1917 revolution, stalin collectivisation, khrushchev peaceful coexistence, brezhnev afghanistan, soviet planned economy state ownership, soviet collapse not nato war, lithuania first independence 1990 |
| T6 | ussr after 1917 revolution, soviet bureaucratic authoritarian, soviet lagged west living standard, communist party dominance, berlin wall falls 1989, yeltsin elected june 1991, soviet coup august 1991, ussr dissolved december 1991, czechoslovakia split peacefully, germany unified 1990, yugoslavia violent breakup, baltic states eu nato, india oil investments russia kazakhstan |
| T7 | gorbachev last soviet leader, central asia hydrocarbons, russia supports india kashmir, gorbachev reforms unleashed expectations |
| T8 | ukraine eastern europe republic, kazakhstan central asia, georgia caucasus, latvia baltic, soviet ideology communism, gorbachev no intervention eastern europe, eastern europe communist collapse 1989 |
| T9 | soviet economy second to us, soviet minimum living standard, soviet no multiparty false, soviet arms spending burden, indo russian strategic agreement 2001, russia successor state ussr, warsaw pact dissolved consequence |
| T10 | chechnya violent secession, tajikistan decade civil war, nagorno karabakh armenia, georgia two provinces secession, ussr formed 1922, soviet troops hungary 1956, soviet invasion czechoslovakia 1968, tajik civil war ended 2001, russian dominance other regions, soviet energy resources oil steel |
| T11 | soviet shortages consumer goods, gorbachev criticised both sides, shock therapy collective farms food security, russia not nato, russia nuclear energy space india, us sole superpower after 1991, russia gdp 1999 below 1989 |
| T12 | gorbachev normalise west, citizens aware western progress, ussr dissolved by un false, russia ukraine belarus cis, spain not soviet bloc, end ideological rivalry |

### W2 Alternative centres of power

| Test | Answer facts |
|---|---|
| T1 | asean 1967, asean regional forum 1994, maastricht treaty 1992, china wto 2001, asean founding members, asean way informal cooperative, japan g7 nuclear |
| T2 | eu flag anthem currency, eec 1957, maastricht created eu, china special economic zones, rajiv gandhi china 1988 |
| T3 | eec 1957, asean 1967, maastricht treaty 1992, euro notes 2002, china agriculture 1982 industry 1998, south korea miracle han river, asean community three pillars |
| T4 | schengen border free, euro common currency, asean economic community market, asean vision 2020, china revolution 1949, china open door 1978, china agriculture 1982 industry 1998, china wto 2001, asean objective growth |
| T5 | eu flag stars solidarity, japan 1 percent gdp military, china reforms coastal inland gap, eu military second largest |
| T6 | marshall plan us aid, oeec 1948 channel aid, council of europe 1949, not all eu members euro, eu influence economic political diplomatic |
| T7 | asean bangkok declaration 1967, japan un budget contributor, south korea brands, eu biggest economy 2005, asean founded 1967, china open door 1978, rajiv visit china 1988, euro introduced 2002, china overtake us 2040, japan hiroshima nagasaki |
| T8 | asean ten members, eu no binding common foreign policy, china fdi trade growth, south korea un 1991, thailand asean founder, japan few resources imports, india china trade talks since 1988 |
| T9 | japan brands sony toyota, south korea asian tiger, denmark sweden resisted euro, india look east 1991, korea divided 38th parallel 1945, korean war ended 1953, koreas joined un 1991, south korea oecd 1996, euro challenge dollar, france eu permanent unsc |
| T10 | china soviet model 1949, deng xiaoping reforms, eu eastern enlargement, asean not supranational, india fta singapore thailand, sri lanka not asean, india china ties restored 1976 |
| T11 | mao communist revolution 1949, deng open door announced, japan only asian g7, britain no euro left eu, asean mediated cambodia east timor, eu world trade three times us, china no shock therapy gradual |
| T12 | india china nuclear powers, sez foreign investment china, afta free trade area, japan not permanent, korean war ended 1953 order, india china full ties 1976 order, look east launched 1991, arf set up 1994, china reforms unemployment, eu divided iraq 2003 |

### W3 South Asia after the Cold War

| Test | Answer facts |
|---|---|
| T1 | saarc 1985, safta 2004, maldives multiparty 2005, nepal monarchy abolished 2008, ipkf 1987 accord, bhutan flushed out militants, musharraf 1999 |
| T2 | mujib bangladesh, bhutto pakistan, gyanendra nepal, ltte sri lanka, bangladesh independence 1971, saarc 1985, pakistan nuclear test 1998, safta in force 2006, saarc members myanmar not, pakistan army clergy landowners |
| T3 | bangladesh part of pakistan 1971, sri lanka democracy since 1948, bangladesh presidential 1975, sri lanka tamil conflict, nepal monarchy abolished 2008, bangladesh look east, sri lanka human development |
| T4 | indus waters treaty 1960, ganga water dispute bangladesh, india sri lanka fta, bhutan hydro projects, ayub khan 1958, maldives republic 1968, safta tariffs 20 percent 2007 |
| T5 | bhutan move to democracy, nepal 1990 democratic constitution, mujib assassinated 1975, sri lanka retained democracy, siachen glacier dispute, bangladesh refused gas export, benazir nawaz alternating |
| T6 | nepal open border treaty, maldives 1988 coup foiled, sri lanka tsunami help, bangladesh illegal migration, maldives island country, nepal maoists insurgency, pakistan nuclear tests 1998 |
| T7 | india pakistan cbms, bangladesh military rule, nepal hindu kingdom, ltte defeated 2009, saarc full form, pakistan democracy lack international support, nepal china relations friction |
| T8 | sinhala majority, ltte armed struggle 1983, ipkf withdrew 1989, sri lanka growth despite conflict, norway iceland mediation |
| T9 | ayub khan coup 1958, zia ul haq 1977, musharraf takeover 1999, bangladesh democracy restored 1991, maldives economy tourism fishing, awami league 1970 elections, smaller neighbours fear india dominance |
| T10 | nepal 2006 protests seven party, bangladesh river water sharing, sir creek dispute, maldivian democratic party, bangladesh constitution secular socialist, safta fear india invade markets, bhutto power after 1971 |
| T11 | india pakistan wars 1947 1965 1971, bhutan monarchy, bangladesh saarc founder, nepal india no visa false, sri lanka independence 1948, mujib assassinated 1975 order, maldives coup foiled 1988, nepal democracy 1990, urdu imposition east pakistan, nepal bhutan landlocked |
| T12 | zia takes power 1977 order, ipkf sent 1987 order, safta signed 2004 order, ltte defeated 2009 order, eelam tamil homeland, mujib one party awami, china pakistan partnership |

### W4 International organisations

| Test | Answer facts |
|---|---|
| T1 | imf financial regulation, world bank loans development, wto global trade rules, iaea peaceful nuclear energy, security council 15 members, kofi annan ghana, amnesty international ngo human rights |
| T2 | un founded 1945, five permanent veto, general assembly one vote, india non permanent member, guterres portugal, wto 1995 successor gatt |
| T3 | trygve lie norway, hammarskjold sweden, u thant burma, ban ki moon south korea, league of nations 1919, un charter 1945, iaea 1957, wto 1995, unsc new members criteria, human rights watch ngo us |
| T4 | un 51 founding states, india founding member un, imf g7 votes, world bank president us, non permanent members two years, icj hague, unhcr refugees |
| T5 | unicef children, unesco education culture, who health, undp development, atlantic charter 1941, declaration united nations 1942, san francisco conference 1945, un founded 24 october 1945, un headquarters new york, bretton woods 1944 |
| T6 | ga one vote each, sg appointed ga on sc recommendation, p5 veto, india non permanent several times, un 193 members, germany not permanent member |
| T7 | ecosoc economic social, trusteeship council territories, secretariat sg daily work, security council peace, wto 1995, brazil permanent seat claim, un relevance unipolar world |
| T8 | imf oversees international finance, world bank loans grants, wto unanimity major powers, amnesty not un agency, un founded 1945 org, unsc enlarged 1965, wto set up 1995 succession, human rights council 2006, veto criticism undemocratic, us largest un budget contributor |
| T9 | boutros ghali egypt, perez de cuellar peru, waldheim austria, annan ghana sg, india permanent seat peacekeeping, peacebuilding commission 2005, world bank areas human development |
| T10 | unsc reflects 1945 power, unsc underrepresented developing regions, veto reform debate passage, council not expanded with ga, unsc reform needs p5 consent |
| T11 | un reform two kinds, un needed global issues, non permanent elected ga, sg no veto false, trygve lie first sg, u thant sg 1961, boutros ghali sg 1992, ban ki moon sg 2007, unicef not principal organ, un created prevent war |
| T12 | human rights council 2006 body, peacebuilding commission recovery, democracy fund un, mdgs agreed 2005, iaea inspections, wto dominated rich powers, unsc criteria not nuclear |

### W5 Security in the contemporary world

| Test | Answer facts |
|---|---|
| T1 | npt 1968, bwc 1972, start i 1991, cwc 1992, human security freedom from want fear, internally displaced persons |
| T2 | traditional security military threat, terrorism non traditional, global poverty threat, hiv aids epidemic threat, balance of power meaning |
| T3 | abm treaty limits defence, cwc bans chemical, npt nuclear states 1967 rule, start reduce strategic, cooperative security many actors, india security strategy components |
| T4 | npt 1968, bwc 1972, cwc 1992, ctbt 1996, 9 11 2001 terrorism, human rights three categories |
| T5 | deterrence meaning, defence meaning, alliance building meaning, global poverty meaning, nontraditional not border war, arms control meaning |
| T6 | wmd three types, rwanda genocide 1994, sars epidemic |
| T7 | human security individuals, global threats cooperation, terrorism targets civilians, refugees cross borders, abm treaty 1972, salt ii 1979, ctbt 1996, september 11 attacks 2001, sub saharan africa poorest |
| T8 | political rights examples, economic rights examples, minority rights cultural identity, humanitarian intervention meaning, security basic meaning freedom from threats, arms race meaning |
| T9 | population growth six countries, human security people not states false, india internal militancy, migrants vs refugees, global warming sea level maldives, cooperative security ngos red cross |
| T10 | start i 1991 signed, start ii 1993, rwanda 1994 genocide, sars 2003 outbreak, human security narrow broad, bird flu mad cow epidemics |
| T11 | disarmament meaning, arms control regulating, confidence building meaning, balance of power rival, third world internal external threats, cooperative security force last resort |
| T12 | human security people first, global threats affect all, terrorism targets civilians concept, cooperative security many partners, non state actors threats |

### W6 Environment and natural resources

| Test | Answer facts |
|---|---|
| T1 | earth summit rio 1992, kyoto protocol 1997, montreal protocol 1987, antarctic treaty 1959, cbdr rio declaration, sacred groves common property |
| T2 | global commons four areas, montreal protocol ozone, global commons cooperation difficult north south, outer space technology north south, common property community rules |
| T3 | agenda 21 development practices, unfccc 1992, kyoto binding targets industrial, wcip 1975, club of rome limits to growth, india ratified kyoto 2002 |
| T4 | rio conventions climate biodiversity forestry, brundtland sustainable development, south development priority, india no binding targets, indigenous peoples un definition, gulf oil 30 percent |
| T5 | auto fuel policy cleaner fuels, energy conservation act 2001, electricity act 2003 renewable, india per capita emissions low, antarctic treaty 1959, limits to growth 1972, brundtland report 1987, kyoto protocol 1997, rio 170 states |
| T6 | ozone hole antarctic, grasslands overgrazed fisheries, coastal pollution rising, safe water 1 2 billion, carbon dioxide greenhouse gas, shared rivers conflict reason |
| T7 | ozone depletion cfcs, acid rain sulphur nitrogen, biodiversity loss forests, desertification overgrazing, rio brazil earth summit, indigenous displacement development |
| T8 | india per capita above average false, north wants equal responsibility, industrialised historical emissions, ozone layer uv protection, kyoto japan, oil central world economy |
| T9 | western mining philippines, narmada anti dam, franklin river australia, antarctic environmental protocol 1991, resource geopolitics cold war supply, unep environment conferences |
| T10 | kyoto based on unfccc, global north industrialised, antarctica not owned, environment global agenda 1960s, forest movements south countries |
| T11 | sacred groves community forest, outer space technology gap, atmosphere montreal ozone, antarctica scientific research treaty, indigenous demand land rights, agenda 21 criticism growth bias |
| T12 | commons decline privatisation, montreal not ghg false, un working group indigenous 1982, antarctica largest wilderness, saudi arabia quarter oil reserves, sustainable development meaning |

### W7 Globalisation and its critics

| Test | Answer facts |
|---|---|
| T1 | globalisation flows four kinds, mcdonaldisation homogenisation, wsf porto alegre 2001, india reforms 1991, wsf mumbai 2004, cultural heterogenisation jeans kurta |
| T2 | left critics capitalism phase, right critics traditional culture, advocates prosperity, wsf neo liberal opposition, minimalist state welfare, right wing valentines day |
| T3 | state capacity globalisation mixed, technology internet globalisation, people flows restricted, interconnectedness, technology cause globalisation, neem patent resistance |
| T4 | mnc meaning, social safety net, wsf meaning, neo liberalism meaning, globalisation dimensions, seattle 1999 wto protests |
| T5 | globalisation flows four, people movement restricted, mcdonaldisation, globalisation uneven effects, wto trade rules, indian social forum |
| T6 | economic globalisation trade investment, political globalisation welfare state, cultural globalisation western food dress, technology internet flows, outsourcing call centres, critics arguments not reduce poverty |
| T7 | india globalisation not 1947, foreign investment india rose, resistance left right india, 1991 reforms controls removed, globalisation interconnectedness, globalisation not new india history |
| T8 | flow of ideas, flow of capital, flow of commodities, flow of people, consumer choice globalisation |
| T9 | globalisation only economic false, welfare state minimalist, recolonisation critique, colonial india primary exporter, welfare cuts poor vulnerable, imf wto drive globalisation |
| T10 | seattle 1999 wto ministerial, nairobi wsf 2007, neem patent symbol, indian social forum counterpart, mncs reduce state decision, cultural globalisation enlarges choices |
| T11 | neo liberal market over state, india trade before 1991 false, technology enhances state capacity, wsf broad coalition, state remains primary political community, economic globalisation removes barriers |
| T12 | rich richer poor poorer, resistance against particular programme, resisters use global networks, wsf not party, resistance itself global inference |
