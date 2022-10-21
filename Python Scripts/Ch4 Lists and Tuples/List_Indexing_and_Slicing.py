# List Indexing OR accessing a value of a list using index number.

a = [1,2,3,4,5,6]

'''
Indexing of a list:
       a =     [ 1 , 2 , 3 , 4 , 5 , 6 ]
                 ^   ^   ^   ^   ^   ^
index values:    0   1   2   3   4   5

'''

# To print the value using index:

print(a[0])

print("******************************************")

# Overwriting/Changing the value of list.

a[0] = 50

# Printing the list with changed value.

print(a)

print("******************************************")

# List slicing

'''
It is similar to String slicing.
'''

fruits = ["Apple","Banana","Pineapple","Orange","Watermelon","Kiwi"]

print(fruits[0:4])
print(fruits[-4:])