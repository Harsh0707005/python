# Write a program to print multiplication table of n using 'for' loop in reversed order.
num = int(input("Enter number for reverse multiplication table:\n"))



for i in range(1,11):
    i = 11 - i 
    product = num * i
    print(f"{num} x {i} = {product}")