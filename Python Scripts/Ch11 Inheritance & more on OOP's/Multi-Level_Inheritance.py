# # Multi-level Inheritance
'''
When a child class becomes a parent for another child class, it is called Multi-level Inheritance.

                    Parent
                      ||
                      \/
                    Child 1
                      ||
                      \/
                    Child 2


For Example:
'''

class Person:
    country = "India"

    def takeBreath(self):
        print("I am Breathing...")

class Employee(Person):  # Derieved class from parent class(Person)

    company = "Honda"

    def getsalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so i am luckily breating...")

class Programmer(Employee): # Derieving class from derieved class(Employee)
    company = "Fiverr"

    def getSalary(self):
        print("No salary for programmers.")

    def takeBreath(self):
        print("I am a Programmer so i am breating")


p = Person()
e = Employee()
pr = Programmer()

p.takeBreath()
e.takeBreath()
pr.takeBreath() # This will overwrrite the takeBreath() method from the recent parent.

# print(p.company) # will throw an error as company is present in person class.

print(e.company)
print(pr.company)
print(pr.country) # will return india as neither programmer nor employee class has its own country.