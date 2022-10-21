# 'Continue'    
'''
It is used to stop the current iteration of the loop and continue with the next one. In other words, it instructs python to "skip this iteration".
For Example:
'''
for i in range(10):
    if i == 4:
        continue    # If i is 4, skip the iteration.
    print(i)