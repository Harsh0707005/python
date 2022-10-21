# # Operator Overloading
'''
Operators in python can be overloaded using dunder methods.

These methods are called when a given operator is used on the objects.

Operators in python can be overloaded using the following methods:

p1 + p2 -> p1.__add__(p2)

p1 – p2 -> p1.__sub__(p2)

p1 * p2 -> p1.__mul__(p2)

p1 / p2 -> p1.__truediv__(p2)

p1 // p2 -> p1.__floordiv__(p2)

Other dunder/magic methods in Python

__str__() -> used  to set what gets displayed upon calling str(obj)

__len__() -> used to set what gets displayed upon calling .__len__() or len(obj)
'''

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Let's Add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Let's Multiply")
        return self.num * num2.num


n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
print(sum)
mul = n1 * n2
print(mul)