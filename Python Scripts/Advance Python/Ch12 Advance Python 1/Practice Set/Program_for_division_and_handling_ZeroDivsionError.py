# Write a program to display a/b where a and b are integers. If b = 0, display 'infinite' by handling ZeroDivsionError.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

try:
    print(f"The division of your numbers (a/b) is {num1/num2}")
except:
    print("The division of your numbers is infinite as you entered 0 to divide a number!")
