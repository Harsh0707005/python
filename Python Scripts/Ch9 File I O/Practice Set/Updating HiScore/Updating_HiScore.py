# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'hiscore.txt' which is either blank or contains previous Hi-Score. You need to write a program to update 'hiscore.txt' whenever game() breaks the Hi-Score.

def game():
    return 64

score = game()

with open("hiscore.txt") as f:
    HiScore = f.read()

if HiScore == "":
    with open("hiscore.txt", "w") as f:
        f.write(str(score))  # As files can only be written in string format
elif score>int(HiScore):
    with open("hiscore.txt", "w") as f:
        f.write(str(score))