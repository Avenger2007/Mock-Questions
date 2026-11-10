U={'C1':('A','Algebra: Matrices, Determinants, Inverse and the Matrix Method',4),
'C2':('A','Calculus: Derivatives, Increasing/Decreasing Functions, Maxima and Minima',3),
'C3':('A','Integration and its Applications',3),
'C4':('A','Differential Equations',2),
'C5':('A','Probability Distributions',2),
'C6':('A','Linear Programming',1),
'M1':('B1','Unit I: Relations and Functions',3),
'M2':('B1','Unit I: Inverse Trigonometric Functions',2),
'M3':('B1','Unit II: Matrices',2),
'M4':('B1','Unit II: Determinants',3),
'M5':('B1','Unit III: Continuity and Differentiability',4),
'M6':('B1','Unit III: Applications of Derivatives',3),
'M7':('B1','Unit III: Integrals',4),
'M8':('B1','Unit III: Applications of the Integrals',1),
'M9':('B1','Unit III: Differential Equations',3),
'M10':('B1','Unit IV: Vectors',3),
'M11':('B1','Unit IV: Three-dimensional Geometry',3),
'M12':('B1','Unit V: Linear Programming',1),
'M13':('B1','Unit VI: Probability',3),
'AM1':('B2','Unit I: Numbers, Quantification and Numerical Applications',6),
'AM2':('B2','Unit II: Algebra',4),
'AM3':('B2','Unit III: Calculus',8),
'AM4':('B2','Unit IV: Probability Distributions',5),
'AM5':('B2','Unit V: Time-based Data',3),
'AM6':('B2','Unit VI: Inferential Statistics',3),
'AM7':('B2','Unit VII: Financial Mathematics',4),
'AM8':('B2','Unit VIII: Linear Programming',2)}
SEC={'A':15,'B1':35,'B2':35}
DIFF={'A':{'easy':2,'medium':10,'hard':3},'B1':{'easy':6,'medium':22,'hard':7},'B2':{'easy':6,'medium':22,'hard':7}}
FMT={'A':{'match-list':1,'statements':2},'B1':{'match-list':3,'statements':4},'B2':{'match-list':3,'statements':4}}
def KEY(n,sec):
    odd=n%2==1
    if sec=='A': return dict(zip('ABCD',(4,4,4,3) if odd else (3,4,4,4)))
    return dict(zip('ABCD',(9,8,9,9) if odd else (9,9,8,9)))
def topic(u): return U[u][1]
def section(u): return U[u][0]
