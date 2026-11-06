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

### H2 Early states: inscriptional evidence

| Test | Answer facts |
|---|---|
| T1 | prayaga prashasti harisena, junagadh sudarshana lake, prabhavati gupta land grant, ashokan inscriptions dhamma prakrit, chandragupta maurya c 321 bce, ashoka 3rd c bce, kanishka kushana, samudragupta 4th c ce, megasthenes indica, punch-marked coins silver copper |
| T2 | sreni guild, gahapati head of household, agrahara land to brahmanas, gana sangha oligarchy, magadha rise reasons, rajagaha pataliputra capital, prinsep mint officer, dhamma mahamatta |
| T3 | vajji vaishali, kosala shravasti, avanti ujjayini, gandhara taxila, arthashastra kautilya, five mauryan political centres, kushana first gold coins, iron ploughshare |
| T4 | yaudheya copper coins, gupta gold coins, roman coins south india, kushana first gold coins, mat mathura kushana statues, sixteen mahajanapadas, kharosthi northwest |

### H3 Social histories: the Mahabharata

| Test | Answer facts |
|---|---|
| T1 | eight forms of marriage, kanyadana father's duty, paternal estate divided among sons, endogamy, ghatotkacha bhima hidimba, mahabharata composed over 1000 years |
| T2 | varna duties brahmanas kshatriyas vaishyas shudras, sukthankar critical edition 1919, mlechchha meaning, duryodhana eldest kaurava |
| T3 | ekalavya thumb, drona teacher, hidimba rakshasa bhima, draupadi polyandry, manusmriti 200 bce 200 ce, stridhana, patriliny |
| T4 | exogamy outside unit, polygyny several wives, polyandry several husbands, endogamy, chandalas outside village, chandalas discarded utensils, fa xian clapper, xuanzang outcastes outside city, mahabharata 100000 verses, bhagavad gita krishna arjuna |

### H4 Buddhism and Jainism

| Test | Answer facts |
|---|---|
| T1 | vinaya pitaka rules for sangha, sutta pitaka teachings, abhidhamma pitaka philosophy, therigatha bhikkhunis, tirthankara meaning, amaravati andhra pradesh, bodhisatta mahayana |
| T2 | lumbini birth, bodh gaya enlightenment, sarnath first sermon, kusinagara mahaparinibbana, jaina five vows, makkhali gosala fatalist, vishnu ten avatars |
| T3 | rigveda compiled, buddha teaching, ashoka relics stupas, mahayana develops, mahapajapati gotami first bhikkhuni, anicca anatta dukkha, buddhism conduct over birth, chaitya chita funeral pyre, garbhagriha sanctum |
| T4 | sanchi plaster casts, amaravati dispersed sanchi preserved, hh cole casts, wheel first sermon, shalabhanjika popular beliefs |

### H5 Travellers' accounts

| Test | Answer facts |
|---|---|
| T1 | kitab-ul-hind al-biruni, rihla ibn battuta, travels in the mughal empire bernier, abdur razzaq ambassador herat, al-biruni barriers, ibn battuta muhammad bin tughlaq, al-biruni 11th century, ibn battuta 1333, abdur razzaq 1440s, bernier 1656-68 |
| T2 | al-biruni arabic writer, al-biruni translated sanskrit works, al-biruni caste persia comparison, bernier physician dara shukoh, barbosa south india trade |
| T3 | ibn battuta coconut paan, bernier sati lahore, al-biruni sanskrit caste texts, tavernier jeweller six visits, slaves sold in markets, female slaves spies, ibn battuta bought slaves gifts, kitab-ul-hind 80 chapters, ibn battuta tangier morocco |
| T4 | delhi vast city wall, daulatabad size, indian textiles demand, marco polo 13th century, nikitin 15th century, barbosa 16th century, manucci 17th century, al-biruni languages syriac persian hebrew sanskrit, karkhanas workshops |

### H6 Bhakti–Sufi traditions

| Test | Answer facts |
|---|---|
| T1 | 12 alvars 63 nayanars, karaikkal ammaiyar nayanar, tevaram nayanars, basavanna virashaiva, khanqah hospice, bijak kabirpanth |
| T2 | muinuddin chishti ajmer, nizamuddin auliya delhi, fariduddin ajodhan, salim chishti fatehpur sikri, appar nayanar 7th century, basavanna 12th century, nizamuddin d 1325, guru nanak 1469, mirabai raidas guru, guru nanak nankana sahib |
| T3 | silsila chain, ziyarat pilgrimage, sama music, murid disciple, kabir granthavali dadupanth, jagannatha vishnu puri, shankaradeva assam vaishnavism |
| T4 | nalayira divyaprabandham alvars, tevaram nayanars, adi granth guru arjan, vachanas virashaiva, ulama scholars, zimmi jizya, guru angad successor |

### H7 Vijayanagara

| Test | Answer facts |
|---|---|
| T1 | colin mackenzie surveyor, krishnadeva raya amuktamalyada, domingo paes, abdur razzaq vijayanagara visit, rama raya talikota 1565, hampi pampadevi, vijayanagara dynasties |
| T2 | vijayanagara founded 1336, krishnadeva raya accession 1509, talikota 1565, mackenzie hampi 1800, tungabhadra north-east basin, kamalapuram tank, hiriya canal, abdur razzaq seven fortifications, amara-nayaka military commanders, kudirai chettis horse merchants |
| T3 | virupaksha hall krishnadeva raya, gopurams dwarfed shrines, vitthala vishnu, lotus mahal name british, krishnadeva raya tuluva, hazara rama temple royal, orders signed shri virupaksha |
| T4 | nicolo de conti italian, abdur razzaq persia, nikitin russian merchant, nuniz portuguese, raya king, gajapati orissa, vitthala stone chariot |

### H8 Mughal empire and agrarian society

| Test | Answer facts |
|---|---|
| T1 | khud-kashta, pahi-kashta, muqaddam headman, jins-i kamil, ain-i akbari abul fazl, jahangir tobacco ban, muqaddam chosen by elders, panchayat expulsion power, panchayat common fund |
| T2 | polaj, chachar banjar fallow years, one-third average produce revenue, ain prices wages agra region, land classification graded revenue |
| T3 | babur panipat 1526, akbar accession 1556, ain-i akbari completed 1598, aurangzeb death 1707, women field work, women crafts spinning, women inheritance rights, bride-price, milkiyat zamindar, jangli forest dwellers |
| T4 | amin official, patwari accountant, jajmani system, raiyat peasant, silver bullion exports, babur irrigation wheel lahore, peshkash elephants |

### H9 Colonialism and rural society

| Test | Answer facts |
|---|---|
| T1 | permanent settlement 1793, sunset law, jotedars rich peasants, fifth report 1813, paharias rajmahal hills, 1793 permanent settlement, 1813 fifth report, santhal revolt 1855-56, deccan riots 1875 |
| T2 | ryotwari bombay deccan, limitation law 1859, lathyal, jotedars rich peasants, cotton boom american civil war 1861, burdwan auction 1797, buchanan physician survey |
| T3 | benami fictitious name, amla rent collector, mahal revenue estate, jhum shifting cultivation, permanent settlement aims, ryotwari 30 years, sahukar moneylender |
| T4 | revenue demand fixed high, prices low 1790s, revenue invariable, bombay deccan settlement 1820s, limitation law 1859, american civil war 1861, deccan riots report 1878, cornwallis permanent settlement, cotton 90 percent 1862 |

### H10 The Revolt of 1857

| Test | Answer facts |
|---|---|
| T1 | shah mal barout, gonoo singhbhum, ahmadullah shah faizabad, kunwar singh arrah, subsidiary alliance wellesley 1798, meerut 10 may 1857, dalhousie cherry awadh |
| T2 | cartridges greased rumour, bone dust flour rumour, plassey hundred years prophecy, plassey 1757, awadh subsidiary alliance 1801, awadh annexation 1856, revolt 1857 meerut, bahadur shah zafar rangoon, thomas jones barker relief of lucknow |
| T3 | meerut outbreak may 1857, delhi recaptured september 1857, rani lakshmi bai dies 1858, bahadur shah dies rangoon 1862, martial law 1857, estates returned to landholders, ishtahar proclamation, chapatis distribution |
| T4 | in memoriam noel paton, thomas jones barker relief of lucknow, clemency canning punch, justice punch cartoon, officers sepoys 1820s friendly, 1840s officers superiority, sepoys from awadh villages, mangal pandey barrackpore, sepoys marched delhi |

### H11 Mahatma Gandhi and the national movement

| Test | Answer facts |
|---|---|
| T1 | khilafat non-cooperation, chauri chaura 1922 withdrawal, lawyers boycott courts, champaran 1917, rowlatt satyagraha 1919, lahore purna swaraj 1929, gandhi-irwin pact 1931, gandhi return 1915, lahore 1929 nehru president, quit india august 1942 |
| T2 | fortnightly reports home department, hind swaraj 1909, harijan journal, gandhi autobiography, kheda 1918, non-cooperation 1920, salt march 1930, quit india 1942, champaran bihar, second round table 1931, gandhi assassination 30 january 1948 |
| T3 | northern andhra hill tribes forest laws, kumaun refused loads, awadh peasants taxes, students left government schools, satyagraha south africa, charkha dignity of labour, shahid amin gorakhpur rumours |
| T4 | gokhale year travel, pre-gandhi nationalism professionals, gandhi two decades south africa, second round table 1931, government of india act 1935, congress ministries resign 1939, cripps mission 1942, ali brothers khilafat, 1937 congress eight provinces, league 1940 autonomy |

### H12 The making of the Constitution

| Test | Answer facts |
|---|---|
| T1 | rajendra prasad president ca, ambedkar drafting committee, nehru objectives resolution, s n mukherjee chief draughtsman, ca 11 sessions 165 days, ca elected by provincial legislatures, muslim league boycott, gandhi hindustani national language |
| T2 | three lists union state concurrent, no national language declared, ambedkar strong centre, ca first meeting 9 december 1946, ng ranga minorities poor, bn rau constitutional adviser |
| T3 | pocker bahadur separate electorates, minorities need own voice, patel poison body politic, pant suicidal minorities, separate electorates partition fear |
| T4 | somnath lahiri british influence, dhulekar hindi, durgabai hindi opposition, santhanam states powers, objectives resolution december 1946, independence 15 august 1947, pocker bahadur 27 august 1947, constitution in force 26 january 1950, ca 300 members, patel behind the scenes |
