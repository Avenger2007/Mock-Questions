# Coverage map — CUET History, Tests 1–15

This map was written **before** any test, so that repeats are prevented rather than fixed. Rules:

- Every source-passage theme in §A is used **once** in the series.
- Each **answer fact** is a short key such as `kalibangan ploughed field`, `fifth report 1813` or `dandi march 1930`.
  - An answer fact is the fact a question turns on. Each correct pair in a match item, and each event in a sequence, is its own fact.
  - A key may be used **at most twice in the series**, in different tests and different formats.
  - Before a test ships, its keys are checked against the ledgers in §C (`his_check.py`, flag `REPEAT-TARGET`) and then added to them (`mark_his.py`).
  - Distractors may repeat.
- Every test covers all twelve themes in the quotas set in the blueprint (§3).

## A. Source passage per test (5 linked questions)

| Test | Theme | Source (original summary) |
|---|---|---|
| 1 | H1 | Drains and town planning at Mohenjodaro, as excavators described them |
| 2 | H8 | The *Ain-i Akbari*'s classification of land (polaj, parauti, chachar, banjar) and revenue |
| 3 | H12 | The Constituent Assembly debate on separate electorates |
| 4 | H4 | Sanchi: how the stupa survived, the Begums of Bhopal and its gateways |
| 5 | H10 | The annexation of Awadh and the dispossession of the taluqdars |
| 6 | H5 | Ibn Battuta on the postal system (*uluq* and *dawa*) |
| 7 | H9 | The Santhals and the Damin-i-Koh |
| 8 | H2 | The Prayaga prashasti of Samudragupta and what prashastis can and cannot tell |
| 9 | H6 | The Chishti khanqah: Nizamuddin Auliya's hospice and its visitors |
| 10 | H11 | The Salt March (Dandi, 1930) |
| 11 | H7 | Paes on the Mahanavami festival and the Mahanavami dibba |
| 12 | H3 | Gotra rules and the names of Satavahana queens |
| 13 | H5 | Bernier on crown ownership of land |
| 14 | H9 | The Deccan riots of 1875 and the Deccan Riots Commission |
| 15 | H1 | Craft production: Chanhudaro, Nageshwar, Balakot and the search for raw materials |

## B. Slot rotation (keeps each theme's questions moving across the series)

- **H1:** sites and their evidence; subsistence; drainage and planning; crafts and raw materials; seals, script, weights; social difference (burials, luxuries); the decline debate as NCERT keeps it; discovery (Cunningham, Daya Ram Sahni, R.D. Banerji, Marshall, Wheeler); archaeogenetics.
- **H2:** Prinsep and the scripts; mahajanapadas; Magadha; Mauryas and their sources; Gupta prashastis; land grants (Prabhavati Gupta); the *Arthashastra*, the *Indica*; coins (punch-marked, Kushana, Gupta gold); urban centres; the limits of inscriptions.
- **H3:** the critical edition (Sukthankar); kinship terms (kula, jati, vamsha); gotra; marriage forms; varna and jati; Manusmriti; Ekalavya, Hidimba, Draupadi; Satavahanas; Sakas; *mlechchhas*; property rules; the text's composition.
- **H4:** sixth-century BCE thinkers; Vedic deities; Buddha's teachings; the sangha and bhikkhunis; the Tipitaka; the Jaina tradition; stupas (Sanchi, Amaravati); chaitya and vihara; the Mahayana; Puranic Hinduism; cave temples and early temple architecture.
- **H5:** al-Biruni (*Kitab-ul-Hind*); Ibn Battuta (*Rihla*); Bernier (*Travels in the Mughal Empire*); other travellers (Barbosa, Monserrate, Tavernier, Manucci); slavery; women (sati); towns and trade; land ownership.
- **H6:** Alvars and Nayanars; Virashaivas (Basavanna); the Sufi silsilas; Chishti saints and dargahs; Kabir; Guru Nanak; Mirabai; the integration of cults (Jagannatha); terms (*khanqah*, *ziyarat*, *sama*, *pir*, *murid*).
- **H7:** discovery (Mackenzie); dynasties and rulers; Krishnadeva Raya; the amara-nayakas; the battle of Talikota (Rakshasi-Tangadi); water resources (Tungabhadra, Kamalapuram tank); fortifications; the royal centre; the sacred centre (Virupaksha, Vitthala); travellers to Vijayanagara.
- **H8:** sources (*Ain-i Akbari*); peasants (*khud-kashta*, *pahi-kashta*); irrigation; crops (jins-i kamil); the village panchayat and the muqaddam; artisans; women; forests and tribes; zamindars (milkiyat); land revenue (jama, hasil, amin, amil-guzar); the flow of silver.
- **H9:** the Permanent Settlement (1793); the Sunset Law; jotedars; the Fifth Report (1813); Buchanan; the Paharias; the Santhals and the 1855–56 revolt; the Ryotwari settlement; the Deccan riots (1875); the cotton boom; the Limitation Law.
- **H10:** how the revolt spread (Meerut, Delhi, Bahadur Shah Zafar); leaders (Nana Sahib, Rani Lakshmi Bai, Kunwar Singh, Shah Mal, Maulvi Ahmadullah Shah, Birjis Qadr, Begum Hazrat Mahal); Awadh and subsidiary alliance; rumours and prophecies; rebel proclamations (*ishtahar*); British repression; images and representations.
- **H11:** South Africa; Champaran, Kheda, Ahmedabad; the BHU speech (1916); Rowlatt Satyagraha; Non-Cooperation and Chauri Chaura; Khilafat; Purna Swaraj (Lahore 1929); the Salt March; Gandhi–Irwin Pact; Round Table Conferences; Poona Pact; Quit India; sources (letters, autobiography, police records, newspapers).
- **H12:** the Constituent Assembly (composition, sessions, dates); the Objectives Resolution; separate electorates; the depressed classes and Ambedkar; tribal protection (Jaipal Singh); the powers of the states and the centre; the national language; Rights; the Constitution's adoption and its coming into force.

## C. Ledgers (filled as tests are shipped)

### H1 Harappan civilisation and archaeology

| Test | Answer facts |
|---|---|
| T1 | drains laid out first, harappan brick ratio 4-2-1, citadel west raised platform, harappan house privacy, drainage implies planning authority |
| T2 | harappa brick robbers railway, mohenjodaro great bath, kalibangan ploughed field, dholavira water reservoirs, harappan script undeciphered, harappan script right to left, harappan script not alphabetic, daya ram sahni harappa, lothal gujarat, archaeogenetics ancient dna rakhigarhi |
| T3 | cunningham first dg asi, marshall announced 1924, wheeler stratigraphy, rd banerji mohenjodaro seals, harappa excavations 1921, mohenjodaro excavations 1925, lothal sr rao 1955, dholavira rs bisht 1990, steatite seals, harappan weights chert binary, faience ground sand |
| T4 | harappan burials pits, burial goods afterlife, jewellery men women burials, named after first site, mohenjodaro great bath, archaeozoologists |
| T5 | citadel mud brick platforms, lower town residential walled, warehouse wooden upper portions, great bath steps north south, mother goddess figurines, proto-shiva seal, stone lingas, harappan religion uncertain, millets gujarat, mohenjodaro 700 wells, mature harappan 2600 1900 bce |
| T6 | cunningham seal report 1875, marshall announced 1924, wheeler dg 1944, rakhigarhi dna 2010s, meluhha mesopotamian texts, meluhha products, omani copper nickel, 375 400 signs, mohenjodaro sindh, marshall horizontal units |
| T7 | rakhigarhi haryana, kalibangan rajasthan, harappa punjab pakistan, dholavira kutch, cholistan banawali plough models, shortughai canals not punjab, dholavira reservoirs agriculture, fire altars kalibangan lothal, houses courtyard, cholistan sites abandoned 1800 bce |
| T8 | stratigraphy layers, palaeobotany plant remains, archaeozoologists, archaeogenetics ancient dna, script on many objects signboard, kalibangan two crops furrows, indus valley civilisation |
| T9 | seals long-distance communication, intact sealing untampered, seals animal motif script, early harappan before 2600, mature harappan 2600 1900 bce, cholistan sites abandoned 1800 bce, daya ram sahni harappa, streets grid right angles, priest-king statue, great bath citadel |
| T10 | fish bones harappan diet, domesticated cattle sheep goat buffalo pig, wild boar deer gharial bones, chert weights, harappan script right to left, meluhha mesopotamia, harappa first site named |
| T11 | decline theories climate floods, late harappan seals weights disappear, writing trade disappear end, harappan decline not uniform, dales massacre skeletons, house drains connected street drains, staircases second storey, harappan sites afghanistan |

### H2 Early states: inscriptional evidence

| Test | Answer facts |
|---|---|
| T1 | prayaga prashasti harisena, junagadh sudarshana lake, prabhavati gupta land grant, ashokan inscriptions dhamma prakrit, chandragupta maurya c 321 bce, ashoka 3rd c bce, kanishka kushana, samudragupta 4th c ce, megasthenes indica, punch-marked coins silver copper |
| T2 | sreni guild, gahapati head of household, agrahara land to brahmanas, gana sangha oligarchy, magadha rise reasons, rajagaha pataliputra capital, prinsep mint officer, dhamma mahamatta |
| T3 | vajji vaishali, kosala shravasti, avanti ujjayini, gandhara taxila, arthashastra kautilya, five mauryan political centres, kushana first gold coins, iron ploughshare |
| T4 | yaudheya copper coins, gupta gold coins, roman coins south india, kushana first gold coins, mat mathura kushana statues, sixteen mahajanapadas, kharosthi northwest |
| T5 | ashokan edicts 3rd century bce, rudradaman junagadh 2nd century ce, prayaga prashasti 4th century, prinsep deciphers 1838, pataligrama, gandatindu jataka, numismatics coins |
| T6 | arthashastra kautilya, megasthenes indica, harshacharita banabhatta, sangam muvendar, land grants copper plates, grants to religious institutions, prabhavati gupta chandragupta ii daughter, rudradaman shaka, ashoka grandson chandragupta |
| T7 | bimbisara 6th century bce, mahapadma nanda 4th century bce, prabhavati gupta 5th century, harshavardhana 7th century, kautilya minister chandragupta, kalinga war remorse, samantas landholders |
| T8 | prayaga prashasti harisena, prayaga on ashokan pillar, dakshinapatha kings released, prashasti sanskrit, prashasti limits |
| T9 | prashasti praise, jataka previous births, epigraphy inscriptions, sudarshana lake junagadh, ashoka greek aramaic afghanistan, danguna village grant, pataliputra patna |
| T10 | chandragupta maurya 321 bce, kalinga war 261 bce, kushana rule first century, samudragupta fourth century, taxila northwest centre, ujjayini malwa centre, tosali orissa centre, suvarnagiri karnataka centre, vellalar landowners, megasthenes six subcommittees |
| T11 | dhamma respect elders, dhamma generosity brahmanas renouncers, dhamma treat slaves kindly, dhamma not forced conversion, gramabhojaka headman, gahapati household master, uzhavar ploughmen, adimai slaves, paddy transplantation ganga valley, sangam texts tamil |

### H3 Social histories: the Mahabharata

| Test | Answer facts |
|---|---|
| T1 | eight forms of marriage, kanyadana father's duty, paternal estate divided among sons, endogamy, ghatotkacha bhima hidimba, mahabharata composed over 1000 years |
| T2 | varna duties brahmanas kshatriyas vaishyas shudras, sukthankar critical edition 1919, mlechchha meaning, duryodhana eldest kaurava |
| T3 | ekalavya thumb, drona teacher, hidimba rakshasa bhima, draupadi polyandry, manusmriti 200 bce 200 ce, stridhana, patriliny |
| T4 | exogamy outside unit, polygyny several wives, polyandry several husbands, endogamy, chandalas outside village, chandalas discarded utensils, fa xian clapper, xuanzang outcastes outside city, mahabharata 100000 verses, bhagavad gita krishna arjuna |
| T5 | vyasa ganesha tradition, sutas charioteer-bards, brahmanas wrote down epic, itihasa thus it was, draupadi question dice, kurukshetra war |
| T6 | nishada forest dweller, suta charioteer bard, chandala lowest, mlechchha outsiders, only kshatriyas kings, gandhari advice peace, kuru lineage |
| T7 | shungas kanvas brahmanas, mauryas low origin, shakas mlechchhas, kuru lineage, mahabharata composition begins 500 bce, sukthankar critical edition 1919, hastinapura excavated 1951, critical edition completed 1966, purusha sukta, yudhishthira eldest pandava |
| T8 | jatis not fixed, mandasor silk weavers lata, mandasor sun temple, purusha sukta, dharmasutras 500 bce, manusmriti 200 bce 200 ce, mandasor silk weavers 5th century, narrative didactic sections, kauravas sons dhritarashtra |
| T9 | hidimba married bhima, bb lal hastinapura, vyasa author, ganesha scribe, paternal estate divided among sons, stridhana children inherit, royal women controlled land, dice duryodhana challenge, mahabharata sanskrit |
| T10 | dhritarashtra blind king, pandu father pandavas, kunti mother pandavas, draupadi married five pandavas, only kshatriyas kings, fa xian clapper, war between cousins |
| T11 | draupadi marriage before dice, dice before exile, exile before war, war at the end, epic dynamic text retellings, shudras serve higher varnas, draupadi panchala |

### H4 Buddhism and Jainism

| Test | Answer facts |
|---|---|
| T1 | vinaya pitaka rules for sangha, sutta pitaka teachings, abhidhamma pitaka philosophy, therigatha bhikkhunis, tirthankara meaning, amaravati andhra pradesh, bodhisatta mahayana |
| T2 | lumbini birth, bodh gaya enlightenment, sarnath first sermon, kusinagara mahaparinibbana, jaina five vows, makkhali gosala fatalist, vishnu ten avatars |
| T3 | rigveda compiled, buddha teaching, ashoka relics stupas, mahayana develops, mahapajapati gotami first bhikkhuni, anicca anatta dukkha, buddhism conduct over birth, chaitya chita funeral pyre, garbhagriha sanctum |
| T4 | sanchi plaster casts, amaravati dispersed sanchi preserved, hh cole casts, wheel first sermon, shalabhanjika popular beliefs |
| T5 | bhikkhu alms, upasika lay follower, kutagarashala debate hut, theravada elders, rigveda 1500 bce, barabar caves ajivikas, dashavatara deogarh 5th century, kailashnatha ellora 8th century, pali language buddhist texts, mahavira 24th tirthankara |
| T6 | harmika abode of gods, yashti chhatri, vedika railing, buddha images mathura taxila, puranas simple sanskrit, ahimsa jainism |
| T7 | makkhali gosala fatalist, ajita kesakambalin materialist, mahavira karma renunciation, buddha individual agency, sangha simple life, bhikkhus alms, sangha equality, vessantara jataka sanchi, siddhartha gautama |
| T8 | sanchi carved gateways, ajanta paintings jatakas, ellora kailashnatha monolith, barabar ajivika caves, buddha teaching 6th century bce, buddha images mathura taxila, amaravati discovered 1796, sanchi rediscovered 1818, vedic deities agni indra soma, upanishads atman brahman |
| T9 | jainism life in stones, jaina scholars languages, jaina five vows, vedic deities agni indra soma, upanishads atman brahman, ashokan inscriptions dhamma prakrit, puranas simple sanskrit, shiva linga, be lamps unto yourselves |
| T10 | mahapajapati gotami bhikkhuni, therigatha bhikkhunis, sangha consensus vote, bodhisattas mahayana, makkhali gosala ajivika, hinayana lesser vehicle |
| T11 | early temples small rooms, shikhara over sanctum, temple walls sculpted, temples grew elaborate, upasaka lay follower, stupa mound relics, vihara monastery, pradakshina patha, buddha teachings oral, buddha sakya clan |

### H5 Travellers' accounts

| Test | Answer facts |
|---|---|
| T1 | kitab-ul-hind al-biruni, rihla ibn battuta, travels in the mughal empire bernier, abdur razzaq ambassador herat, al-biruni barriers, ibn battuta muhammad bin tughlaq, al-biruni 11th century, ibn battuta 1333, abdur razzaq 1440s, bernier 1656-68 |
| T2 | al-biruni arabic writer, al-biruni translated sanskrit works, al-biruni caste persia comparison, bernier physician dara shukoh, barbosa south india trade |
| T3 | ibn battuta coconut paan, bernier sati lahore, al-biruni sanskrit caste texts, tavernier jeweller six visits, slaves sold in markets, female slaves spies, ibn battuta bought slaves gifts, kitab-ul-hind 80 chapters, ibn battuta tangier morocco |
| T4 | delhi vast city wall, daulatabad size, indian textiles demand, marco polo 13th century, nikitin 15th century, barbosa 16th century, manucci 17th century, al-biruni languages syriac persian hebrew sanskrit, karkhanas workshops |
| T5 | bernier widows forced, women labour crucial, merchant women courts, delhi 28 gates, al-biruni ghazni mahmud, bernier france |
| T6 | uluq horse post, dawa three stations per mile, dawa rod copper bells, foot post faster khurasan fruits, postal system integration |
| T7 | al-biruni ghazni mahmud, ibn battuta muhammad bin tughlaq, bernier physician dara shukoh, monserrate jesuit akbar, bernier camp towns, al-biruni rejected pollution, ibn battuta qazi |
| T8 | al-biruni language barrier, al-biruni religious difference, al-biruni insularity, ibn battuta envoy china, bernier published 1670, rihla arabic |
| T9 | delhi 28 gates, bernier camp towns, al-biruni rejected pollution, barbosa south india trade, tarababad musicians market, kitab-ul-hind al-biruni |
| T10 | battuta left tangier, battuta reached sind 1333, battuta qazi delhi, battuta china envoy 1342, monserrate jesuit akbar, tavernier jeweller, manucci never returned, abdur razzaq calicut, bernier contrasts europe, kitab-ul-hind arabic |
| T11 | bernier translated european languages, bernier contrasts europe, bernier 1656-68, bernier wrote french, al-biruni brahmana head, al-biruni kshatriya shoulders hands, al-biruni vaishya thigh, al-biruni shudra feet, battuta imprisoned restored, barbosa portugal |

### H6 Bhakti–Sufi traditions

| Test | Answer facts |
|---|---|
| T1 | 12 alvars 63 nayanars, karaikkal ammaiyar nayanar, tevaram nayanars, basavanna virashaiva, khanqah hospice, bijak kabirpanth |
| T2 | muinuddin chishti ajmer, nizamuddin auliya delhi, fariduddin ajodhan, salim chishti fatehpur sikri, appar nayanar 7th century, basavanna 12th century, nizamuddin d 1325, guru nanak 1469, mirabai raidas guru, guru nanak nankana sahib |
| T3 | silsila chain, ziyarat pilgrimage, sama music, murid disciple, kabir granthavali dadupanth, jagannatha vishnu puri, shankaradeva assam vaishnavism |
| T4 | nalayira divyaprabandham alvars, tevaram nayanars, adi granth guru arjan, vachanas virashaiva, ulama scholars, zimmi jizya, guru angad successor |
| T5 | basavanna karnataka, shankaradeva assam, mirabai rajasthan, kabir benares, alvars 6th 9th century, muinuddin ajmer 12th century, kabir 14th 15th century, adi granth 1604, lingayats burial, be-sharia qalandars |
| T6 | saguna attributes, nirguna abstract, pir master, wali friend of god, kabir terms many traditions, khalsa 1699 gobind singh |
| T7 | alvars nayanars diverse backgrounds, karaikkal ammaiyar woman devotee, chola support shiva temples, ulatbansi upside-down, namghar shankaradeva, vachanas kannada |
| T8 | basavanna questioned caste rebirth, kabir one reality, guru nanak rejected ritual, mirabai krishna devotion, nalayira compiled 10th century, hujwiri lahore 11th century, shankaradeva 15th century, khalsa 1699 gobind singh, baba farid adi granth, shaikh pir murshid |
| T9 | jamaat khana hall, langar futuh charity, khanqah visitors all walks, ghiyaspur yamuna, chishti assimilated local traditions |
| T10 | bijak granthavali adi granth, kabir many names ultimate reality, ulatbansi, nanak talwandi, mirabai raidas, hujwiri kashf-ul-mahjub, baba farid adi granth, alvars vishnu devotees, zikr remembrance |
| T11 | hujwiri lahore settles, muinuddin ajmer settled, nizamuddin death 1325, akbar salim chishti fatehpur, jahanara ajmer pilgrimage, khusrau qaul qawwali |

### H7 Vijayanagara

| Test | Answer facts |
|---|---|
| T1 | colin mackenzie surveyor, krishnadeva raya amuktamalyada, domingo paes, abdur razzaq vijayanagara visit, rama raya talikota 1565, hampi pampadevi, vijayanagara dynasties |
| T2 | vijayanagara founded 1336, krishnadeva raya accession 1509, talikota 1565, mackenzie hampi 1800, tungabhadra north-east basin, kamalapuram tank, hiriya canal, abdur razzaq seven fortifications, amara-nayaka military commanders, kudirai chettis horse merchants |
| T3 | virupaksha hall krishnadeva raya, gopurams dwarfed shrines, vitthala vishnu, lotus mahal name british, krishnadeva raya tuluva, hazara rama temple royal, orders signed shri virupaksha |
| T4 | nicolo de conti italian, abdur razzaq persia, nikitin russian merchant, nuniz portuguese, raya king, gajapati orissa, vitthala stone chariot |
| T5 | vijayanagara city of victory, hampi pampadevi, karnataka samrajyamu, yavana northwest, aravidu dynasty, talikota sultanates alliance, vijayanagara tungabhadra |
| T6 | sangama saluva tuluva aravidu order, nagalapuram mother, greenlaw photographs 1856, harihara bukka founders |
| T7 | amara-nayakas collected taxes, amara-nayakas tribute court, amara-nayakas independent kingdoms, nicolo de conti 1420, virupaksha hall 1510, greenlaw photographs 1856, hampi world heritage 1986, king's palace largest enclosure, virupaksha form of shiva |
| T8 | walls enclosed fields, paes rome size, kudirai chettis horse merchants, mackenzie virupaksha priests, chariot streets gopurams, krishnadeva raya amuktamalyada |
| T9 | virupaksha sacred centre, hazara rama temple royal, lotus mahal name british, vitthala stone chariot, hindu suratrana, raya gopurams, hampi karnataka |
| T10 | amara-nayakas territories, narapati lord of men, gajapati elephants, ashvapati horses, vijayanagara dynasties, mackenzie surveyor general, hiriya canal tungabhadra |
| T11 | mahanavami september october, mahanavami great ninth day, mahanavami rituals, king inspected armies last day, mahanavami display power suzerainty |

### H8 Mughal empire and agrarian society

| Test | Answer facts |
|---|---|
| T1 | khud-kashta, pahi-kashta, muqaddam headman, jins-i kamil, ain-i akbari abul fazl, jahangir tobacco ban, muqaddam chosen by elders, panchayat expulsion power, panchayat common fund |
| T2 | polaj, chachar banjar fallow years, one-third average produce revenue, ain prices wages agra region, land classification graded revenue |
| T3 | babur panipat 1526, akbar accession 1556, ain-i akbari completed 1598, aurangzeb death 1707, women field work, women crafts spinning, women inheritance rights, bride-price, milkiyat zamindar, jangli forest dwellers |
| T4 | amin official, patwari accountant, jajmani system, raiyat peasant, silver bullion exports, babur irrigation wheel lahore, peshkash elephants |
| T5 | jati panchayat each caste, rajasthan jati panchayats disputes, state respected jati panchayats, kharif rabi seasons, maize africa spain, ain five books |
| T6 | ain-i akbari abul fazl, baburnama memoir, rajasthan gujarat maharashtra revenue records, east india company records eastern india, miras watan artisans, khud-kashta, shikar emperor justice |
| T7 | cotton deccan, sugarcane bengal, maize western india, tobacco deccan first, polaj parauti chachar banjar order, shah nahar punjab, muzarian |
| T8 | peshkash elephants, jangli forest dwellers, milkiyat zamindar, miras watan artisans, zamindars sell bequeath, zamindars forts contingents, zamindars colonised land, women petitions panchayat, abul fazl akbar court |
| T9 | wooden plough iron tip, seed drill oxen, babur irrigation wheel lahore, baburnama memoir, akbar nama 1590s, rajasthan gujarat maharashtra revenue records, east india company records eastern india, little republics village, pahi-kashta |
| T10 | tobacco reached deccan, akbar tobacco 1604, jahangir banned tobacco, tobacco widely consumed seventeenth, jins-i kamil perfect crops, muqaddam headman, patwari accountant, kharif autumn, shikar hunting, babur villages set up quickly |
| T11 | manzil-abadi household, sipah-abadi military, mulk-abadi fiscal, ain fourth fifth books culture, ain five revisions, rani bhabani rajshahi, land revenue economic mainstay |

### H9 Colonialism and rural society

| Test | Answer facts |
|---|---|
| T1 | permanent settlement 1793, sunset law, jotedars rich peasants, fifth report 1813, paharias rajmahal hills, 1793 permanent settlement, 1813 fifth report, santhal revolt 1855-56, deccan riots 1875 |
| T2 | ryotwari bombay deccan, limitation law 1859, lathyal, jotedars rich peasants, cotton boom american civil war 1861, burdwan auction 1797, buchanan physician survey |
| T3 | benami fictitious name, amla rent collector, mahal revenue estate, jhum shifting cultivation, permanent settlement aims, ryotwari 30 years, sahukar moneylender |
| T4 | revenue demand fixed high, prices low 1790s, revenue invariable, bombay deccan settlement 1820s, limitation law 1859, american civil war 1861, deccan riots report 1878, cornwallis permanent settlement, cotton 90 percent 1862 |
| T5 | kist instalment, taluqdar holds taluq, ryot cultivator, bigha land unit, fifth report thousand pages, fifth of series, fifth report read critically, cleveland pacification paharias, permanent settlement zamindars |
| T6 | cornwallis permanent settlement, cleveland pacification paharias, buchanan physician survey, burdwan auction 1797, paharias mahua, hodges watercolours, interest not exceed principal |
| T7 | damin-i-koh 1832, santhals settled agriculture plough, santhal villages 1473, santhal revolt causes, paharias pushed deeper |
| T8 | paharias rajmahal hills, santhals damin-i-koh plough, sahukar moneylender, collector district revenue, santhals arrive 1780s, damin-i-koh 1832, santhal villages 1473, santhal pargana created, paharias hoe, revenue fixed perpetuity |
| T9 | ryotwari settled with ryot, soil survey average income, early demands high ryots deserted, cotton supply association 1857, buchanan 1810-11 journey, ryot cultivator |
| T10 | sunset law, revenue fixed in perpetuity, revenue due despite harvest failure, fifth report 1813, amla rent collector, paharias jhum shifting |
| T11 | bombay deccan ryotwari 1820s, santhal hool 1855, cotton supply association founded 1857, riots commission report 1878, ricardo theory of rent, sidhu manjhi santhal leader, permanent settlement improving landlords |

### H10 The Revolt of 1857

| Test | Answer facts |
|---|---|
| T1 | shah mal barout, gonoo singhbhum, ahmadullah shah faizabad, kunwar singh arrah, subsidiary alliance wellesley 1798, meerut 10 may 1857, dalhousie cherry awadh |
| T2 | cartridges greased rumour, bone dust flour rumour, plassey hundred years prophecy, plassey 1757, awadh subsidiary alliance 1801, awadh annexation 1856, revolt 1857 meerut, bahadur shah zafar rangoon, thomas jones barker relief of lucknow |
| T3 | meerut outbreak may 1857, delhi recaptured september 1857, rani lakshmi bai dies 1858, bahadur shah dies rangoon 1862, martial law 1857, estates returned to landholders, ishtahar proclamation, chapatis distribution |
| T4 | in memoriam noel paton, thomas jones barker relief of lucknow, clemency canning punch, justice punch cartoon, officers sepoys 1820s friendly, 1840s officers superiority, sepoys from awadh villages, mangal pandey barrackpore, sepoys marched delhi |
| T5 | awadh annexed misgovernment, wajid ali shah calcutta, summary settlement 1856, court dependents lost livelihood, awadh grievances linked |
| T6 | rebel administration mughal model, rebels collected revenue, rebel structures could not survive, summary settlement 1856, mangal pandey barrackpore, meerut 10 may 1857, bahadur shah zafar rangoon, felice beato photographs, lakshmi bai jhansi |
| T7 | lakshmi bai adopted son, sepoy panchayats night, bahadur shah leader, firangi foreigners |
| T8 | dalhousie annexed awadh, canning governor-general 1857, colin campbell relief lucknow, subsidiary alliance wellesley 1798, british images saviours, first war of independence, lakshmi bai masculine warrior, danka shah drum, enfield rifle cartridges |
| T9 | cartridges greased rumour, bone dust flour rumour, chapatis distribution, plassey hundred years prophecy, dalhousie annexed awadh, bahadur shah leader, colin campbell relief lucknow, felice beato photographs, nana sahib peshwa baji rao, british called it mutiny |
| T10 | proclamations all communities, proclamations bahadur shah name, azamgarh proclamation, firangi foreigners term, ishtahar notice, danka shah ahmadullah, taluqdars awadh landholders, in memoriam paton, wajid ali shah calcutta exile |
| T11 | britons power try indians, law trial suspended 1857, rebellion only death, no pardon before troops, azamgarh zamindars assessment, azamgarh merchants monopoly, azamgarh public servants posts, azamgarh artisans english goods, taluqdars armies disbanded forts, delhi recaptured september 1857 |

### H11 Mahatma Gandhi and the national movement

| Test | Answer facts |
|---|---|
| T1 | khilafat non-cooperation, chauri chaura 1922 withdrawal, lawyers boycott courts, champaran 1917, rowlatt satyagraha 1919, lahore purna swaraj 1929, gandhi-irwin pact 1931, gandhi return 1915, lahore 1929 nehru president, quit india august 1942 |
| T2 | fortnightly reports home department, hind swaraj 1909, harijan journal, gandhi autobiography, kheda 1918, non-cooperation 1920, salt march 1930, quit india 1942, champaran bihar, second round table 1931, gandhi assassination 30 january 1948 |
| T3 | northern andhra hill tribes forest laws, kumaun refused loads, awadh peasants taxes, students left government schools, satyagraha south africa, charkha dignity of labour, shahid amin gorakhpur rumours |
| T4 | gokhale year travel, pre-gandhi nationalism professionals, gandhi two decades south africa, second round table 1931, government of india act 1935, congress ministries resign 1939, cripps mission 1942, ali brothers khilafat, 1937 congress eight provinces, league 1940 autonomy |
| T5 | chauri chaura police station burnt, kheda revenue remission, noakhali peace mission, ahmedabad mill workers, ahmedabad mill strike 1918, independence day 26 january 1930, quit india 1942, noakhali 1946, harijan children of god, purna swaraj complete independence |
| T6 | swadeshi indian goods, boycott foreign cloth, satyagraha truth force, ahimsa nonviolence, gandhi arrested quit india, quit india strikes sabotage, jp narayan underground, south africa 1893, hind swaraj 1909, gandhi return 1915, bhu speech 1916, gandhi dhoti poor, rowlatt act campaign |
| T7 | gandhi calcutta 15 august 1947, gandhi noakhali bihar, godse assassination, chauri chaura 1922 withdrawal, lahore purna swaraj 1929, gandhi-irwin pact 1931, government of india act 1935, gandhi-irwin salt coast, gokhale mentor |
| T8 | gandhi untouchability programme, gandhi khadi, gandhi village self-reliance, jallianwala bagh amritsar 1919, congress linguistic committees, fortnightly reports home department, gandhi born 1869 |
| T9 | gokhale mentor, jinnah moderate, tilak radical, lahore 1929 nehru president, newspapers gandhi journals, gandhi letters published, police reports bias, swaraj within a year, first rtc 1930 without congress, gandhi lawyer |
| T10 | salt law state monopoly, salt every household grievance, march began sabarmati ashram, officials resign posts march, march world attention press |
| T11 | hind swaraj modern civilisation critique, charkha dignity of labour, gandhi hindu muslim unity, gandhi against industrialisation, chauri chaura police station fire, jallianwala massacre, dandi salt law broken, sabarmati ashram gandhi, kamaladevi women salt protests, do or die quit india, father of the nation |

### H12 The making of the Constitution

| Test | Answer facts |
|---|---|
| T1 | rajendra prasad president ca, ambedkar drafting committee, nehru objectives resolution, s n mukherjee chief draughtsman, ca 11 sessions 165 days, ca elected by provincial legislatures, muslim league boycott, gandhi hindustani national language |
| T2 | three lists union state concurrent, no national language declared, ambedkar strong centre, ca first meeting 9 december 1946, ng ranga minorities poor, bn rau constitutional adviser |
| T3 | pocker bahadur separate electorates, minorities need own voice, patel poison body politic, pant suicidal minorities, separate electorates partition fear |
| T4 | somnath lahiri british influence, dhulekar hindi, durgabai hindi opposition, santhanam states powers, objectives resolution december 1946, independence 15 august 1947, pocker bahadur 27 august 1947, constitution in force 26 january 1950, ca 300 members, patel behind the scenes |
| T5 | km munshi gujarat, alladi madras, hansa mehta women justice, bn rau constitutional adviser, objectives resolution sovereign republic, justice equality freedom, safeguards minorities tribal depressed, ambedkar law minister, universal adult franchise |
| T6 | union list, state list, concurrent list, article 356, hindi devanagari official, provinces choose own language, gradual transition english, longest constitution, rajendra prasad president ca |
| T7 | separate electorates own representatives, joint electorates all voters, reserved seats, universal adult franchise, ambedkar earlier separate electorates, untouchability abolished, reserved seats jobs, nehru american french revolutions, gandhi hindustani national language |
| T8 | ca first meeting 9 december 1946, objectives resolution december 1946, independence 15 august 1947, constitution in force 26 january 1950, congress 82 percent seats, public suggestions assembly, nehru objectives resolution |
| T9 | pocker bahadur separate electorates, pant suicidal minorities, ng ranga minorities poor, ambedkar strong centre, partition strong centre, ca elected by provincial legislatures, ambedkar drafting committee |
| T10 | dhulekar hindi speech, durgabai hindi propaganda, language committee compromise, no national language, government of india act 1935 ca, provincial elections 1945-46, cabinet mission plan 1946, pocker bahadur speech august 1947, somnath lahiri, congress dominated assembly |
| T11 | 1937 provincial ministries, league boycotts assembly 1946, gandhi assassinated before adoption, constitution adopted 26 november 1949, nagappa depressed castes, santhanam states powers, hansa mehta justice women, sn mukherjee chief draughtsman, league reserved muslim seats 1946, customs company taxes centre |
