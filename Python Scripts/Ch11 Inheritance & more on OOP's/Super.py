# # Super Class
'''
Super method is used to access the methods of a super class in the derived class.

Like:
super().__init__()  # Calls constructor of the base class

For Example
'''

class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person...")

    def takeBreath(self):
        print("I am Breathing...")

class Employee(Person):  # Derieved class from parent class(Person)

    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...")

    def getsalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath() # calls takeBreath() function of the parent or super class
        print("I am an Employee so i am luckily breating...")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...")

    def takeBreath(self):
        super().takeBreath() # calls takeBreath() function of the parent or super class
        print("I am a Programmer so i am breating")


p = Person()
e = Employee()
pr = Programmer()

p.takeBreath()
print("******************")
e.takeBreath()
print("******************")
pr.takeBreath()
print("******************")

'''
In the last part it came "i am breating" because as we called super class in programmer class and then again we called super class in employee class so all the three statement were printed.
There are multiple init as all the classes are called.
If called only last class then:
'''

pro = Programmer()