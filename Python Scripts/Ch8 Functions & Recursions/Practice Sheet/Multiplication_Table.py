# Write a python function to print multiplication table of a given number.

num = int(input("Enter a number for multiplication table:\n"))

def multiplication_table(num):
    print(f"{num} x 1 = {num*1}")
    print(f"{num} x 1 = {num*2}")
    print(f"{num} x 1 = {num*3}")
    print(f"{num} x 1 = {num*4}")
    print(f"{num} x 1 = {num*5}")
    print(f"{num} x 1 = {num*6}")
    print(f"{num} x 1 = {num*7}")
    print(f"{num} x 1 = {num*8}")
    print(f"{num} x 1 = {num*9}")
    print(f"{num} x 1 = {num*10}")

multiplication_table(num)