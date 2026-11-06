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

### H2 Early states: inscriptional evidence

| Test | Answer facts |
|---|---|
| T1 | prayaga prashasti harisena, junagadh sudarshana lake, prabhavati gupta land grant, ashokan inscriptions dhamma prakrit, chandragupta maurya c 321 bce, ashoka 3rd c bce, kanishka kushana, samudragupta 4th c ce, megasthenes indica, punch-marked coins silver copper |

### H3 Social histories: the Mahabharata

| Test | Answer facts |
|---|---|
| T1 | eight forms of marriage, kanyadana father's duty, paternal estate divided among sons, endogamy, ghatotkacha bhima hidimba, mahabharata composed over 1000 years |

### H4 Buddhism and Jainism

| Test | Answer facts |
|---|---|
| T1 | vinaya pitaka rules for sangha, sutta pitaka teachings, abhidhamma pitaka philosophy, therigatha bhikkhunis, tirthankara meaning, amaravati andhra pradesh, bodhisatta mahayana |

### H5 Travellers' accounts

| Test | Answer facts |
|---|---|
| T1 | kitab-ul-hind al-biruni, rihla ibn battuta, travels in the mughal empire bernier, abdur razzaq ambassador herat, al-biruni barriers, ibn battuta muhammad bin tughlaq, al-biruni 11th century, ibn battuta 1333, abdur razzaq 1440s, bernier 1656-68 |

### H6 Bhakti–Sufi traditions

| Test | Answer facts |
|---|---|
| T1 | 12 alvars 63 nayanars, karaikkal ammaiyar nayanar, tevaram nayanars, basavanna virashaiva, khanqah hospice, bijak kabirpanth |

### H7 Vijayanagara

| Test | Answer facts |
|---|---|
| T1 | colin mackenzie surveyor, krishnadeva raya amuktamalyada, domingo paes, abdur razzaq vijayanagara visit, rama raya talikota 1565, hampi pampadevi, vijayanagara dynasties |

### H8 Mughal empire and agrarian society

| Test | Answer facts |
|---|---|
| T1 | khud-kashta, pahi-kashta, muqaddam headman, jins-i kamil, ain-i akbari abul fazl, jahangir tobacco ban, muqaddam chosen by elders, panchayat expulsion power, panchayat common fund |

### H9 Colonialism and rural society

| Test | Answer facts |
|---|---|
| T1 | permanent settlement 1793, sunset law, jotedars rich peasants, fifth report 1813, paharias rajmahal hills, 1793 permanent settlement, 1813 fifth report, santhal revolt 1855-56, deccan riots 1875 |

### H10 The Revolt of 1857

| Test | Answer facts |
|---|---|
| T1 | shah mal barout, gonoo singhbhum, ahmadullah shah faizabad, kunwar singh arrah, subsidiary alliance wellesley 1798, meerut 10 may 1857, dalhousie cherry awadh |

### H11 Mahatma Gandhi and the national movement

| Test | Answer facts |
|---|---|
| T1 | khilafat non-cooperation, chauri chaura 1922 withdrawal, lawyers boycott courts, champaran 1917, rowlatt satyagraha 1919, lahore purna swaraj 1929, gandhi-irwin pact 1931, gandhi return 1915, lahore 1929 nehru president, quit india august 1942 |

### H12 The making of the Constitution

| Test | Answer facts |
|---|---|
| T1 | rajendra prasad president ca, ambedkar drafting committee, nehru objectives resolution, s n mukherjee chief draughtsman, ca 11 sessions 165 days, ca elected by provincial legislatures, muslim league boycott, gandhi hindustani national language |
