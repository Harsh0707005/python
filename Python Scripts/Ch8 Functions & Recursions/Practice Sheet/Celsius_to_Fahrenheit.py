# Write a python program to convert celsius to fahrenheit.

C = int(input("Enter Celsius:"))

def fahrenheit(C):
    return (C * (9/5)) +32
F = fahrenheit(C)

print(f"Farhenheit Temperature is {F}")