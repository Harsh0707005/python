# Write a program for a list of words to be censored from a file.

words = ["donkey", "kaddu", "mote"]

with open("Censor Sample.txt") as f:
    content = f.read()

for item in words:
    content = content.replace(item, "$%^@$^#")
    with open("Censor Sample.txt", "w") as f:
        f.write(content)