import random
# Result function
def gameWin(comp,you):
    if comp==you:
        print("This is a tie!!!!")
    elif comp=='s':
        if you=='w':
            print("You  Lost!!!")
        elif you=='g':
            print("You  Win!!!")
    elif comp=='w':
        if you=='s':
            print("You  Win!!!")
        elif you=='g':
            print("You  Lost!!!")
    elif comp=='g':
        if you=='s':
            print("You  Lost!!!")
        elif you=='w':
            print("You  Win!!!")
# inputs           
you=input("Your Turn : Snake(s) Water(w) Gun(g) ")
print("Computer turn : Snake(s) Water(w) Gun(g) ")
no=random.randint(1,3)
if no==1:
    comp='s'
elif no==2:
    comp='w'
else:
    comp='g'
#processing
print(f"\nYou chose {you}")
print(f"Computer chose {comp}\n")
gameWin(comp,you)

    