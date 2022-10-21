# Write a python function which converts inches into centimetres.

inches = int(input("Enter length in inches:\n"))

def Cm(inches):
    return inches * 2.54

print(f"The length in centimetres is {Cm(inches)}")