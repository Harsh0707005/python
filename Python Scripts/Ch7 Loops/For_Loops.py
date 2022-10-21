# # 'For' Loop
'''
A 'for' loop is used to iterate through a sequence like lists, tuple or string[iterables -> These can be traversed one by one easily].

For Example:
'''

Fruits = ["Apple", "Banana", "Grapes", "Orange", "Watermelon"]

for item in Fruits:
    print(item)

'''
'For' Loops are sometimes comparatively easy and short unlike 'while' loops.
'''

# # 'Range' function
'''
The range function in python is used to generate a sequence of numbers.
Its default value is 0.
Syntax:
for i in range(n):
    # Body of loop

Here it will execute till (n-1) value like if n is 8 then it will execute till 7.

We can also specify the start, stop and step-size as follows:
range(start,stop,step-size) 
# Step-size is usually not used with range().
Default value of step-size is 1.
For Example:
'''
for i in range(1,8,2):
    print(i)

print("'For' loop with else ")

# # 'For' loop with else
'''
An optional 'else' can be used with a 'for' loop if the code is to be executed when the loop exhausts.
The 'else' statement is executed once the 'for' loop is executed completely.
For Example:
'''
l = [1, 7, 8]
for item in l:
    print(item)
else:
    print("Done")