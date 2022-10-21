import math  # math is a built-in module to perform operations.

# Defining operations:


def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def exp(a, b):
    return a ** b


def sqrt(a):
    return math.sqrt(a)


def cubert(a):
    return a ** (1/3)


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def tan(a):
    return math.tan(a)


print("******** Welcome to the best calculator ********")

print("Press :")
print("1 to add (a, b). ")
print("2 to subtract (a, b). ")
print("3 to multiply (a, b). ")
print("4 to divide (a, b). ")
print("5 for exponential operation (a, exp(b)). ")
print("6 for square root (a). ")
print("7 for cube root (a). ")
print("8 for sin function (a). ")
print("9 for cos function (a). ")
print("10 for tan function (a). ")


def Process():

    Response = int(input("Enter your choice...\n"))

    if Response == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = sum(a, b)
        print(result)
    elif Response == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = sub(a, b)
        print(result)
    elif Response == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = mul(a, b)
        print(result)
    elif Response == 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = div(a, b)
        print(result)
    elif Response == 5:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = exp(a, b)
        print(result)
    elif Response == 6:
        a = int(input("Enter a number for square root: "))
        result = sqrt(a)
        print(result)
    elif Response == 7:
        a = int(input("Enter a number for square root: "))
        result = cubert(a)
        print(result)
    elif Response == 8:
        a = int(input("Enter a number for square root: "))
        result = sin(a)
        print(result)
    elif Response == 9:
        a = int(input("Enter a number for square root: "))
        result = cos(a)
        print(result)
    elif Response == 10:
        a = int(input("Enter a number for square root: "))
        result = tan(a)
        print(result)
    else:
        print("Please enter a Valid Response: ")
        Process()

    def Repeat():
        Again = input("Do you want to continue(y) or quit(q): ")

        if Again == 'y':
            Process()
        elif Again == 'q':
            quit()
        else:
            print("Please press a valid Response!!!")
            Repeat()
    Repeat()


Process()
