# # Static Method
'''
Sometimes we need a function that doesn’t use the self-parameter. We can define a static method like this:
'''

class Employee():
    @staticmethod    # decorator to mark greet() as a static method
    def greet(signature):     # No need of writing 'self'
        print(f"Hello User!\n{signature}")

harsh = Employee()
harsh.greet("~Python")