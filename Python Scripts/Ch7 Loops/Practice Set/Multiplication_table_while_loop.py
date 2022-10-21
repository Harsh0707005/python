# Write a program to print multiplication table of a given number using 'while' loop.

num = int(input("Enter the number for multiplication table:\n"))

i = 1

while i<=10:
    product = num*i   
    print(f"{num} x {i} = {product}")
    i = i+1