# Importing a module
import random

# Defining a function named GameWin(Comp, player)
def GameWin(Comp, player):
    
    # Checking if both computer and player chose same choice.
    if Comp == player:
        return None
    
    # Checking all possibilites when computer chooses snake(s)
    elif Comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True

    # Checking all possibilites when computer chooses water(w)
    elif Comp == 'w':
        if player ==  's':
            return True
        elif player == 'g':
            return False

    # Checking all possibilites when computer chooses gun(g)
    elif Comp == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True
        

print("Computer's turn: Snake(s), Water(w) or Gun(g)?")

RandNo = random.randint(1,3)

if RandNo == 1:
    Comp = 's'
elif RandNo == 2:
    Comp = 'w'
else:
    Comp = 'g'

player = input("Your's turn: Snake(s), Water(w) or Gun(g)?\n")


valid = True

# Checking if player input values except for  the choices.
if player == 's' or player == 'w' or player == 'g':
    pass
else:
    valid = False
    # Creating a loop that keeps on executing untill player enters a valid choice.
    while valid == False:
        print("Please input a valid choice!")
        player = input("Your's turn: Snake(s), Water(w) or Gun(g)?")
        if player == 's' or player == 'w' or player == 'g':
            valid = True
        else:
            pass

GameWin(Comp, player)

print(f"Computer chose {Comp}.")
print(f"You chose {player}.")

# Printing the result of the game.

if GameWin(Comp, player) == None:
    print("The Game is a tie!")
elif GameWin(Comp, player) == True:
    print("You Won the game!")
else:
    print("You lose the game!")