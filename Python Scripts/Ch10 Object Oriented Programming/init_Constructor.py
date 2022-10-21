# # __init__() constructor
'''
__init__() is a special method which runs as soon as the object is created.

__init__() method is also known as constructor.

It takes self-argument and can also take further arguments.

For Example:
'''

class Status:
    company = "Axis Bank"

    def __init__(self):
        print("The money is transferred successfully!")

Exchange = Status()

'''
Note:
There is no need to call __init__() method, it is called automatically when the class is initiated and object is created.
'''

print("****************")

# A detailed Example

class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is Created successfully!")
    
    def getDetails(self):
        print(f"The name of the Employee is {self.name}.")
        print(f"The salary of the Employee is {self.salary}.")
        print(f"The subunit of the Employee is {self.subunit}.")


harsh = Employee("Harsh", 100000, "YouTube")
harsh.getDetails()