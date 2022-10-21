# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word "Twinkle"

f = open("poems.txt")
t = f.read()

if "Twinkle" in t:
    print("Yes, 'Twinkle'it is present")
else:
    print("No, 'Twinkle' it is not present")
f.close()