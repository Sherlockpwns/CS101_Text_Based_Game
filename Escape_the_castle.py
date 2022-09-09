#!/usr/bin/python 3
# ############################################################################
# Program name: escape the castle 
# Author: Sherlockpwns
# State: works
# Description: can you escape the catle in this text based game with multiple choices.
# ############################################################################

#  Things to do
# 1. add some colour on diffren things to enchnage user experince 
# 2. generate a loop wher eyou can play again rather than having to exit the program 


import time
import random


def draw_line():
    dots = "-" * 124
    print(dots)


# now we can remove the excess by recalling this every time.

draw_line()
print("                                                        THE MYSTIC CASTLE")
draw_line()

print(" You are in a dark room in a mysterious castle")
print()

time.sleep(2)

print("In front of you is FOUR doors you must choose one !")
playerchoice = input("Choose 1, 2, 3 or 4 .....")  # Ask player to make a choice  1 2 3 or 4.

# 1
if playerchoice == "1":
    print("You find a room full of treaure. You are Rich!")
    print("----------------------------- !! GAME OVER YOU WIN !! --------------------------------------------")

# 2
elif playerchoice == "2":
    print("The door opens ... The guards pounce on you and arrest you ....")
    print("Later that night you are taken from your cell and executed")
    print()
    print("----------------------------- !! GAME OVER YOU LOOSE !! --------------------------------------------")

# 3
elif playerchoice == "3":
    print("You head into the room and find a sleeping dragon")
    print(" You can either")
    print("1) Try steal some of the dragons gold.")
    print("2) try to sneak around the drgaon to the exit")

    dragonchoice = input("type 1 or 2 ")

    # 1
    if dragonchoice == "1":
        print("As you try to steal the gold quitely you accidntly drop soemthing which awakes the dragon... ")
        print("As you attaempt to run for the exit you trip over and the dragon eats you before you are able to escape")
        print("----------------------------- !! GAME OVER YOU LOOSE !! --------------------------------------------")

    # 2
    elif dragonchoice == "2":
        print(
            " You are able to sneak around the dragon and exit the castle and in doing so find some small amount of gold as you exit the secret tunnel to the outside world.")
        print("----------------------------- !! GAME OVER YOU WIN !! --------------------------------------------")

    # error catcher
    else:
        print("Sorry you didnt choose 1 or 2 try again")
        print("Run the game again and have another go")

# 4
elif playerchoice == "4":
    print("You enter the room with a Sphinx")
    print(
        "The sphinx gives you a choice to play a game that if you guess the number correctly you will be set free with all the gold, if not you are her prisoner forever !!")
    print("SO what number am i thinking of between 1 and 5 ")
    number = int(input(
        "What number do you choose ? "))
    random_choice = random.randint(1, 2)
    print(" The sphix declares the number that she is thinking is " + str(random_choice))
    if number == random_choice:
        print("The sphinx hisses with disappointment. you guessed correctly")
        print("She must let you gop free")
        print("----------------------------- !! GAME OVER YOU WIN !! --------------------------------------------")
    else:
        print("The sphinx tells you that your guess is incorrect.")
        print("You are now a prisoner forever")
        print("----------------------------- !! GAME OVER YOU LOOSE !! --------------------------------------------")
