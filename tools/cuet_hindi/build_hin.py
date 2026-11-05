# usage: build_hin.py N hinNN.json -> CUET/Hindi/CUET HINDI TEST N.json
import json,sys
n=int(sys.argv[1]); src=json.load(open(sys.argv[2],encoding='utf-8'))
T={'R1':'Reading Comprehension: Factual Passage','R2':'Reading Comprehension: Narrative Passage','R3':'Reading Comprehension: Literary Passage',
'V1':'Verbal Ability: Rearranging the Parts','V2':'Verbal Ability: Match the Following','V3':'Verbal Ability: Choosing the Correct Word',
'V4':'Verbal Ability: Synonyms, Antonyms and Word Knowledge','V5':'Verbal Ability: Grammar in Use','V6':'Verbal Ability: Poetics and Hindi Literature'}
meta={"test_id":f"CUET27_HINDI_TEST_{n:02d}","series_id":"CUET27_HINDI","exam":"CUET (UG) 2027","title":f"CUET Hindi Test {n}",
 "subject":"Hindi (Code: 102)","subject_code":"102","test_number":n,"paper_number":n,"status":"revised",
 "syllabus_source":"CUET SYLLABUS/Hindi - 102.pdf (NTA syllabus for CUET (UG) 2026, latest published)",
 "notification_source":"Hermes folder/Information Bulletin.pdf (NTA CUET (UG) 2026)",
 "past_paper_reference":"Pattern benchmark only: CUET (UG) 2025 and 2026 Hindi paper formats (no questions or passages copied)",
 "duration_minutes":60,"total_questions":50,"questions_to_attempt":50,"marking_scheme":{"correct":"+5","incorrect":"-1","unattempted":"0"},
 "instructions":["सभी 50 प्रश्न अनिवार्य हैं। (All 50 questions are compulsory.)",
  "प्रत्येक सही उत्तर पर 5 अंक मिलेंगे, प्रत्येक गलत उत्तर पर 1 अंक काटा जाएगा, अनुत्तरित प्रश्न पर 0 अंक। (+5 / −1 / 0)",
  "अंतिम 15 प्रश्न तीन अवतरणों (तथ्यात्मक, कथात्मक, साहित्यिक) पर आधारित हैं; प्रत्येक अवतरण के 5 प्रश्न एक साथ हैं। (The last 15 questions are three passage sets of 5 questions each.)"]}
P={'R1':1,'R2':2,'R3':3}; qs=[]
for i,q in enumerate(src['q'],1):
    o={'id':f'CUET27-HIN-T{n:02d}-Q{i:02d}'}
    if q.get('case'):
        o['case_id']=f'CUET27-HIN-T{n:02d}-P{P[q["case"]]}'
        pas=src['passages'][q['case']]; kind='पद्यांश' if src.get('verse',{}).get(q['case']) else 'गद्यांश'
        q['question']=f'निम्नलिखित {kind} को ध्यानपूर्वक पढ़कर दिए गए प्रश्न का उत्तर दीजिए।\n\n'+pas+'\n\nप्रश्न: '+q['question']
    if q['format'] in ('statements','match-list','sequence') and 'सही उत्तर चुनिए' not in q['question']: q['question']+='\nनीचे दिए गए विकल्पों में से सही उत्तर चुनिए:'
    o['topic']=T[q['topic']]
    for k in ['sub_topic','difficulty','format','question','options','correct_option','explanation']: o[k]=q[k]
    qs.append(o)
assert len(qs)==50, len(qs)
meta['questions']=qs
p=f'CUET/Hindi/CUET HINDI TEST {n}.json'
json.dump(meta,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2);open(p,'a').write('\n');print('wrote',p,len(qs))
