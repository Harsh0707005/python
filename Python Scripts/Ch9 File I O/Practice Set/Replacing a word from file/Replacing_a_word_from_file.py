# A file contains a word 'Donkey' multiple times. You need to write a program which replaces the word with ###### by updating the same file.

with open("Donkey.txt") as f:
    t = f.read()

t = t.replace("donkey", "######")
t = t.replace("Donkeys", "######")


with open("Donkey.txt", "w") as f:
    f.write(t)