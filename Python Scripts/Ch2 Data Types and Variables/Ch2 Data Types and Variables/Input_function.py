# Input() function

'''
This function allows the user to take input from the keyboard.
Note:- Input function only takes the input as a string even if a numberic value is entered ; if want as a integer, float etc. one needs to do typecasting.
'''

a = input("Enter your name: ")
print(a)
print(type(a))

b = input("Enter a number: ")
b = int(b) # Converting a string to integer.
print(b)
print(type(b))