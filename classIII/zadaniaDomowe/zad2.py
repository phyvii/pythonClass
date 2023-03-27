import random

moja_lista = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań",
              "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]

index = random.randint(0, len(moja_lista)-1)

print("Naszym celem wycieczki jest "+str(moja_lista[index]))
