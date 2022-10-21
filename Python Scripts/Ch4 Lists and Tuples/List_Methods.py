l1 = [1, 8, 7, 2, 21, 15]

# Some of important and most used list methods.
# 1. Sort Function

'''
This function is used to sort the list item in an ascending order.

This function can also be used to arranged words in alphabetic order.
'''
l1.sort()
print(l1)  # Printing the sorted l1 list.

print("******************************************")

ls = ["Harry", "Harsh", "Ankit", "Tirth"]
ls.sort()
print(ls)

print("******************************************")

# 2. Reverse Function

'''
This function reverses the order of items in the list.
'''
l2 = [1, 8, 7, 2, 21, 15]
l2.reverse()
print(l2)

'''
Here if done l1.reverse() then it will reverse the sorted l1 list not the original.
'''

print("******************************************")

# 3. Append function

'''
This function is used to add a specified value/character at the end of the list. 
'''

l3 = [1, 8, 7, 2, 21, 15]
l3.append(45)  # It adds 45 at the end of the list
l3.append(80)  # It adds 80 at the end of the list
print(l3)

print("******************************************")

# 4. Insert function
# { Syntax: variable of list.insert(index value, value to be inserted) }

''' 
It basically inserts the specified value to a specified index value in between the list without changing the original values of the list.
'''

l4 = [1, 8, 7, 2, 21, 15]
l4.insert(0,  550)
#         ^      ^
# index value | value to be inserted at specified index value.
l4.insert(2, 640)  # Inserts 640 at the index value of 2.
print(l4)

print("******************************************")

# 5. Pop function

'''
It removes the value at the specified index value.
'''
l5 = [1, 8, 7, 2, 21, 15]
l5.pop(2)  # It removes the value at index 2.
l5.pop(4)  # It removes the value at index 4.
print(l5)

print("******************************************")

# 6. Remove function

'''
It is same as 'pop' function but here instead of removing a value at specified index it removes the specific value.
For example:
'''

l6 = [1, 8, 7, 2, 21, 15]
l6.remove(21)  # It removes 21 from the list.
l6.remove(8)  # It removes 8 from the list.
print(l6)

print("******************************************")

# 7. Index function
'''
It is used to get the index of a literal in a list
For example:
'''

l7 = [1, "Harsh", 3.14, "Xeno"]
a7 = l7.index("Xeno")
b7 = l7.index(1)
print(a7)
print(b7)


print("******************************************")

# # 8. Any function
'''
The any() function returns True if any element of an iterable is True. If not, it returns False.
'''

boolean_list = ['True', 'False', 'True']

result = any(boolean_list)
print(result)

s = "Harsh1"

print(any(char.isdigit() for char in s))

print("******************************************")
