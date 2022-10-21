# # Self Parameter

'''
'self' refers to the instance of the class.

It is automatically passed with a function call from an object.

harsh.getSalary()

here, self is harsh and above line of code is equivalent to Employee.getSalary(harsh)

This function getsalary is defined as:
'''

class Employee:
    company = "Google"
    def getsalary(self):
        print(f"Salary of this employee working in {self.company} is {self.salary}")

harsh = Employee()
harsh.salary = 100000
harsh.getsalary() # same as Employee.getSalary(harsh)