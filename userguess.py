import random
num=random.randint(20,100)
print(" You have five chances to guess the number")

chances=0
while True:
    if(chances==5):
        print(" You Lost The Game")
        break
    else:
        user=int(input(" Guess the number between 20 to 100:"))
        if (user <num ):
            print("Wrong  " + " Think Little bit Higher ")
            chances=chances+1

        elif (user >num ):
            print("Wrong  " + " Think Little bit Lower ")
            chances=chances+1
        elif(user==num):
            print("Congratulation Guys You Won this Game" )
        