# # 1. 'f'-string
'''
'f' strings are simply strings in which one can put strings, variables and evaluate values easily.
This are created simply by adding 'f' before a string.
Integers or variables can be written by adding curly brackets ('{}'). 
And strings are written simply like that
For Example:
'''

print(f"{1}+{2} is {3}")

num = int(input("Enter a number: "))
print(f"Your number after multiplying {9} is {num*9}")

print("***************************")

# # 2. Using %
'''
Similar to format.
'''
s = "Welcome %a to %a" % (
    'Harsh', 'Python')  # not necessary to %a can be %b, %c etc
print(s)

print("***************************")

# # 3. Using format function

s = "Welcome {} to the world of {}.".format("Harsh", "Python")
print(s)
a = "Welcome {1} to the world of {0}.".format("Harsh", "Python")  # indexed
print(a)
