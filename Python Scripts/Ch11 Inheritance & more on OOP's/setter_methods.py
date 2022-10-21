# # @setter method
'''
We can define a function + @name.setter decorator like below:
'''

class Employee:
    company = "Bharat Gas"
    salary = 5600
    salaryBonus = 500

    @property    # making a property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter  #Creating a setter method
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary
    
e = Employee()
print(f"The total salary is Rs. {e.totalSalary}")
print(f"Initial Salary Bonus is Rs. {e.salaryBonus}")

e.totalSalary = 5800  # Defining total Salary.

print(e.salary)

print(f"The new Salary Bonus is Rs. {e.salaryBonus}") # printing salary bonus after manipulating.