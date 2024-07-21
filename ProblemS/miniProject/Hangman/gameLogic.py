import random
import Pyart


def start():
    chosenWords = random.choice(Pyart.Word_Stock).lower()
    chances = 6
    End_of_Loop = False
    fillWord = []
    # @ Create a list which fill with underscores
    for i in chosenWords:
        fillWord.append("_")
    # @ Display the Premier status of the User
    print("Guess the Word :", end=' ')
    print("".join(fillWord))
    print(f"{len(chosenWords)} letters word have to guess")
    print(f"The Chances left : {chances}")

    while not End_of_Loop:

        guessLater = input("Guess a later : ").lower()
        # @ Check Weather the Chosen word is correct or not, if not then reduce the chance
        if not (guessLater in chosenWords):
            chances -= 1
            print("Wrong Attempted <<---\n")
        elif guessLater in fillWord:
            print("Already Chosen this Latter\n")

        # @ now replace empty space of word with guessed letter if the @
        index = 0
        for latter in chosenWords:
            if guessLater == latter:
                fillWord[index] = guessLater
            index += 1

        # * Display the status of the the User:
        print("".join(fillWord))
        print(f"The Chances left : {chances}")
        # print(Pyart.punishment_Stage[6-chances])
        print(Pyart.stages[chances])

        # @ Check if their Any blank space left or not , for win
        if '_' not in fillWord:
            print("** You win this Match **")
            End_of_Loop = True
        elif chances == 0:
            print("** You Loos All chances and Loos the Game **")
            print(f"The Word was {chosenWords}\n")
            End_of_Loop = True
