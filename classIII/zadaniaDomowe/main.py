# This is a sample Python script.
# temperature = float(input("pomiar temperatury: "))
    #print("temperatura zagraza zyciu")
#lese:
    #print("temp: " + str(temperatura))


# # while True:
# #     dane = input("podaje dane (end konczy dzialanie): ")
# #     if dane == "end":
# #         break
# #     print("petla "+dane)
# #
# # i = 0
# #
# # while i <10:
# #     if i ==5:
# #         i+=1
# #         continue
# #     print(i)
# #
# # i=0
# # while i <10:
# #     i+=1
# #     if i -1 == 5:
# #         continue
# #     print(i-1)
# #
# # for i in range(0, 10):
# #     print(i)
#
# # for i in range(0,10):
# #     if i ==5:
# #         continue #bez piÄ…tki, piÄ…tke pomijamy
# #     print(i)
# #
# # for i in range(0,10,2):
# #     print(i)
#
#
moja_lista = ["Warszawa", "KrakĂłw", "WrocĹ‚aw", "ĹĂłdĹş", "PoznaĹ„",
              "GdaĹ„sk", "Szczecin", "Bydgoszcz", "Lublin", "BiaĹ‚ystok"]

# # for element in moja_lista:
# #     element = "brak"
# #
# # print(moja_lista)
#
# for i in range(0,len(moja_lista)):
#     print(moja_lista[i])
#
# moja_lista[i] = "PĹ‚ock"
# print(moja_lista)
#
# moja_lista.append("SuwaĹ‚ki")
# print(moja_lista)
#
# moja_lista.insert(0, "Nowe")
# moja_lista.insert(0, "Nowe")
#
# # print(moja_lista)
# #
# # print(moja_lista[-3])
# #
# # #moja_lista.extend() do jednej listy dodajemy drugÄ…
# # #https://docs.python.org/3/tutorial/datastructures.html
# # moja_lista.extend(["Nowe","Nowe"])
# # print(moja_lista)
# #
# # del moja_lista[0]
# # print(moja_lista)
# #
# # print(moja_lista.pop())#element jest usuwany?
# #
# # index = moja_lista.index("Nowe")
# # print(moja_lista.pop(index))
# #
# miasto = "Nowe"
# # if miasto in moja_lista:
# #     moja_lista.remove(miasto)
# # else:
# #     print("brak elementu")
# #
# # print(moja_lista)
# while miasto in moja_lista:
#     moja_lista.remove(miasto)
#
# print(moja_lista)
#
# print(max(moja_lista))# Ĺ po W !!!
#
# liczby = list(range(0,10))
# print(max(liczby))
# print(min(liczby))
# print(sum(liczby))

import random

print(random.randint(0,1))
#
# index = random.randint(0,len(moja_lista))
# print(moja_lista[index])

import getpass

choice = getpass.getpass("wybĂłr:")
print(choice) #emualte terminal w konfiguracji

miasta_string = "warszawa,lublin,pĹ‚ock"
miasta_from_string = miasta_string.split(",")
print(miasta_from_string)

lista2d = [ [1,2], [1,2]]
print(lista2d)
lista2d.append(["trzecia"])
print(lista2d)