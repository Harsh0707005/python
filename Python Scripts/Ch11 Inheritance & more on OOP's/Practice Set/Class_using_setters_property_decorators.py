# Create a class Employee and add salary and increment properties to it.  Write a method SalaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    company = "Google"
    salary = 1000
    increment = 1.5   # 1.5 times original salary

    # salaryAfterIncrement = Salary * Increment

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):  # sai = salaryAfterIncrement
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)  # Increment value before setter
e.salaryAfterIncrement = 2000
print(e.increment)  # Increment value after setter