a = set()

# # 1. Adding values to Set

'''
To add a value to the set;
Syntax:
<variable of set>.add(<value to be added>)
For Example:
'''
a.add(8)
a.add(9)
a.add(10)
a.add(6)
a.add(8) #This won't be added to set as set is collection of non-repetitive elements.
print(a)

'''
We cannot add a list or a dictionary to the set as it can be changed while tuple can be added to it as it cannot be changed.
'''

a.add((1, 4, 3))
# a.add([1, 8, 2])   # It will returm an error as "unhashable type".
# a.add({1 : 7})   # It will returm an error as "unhashable type".
print(a)


# # 2. Length of a set
'''
Printing the length of a set can be printed by;
Syntax:
print(len(<variable of a set>))
'''
print(len(a))
'''
Note:
A tuple is counted as one element/item.
'''

# # 3. Removal of an item
'''
An item of a set can be removed, if present, by;
Syntax:
<variable of set>.remove(<value to be removed>)

If an item is not present in the set then it will return an error.
'''
a.remove(8) # 8 is removed from the set.
print(a) # Printing 'a' after removal of 8.


# # 4. Pop Method
'''
It removes an arbitrary element from the set and returns the element removed.
It removes any random element from the set.
Syntax:
<variable of set>.pop()
'''
print(a.pop()) # Printing the element removed.

# # 5. Clearing of set
'''
This method empties the set.
Syntax:
<variable of set>.clear()
'''

a.clear() # Clears the set 'a'.
print(a)  # Printing the set after being cleared.


b = {5, 9, 8, 13, 11}


# # 6. Union of set
'''
It returns a new set with all items from both sets.
Syntax:
<variable of set>.({<another set>})
'''

print(b.union({7, 12}))  # Printing a union set.


# # 7. Intersection of set
'''
It returns a set that contains only item from both the sets.
Syntax:
<variable of set>.intersection({<another set>})
'''

print(b.intersection({8, 14, 11}))  # Printing a intersection set.

# ________________________X_________________________________X___________________________X


# # Properties of Sets
'''
1. Sets are unordered (order doesn't matter.)
2. Sets are unindexed (cannot be accessed by index.)
3. There is no way to change items in sets.
4. Sets cannot contain duplicate(repetitive) values.
'''