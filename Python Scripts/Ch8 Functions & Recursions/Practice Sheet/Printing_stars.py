# Write a python function to print first 'n' lines of following pattern:
'''
***
**  
*
(for n = 3)
'''
n = 3

for i in range(n):
    print("*"* (n-i))