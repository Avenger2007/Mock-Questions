U={'H1':('Themes in Indian History Part I','Harappan Civilisation and Archaeology',5),
'H2':('Themes in Indian History Part I','Political and Economic Systems in Early States: Inscriptional Evidences',4),
'H3':('Themes in Indian History Part I','Social Histories of Early Societies: Mahabharata',4),
'H4':('Themes in Indian History Part I','History of Buddhism and Jainism: Cultural Developments',4),
'H5':('Themes in Indian History Part II','Medieval Society through Travellers Accounts',4),
'H6':('Themes in Indian History Part II','Religious History: Bhakti-Sufi Traditions',4),
'H7':('Themes in Indian History Part II','Vijayanagara Empire: Politics, Economy and Architecture',4),
'H8':('Themes in Indian History Part II','The Mughal Empire and Agrarian Society',4),
'H9':('Themes in Indian History Part III','Colonialism and Rural Society: Evidence from Official Reports',4),
'H10':('Themes in Indian History Part III','Revolt of 1857: Patterns and Representations',4),
'H11':('Themes in Indian History Part III','Mahatma Gandhi and National Movements',5),
'H12':('Themes in Indian History Part III','The Making of the Constitution',4)}
PART={'I':('H1','H2','H3','H4'),'II':('H5','H6','H7','H8'),'III':('H9','H10','H11','H12')}
def topic(u): b,c,_=U[u]; return f'{b}: {c}'
