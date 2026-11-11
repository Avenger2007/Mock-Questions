U={'I1':('Politics in India since Independence','Era of One-Party Dominance',3),
'I2':('Politics in India since Independence','Nation-Building and Its Problems',3),
'I3':('Politics in India since Independence','Politics of Planned Development',2),
'I4':('Politics in India since Independence',"India's External Relations",3),
'I5':('Politics in India since Independence','Challenge to and Restoration of Congress System',3),
'I6':('Politics in India since Independence','Crises of the Constitutional Order',3),
'I7':('Politics in India since Independence','Regional Aspirations and Conflicts',3),
'I8':('Politics in India since Independence','Democratic Upsurge and Coalition Politics',3),
'I9':('Politics in India since Independence','Recent Issues and Challenges',2),
'W1':('Contemporary World Politics',"Disintegration of the 'Second World' and the Collapse of Bipolarity",4),
'W2':('Contemporary World Politics','Alternative Centres of Economic and Political Power',4),
'W3':('Contemporary World Politics','South Asia in the Post-Cold War Era',4),
'W4':('Contemporary World Politics','International Organisations in a Unipolar World',4),
'W5':('Contemporary World Politics','Security in the Contemporary World',3),
'W6':('Contemporary World Politics','Environment and Natural Resources in Global Politics',3),
'W7':('Contemporary World Politics','Globalisation and Its Critics',3)}
PART={'India':tuple(f'I{i}' for i in range(1,10)),'World':tuple(f'W{i}' for i in range(1,8))}
def topic(u): b,c,_=U[u]; return f'{b}: {c}'
