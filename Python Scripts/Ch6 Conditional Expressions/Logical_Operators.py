# # Logical Operators
'''
In python logical operators operate on conditional statements.
Example:
and   => True if both operands are true else false  
or   => True if atleast one operand is true true else false  
not   => Inverts true to false & false to true.
'''

age = int(input("Enter your age:\n"))

# 'and' statement

if age > 34 and age < 45:
    print("You can work with us!")
else:
    print ("No")


# 'or' statement

if age == 18 or age > 18:
    print("You can work with us!")
else:
    print ("No")


# 'not' statement

if not age<18:
    print("You can work with us!")
else:
    print ("No")