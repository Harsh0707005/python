# 'is' 
'''
It checks if something is same or not.
For Example:
'''

a = None

if a is None:
    print("Yes")
else:
    print("No")

'''
It is basically same as "==" .
It can also be written as:

a = None

if a == None:
    print("Yes")
else:
    print("No")
'''

# One more Example:

a = 5

if a is 5:
    print("True")
else:
    print("False")



# 'in'
'''
It basically checks whether the specified element present in the defined list/dictionary/tuple etc...
For Example:
'''

b = [2, 6, 3, 8, 13]

print(3 in b)

# OR

if 3 in b:
    print("Yes")
else:
    print("No")

# In a string: 

c = ("Once upon a time")

print("Once" in c)
print("tree" in c)

# etc....