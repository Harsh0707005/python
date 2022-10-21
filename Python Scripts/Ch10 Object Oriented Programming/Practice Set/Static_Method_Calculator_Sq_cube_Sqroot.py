# Add a static method to greet the user with "hello" and Write a class calculator capable of finding square, cube and the square root of a number.

class Calculator:
    @staticmethod
    def greet():
        print("****** Hello, Welcome to the best calculator of the world...! ******")
    
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The square of {self.number} is {self.number **2}")

    def squareRoot(self):
        print(f"The square root of {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number **3}")

Calculator.greet()

a = Calculator(int(input("Enter a number for Square, Square Root, Cube\n")))

a.square()
a.squareRoot()
a.cube()