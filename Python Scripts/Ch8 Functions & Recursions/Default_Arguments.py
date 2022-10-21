# Default Parameter Value (arguments)
'''
We can have a value as default argument in a function.
For Example:
'''
# def greet(name):
#     print(f"Hello, {name}")

# greet("Harsh")
'''
Here, If we specify (name = "Stranger") in the line of 'def', this value would be used when no argument is passed.
'''

def greet(name = "Stranger"):
    print(f"Hello, {name}")

greet("Harsh")
greet()