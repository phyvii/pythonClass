
import random
import getpass

print("==========ROCK PAPER SCISSORS==========")

choices = ["p","r","s"]
myChoice = []
botChoice = []
myScore = 0
botScore = 0

while True:
    gameMode = input("GAME MODE: \n (P) 2 PLAYERS: \n (C) COMPUTER: ").upper()
    if(gameMode == "P"):
        rounds = int(input("How many rounds would you like to play?(enter a number): "))
        player1 = input("Enter your name")
        player2 = input("Enter your opponent's name")
        for i in range(0,rounds):
            player = getpass.getpass(player1+" (r) rock, (p) paper, (s) scissors")
            bot = getpass.getpass(player2+" (r) rock, (p) paper, (s) scissors")
            myChoice.append(player)
            botChoice.append(bot)
        for i in range(0,rounds):
            if (myChoice[i] == "p" and botChoice[i] == "r") or (myChoice[i] == "r" and botChoice[i] == "s") or (
                    myChoice[i] == "s" and botChoice[i] == "p"):
                myScore = myScore + 1
            elif(myChoice[i] == "p" and botChoice[i] == "p") or (myChoice[i] == "r" and botChoice[i] == "r") or (
                    myChoice[i] == "s" and botChoice[i] == "s"):
                    myScore+=1
                    botScore+=1
            else:
                botScore+=1

        if myScore>botScore:
            print(player1+" win!")
        elif myScore == botScore:
            print("draw!")
        else:
            print(player2+" wins!")

        myChoice.clear()
        botChoice.clear()
        myScore = 0
        botScore = 0

    elif(gameMode == "C"):
        rounds = int(input("How many rounds would you like to play?(enter a number): "))
        for i in range(0,rounds):
            player = input("(r) rock, (p) paper, (s) scissors")
            bot =choices[random.randint(0,len(choices))-1]
            myChoice.append(player)
            botChoice.append(bot)
        for i in range(0,rounds):
            if (myChoice[i] == "p" and botChoice[i] == "r") or (myChoice[i] == "r" and botChoice[i] == "s") or (
                    myChoice[i] == "s" and botChoice[i] == "p"):
                myScore = myScore + 1
            elif (myChoice[i] == "p" and botChoice[i] == "p") or (myChoice[i] == "r" and botChoice[i] == "r") or (
                    myChoice[i] == "s" and botChoice[i] == "s"):
                myScore += 1
                botScore += 1
            else:
                botScore += 1

        if(myScore>botScore):
            print("you win!")
        elif(myScore == botScore):
            print("draw!")
        else:
            print("bot wins!")
        myChoice.clear()
        botChoice.clear()
        myScore = 0
        botScore = 0

    elif(gameMode=="0"):
        break
    else:
        print("Incorrect choice, try again or enter 0 to leave")



