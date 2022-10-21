# # Exception Handling in Python
'''
There are many built-in exceptions which are raised in Python when something goes wrong.
Excepions in Python can be handled using a 'try' statement. The code that handles the exception is written in the 'except' clause.
Example of syntax:

try:
    #code
except exception as e:
    print(e)

When the exception is handled, the code flow continues without program interruption.

While using the the try-except statements the whole code is not broke if an exception occurs, it just executes the exception code and moves on.

For Example:
'''

while (True):
    print("Press 'q' to quit!")
    a = input("Enter a number:\n")
    if a == "q":
        break

    try:   # It will execute untill when the statement unsatisfies and from that point will execute the except statement.
        print("Trying...")  # this will print and then if next code becomes unsatisfactory will start executing except 'statement'
        a = int(a)
        if a > 6:
            print("You entered a number that is greater than 6.")
        else:
            print("You entered a number that is less than 6.")
    except Exception as e:   # It will execute below code instead of an returning an error.
        print(f"Your input resulted in error - {e}")

'''
We can also specify the exceptions to catch like below:

try:
    #code
except ZeroDivisionError:
    #code
except TypeError:
    #code
except:  # All the other Exceptions are handled.
    #code
'''

try:
    a = int(input("Enter a Number: "))
    c = 1/a
    print(c)
except ValueError as e:
    print("Enter a valid value")
except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero.")

print("Thanks for using the code!")