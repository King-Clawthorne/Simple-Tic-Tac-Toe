import random
import sys
from time import sleep

RPSTable = {
    1 : ("Rock", 3),
    2 : ("Paper", 1),
    3 : ("Scissors", 2)
}

Playing = True

def getComputerResponse():
    pickedNumber = random.randint(1, 3)

    return {"Picked" : pickedNumber, "Tab" : RPSTable[pickedNumber]}

while Playing:
    try:
        playerInput = input("Rock, Paper, Or Scissors?\n")

        picked = False

        for i,v in RPSTable.items():
            if v[0].lower() == playerInput.lower():
                picked = {"Picked" : i, "Tab" : v}

        computerResponse = getComputerResponse()

        while True:
             if computerResponse["Picked"] != picked["Picked"]:
                  break
             else:
                computerResponse = getComputerResponse()

        if computerResponse["Tab"][1] == picked["Picked"]:
                print(f"The computer picked {computerResponse['Tab'][0]}, the computer wins!")
        elif picked["Tab"][1] == computerResponse["Picked"]:
            print(f"The computer picked {computerResponse['Tab'][0]}, you win!")
        user_Input = input("Would You like to play again? (y/n)\n")
        print(user_Input)
        if user_Input.lower() == "n" or user_Input.lower() == "no":
             break        
    except:
        print("Please pick one of the three!")
