# # If__name__ == "__main__" in Python
'''
__name__ evaluates to the name of the module in Python from where the program is run.
If the module is being run directly from the command line, the __name__ is set to string "__main__".
Thus, this behaviour is used to check whether the module if run directly or imported to another file.
'''


def greet(name):
    print(f"Good Morning, {name}")

# print(__name__) # If this is executed from this file then it will print __main__ and if this file is imported and ran from other file then this will execute as the name of this file.

if __name__ == "__main__":  # if this is not written then when imnported this will also run.
    n = input("Enter your name:\n")
    greet(n)