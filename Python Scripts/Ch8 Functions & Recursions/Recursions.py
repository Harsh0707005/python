# Recursions
'''
Recursion is a function which calls itself. It is used to directly use a mathematical formula as a function.
For Example:

factorial(n) = 1 * 2 * 3...n
'''
# Q. Find Factorial of a given number.

num = int(input("Enter a number for factorial:\n"))

def factorial_iter(num):    # iter means iterable
    product = 1 
    for i in range(num):
        product = product * (i+1)
    return product

print(factorial_iter(num))

'''
{factorial(n) = 1 * 2 * 3...n} can also be written as 
n! = 1 * 2 * 3 * (n-1) * n
and 
1 * 2 * 3 * (n-1) is same as (n-1)! or factorial(n-1).

So,
n! = factorial(n-1) * n
'''

# Factorial of number using this formula.

n = int(input("Enter a number for factorial:\n"))

def factorial_recursive(n):
    if n == 1 or n == 0:     # It is the base condition which doesn't call the function further.
        return 1
    return n * factorial_recursive(n-1)   # Function calling itself

print(factorial_recursive(n))

'''
The programmer needs to be extremely careful while working with recursion to ensure that the function doesn't infinitely keep calling itself.
Recursion is sometimes the most direct way to code on algorithm.
'''