# Arithmetic Operators
a = 3
b = 4

print("The value of a+b is", a+b)

# Note: One can input multiple expressions to print by putting comma(,) after one expression.

print("The value of a-b is", a-b)
print("The value of a*b is", a*b)
print("The value of a/b is", a/b)

'''
There are many Arithmetic operators in python
Ex. +,-,*,/ etc. 
'''


# Assignment Operators

'''
Assignment operators are basically shortcuts that can be used to add, divide,
subtract, multipy etc. to previously assigned variables.
'''

a = 36
a += 2
a -= 10
a *= 8
a /= 10
print(a)


# Comparison Operators

''' 
Comparison operators are used to compare the values.
These gives a boolean.
A boolean basically gives the value to be either true or false.
'''

b = (14>=7)
# b = (14<=7) (It means that 14 is either greater then or equal to 7) 
# b = (14<7)
# b = (14>7)
# b = (14!=7) (It means that 14 is not equal to 7) 

print(b)

# There are many more but here are some comparison operators that are most commonly used.


# Logical Operators

bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2)) 
# If both the bool1 and bool2 are true then it print true 
print("The value of bool1 or bool2 is", (bool1 or bool2)) 
# If any one the one bool1 or bool2 is true then it print true.
print("The value of not bool2 is", (not bool2)) 
# not bool2  prints the opposite of bool2
# print true in case of false and prints false in case of true.