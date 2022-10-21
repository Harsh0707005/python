# Write a program to find whether a given number is prime or not.

num = int(input("Enter a number to check if prime:\n"))

prime = True

for i in range(2,num):      # As any number will definitely be divisible by 1 hence starting with 2.
    if num%i == 0:  # if any number divides the entered number completely leaving remainder then prime becomes false.
        prime = False
        break
if prime:
    print("This number is a prime number!")
else:
    print("This number is not a prime number!")