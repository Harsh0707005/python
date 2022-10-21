# # Functions with arguments
'''
A function cam accept some values it can work with. We can put these values in parenthesis.
A function can also return values as below:
'''
def mySum(num1, num2):   # -> It can contain multiple arguments.
    return num1 + num2   # -> 'return' takes the instructions and returns back.


s = mySum(32, 6)
print(s)

def myProduct(num3, num4):
    pr = num3*num4
    return pr

p = myProduct(4, 10)
print(p) 

'''
Print can also be directly entered in 'function definition' as:

def myProduct(num3, num4):
    pr = num3*num4
    print(pr)
'''