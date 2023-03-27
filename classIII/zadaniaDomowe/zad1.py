tablica = input("enter numbers separated by ',' (coma): ")
tablica_liczb_stringow = tablica.split(",")
tablica_liczb = [];

for i in range(0, len(tablica_liczb_stringow)):
    tablica_liczb.append(int(tablica_liczb_stringow[i]))




max = tablica_liczb[0]
min = tablica_liczb[0]

for i in range(0, len(tablica_liczb)):
    if(tablica_liczb[i]>max):
        max = tablica_liczb[i]
    if(tablica_liczb[i]<min):
        min = tablica_liczb[i]

print("max: "+ str(max))
print("min: "+str(min))
