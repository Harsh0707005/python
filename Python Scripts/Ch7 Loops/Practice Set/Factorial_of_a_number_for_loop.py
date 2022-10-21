# Write a program to find the factorial of a given number using 'for' loop.

'''
Q. What is a factorial?
A. A factorial is a function that multiplies a number by every number below it. For Example:
5! (factorial of 5) = 1 x 2 x 3 x 4 x 5 = 120
4! = 1 x 2 x 3 x 4 = 24
'''

num = int(input("Enter a number to find factorial of:\n"))

factorial = 1

# as, if only done 'num', it will only go till num-1.
for i in range(1, num+1):
    factorial = factorial * i
    print(factorial)
print(f"The factorial of {num} is {factorial}")
