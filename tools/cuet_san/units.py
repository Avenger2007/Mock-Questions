U={'S1':('शब्दरूपाणि वाक्येषु विभक्तिप्रयोगाः च','Noun and Pronoun Forms, Case Usage',6),
'S2':('धातुरूपाणि','Verb Forms',6),
'S3':('सन्धयः सन्धिविच्छेदाः च','Sandhi',5),
'S4':('समासाः विग्रहाः च','Compounds',5),
'S5':('प्रत्ययाः','Suffixes: Krt, Taddhita and Stri',6),
'S6':('उपपदविभक्तिप्रयोगाः','Upapada Vibhakti',4),
'S7':('भाषिककार्यम्','Language Work: Adjective-Noun, Subject-Verb, Synonyms and Antonyms',5),
'S8':('छन्दांसि','Metres',4),
'S9':('अलङ्काराः','Figures of Speech',4),
'S10':('संस्कृतसाहित्यस्य सामान्यपरिचयः','General Introduction to Sanskrit Literature',5)}
PART={'Grammar':('S1','S2','S3','S4','S5','S6','S7'),'Poetics and Literature':('S8','S9','S10')}
def topic(u): a,b,_=U[u]; return f'{a} ({b})'
