import sys

a = 1000
b = 1000

b = a
print(id(a), id(b))

b =2000
type(b)

#10

bool(1)

float("345")
float("345.60")
#przybliżanie do najbliższej liczbt parzystej
import math
a,b,c,d,e = 1.5,2.5,3.5,4.5,5.5
print(a+b+c+d+e)
print(round(a)+round(b)+round(c)+round(d)+round(e))
print(int(a)+int(b)+int(c)+int(d)+int(e))
print(math.ceil(a)+math.ceil(b)+math.ceil(c)+math.ceil(d)+math.ceil(e))
#math.ceil -celling zaokrągla w góre
#math.floor - zaokrągla w dół

a = 20
#blok kodu
#zwykle oddalony 4 spacjami a nie tabem
if a > 21:
    print("a wieksze od 21")
else:
    print("czy a mnijeszcze od 21?")

a = 21

if a > 21:
    print("a wieksze od 21")
else:
    print("a rowne 21")

a = "tekst string"
print(sys.getrefcount(a))

c=5252332
print(sys.getrefcount(c))
