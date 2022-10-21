# Write a program to make a copy of "this.txt" file.

with open("this.txt") as f:
    content = f.read()

with open("copy.txt", "w") as f:
    content = content.replace("original", "copy of original")  # To differentitate between original and copied file
    f.write(content)