# # Multiple Inheritance
'''
Multiple Inheritance occurs when the child class inherits from more than one parent class.

                     Parent 1               Parent 2
                        |______________________|
                                  ||
                                  \/
                                 Child

For Example:
'''

class Employee:
    company = "VISA"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0
    def upgradeLevel(self):   # Upgrading level
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Harsh"

p = Programmer()
print(p.level)
p.upgradeLevel()  # Calling upgradeLevel()
print(p.level)
print(p.company) # Here , VISA will be printed as while defining class Programmer we specified Employee class first and then Freelancer.
