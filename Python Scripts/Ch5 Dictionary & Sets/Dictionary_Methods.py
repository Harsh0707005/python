myDict = {
    "Amiable": "Friendly or pleasant",
    "Fast": "In a Quick manner",
    "Marks": [1, 5, 7, 9],
    "anotherdict": {"Ronaldo": "Player"},
    1: 2
}

# Dictionary Methods
# # 1. <var of dictionary>.keys()
'''
It will print the keys used in the specified dictionary in the form of list. 
'''

print(myDict.keys())
print("*******************************")

print(type(myDict.keys()))
print("*******************************")

'''
But its type is not list, its type is 'dict_keys'.
It can be converted into list by typecasting, as follows.
'''
print(list(myDict.keys()))
print("*******************************")

# # 2. <var of dictionary>.values()
'''
It will print the values used in the specified dictionary in the form of list.
But its type is not list it's type is 'dict_values'
It can be converted into list as by typecasting as done above.
'''
print(myDict.values())
print("*******************************")

# # 3. <var of dictionary>.items()
'''
It will print the (keys,values) pair for all the contents in the specified dictionary.
It's type is 'dict_items'
'''
print(myDict.items())

print("*******************************")

# # 4. <var of dictionary>.update()
'''
It basically updates the dictionary by adding (key : value) pairs from the updated dictionary.
'''
# For Example:

updateDict = {
    "Foe": "Enemy",
    "New Marks": [5, 4, 8, 6]
}

# It updates the initial dictionary by adding (key : value) pair from new specified dictionary.
myDict.update(updateDict)

# Printing updated dictionary:

print(myDict)
print("*******************************")

'''
If the same 'key' with different 'value' is provided in the new dictionary then it will 'update' the value of the initial 'key' with the new 'value' from the updated dictionary.
'''

# # 5. <var of dictionary>.get()
'''
It prints the value of the specified 'key', if present, else returns 'none'.
'''
# For Example:
print(myDict.get("Fast"))

print("*******************************")
# _____________________________X___________________________X_________________X

'''
A very important question:

Q. The same thing of 'get' method can be done with {print(myDict["Fast"])}, then why do we use 'get' method ?
A. When 'get' method is used, it will print the value, but if the specified 'key' is not present in the dictionary then it will print 'none'.
But in {print(myDict["Fast"])}, if the key is not present it will return an error.
'''
# If key is not present :

print(myDict.get("valient"))  # It will print 'none'.

# Whereas this {print(myDict["Fast"])} will return an error.

print("*******************************")

# # 6. Get key from value
'''
There is no specific function for getting key from particular value but we can get it by converting both keys and values to list and comparing the indices.
'''
# For Example:
my_dict = {"java": 100, "python": 112, "c": 11}

key_list = list(my_dict.keys())
val_list = list(my_dict.values())

position = val_list.index(100)
print(key_list[position])

print("*******************************")

'''
It can alse be done by comparing values with .items() functions, as follows:
'''
for key, value in my_dict.items():
    if 100 == value:
        print(key)

print("*******************************")
