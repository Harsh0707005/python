# Write a program to wipe out the contents of a file using python.

filename = "this.txt"

with open(filename, "w") as f:
    f.write("")