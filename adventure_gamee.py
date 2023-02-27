import time
import random


def PrintMassegeMethod(Massege):
    print(Massege)
    time.sleep(2)


def GameBegins():
    PrintMassegeMethod("You find yourself in a Dark Street \n")
    PrintMassegeMethod(",No One Around And There was a lots of car and bus noises \n")
    PrintMassegeMethod(",To get Back home You have To choose the right doors that contains The key  \n")
    PrintMassegeMethod("There was 2 Doors The Black Door That Has Number 1\n")
    PrintMassegeMethod(",The Second Door The Dark blue That Has Number 2....\n")
    PrintMassegeMethod(",You Have Heard a Voise telling You That You Have To Choose A door....\n")


def BlackDoor():

         PrintMassegeMethod("The door opend")
         PrintMassegeMethod("Go ahead , The key is there , You Won !!  ")
         randoms()



def BlueDoor():
    PrintMassegeMethod("The door opend")
    PrintMassegeMethod("Go ahead , Unfortunatlly , The key is not in here !!  ")
    PrintMassegeMethod("Game Over ")
    GameRestart()

def randoms():
     Encourge= ["You Did a great Work !","Congrats on winning ","Wohooo"]
     print(random.choice(Encourge))

def GameRestart():
    PrintMassegeMethod("do you like to Restart the game again?")
    answer = input("please enter Yes or No\n")
    if answer == "Yes":
        Begins()
    if answer == "No":
        exit()
    else:
        PrintMassegeMethod("Please enter a valid option ")

def Begins():
    GameBegins()
    while True:
        Value = input("Enter 1 to Enter The black door\n"
                      "Enter 2  to Enter The black door\n"
                      "What would you like to do? \n")

        Value=int(Value)
        if Value == 1:
            BlackDoor()

        elif Value == 2:
             BlueDoor()

        else:
            print("Invalid Input")
            Value = input("Please enter 1 Or 2 \n")
            Value = int(Value)


Begins()




