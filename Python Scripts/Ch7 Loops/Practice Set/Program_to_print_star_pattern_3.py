# Write a program to print the following star pattern:
'''
***
* *
***
for n = 3
'''

n = 3

for i in range(3):
    print("*" * (n-i))
    print("*" + " " + "*")
    print("*" * (i))

# Not Done