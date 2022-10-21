# To change a class attribute

'''
For example:
class Employee:
    salary = 100

    def changeSalary(self, sal):
        self.salary = sal

Here, a new instance attribute will be created instead changing class attribute salary if we do employee.salary, it will print 100 only.

To change a class attribute, there are two methods:

1. 
class Employee:
    salary = 100

    def changeSalary(self, sal):
        self.__class__.salary = sal

Now here the class attribute(salary) will be changed.
These methods in which underscores are added as prefix and suffix are called dunder methods/magic methods. For Example: __class__, __init__

Note: 
Two fullstops should be added while using these method.

2. Class Methods
A class method is a method which is bound to the class and not the object of the class.

@classmethod decorator is used to create a class method.

Syntax:

    @classmethods
    def(cls,p1,p2...):      # p1, p2 are arguments and more can be added as well.
        ....
            
'''

class Employee:
    company = "Camel"
    salary = 100

    @classmethod     # This decorator is must to use class method
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)     # Salary is changed to 455.
print(e.salary)  