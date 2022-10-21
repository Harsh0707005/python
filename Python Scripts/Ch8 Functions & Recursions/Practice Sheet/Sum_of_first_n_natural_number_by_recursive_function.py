# Write a recursive function to calculate the sum of first 'n' natural numbers.

n = int(input("Enter till what number you want sum of natural numbers:\n"))

def sum(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return sum(n-1) + n

print(sum(n))