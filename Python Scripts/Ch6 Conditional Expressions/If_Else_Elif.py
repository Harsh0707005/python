'''
If, Else and Elif are multuiway decision taken by our program due to certain conditions in our code.
Syntax:

if (Condition1):
    print("Yes")         => If condition 1 is true.
Elif (Condition2):       
    print("No")          => If condition 1 is true.
Else:
    print("Maybe")       => otherwise

'''

'''
Elif means 'else if'.
An if statement can be chained together with a lot of these elif statements followed by else statement.

A general If-Elif-Else ladder:

if (condition 1):
    # code
elif (conditon 2):
    # code
else (condition 3):
    # code

Note:
This ladder stops once a condition in an 'if' or 'elif' is not met.
There can be many number of 'elif' statement.
Last condition 'else' is only executed if 'if' or 'elif' fails.
Else is 'optional'.
'''

# Exapmle:
# 1. If-Elif-Else Ladder in Python

a = 45

if (a<3):
    print("This number is greater than 3")
elif (a>10):
    print("This number is greater than 10")
else:
    print("This value is neither greater than 3 or 10")


# # Quick Quiz

# Write a program to print yes when the age entered by the user is greater than or equal to 18.

age = int(input("Enter your age:\n"))   

if age>=18:
    print("Yes")
else:
    print("No")

