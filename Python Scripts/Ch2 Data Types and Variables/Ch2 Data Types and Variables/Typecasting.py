# Type Casting
a = "3534"
a = int(a) #Convert 'a' to integer (if possible).
print(type(a))
print(a + 5)

'''
Type casting is basically conversion of one data type to another using some specific functions or expression.
A number can be converted into a string and vice-versa (if possible).

There are many function to convert one data type into another:
For ex. 
1. str(31) => "31" =>(integer to string conversion)

Here "31" is a string literal and 31 is a numeric literal.

2. int("32") => 32 =>(string to integer conversion)
3. float(33) => 33.0 =>(integer to float decimal conversion).
... and so on

Note:- a string like "348fg4" cannot be converted to numeric literal. Hence it can only be converted if possible.
'''