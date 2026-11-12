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
| T2 | passage2 tasmat apadana kri, rajan trtiya eka, atman caturthi eka, vac saptami eka, dhanin sasthi bahu, pitr saptami eka, nadi saptami eka, madhu saptami eka, tat sah prathama, tat tena trtiya, tat tasmai caturthi, tat tasmin saptami, matr prathama eka, pathin prathama bahu |
| T3 | passage3 chatrebhyah sampradana, mati sasthi bahu, nadi sasthi bahu, pitr sasthi bahu, idam stri prathama iyam, idam stri dvitiya imam, idam stri trtiya anaya, idam stri caturthi asyai, bhavat sasthi eka, balaka caturthi bahu, svasr dvitiya bahu |
| T4 | passage4 chadebhyah apadana, go trtiya eka gava, sakhi sasthi eka sakhyuh, aksi trtiya eka aksna, pathin trtiya eka patha, rajan dvitiya eka, rajan trtiya eka, rajan caturthi eka, rajan saptami eka, rama trtiya eka, asmad sasthi bahu, vidvas trtiya vidusa not vidvasa |
| T5 | passage5 apatsu saptami bahu, datr trtiya eka, vadhu saptami eka, marut trtiya bahu, dis sasthi bahu, sakhi prathama bahu sakhayah, pitr prathama bahu not dvitiya, sarva prathama bahu, sarva trtiya bahu, sarva sasthi bahu, sarva saptami bahu, phala prathama bahu, kim pum caturthi kasmai |
| T6 | passage6 alasyena hetu trtiya, balaka pancami eka, yusmad sasthi bahu, atman saptami eka, go dvitiya eka, vari caturthi varine |
| T7 | passage7 nagarapalikayah sasthi, vac trtiya eka, bhavat prathama bahu, sisu caturthi eka, kartr dvitiya bahu, kavi trtiya bahu, nadi trtiya bahu, rajan trtiya bahu, tat stri sa, tat stri tam, tat stri taya, tat stri tasyai, nadi prathama bahu, idam pum prathama ayam |
| T8 | passage8 vardhakyat hetu pancami, kavi prathama bahu, pitr pancami eka, yat pum prathama yah, pathin dvitiya eka, aksi trtiya aksna not aksina |
| T9 | passage9 vrstau saptami eka, vari trtiya eka, guru saptami bahu, nrpa dvitiya bahu, matr dvitiya eka, phala saptami not pancami, rajan saptami not pancami, kim stri ka, kim stri kam, kim stri kaya, kim stri kasyai, sisu dvitiya eka, vidvas sasthi bahu |
| T10 | passage10 sudhayai sampradana dana, balaka trtiya bahu, muni trtiya bahu, nadi trtiya bahu, rajan trtiya bahu, asmad sasthi eka mama, pitr dvitiya bahu pitrn, vapi saptami eka, go prathama bahu gavah |
| T11 | passage11 hastabhyam karana trtiya, manas trtiya eka, dhenu sasthi bahu, hari saptami eka, sadhu dvitiya bahu, bhavat pum eka order, lata prathama bahu, yusmad dvitiya eka tvam, madhu sasthi eka madhunah |
| T12 | passage12 svacchatayai tadarthya caturthi, vana saptami bahu, mati saptami bahu, pitr saptami bahu, phala prathama dvi phale, bhavati sasthi eka bhavatyah, atman trtiya eka atmana, sakhi caturthi eka sakhye |
| T13 | passage13 utsavat purva yoge pancami, pituh base pitr, atmanah base atman, vidusah base vidvas, mateh base mati, sadhu eka order, balika dvitiya eka, asmad trtiya eka maya, pathin sasthi eka pathah |
| T14 | passage14 adhyayane adhikarana saptami, balaka caturthi eka, mati caturthi eka second, nadi caturthi eka, guru sasthi eka guroh, tat stri sasthi tasyah, naman prathama eka nama, yusmad pancami eka tvat |

### S2 धातुरूपाणि

| Test | Answer facts |
|---|---|
| T1 | pac lrt praksyati, nam lan anamat, has lot hasatu, nrt vidhilin nrtyet, kr lrt karisyati, jna lrt jnasyati, sak lrt saksyati, kath lat prathama eka, kath lat prathama bahu, kath lat madhyama eka, kath lat uttama bahu, nam lat prathama bahu, labh lan prathama eka, gam lrt madhyama bahu |
| T2 | srnu lot, apnotu lot, prcchantu lot, sev lat prathama eka, sev lat madhyama eka, sev lat uttama eka, sev lat uttama bahu, as lat prathama bahu, jna lat prathama eka, vand lan uttama eka, pracch lan prathama bahu |
| T3 | ni lrt nesyati, pac lan apacat, is vidhilin icchet, nas lot nasyatu, gam lat prathama eka, labh lrt prathama eka, bhaks vidhilin madhyama bahu, apnot lan vrddhi not, yac lan uttama bahu |
| T4 | prcch lan aprcchat not lrt, cint vidhilin not lrt, sru lat prathama eka, sru lat madhyama eka, sru lat uttama eka, sru lat uttama bahu, has lat prathama bahu, vand lrt uttama eka, gam lot madhyama eka, kr vidhilin kuryat |
| T5 | cint lat madhyama dvi, ap lat uttama bahu, is lot prathama bahu, nrt lat uttama eka, nam lat uttama eka, jna lrt prathama bahu, as lan asit, sev lan prathama eka, kr lot karotu not kurutu |
| T6 | sru lan asrnot, is lan aicchat, nrt lan anrtyat, bhaks lan abhaksayat, sak parasmai saknoti, pracch parasmai prcchati, labh lan prathama eka, labh lan prathama bahu, labh lan madhyama eka, labh lan uttama eka, cint lat madhyama bahu, nas vidhilin nasyet, vand lan prathama bahu |
| T7 | sev lrt prathama eka, vand lan prathama eka, labh lat prathama eka, ap vidhilin apnuyat, is lat madhyama eka, pac lot uttama eka, ap lrt madhyama eka, sak vidhilin saknuyat, has lan uttama bahu |
| T8 | nam lrt prathama bahu, cint lan prathama bahu, jna vidhilin janiyat, pracch vidhilin prathama bahu, pac lan apacat, as lan asit, ni lan anayat, yac lat prathama eka, yac lat madhyama eka, yac lat uttama eka, yac lat uttama bahu, gam lan prathama eka, kath lrt prathama eka, sru lot madhyama bahu |
| T9 | ni lot nayatu, sak lot saknotu, is lot icchatu, jna lot janatu, gam lat uttama dvi, cint lrt uttama eka, nrt lan prathama bahu, sev lrt uttama bahu, sak lat prathama bahu saknuvanti |
| T10 | karisyanti lrt, agaccham lan, likhantu lot, bhaveyuh vidhilin, apasyat not lrt, pathet not lrt, vad lan forms order, gam lot madhyama bahu, path lat prathama bahu, vand lrt prathama eka |
| T11 | bhu lot madhyama eka bhava, gam lrt uttama bahu, yacch lan prathama eka, labh vidhilin prathama eka, nayantu lot not lat, kr lat prathama dvi kurutah |
| T12 | path bhvadi, nrt divadi, cint curadi, is tudadi, pathati not atmanepada, gacchanti not atmanepada, kr lat forms order, drs lat pasyati, as lat madhyama dvi sthah, ji lrt jesyati |
| T13 | pathatu lot, gacchantu lot, bhavani lot, likh lat uttama eka, path lan uttama eka apatham, stha lat tisthati, vadenti wrong vidhilin, sru lrt srosyati |
| T14 | da lrt dasyati, drs lrt draksyati, ni lrt nesyati second, stha lrt sthasyati, pathisyati not lan, pathet not lan, bhu lrt forms order, vad lat prathama dvi, pracch lat madhyama eka prcchasi, bhaks lrt bhaksayisyati |

### S3 सन्धयः

| Test | Answer facts |
|---|---|
| T1 | passage1 visarga s to s scutva, sadaiva vrddhi, ityadi yan, vidyalaya dirgha, nayanam ayadi, sat cit scutva |
| T2 | devalaya dirgha, suryodaya guna, pratyekam yan, pavaka ayadi, himalaya dirgha, vak isa jastva, ramo vadat utva purvarupa, mahotsava not visarga guna |
| T3 | passage3 sanmitra anunasika, svagatam yan su, pavana ayadi po, ramesa guna, tat tika stutva, nirdhana rutva |
| T4 | gangodakam guna, atyuttamam yan, ekaikam vrddhi, sajjana scutva, manohara utva, niscala visarga scutva, punaragata rutva, sukti dirgha, sancaya parasavarna, ramas cinoti scutva not |
| T5 | passage5 pratyupakara yan, diggaja jastva, ujjvala scutva, sanmasa anunasika, pustakalaya dirgha, hari ayam rutva, vanausadhi vrddhi |
| T6 | gayaka ayadi gai, laghurmi dirgha, devarsi guna, ajanta jastva, anvesana yan, madhvari yan, pitrajna yan, ravindra dirgha, tapovana utva, sadanana jastva |
| T7 | passage7 itastatah visarga satva, manobala visarga manah, uccarana ut scutva, paramartha dirgha, harim vande anusvara, nayaka ayadi |
| T8 | punarapi rutva, deva atra visarga lopa, sivoham utva purvarupa, duscaritra visarga s, sadananda dirgha, mahaisvarya vrddhi, anvaya yan, tat citram scutva |
| T9 | passage9 tacchrutva scutva, bhavana ayadi, navika ayadi, pavitra ayadi, girisa dirgha, yasoda utva, udgama jastva |
| T10 | paropakara guna, sadaiva vrddhi, svagatam yan, sayanam ayadi, saccit scutva, jagannatha anunasika, himalaya dirgha, pavaka vigraha pa not po |
| T11 | passage11 nyalimpat yan, manoratha visarga, niscaya visarga, namaskara visarga, durbala visarga, digambara jastva, tavaiva vrddhi, sadaiva not yan |
| T12 | yasodhana visarga o, niriksana visarga r, haris candra visarga s, dhanustankara visarga s, sangama parasavarna, maharsi guna sandhi, gurvadesa yan, po anah pavana not ponah |
| T13 | passage13 prajvalayan dirgha, vanausadhi not guna, pratyekam not guna, ramesa guna, saroja utva, sanmukha anunasika |
| T14 | nayanam ayadi vigraha, sukti dirgha vigraha, abhyudaya yan vigraha, vagisa jastva second, vidyalaya dirgha, namaste visarga s, tallina parasavarna, kapisa dirgha not guna |

### S4 समासाः

| Test | Answer facts |
|---|---|
| T1 | ramalaksmanau itaretara dvandva, pitambara bahuvrihi, nilotpala karmadharaya, yathasakti avyayibhava, rajapurusa sasthi tatpurusa, nilakamala not dvigu, kumbhakara upapada, upagangam samipa avyayibhava |
| T2 | passage2 satyavadin upapada, anurupam avyayibhava, pratidinam avyayibhava, nirmaksikam avyayibhava, candrasekhara bahuvrihi, panipadam samahara dvandva, ghanasyama karmadharaya upamana |
| T3 | triloki dvigu, yathavidhi avyayibhava, nilakantha bahuvrihi, pitarau ekasesa, cakrapani bahuvrihi vigraha, mahapurusa karmadharaya, caurabhaya pancami tatpurusa, pankaja not dvigu upapada |
| T4 | passage4 jalasamraksana sasthi, dasanana bahuvrihi, pancapatra dvigu, upakrsnam avyayibhava, krsnarjunau dvandva, pitambara not tatpurusa, yathakramam not tatpurusa, vidyalaya sasthi tatpurusa, krsnasrita dvitiya tatpurusa |
| T5 | sitaramau dvandva, jitendriya bahuvrihi, astadhyayi dvigu, jalada upapada, maharsi karmadharaya not dvandva |
| T6 | passage6 prasannamukha bahuvrihi, prativarsam avyayibhava, caturyuga dvigu, kamalanayana bahuvrihi, matapitarau dvandva, dasamukha not karmadharaya, rajapurusa not karmadharaya, pancavati dvigu, yathamati avyayibhava |
| T7 | nilambaram karmadharaya, sarahata trtiya tatpurusa, saharsam avyayibhava, caturbhuja bahuvrihi, yathasakti not tatpurusa |
| T8 | passage8 sakaphala dvandva, vanagata dvitiya tatpurusa, gunayukta trtiya tatpurusa, yupadaru caturthi tatpurusa, vrksapatita pancami tatpurusa, pratidinam not bahuvrihi, rajaputra not bahuvrihi, gangayamune dvandva, satabdi dvigu |
| T9 | rajapatha not avyayibhava, mahatma not avyayibhava, naranaryau dvandva, triphala dvigu, asvarudha dvitiya tatpurusa, dasanana not dvandva |
| T10 | passage10 jalasuddhiyantra caturthi tatpurusa, lambodara bahuvrihi, mahapurusa karmadharaya, simhabhita pancami tatpurusa, sukhaduhkhe dvandva, rajaputra tatpurusa, gramagata tatpurusa, desabhakti tatpurusa, pratigrham avyayibhava, triloki vigraha samahara |
| T11 | rajapurusa not bahuvrihi, yathasakti not bahuvrihi, maharaja karmadharaya, navaratra dvigu samahara, vidyahina trtiya tatpurusa, anuratham avyayibhava pascat |
| T12 | passage12 mrttikanirmita trtiya tatpurusa, jalaja upapada, pancanana bahuvrihi, devalaya sasthi tatpurusa, yathavidhi avyayibhava second, pitaputrau dvandva, pancatantra dvigu, adhihari avyayibhava saptami |
| T13 | gajanana bahuvrihi vigraha, nilagagana karmadharaya vigraha, anudinam avyayibhava vigraha, hastalikhita trtiya vigraha, ramakrsnau dvandva, trinetra bahuvrihi, nilakamala not bahuvrihi, praptodaka bahuvrihi |
| T14 | passage14 savinayam avyayibhava, nilambaram karmadharaya second, mahakavi karmadharaya, ghanasyama karmadharaya, hariharau dvandva, purusottama saptami tatpurusa, jitakrodha bahuvrihi |

### S5 प्रत्ययाः

| Test | Answer facts |
|---|---|
| T1 | passage1 srutva ktva, gantum tumun, pathitavan ktavatu, karaniyam aniyar, dhanavan matup, laghutvam tva, path satr pathan, balika tap, dharmika thak |
| T2 | passage2 dhavan satr, hasitavyam tavyat, gatih ktin, nartaki nip, buddhiman matup, pranamya lyap, kr trc karta, guni in not matup, sev sanac sevamana |
| T3 | passage3 santi ktin, kartum tumun, drastum tumun, netum tumun, kr kta krta, dandin in, madhurata tal, vadan satr not sanac |
| T4 | passage4 nitam kta, gatavan ktavatu, darsaniyam aniyar, labdhva ktva, neta trc, vidyavan matup, samajika thak, upakrtya lyap, vardh sanac vardhamana |
| T5 | passage5 bhutva ktva, kr tavyat kartavyam, jna ktva jnatva, bala matup balavan, dhana in dhani, buddhiman not stri, gatih ktin not stri, likh ktavatu likhitavan, mahat tva mahattvam, agatya lyap |
| T6 | passage6 siksika tap, datum tumun, srotavya tavyat, cal satr calan, sriman matup, vihasya lyap not ktva |
| T7 | passage7 karaniyah aniyar, sthatum tumun, vartamana sanac, niti ktin, adaya lyap, gantavya krt not taddhita, krtavan krt not taddhita, hasitva ktva, jnani in, netavya tavyat |
| T8 | passage8 raksita kta tap, gatavati ktavatu, krtavan ktavatu, drstavantah ktavatu, pathaniya aniyar, mitrata tal, smrti ktin, aja tap not nip |
| T9 | passage9 utthaya lyap, ganta trc, pitva ktva, srutavan ktavatu, sukhi in, nitva ktva, balatvam tva, yac sanac yacamana, dhavitum tumun not tavyat |
| T10 | passage10 drastum drs tumun, agatya not ktva, nidhaya not ktva, pathaniyam aniyar, sriman matup, kr tavyat kartavyam, gam ktavatu stri gatavati |
| T11 | passage11 muktam muc kta, hasan satr, likhitam kta, datavyam tavyat, vidhaya lyap, khad ktva khaditva, calitum tumun, laghuta tal, gunavati matup nip |
| T12 | passage12 upavisya lyap, sthita kta, neta trc, papi in, manavata tal, pathan satr, gacchanti satr stri, kurvan satr, gatva ktva, kumari nip, path tumun pathitum |
| T13 | passage13 dhrtva dhr ktva, dhanavan taddhita, madhurata taddhita, jnani taddhita, datum tumun second, has satr hasan, vismrtya lyap, sayana si sanac |
| T14 | passage14 avagantum tumun, labdhva labh ktva, prastum pracch tumun, vandaniya aniyar, vidyavan matup, pathitavyam tavyat, da ktavatu stri dattavati, manusyatvam tva, drstavan drs ktavatu |

### S6 उपपदविभक्तिः

| Test | Answer facts |
|---|---|
| T1 | namah caturthi, svasti caturthi, abhitah dvitiya, saha trtiya sitaya, bhi bhayahetu pancami |
| T2 | paritah dvitiya, sakam trtiya, bahih pancami, upari sasthi, nikasa dvitiya, nipuna saptami, dhik dvitiya |
| T3 | rte pancami, samaya dvitiya, sprh caturthi, puratah sasthi, adhah sasthi not saptami, prthak pancami not saptami, svaha caturthi, anga vikara trtiya |
| T4 | ubhayatah dvitiya, prabhrti pancami, krte sasthi, saha trtiya not dvitiya |
| T5 | antarena dvitiya, hina trtiya, druh caturthi, arat pancami, paritah gramam dvitiya, ruc caturthi balakaya, saha trtiya ramena, samaksam sasthi, kusala saptami |
| T6 | bahih pancami, rte pancami, prthak pancami, sarvatah dvitiya, alam caturthi samartha, nirdharana sasthi |
| T7 | ha dvitiya, vasat caturthi, itara pancami, prsthatah sasthi, prati dvitiya, visvas saptami, bhave saptami |
| T8 | upari sasthi not dvitiya, namah caturthi not dvitiya, antara dvitiya, asuy caturthi, jugupsa pancami |
| T9 | samam trtiya, svadha caturthi, adhah sasthi, pravina saptami, vina dvitiya, tra pancami, alam trtiya nisedha |
| T10 | paritah dvitiya sentence, ramaya namah sentence, pitra saha sentence, ubhayatah dvitiya nadi, svaha caturthi agni, dhik dvitiya durjana |
| T11 | abhitah dvitiya, arat pancami, puratah sasthi, kusala saptami, balakaya rocate, gurave namah, mitraya krudhyati, samipe sasthi grha, bahih pancami second |
| T12 | alam vivadena not vivadam, ramena saha not ramam, prabhrti pancami balyat, krte sasthi second, anu dvitiya pascat |
| T13 | nikasa dvitiya second, alam nisedha trtiya second, sprh caturthi second, jugups pancami second, samaya dvitiya second, prthak pancami parivarat, anga vikara trtiya padena |
| T14 | matari vina wrong, gurum namah wrong, prsthatah sasthi second, hina trtiya second, asuy caturthi second |

### S7 भाषिककार्यम्

| Test | Answer facts |
|---|---|
| T1 | passage1 heat cause few trees, passage1 aropayan karta chatrah, unnatah visesana himalaya, uttarasyam visesana disi, vayam nrtyamah agreement, jalam paryaya niram |
| T2 | passage2 five hundred rupees, passage2 adhikam visesya dhanam, ratri divasa vilom, sukha duhkha vilom, unnati vilom avanati, balakau gacchatah agreement |
| T3 | passage3 ramesa no interest reading, passage3 dadati karta sah, surya paryaya divakara, candra paryaya sasi, pavana paryaya vayu, nrpa paryaya raja, pracina vilom arvacina, tvam pathasi agreement, te balikah agreement, avam likhavah agreement |
| T4 | passage4 villagers dug pond, passage4 purna vilom rikta, sundarah visesana, madhuram visesana, uttama vilom adhama, gacchatha karta yuyam |
| T5 | passage5 suresa ill, passage5 abodhayat karta viveka, adana vilom pradana, jaya vilom parajaya, prasna vilom uttara, guna vilom dosa, ramye visesya udyane, avam gamisyavah agreement |
| T6 | passage6 yoga healthy body calm mind, passage6 tena refers rahula, agni paryaya anala, grha paryaya bhavana, vrksa paryaya taru, puspa paryaya kusuma, nara manusya paryaya not vilom, ratri nisa paryaya not vilom, kridanti karta balakah |
| T7 | passage7 streets parks, passage7 nirmalah visesya margah, kamala pankaja paryaya, surya bhaskara paryaya, megha jalada paryaya, komala vilom kathora, yuvam kuruthah agreement |
| T8 | passage8 reads ramayana stories, passage8 ahvayat karta priya, sundari balika, madhurani phalani, visalah vrksah, dhavalena vastrena, arohana vilom avarohana, likhavah karta avam |
| T9 | passage9 mohan asked why so much labour, passage9 aviratam paryaya nirantaram, sitalam jalam, madhurah amrah, visalesu nagaresu, netra paryaya locana, labha vilom hani |
| T10 | passage10 sudha made solar vehicle, passage10 pariksitavan karta sah, utkarsa vilom apakarsa, adana vilom pradana, pracina vilom arvacina, sajjana vilom durjana, vrksa paryaya not vihaga, te balakah kridati wrong agreement |
| T11 | passage11 bird could not fly wing hurt, passage11 svastha vilom rugna, divasa ratri not paryaya, adi anta not paryaya, murkha vilom pandita, bhavan karta prathama purusa gacchati |
| T12 | passage12 went with grandmother, passage12 sahasraih visesya dipaih, candra sasi, pavana vayu, nadi sarit, parvata saila, udaya vilom asta, caturah balika wrong agreement |
| T13 | passage13 diyas lit to welcome rama, passage13 purvam vilom pascat, sa likhanti wrong, aham kridasi wrong, akasa paryaya gagana, kathina vilom sarala |
| T14 | passage14 curiosity root of knowledge, passage14 nisphala vilom saphala, agamana vilom gamana, svatantrata vilom paratantrata, sammana vilom apamana, jnana vilom ajnana, putra paryaya suta, svah apasyan wrong tense |

### S8 छन्दांसि

| Test | Answer facts |
|---|---|
| T1 | anustup 8 varna, vamsastha 12 varna, malini 15 varna, sardula 19 varna, vasantatilaka laksana order, indravajra ta ta ja ga ga, kascit kanta mandakranta identify |
| T2 | indravajra 11 varna, upajati 11 varna, upendravajra 11 varna, sikharini laksana order, malini yati 8 7, ya kundendu sardula identify |
| T3 | mandakranta yati 4 6 7, sikharini yati 6 11, sardula yati 12 7, malini yati 8 7, mandakranta gana order, sarasijam malini identify, vasantatilaka 14 varna |
| T4 | sikharini 17 varna, mandakranta 17 varna, sardula laksana order, upendravajra first ja, sriyah kurunam vamsastha identify |
| T5 | indravajra ta ta ja ga ga, vamsastha ja ta ja ra, malini na na ma ya ya, vasantatilaka ta bha ja ja ga ga, anustup laksana order, sikharini end la ga, yada kincijjno sikharini identify |
| T6 | indravajra first ta, vasantatilaka first ta, vamsastha laksana order, upajati mixture indravajra upendravajra, vidya vivadaya indravajra identify |
| T7 | vasantatilaka 14 varna, vamsastha 12 varna, anustup 8 varna, sardula 19 varna, malini laksana order, vasantatilaka second bha, santakaram mandakranta identify |
| T8 | upendravajra laksana phrase, vamsastha laksana phrase, vasantatilaka laksana phrase, malini laksana phrase, sikharini more than 15, sardula more than 15, mandakranta more than 15, indravajra laksana order, vagarthaviva anustup identify |
| T9 | sikharini not ma bha na, vasantatilaka not ta ja ja bha, upendravajra laksana order, malini six laghu start, ratrir gamisyati vasantatilaka identify |
| T10 | malini first na, mandakranta first ma, sikharini first ya, vamsastha first ja, upajati laksana order, indravajra upendravajra differ first gana, dharmaksetre anustup identify |
| T11 | vamsastha ja ta ja ra second, malini na na ma ya ya second, vasantatilaka ta bha ja ja ga ga second, sardula ma sa ja sa ta ta ga, indravajra 11 varna second, upendravajra 11 varna second, upajati 11 varna second, indravajra laksana order second, tvameva mata upendravajra identify |
| T12 | sikharini ya ma na sa bha la ga, mandakranta ma bha na ta ta ga ga, upendravajra ja ta ja ga ga, upajati mixture second, vasantatilaka laksana order second, malini 15 varna second, astyuttarasyam upajati identify |
| T13 | meghaduta mandakranta, gita anustup, kumarasambhava canto1 upajati, kiratarjuniya canto1 vamsastha, sikharini 17 varna second, mandakranta 17 varna second, sikharini laksana order second, mandakranta yati second |
| T14 | upendravajra first laghu, vamsastha first laghu, malini first laghu, malini laksana order second, anustup sixth guru, prathamavayasi malini identify |

### S9 अलङ्काराः

| Test | Answer facts |
|---|---|
| T1 | yamaka sabdalankara, slesa sabdalankara, anuprasa sabdalankara, utpreksa laksana order, upama laksana fill, udeti savita arthantaranyasa |
| T2 | upama samya, rupaka abhedaropa, utpreksa sambhavana, slesa anekartha, rupaka laksana order, anuprasa laksana svarasya fill, limpativa utpreksa |
| T3 | utpreksa arthalankara, rupaka no iva, yamaka laksana order, mukham candra eva rupaka, navapalasa yamaka |
| T4 | mukham kamalam iva upama, caranakamalam rupaka, giri sprastum iva utpreksa, kalakala anuprasa, arthantaranyasa laksana order, sarvado madhava slesa, slesa laksana fill |
| T5 | upama arthalankara, arthantaranyasa arthalankara, upama laksana order, eko hi doso arthantaranyasa, sita mukham candram iva upama |
| T6 | aravindam iva upama, samsarasagaram rupaka, nrtyanti iva manye utpreksa, santah santapa anuprasa, anuprasa laksana order, raja kalpavrksa rupaka, anuprasa sabdalankara |
| T7 | balaka simha iva upama, tadaga darpana iva upama, yasah hamsa iva upama, slesa laksana order, hanuman abdhim arthantaranyasa, iva vacaka upama |
| T8 | anuprasa varnasamya, yamaka bhinnartha avrtti, arthantaranyasa samarthana, utpreksa sambhavana, upama anga order, vidya dhanam rupaka, manye utpreksa vacaka |
| T9 | kamalam iva komalam upama, vacanamrtam rupaka, payodhara slesa, sarad sasi anuprasa, utpreksa sambhavana statement, rupaka abheda statement, anuprasa varna avrtti statement, utpreksa laksana order, slesa one word many meanings |
| T10 | rupaka laksana order second, limpativa utpreksa second, kamalam iva ramyam sadharana dharma, navapalasa yamaka second |
| T11 | bhavasagara rupaka, mukham manye candrah utpreksa, kalakokila anuprasa, brhatsahayah arthantaranyasa, yamaka not arthalankara, anuprasa not arthalankara, yamaka laksana order second, iva vacaka upama second |
| T12 | simha iva parakrami upama, vani amrtatulya upama, mukham candra iva upama, upama laksana order second, rama vana mahantah arthantaranyasa, amrtam iva madhuram upamana |
| T13 | puspam iva komala upama, hrdayasarovara rupaka, surya api patati arthantaranyasa, carucandra anuprasa, kamalam iva netram not rupaka, manye gaganam not rupaka, slesa laksana order second, manye utpreksa vacaka second |
| T14 | kundam iva upama, nunam candrah utpreksa, harih slesa, madhuramadhukara anuprasa, arthantaranyasa laksana order second, slesa both sabda artha, purnopama four anga |

### S10 साहित्यपरिचयः

| Test | Answer facts |
|---|---|
| T1 | uttararamacarita bhavabhuti, mrcchakatika sudraka, mudraraksasa visakhadatta, svapnavasavadatta bhasa, uttararamacarita not kalidasa, sivarajavijaya not kalidasa, ramayana valmiki, kadambari not drama gadya, brhattrayi naisadhiya |
| T2 | kiratarjuniya bharavi, sisupalavadha magha, naisadhiya sriharsa, buddhacarita asvaghosa, meghaduta not gadya, gitagovinda not gadya, mahabharata vyasa, hitopadesa narayana, ayurveda not veda upaveda |
| T3 | abhijnana kalidasa, kadambari bana, pancatantra visnusarma, rajatarangini kalhana, ramayana kanda order, dhanurveda not vedanga, gitagovinda jayadeva, meghaduta gitikavya |
| T4 | raghuvamsa mahakavya, svapnavasavadatta natakam, dasakumaracarita gadya, nitisataka muktaka, raghuvamsa laghutrayi, kumarasambhava laghutrayi, sivarajavijaya ambikadatta, isa upanisad yajurveda, natyasastra bharata |
| T5 | pratijnayaugandharayana bhasa, urubhanga bhasa, svapnavasavadatta bhasa, mahabharata parva order, kumarasambhava kalidasa, harsacarita bana, sahityadarpana not dandin |
| T6 | kavyadarsa dandin, dhvanyaloka anandavardhana, kavyaprakasa mammata, sahityadarpana visvanatha, pancatantra tantra order, meghaduta kalidasa, nagananda harsa, mahabharata not purana itihasa |
| T7 | hitopadesa nitikatha, gitagovinda gitikavya, mudraraksasa natakam, kadambari gadya, uttararamacarita not kalidasa, mrcchakatika not kalidasa, veda order, ramayana seven kanda, vasavadatta subandhu |
| T8 | dasakumaracarita not bana, vasavadatta not bana, ramayana later kanda order, gita mahabharata, adikavi valmiki, vyakarana vedasya mukham |
| T9 | raghuvamsa subject raghu kings, kumarasambhava subject, kiratarjuniya subject, sisupalavadha subject, vedic literature order, sakuntala heroine, mahabharata 18 parva, kavyaprakasa not katha |
| T10 | uttararamacarita nayaka rama, svapnavasavadatta nayaka udayana, mrcchakatika nayaka carudatta, abhijnana nayaka dusyanta, mudraraksasa not bhavabhuti, venisamhara not bhavabhuti, vedanga order siksa kalpa, purana count 18, ramayana 24000 sloka |
| T11 | kalidasa upama, bharavi arthagaurava, dandin padalalitya, magha all three, mahabharata parva order second, gita part of mahabharata, upanisad vedanta name, meghaduta not mahakavya |
| T12 | naisadhiya not kalidasa, buddhacarita not kalidasa, mahakavya chronology raghu kirata sisupala naisadha, ramayana valmiki second, pancatantra five tantra, kiratarjuniya not gadya |
| T13 | nitisataka bhartrhari, buddhacarita asvaghosa, gitagovinda jayadeva second, rajatarangini kalhana second, raghuvamsa king order, meghaduta kalidasa second, venisamhara bhattanarayana, ayurveda not veda |
| T14 | raghuvamsa 19 sarga, kiratarjuniya 18 sarga, sisupalavadha 20 sarga, naisadhiya 22 sarga, kadambari not nataka second, meghaduta not nataka, pancatantra tantra order second, hitopadesa narayana pandita, raghuvamsa not brhattrayi |
