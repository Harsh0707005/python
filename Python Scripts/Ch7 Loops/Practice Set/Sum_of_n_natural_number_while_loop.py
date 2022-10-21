# Write a program to find the sum of first 'n' natural numbers using 'while' loop.

num = int(input("Enter the number for sum of number of natural numbers.\n"))


s = 0
n = 0
if num<0:
    print("Enter a positive number.")
else:
    while n<=num:
        s = s+n
        n = n+1
    print(f"The sum of first {num} natural numbers is {s}")