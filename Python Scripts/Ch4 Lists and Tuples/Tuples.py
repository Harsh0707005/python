# Tuples

'''
A tuple is an immutable (cannot change) data type in python.
'''

# Creating tuples
'''
Tuples are always created using '()' unlike square brackets of lists.
For Ex:
'''

t = (1, 2, 4, 5)

# Tuple can have repeated values.

# Printing element of a Tuple (using indexing similar to lists.)

print(t[0])

'''
Note: 
In tuples item assignment is not allowed. 
Like:
t[0] = 34  => will return an error as item assignment is not allowed.
'''

print("******************************************")

# Types of Tuples:

# 1. Empty Tuple
'''
It is basically a tuple with no values in it.
'''
t1 = ()
print(t1)

print("******************************************")

# 2. Tuple with single element.
'''
This type tuple only consists a single value in it.
'''
t2 = (1,)
print(t2)

# Note: If one doesn't put ',' while declaring a tuple then python will consider the value in the parenthesis to be an integer. For Example: t2 = (1) will only print '1' hence python would consider it an integer.

print("******************************************")

# 3. Tuple with multiple elements.
'''
This type of tuple consists more than one elements (multiple).
Like:
'''

t3 = (4, 9, 2, 5)
print(t3)