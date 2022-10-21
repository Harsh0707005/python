# How do you prevent a python print() function to print a new line at the end.
'''
'end' argument is used to prevent python print() function to print a new line at the end.
'''

# Before 'end' argument -

print("Hello")
print("How")
print("are")
print("you?")

# After 'end' argument -

print("Hello", end = " ")
print("How", end = " ")
print("are", end = " ")
print("you?")