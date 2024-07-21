import gameLogic

# Formal Greetings :
print("\n-------------Welcome to Hangman-------------\n")
print("Let's Start the Game")
# Instructions :
print("CHoose One latter at a time\n You given Total 6 Chances to guess the Correct word")

LoopingCond = False
while not LoopingCond:
    user = input("Do you want to play Hangman? (y/n): ").lower()
    if user == 'y' or user == 'yes':
        gameLogic.start()
    elif user == 'n' or user == 'no':
        print("Program Exit Successful")
        print("Print again to play Hangman!!")
        LoopingCond = True
    else:
        print("Your given input could not be processed.")
        print("Please enter a correct input.")
