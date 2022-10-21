'''
Instance attributes take preference over class attributes during assignment and retrieval.
'''
# For Example:

class Employee:
    company = "Google"
    salary = 100

# Object Instantiation
harsh = Employee()
harry = Employee()
harish = Employee()

# Creating instance attributes for both objects.
harsh.salary = 500
harry.salary = 300

print(harsh.salary)
print(harry.salary)
print(harish.salary)  # Here as salary of harisgh is not defined so it will take base salary in class.

# Below code will throw an error as it is not present in instance/class.    
# print(harish.address)

'''
When a salary is defined for someone, a new instance is created rather changing the original in the class.
'''

'''
If the instance attribute were not created then would take 100 as salary for each.
Instance attributes take preference over class attributes during assignment and retrieval.
'''