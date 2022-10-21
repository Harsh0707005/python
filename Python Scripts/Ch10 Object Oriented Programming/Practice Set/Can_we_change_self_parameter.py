# Can we change the 'self' parameter inside a class to something else (say 'harsh'). Try changing 'self' to 'slf' or 'harsh' and see the effects.

name = input("Please enter your name...\n")
class Greet: 
    def greet(harsh):
        print(f"Good Morning, {name}.")

user = Greet()
user.greet()

'''
Hence, yes we can replace 'self' parameter with something else, but generally we do not do that as this may confuse the programmers.
'''