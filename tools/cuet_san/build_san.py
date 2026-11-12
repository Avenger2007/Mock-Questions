# usage: build_san.py N sanNN.json -> CUET/Sanskrit/CUET SANSKRIT TEST N.json
import json,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from units import topic
n=int(sys.argv[1]); src=json.load(open(sys.argv[2],encoding='utf-8'))
meta={"test_id":f"CUET27_SANSKRIT_TEST_{n:02d}","series_id":"CUET27_SANSKRIT","exam":"CUET (UG) 2027","title":f"CUET Sanskrit Test {n}",
 "subject":"Sanskrit (Code: 325)","subject_code":"325","test_number":n,"paper_number":n,"status":"revised",
 "syllabus_source":"CUET SYLLABUS/Sanskrit - 325.pdf (NTA syllabus for CUET (UG) 2026, latest published)",
 "notification_source":"Hermes folder/Information Bulletin.pdf (NTA CUET (UG) 2026)",
 "past_paper_reference":"Pattern benchmark only: NTA CUET (UG) Sanskrit papers 2025 and 2026, analysed for format only (no questions or passages copied)",
 "textbooks":["NCERT Class 11 and 12 Sanskrit (Bhaswati, Shashwati)","NCERT Vyakaranavithi","NCERT Sanskrit Sahitya Parichaya"],
 "duration_minutes":60,"total_questions":50,"questions_to_attempt":50,"marking_scheme":{"correct":"+5","incorrect":"-1","unattempted":"0"},
 "instructions":["सर्वे 50 प्रश्नाः अनिवार्याः। (All 50 questions are compulsory.)",
  "प्रत्येकस्य शुद्धोत्तरस्य कृते 5 अङ्काः, प्रत्येकस्य अशुद्धोत्तरस्य कृते 1 अङ्कः न्यूनीक्रियते, अनुत्तरिते 0 अङ्काः। (+5 / −1 / 0)",
  "पञ्च प्रश्नाः एकम् अपठितम् अनुच्छेदम् आधृत्य सन्ति; ते सहैव तिष्ठन्ति। (One set of 5 questions is based on an unseen passage; the set stays together.)"]}
qs=[]
for i,q in enumerate(src['q'],1):
    o={'id':f'CUET27-SAN-T{n:02d}-Q{i:02d}'}
    if q.get('case'):
        o['case_id']=f'CUET27-SAN-T{n:02d}-P1'
        pas=src['passages'][q['case']]
        q['question']='अधोलिखितम् अनुच्छेदं पठित्वा प्रश्नस्य उत्तरं चिनुत।\n\n'+pas+'\n\nप्रश्नः – '+q['question']
    if q['format'] in ('statements','match-list','sequence') and 'उत्तरं चिनुत' not in q['question'].split('प्रश्नः – ')[-1]: q['question']+='\nअधोलिखितेषु विकल्पेषु उचिततमम् उत्तरं चिनुत –'
    o['topic']=topic(q['topic'])
    for k in ['sub_topic','difficulty','format','question','options','correct_option','explanation']: o[k]=q[k]
    qs.append(o)
assert len(qs)==50, len(qs)
meta['questions']=qs
p=f'CUET/Sanskrit/CUET SANSKRIT TEST {n}.json'
json.dump(meta,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=2);open(p,'a').write('\n');print('wrote',p,len(qs))
