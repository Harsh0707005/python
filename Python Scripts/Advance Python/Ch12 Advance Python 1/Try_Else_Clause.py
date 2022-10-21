# # Try-Except-Else Statements
'''
Used to exceute a piece of code if 'try' is successful.

Syntax:

try:
    # code
except:
    # code
else:   # Executes if 'try' is successful.
    # code
For Example:
'''

try:
    i = int(input("Enter a number: "))
    c = 2 * i
    print(c)
except Exception as e:
    print(e)
else:
    print("We were Successful in running 'try', so this code executed...")