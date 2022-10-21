# # Raising Exceptions
'''
We can also raise exceptions in Python by using a 'raise' keyword.
For Example:
'''

def Increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("It is a Value Error, enter a valid value!")

a = Increment(5)
print(a)
b = Increment("df9")
print(b)