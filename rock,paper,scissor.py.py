import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return False
        elif you == 's':
            return True
    elif comp == 'p':
        if you == 's':
            return False
        elif you == 'r':
            return True
    elif comp == 's':
        if you == 'r':
            return False
        elif you == "p":
            return True
        
print("comp Trun : Rock(r) Paper(p) scissor(s)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Rock(r) Paper(p) scissor(s)?")
a = gameWin(comp, you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("The game is tie!")
elif a :
    print("you Win!")
else:
    print("You Loose!")

