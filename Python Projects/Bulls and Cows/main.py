import random


def choose_number():
    number = random.randint(1000, 9999)  # Choosing a four digit number
    
    # Randomly generating number until all digits are distinct
    while len(str(number)) != len(set(str(number))):
        number = random.randint(1000, 9999)
    print("Computer chose the number !!!")
    return str(number)


def game():
    chosen_num = choose_number()

    count = 0
    while count < 7: # Running th loop until 7 guesses
        user_guess = input("Enter your guess: ")
        count += 1
        bulls = 0
        cows = 0
        for chr in user_guess:
            if chr in chosen_num: # checking if digits in guess exist in number
                
                if user_guess.index(chr) == chosen_num.index(chr): # checking if it is a bull
                    bulls += 1
                else:
                    cows += 1 # checking if it is a cow
            else:
                pass
        if bulls != 0 or cows != 0:
            print(f"Bulls : {bulls}\n")
            print(f"Cows : {cows}\n")
            print(f"Remaining guess : {7-count}\n")
        else:
            print("\nNo matching digit appears in your guess :( \nTry Again...\n")
            print(f"Remaining guess : {7-count}")

        if cows == 0 and bulls == 4:
            score = count
            print(f"You guessed the number in {score} guesses :)")
            print(f"The chosen number was {chosen_num}.")
            return score
        else:
            pass
        
    else:
        print("You were unable to guess the number in 7 guesses :(")
        print()
        print(f"The chosen number was {chosen_num}.")
        print()
        retry = input("Do you want to play again? (Y/N)") # asking if want to play again.
        if retry == 'Y':
            game()
        else:
            print("Good to have you...")
            quit()

score = game()

try: # checking if file exist
    with open("hiscore.txt") as f:
        hiscore = int(f.read())
    
    if hiscore > score: # checking if user broke the hiscore
        print("\nYou have just broken the hiscore!")
        with open("hiscore.txt", 'w') as f:
            f.write(f"{score}") # appending if broke the hiscore
except Exception as e:
    with open("hiscore.txt", 'w') as f:
        f.write(f"{score}")