# # Try-Except-Finally Clauses
'''
Python offers a 'finally' clause which ensures execution of a piece of code irrespective of the exception.

Syntax:

try:
    # code
except:
    # code
finally:   # Executes redardless of 'except'.
    # code
For Example:
'''

try:
    i = int(input("Enter a number: "))
    c = 2 * i
    print(c)
except Exception as e:
    print(e)
finally:  # will execute regardless of error even if except quits the whole program by <quit()>.
    print("We are done")

'''
If we don't do 'finally' clause and instead write 'print' then if 'except' condition quits the program the print statement will not execute.
For Example:
'''
try:
    a = int(input("Enter a number: ")) 
    if a ==9:
        print("Yes")
    else:
        print("No")
except Exception as e:
    print(e)
    quit()
# finally:  
#     print("This is a 'finally' clause and executed regardless of 'except' statement.")

print("Executed") # if except condition met executes then will quit the program and not run this statement code, but if finally condition wrote then it will run regardless of exception or quitting of program.
