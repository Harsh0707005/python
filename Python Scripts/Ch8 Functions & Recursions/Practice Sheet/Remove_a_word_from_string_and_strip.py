# Write a python function to remove a given word from a string and strip it at the same time.

def remove_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

string = "    Harsh is an awesome person!    "

Str = remove_and_strip(string, "Harsh")
print(Str)