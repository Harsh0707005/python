# # Enumerate function
'''
The 'enumerate' function adds counter to an iterable and returns it
'''

list = [54, 93, 6.2, False, "Harsh"]

for index, item in enumerate(list):
    print(index, "--", item)  # prints item along with index number.

'''
If we do not use this then we have to go with:

index = 0
for item in list:
    print(index, item)
    index += 1

But using these looks good and saves a lot of time.
'''

'''
Note:
It is not mandatory to give the name of counter as 'index' we can specify any of our choice, but the thing to be kept in mind is the variable we used instead of 'index' needs to be placed in the same order as :

for <var>, item in enumerate():
    #code
'''
