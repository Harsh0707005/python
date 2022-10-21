# # @property decorators
'''
This decorator is used to make any function a property.
The method name with @property decorator is called getter method.
'''


class Employee:
    company = "Bharat Gas"
    salary = 5600
    salaryBonus = 500

    @property    # making a property
    def totalSalary(self):
        return self.salary + self.salaryBonus


e = Employee()
print(e.totalSalary)