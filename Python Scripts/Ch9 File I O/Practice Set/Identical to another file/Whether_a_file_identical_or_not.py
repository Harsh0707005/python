# Write a program to find out whether a file is identical and matches the content of another file.

with open("Original.txt") as f:
    f1 = f.read()

with open("Identical.txt") as f:
    f2 = f.read()

if f1 == f2 :
    print("Yes, the two files are identical.")
else:
    print("No, the two files are not identical.")