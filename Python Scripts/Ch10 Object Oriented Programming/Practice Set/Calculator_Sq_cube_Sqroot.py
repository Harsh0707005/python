# Write a class calculator capable of finding square, square root and cube of a given number. 


class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The square of {self.number} is {self.number **2}")

    def squareRoot(self):
        print(f"The square root of {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number **3}")



a = Calculator(int(input("Enter a number for Square, Square Root, Cuben\n")))

a.square()
a.squareRoot()
a.cube()