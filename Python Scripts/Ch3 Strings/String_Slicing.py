# # Concatenating strings 
'''
The action of linking of two or more strings is called concatenating of strings.
'''

greetings = "Good Morning, "
name = "Harsh "
last_name = "Master"
c = greetings + name + last_name # => Here, 3 strings are catenated.
print(c)

# # String Indexing
'''
String indexing helps us to access a letter by its index value.

For ex.

H A R S H    OR    H   A   R   S    H     
^ ^ ^ ^ ^          ^   ^   ^   ^    ^
0 1 2 3 4         -5  -4  -3   -2  -1

Indexing starts from 0 if don from left while starts from -1 if done from right.

Negative Indexing is used because if for example one doesn't know the length of the string but 
he wants to print the last letter so he may use '-1' to print the last letter when lenght is unknown.
'''

name = "Harsh"
print(name[0]) 

'''
Note: One can not assign a assgin a letter of string to any other expression or value

For ex.

name[3] = "d"   => This won't work.
'''

# # String Slicing

'''
Syntax:

name[ index start : index end ]
        ^                 ^
        |                 |
first index included      last index is not included
'''

# # String slicing is taking out a piece of a string and using it.
# For ex.

print(name[0:3])

'''
Note: In this case 3 won't print instead 0,1 & 2 would print i:e H,A & R
If taken 0:4 then 4th won't print instead 0,1,2 & 3 would i:e H,A,R & S.
'''

print(name[ 0 : ]) # => it is same as 0 to the last index.
print(name[ : 4 ]) # => it is same as from 0 to 4th index (defined index value).

# # String slicing of negative indices
c = name[-4:-1]  # This is same as name[1:4]
print(c) 

# # String slicing with skip value
# It is used to print the sliced strings by skipping some of the characters.

# Syntax
'''
name [ index start : index end : skip value ]

Skip value skips the characters and prints the next value.
For example:
'''
name = "HarshIsGood"
c = name[0::3] # => Here from 0 to last index everything is needed to be printed with skip value of 3 so every third character after first prints.
print (c)

'''
If skip value is given as 2 then every 2nd character after the first defined index character will be printed and so on.
Note: if skip value given as 1 then no character will be skipped as the next value after defined index is itself as 1st. 
'''

# # To get index number of an element of string
'''
It is used to get the index number of an element in a string.
'''
# Syntax:
'''
<var>.index("<element")

For Example:
'''

a = "My name is Harsh."
print(a.index("i"))