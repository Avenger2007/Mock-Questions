# Coverage map — CUET Sanskrit, Tests 1–15

This map was written **before** any test, so that repeats are prevented rather than fixed later.

**Rules:**
- Every passage theme in §A is used **once** in the series.
- Each **answer fact** is a short Latin key, for example `pitr sasthi eka`, `gam lrt prathama bahu`, `mandakranta 17 varna` or `kalidasa raghuvamsa`.
  - An answer fact is the form, rule or fact a question turns on. Each correct pair in a match item and each position in an order item is its own fact.
  - A key may be used **at most twice in the series**, in different tests.
  - Before a test ships, its keys are checked against the ledgers in §C (`san_check.py`, flag `REPEAT-TARGET`) and then added to them (`mark_san.py`).
  - Distractors may repeat.
- **Closed sets:** the closed sets (the ten metres, the seven alaṅkāras, the listed sandhis, samāsas and प्रत्ययs) recur in every test, each time with a different fact or example.

## A. Unseen passage per test (original prose)

| Test | Theme | 5th question |
|---|---|---|
| 1 | ग्रामे वृक्षारोपणम् | S3 सन्धिः |
| 2 | सत्यवादी फलविक्रेता बालकः | S4 समासः |
| 3 | पुस्तकालयस्य महत्त्वम् | S3 |
| 4 | जलसंरक्षणम् | S4 |
| 5 | मित्रयोः साहाय्यम् | S3 |
| 6 | योगाभ्यासः | S4 |
| 7 | स्वच्छता-अभियानम् | S3 |
| 8 | वृद्धायाः सेवा | S4 |
| 9 | कृषकस्य परिश्रमः | S3 |
| 10 | विद्यालये विज्ञानप्रदर्शनी | S4 |
| 11 | आहतस्य खगस्य रक्षा | S3 |
| 12 | नदीतीरे मेला | S4 |
| 13 | दीपोत्सवः | S3 |
| 14 | गुरुशिष्यसंवादः – जिज्ञासा | S4 |
| 15 | सङ्गणकस्य सदुपयोगः | S3 |

## B. Slot rotation (what each unit draws on)

- **S1:**
  - अजन्त: बालक, फल, रमा, कवि, मति, वारि, नदी, शिशु, धेनु, मधु, पितृ, मातृ, कर्तृ, सखि, दातृ, नृ, स्वसृ, अक्षि, गो, वधू.
  - हलन्त: राजन्, भवत्, आत्मन्, विद्वस्, वाच्, पथिन्, मरुत्, तादृश्, दिश्, धनिन्, पञ्चन्, अष्टन्, नवन्, दशन्.
  - सर्वनाम: सर्व, तत्, यत्, किम्, इदम् (three genders), अस्मद्, युष्मद्.
  - Each test uses one form from at least 5 different words, at least one हलन्त and one सर्वनाम, plus one vibhakti-in-sentence item.
- **S2:**
  - परस्मैपदी roots: गम्, नम्, अस्, हस्, श्रु, नश्, आप्, शक्, इष्, प्रच्छ्, कृ, ज्ञा, भक्ष्, चिन्त्, नृत्, कथ्, नी, पच्, in five lakāras.
  - आत्मनेपदी roots: लभ्, सेव्, वन्द्, याच्, in three lakāras.
  - Each test covers at least four lakāras and at least one आत्मनेपदी root.
- **S3:**
  - स्वर: दीर्घ, गुण, वृद्धि, यण्, अयादि, पूर्वरूप.
  - व्यञ्जन: श्चुत्व, ष्टुत्व, जश्त्व, अनुनासिक, अनुस्वार, परसवर्ण.
  - विसर्ग: उत्व, रत्व, लोप, स् / श् / ष्.
  - Each test mixes all three groups, through सन्धि, विच्छेद and naming the sandhi.
- **S4:** अव्ययीभाव (यथा, प्रति, उप, अनु, निर्, सह, अधि); द्वन्द्व (इतरेतर, समाहार, एकशेष); तत्पुरुष (विभक्ति, कर्मधारय, द्विगु, उपपद); बहुव्रीहि. Each test asks for both a विग्रह and a samāsa name.
- **S5:** कृत् (क्त, क्तवतु, तव्यत्, अनीयर्, शतृ, शानच्, क्तिन्, क्त्वा, ल्यप्, तुमुन्, तृच्); तद्धित (मतुप्, इन्, ठक्, ठञ्, त्व, तल्); स्त्री (टाप्, ङीप्). Each test asks for both a प्रकृति-प्रत्यय split and the joining of a word with a प्रत्यय.
- **S6:**
  - द्वितीया: अभितः, परितः, उभयतः, सर्वतः, धिक्, समया, निकषा, हा, प्रति, अन्तरा, अन्तरेण, विना.
  - तृतीया: सह, साकम्, सार्धम्, समम्, विना, अलम्, हीन, अङ्ग-विकार, प्रकृत्यादि.
  - चतुर्थी: नमः, स्वस्ति, स्वाहा, स्वधा, अलम्, वषट्, रुच्, क्रुध्, द्रुह्, ईर्ष्य्, असूय्, दा, स्पृह्.
  - पञ्चमी: बहिः, ऋते, आरात्, प्रभृति, विना, भी / त्रा, जुगुप्सा, अन्य, इतर, पृथक्, दूर, अन्तिक, अपादान.
  - षष्ठी: उपरि, अधः, पुरतः, पृष्ठतः, कृते, समक्षम्, तुल्य, निर्धारण.
  - सप्तमी: स्निह्, विश्वस्, निपुण, कुशल, प्रवीण, भावे सप्तमी, निर्धारण.
- **S7:** विशेषण–विशेष्य agreement, कर्तृ–क्रिया agreement (puruṣa, vacana), पर्याय and विलोम, picked from a sentence.
- **S8:** the ten metres. Each test asks one lakṣaṇa or gaṇa item, one syllable-count or yati item, and one or two items identifying the metre of a quoted line.
- **S9:** the seven alaṅkāras. Each test asks one lakṣaṇa item and two or three items identifying the alaṅkāra in an example line.
- **S10:** the Vedas, Upaniṣads, Vedāṅgas; the epics (Rāmāyaṇa, Mahābhārata, Gītā); the Purāṇas; the mahākāvyas and the Bṛhattrayī and Laghutrayī; the plays (Bhāsa, Kālidāsa, Śūdraka, Viśākhadatta, Bhavabhūti, Harṣa); prose (Daṇḍin, Subandhu, Bāṇa, Ambikādatta Vyāsa); fables (Pañcatantra, Hitopadeśa); gītikāvya (Meghadūta, Gītagovinda, the śatakas of Bhartṛhari); history (Rājataraṅgiṇī); the poetics authors.

## C. Answer-fact ledgers (filled by `mark_san.py`)

### S1 शब्दरूपाणि

| Test | Answer facts |
|---|---|
| T1 | passage1 nadyah sasthi context, pitr trtiya eka, mati caturthi eka, vadhu dvitiya eka, dhenu saptami eka, yusmad tvam prathama, yusmad tvaya trtiya, yusmad tubhyam caturthi, yusmad tava sasthi, kavi sasthi bahu, sakhi trtiya sakhya not sakhina, vidvas prathama bahu |

### S2 धातुरूपाणि

| Test | Answer facts |
|---|---|
| T1 | pac lrt praksyati, nam lan anamat, has lot hasatu, nrt vidhilin nrtyet, kr lrt karisyati, jna lrt jnasyati, sak lrt saksyati, kath lat prathama eka, kath lat prathama bahu, kath lat madhyama eka, kath lat uttama bahu, nam lat prathama bahu, labh lan prathama eka, gam lrt madhyama bahu |

### S3 सन्धयः

| Test | Answer facts |
|---|---|
| T1 | passage1 visarga s to s scutva, sadaiva vrddhi, ityadi yan, vidyalaya dirgha, nayanam ayadi, sat cit scutva |

### S4 समासाः

| Test | Answer facts |
|---|---|
| T1 | ramalaksmanau itaretara dvandva, pitambara bahuvrihi, nilotpala karmadharaya, yathasakti avyayibhava, rajapurusa sasthi tatpurusa, nilakamala not dvigu, kumbhakara upapada, upagangam samipa avyayibhava |

### S5 प्रत्ययाः

| Test | Answer facts |
|---|---|
| T1 | passage1 srutva ktva, gantum tumun, pathitavan ktavatu, karaniyam aniyar, dhanavan matup, laghutvam tva, path satr pathan, balika tap, dharmika thak |

### S6 उपपदविभक्तिः

| Test | Answer facts |
|---|---|
| T1 | namah caturthi, svasti caturthi, abhitah dvitiya, saha trtiya sitaya, bhi bhayahetu pancami |

### S7 भाषिककार्यम्

| Test | Answer facts |
|---|---|
| T1 | passage1 heat cause few trees, passage1 aropayan karta chatrah, unnatah visesana himalaya, uttarasyam visesana disi, vayam nrtyamah agreement, jalam paryaya niram |

### S8 छन्दांसि

| Test | Answer facts |
|---|---|
| T1 | anustup 8 varna, vamsastha 12 varna, malini 15 varna, sardula 19 varna, vasantatilaka laksana order, indravajra ta ta ja ga ga, kascit kanta mandakranta identify |

### S9 अलङ्काराः

| Test | Answer facts |
|---|---|
| T1 | yamaka sabdalankara, slesa sabdalankara, anuprasa sabdalankara, utpreksa laksana order, upama laksana fill, udeti savita arthantaranyasa |

### S10 साहित्यपरिचयः

| Test | Answer facts |
|---|---|
| T1 | uttararamacarita bhavabhuti, mrcchakatika sudraka, mudraraksasa visakhadatta, svapnavasavadatta bhasa, uttararamacarita not kalidasa, sivarajavijaya not kalidasa, ramayana valmiki, kadambari not drama gadya, brhattrayi naisadhiya |
