# project 2. The Perfect Guess
import random
def checkGuess(guess,num):
    attempts=0
    while(True):
        if guess<num:
            guess=int(input("Wrong!!! Guess higher number : "))
            attempts+=1
        elif guess>num:
            guess=int(input("Wrong!!! Guess lower number : "))
            attempts+=1
        else:
            print(f"""Congratulations!!! You guessed right.
Number of Attempts : {attempts}""")
            return attempts
num=random.randint(1,100)
guess=int(input("Guess a number between 1 to 100 : "))
temp=checkGuess(guess,num)
with open("hiscore.txt","r") as f:
    hiscore=int(f.read())
if temp<hiscore:
    print("You broke the record!!!!")
    with open("hiscore.txt","w") as f:
        f.write(str(temp))
























