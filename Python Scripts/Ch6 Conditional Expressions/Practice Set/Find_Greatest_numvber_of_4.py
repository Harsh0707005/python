# Write a Program to find the greatest of the four numbers entered by the user.

num1 = int(input("Enter number 1:\n"))
num2 = int(input("Enter number 2:\n"))
num3 = int(input("Enter number 3:\n"))
num4 = int(input("Enter number 4:\n"))

if (num1>num2):
    f1 = num1
else:
    f1 = num2

if (num3>num4):
    f2 = num3
else:
    f2 = num4

if (f1>f2):
    print(f1, "is greatest")
else:
    print(f2, "is greatest")