# A Dictionary is a collection of key-value pairs.


'''

Syntax:

              Keys      Values
                ^         ^  
                |         |
         a = {"Key"  :  "Value",}

In the place of 'key' one needs to input term and in 'Values' one needs to put value for the specified term.

'''

'''
Note:
Same key cannot be assigned multiple times, if done it will overwrite.
For Example:

dict = {
    "Marks" : [1,7,3,6],
    "Marks" : (99,97,45,65) 
}
Here the value of the 'key' 'marks' will be (99,97,45,65) instead of earlier.
'''

# For Example:

myDict = {
    "Amiable" : "Friendly or pleasant", # For multiple keys in a dictionary ',' after each.
    "Fast" : "In a Quick manner",  
    "Foolish" : "Silly, non Sensible",
    "Numbers" : [1, 5, 7, 9], # A dictionary can have a list as well.
    "Marks" : (88, 76, 55, 4) # A dictionary can also have tuple.
}

# To print a dictionary:

'''
Syntax:
    print( <variable of dictionary>[ "<Key>"])

'''

print(myDict["Fast"])
print(myDict["Numbers"])
print(myDict["Marks"])


'''
Nested Dictionary

A dictionary cam also have another dictionary into it.

'''
# For Example

Dict = {
    "anotherdict" : {"Ronaldo" : "Player"}
}

# Printing a nested dictionary
'''
A nested dictionary can be printed in two ways:
i. the complete dictonary(nested)
OR
ii. The value of the key in the nested dictionary.
'''

# For Example

print(Dict["anotherdict"])

#     OR

print(Dict["anotherdict"]["Ronaldo"])


# A dictionary is mutable(can be changed).

# For example:

Dict["anotherdict"]["Ronaldo"] = ("Football")  # Value of Ronaldo is changed from player to football.

print(Dict["anotherdict"]["Ronaldo"])