# wuerfeln.py
from random import *
from scanner import *

anz = 1000000
eins = 0
zwei = 0
drei = 0
vier = 0
fünf = 0
sechs = 0
z = 0

print("Wie oft sollte es durchlaufen werden?")
anz = scanner

for i in range (1,anz):
    z = randint(1,6)

    if(z==1):       
        eins+=1
    if(z==2):
        zwei+=1
    if(z==3):
        drei+=1
    if(z==4):
        vier+=1
    if(z==5):
        fünf+=1
    if(z==6):
        sechs+=1

print("Eins: ",eins)
print("Zwei: ",zwei)
print("Drei: ",drei)
print("Drei: ",vier)
print("Fünf: ",fünf)
print("Sechs:",sechs)  