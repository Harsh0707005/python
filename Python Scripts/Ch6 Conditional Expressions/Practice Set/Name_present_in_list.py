# Write a program to find whether a name is present in a list or not.

names = ["Harsh", "Harry", "Aditya", "Rohan"]

name = input("Enter the name to check if present in list:\n")

if name in names:
    print("Yes,", name,"is present in the list")
else:
    print("No,", name,"is not present in the list")