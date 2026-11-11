# Physics (322) units, quotas per 50-question test, and per-test targets
U={'P1':('Electrostatics',7),
'P2':('Current Electricity',6),
'P3':('Magnetic Effects of Current and Magnetism',7),
'P4':('Electromagnetic Induction and Alternating Currents',6),
'P5':('Electromagnetic Waves',3),
'P6':('Optics',9),
'P7':('Dual Nature of Matter and Radiation',4),
'P8':('Atoms and Nuclei',5),
'P9':('Electronic Devices',3)}
N=50
DIFF={'easy':8,'medium':32,'hard':10}
FMT={'match-list':6,'statements':6,'sequence':3}
MIN_NUMERICAL=20
def KEY(n): return dict(zip('ABCD',(13,12,13,12) if n%2 else (12,13,12,13)))
def topic(u): return U[u][0]
