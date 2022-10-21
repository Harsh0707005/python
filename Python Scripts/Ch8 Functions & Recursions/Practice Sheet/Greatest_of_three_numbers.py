num1 = int(input("Enter First Number:\n"))
num2 = int(input("Enter Second Number:\n"))
num3 = int(input("Enter Third Number:\n"))

def greatest_num(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3

g = greatest_num(num1, num2, num3)
print(f"{g} is the greatest of the three numbers.")