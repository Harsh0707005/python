'''
We are going to write a program that generates a random number and asks the user to guess it.

If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please”.

When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

Hint: Use the random module
'''

import random

randNumber = random.randint(1, 100)

userGuess = None

guesses = 0

while userGuess != randNumber:
    userGuess = int(input("Enter your Guess (between 1 to 100) :\n"))
    
    guesses += 1

    if userGuess == randNumber:
        print("Your Guess is Correct...!")
    else:
        if userGuess > randNumber:
            print("Your Guess is incorrect! Enter a smaller number...")
        else:
            print("Your Guess is incorrect! Enter a larger number....")
    

print(f"You guessed the correct number in {guesses} guesses.")

try:
    with open("hiscore.txt") as f:
        hiscore = int(f.read())
    
    if hiscore > guesses:
        print("You have just broken the hiscore!")
        with open("hiscore.txt", 'w') as f:
            f.write(f"{guesses}")
except Exception as e:
    with open("hiscore.txt", 'w') as f:
        f.write(f"{guesses}")