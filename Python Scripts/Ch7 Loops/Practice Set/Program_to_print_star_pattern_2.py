# Write a program to print the following star pattern:
'''
   *
  ***
 *****
for n = 3
'''
n = 3

for i in range(3):
    print(" " * (n-i-1), end="")  # if not used 'end' then each print statement will start from new line.
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))