imie = input("Imie: ")
nazwisko = input("Nazwisko:" )





questions = ("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:",
             "W jakich okolicznościach czytasz książki najczęściej?",
             "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
             "Po książki w jakiej formie sięgasz najczęściej?",
             "Ile książek czytasz średnio w ciągu roku?",
             "Jak często średnio czytasz książki?",
             "Po jakie gatunki książek sięgasz najczęściej?")
answers = (
    ("A.oglądanie telewizji/filmów/seriali",
    "B.czytanie książek/czasopism",
    "C.słuchanie muzyki"),
    ("A.podczas podróży",
    "B.w czasie wolnym (po pracy, na urlopie)",
    "C.podczas pracy/nauki (to ich element) "),
    ("A.chęć poszerzenia wiedzy",
    "B.czytanie mnie relaksuje/odpręża",
    "C.fakt, że czytanie jest modne "),
    ("A.papierowej (tradycyjnej)",
    "B.e-booki (książki elektroniczne) na komputerze",
    "C.e-booki na tablecie/telefonie "),
    ("A.0",
	"B.żadnej w całości - jedynie fragmenty",
	"C.1" ),
    ("A.codziennie",
	"B.raz w tygodniu",
	"C.raz w miesiącu "),
    ("A.kryminały/thrillery",
	"B.romanse",
	"C.psychologiczne ")
    )
options = ("A","B","C")
questionNumber = 0
userAnswers = []
for i in questions:
    print("============================")
    print(i)
    print("----------------------------")
    for j in answers[questionNumber]:
        print(j)

    userInput = input("Wybierz A, B, albo C: ").upper()
    userAnswers.append(userInput);
    questionNumber = questionNumber +1

for answers in userAnswers:
    print(answers+" ", end = "")