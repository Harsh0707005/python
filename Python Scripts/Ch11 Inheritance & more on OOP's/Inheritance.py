# # Inheritance
'''
Inheritance is a way of creating a new class from an existing class.
For Example:
'''


class Employee:  # Base class or Parent Class
    company = "Google"

    def showDetails(self):
        print(f"This is an Employee at {self.company}.")


class Programmer(Employee):  # Derived Class or Child Class
    # To Create a Derieved class name of Parent Class or Base class should be written in parenthesis.

    language = "Python"

    def getLanguage(self):
        print(f"The language is {self.language}.")


e = Employee()
e.showDetails()

print("***************")

p = Programmer()

# p.showDetails() # The attribute of Employee class also works well in Programmer class as it is an inherited class.

p.getLanguage()

# The attribute of Employee class also works well in Programmer class as it is an inherited class.
print(p.company)

print("***************")

'''
We can use the methods and attributes of Employee in Programmer object.

Also, we can overwrite or add new attributes and methods in the Programmer class, by adding the new content in the inherited class.

For Exmaple:

If we add:
def showDetails(self):
        print(f"This is a Programmer.")

in Programmer class then when it will print the new content not the earlier one.(Overwritten)
'''

# # Types of Inheritance:
'''
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
'''