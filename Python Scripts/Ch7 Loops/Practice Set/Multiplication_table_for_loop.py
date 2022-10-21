# Write a program to print multiplication table of a given number using 'for' loop.

num = int(input("Enter a number for the multiplication table:\n"))

for i in range(1, 11):  # stop given as 11 as it executes till (n-1) value.
    product = num*i
    print(str(num) + ' x ' + str(i) + ' = ' + str(product))

# OR 
# By using 'f'strings

for i in range(1, 11): 
    product = num*i
    print(f"{num} x {i} = {product}")
    