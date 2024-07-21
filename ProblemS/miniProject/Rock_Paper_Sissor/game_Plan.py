import random
import greet
import startArt as pyArt

#! display the logo:
print(pyArt.letsPlay)

#!  What are choices for computer --
choice = ["Rock", "Paper", "Scissor"]
player = False

#!Greet Player
name = greet.greet()

#! Tell Instruction
greet.instruction()
print("So, lets Start the game ->>>>\n")
i = 3
player_Point = 0
Computer_point = 0

while i > 0:
    computer_Choice = random.choice(choice)
    i -= 1
    player_choice = input("Your Choice :>> ")
    if player_choice == computer_Choice:
        print("Tai !")
    elif player_choice == "Rock":

        if computer_Choice == "Paper":
            Computer_point += 1
            print("Computer Choose: ", pyArt.Paper)
            print("You lose! paper Covers Rock")
        else:
            player_Point += 1
            print("Computer choose: ", pyArt.Scissor)
            print("You win! Rock Smashes Scissor")
    elif player_choice == "Paper":

        if computer_Choice == "Scissor":
            Computer_point += 1
            print("Computer Choose: ", pyArt.Scissor)
            print("You lose!", computer_Choice, "Cut", player_choice)
        else:
            player_Point += 1
            print("Computer Choose: ", pyArt.Rock)
            print("You win!", player_choice, "Covers", computer_Choice)
    elif player_choice == "Scissor":

        if computer_Choice == "Rock":
            Computer_point += 1
            print("Computer Choose: ", pyArt.Rock)
            print("You lose!", computer, "smashes", player_choice)
        else:
            player_Point += 1
            print("Computer Choose: ", pyArt.Paper)
            print("You win!", player_choice, "cut", computer_Choice)
    elif player_choice == "Quit":
        print("Thank you for Playing!\n\tCOOmmE to play again")
        break
    else:
        print("Type Correctly to play again Or 'QUIT' the Game")
        i += 1
        continue


if Computer_point > player_Point:
    print(f"Alas!{name}\n\tYou Loos by {Computer_point - player_Point}")
elif Computer_point == player_Point:
    print("both Score same")
else:
    print(
        f"Congratulations!!{name}\n\tYou Won the game by {player_Point- Computer_point}")
