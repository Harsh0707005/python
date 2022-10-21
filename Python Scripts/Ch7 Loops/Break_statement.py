# # Break Statement
'''
"Break" is used to come out of the loop when encountered. 
It instructs the program to- 'Exit' the loop now.
For Example:
'''
for i in range(10):
    print(i)
    if i == 5:
        break    # The loop will break once i becomes 5 (i=5).
else:
    print("Done")

# # Important question
'''
Q. Why do we use else statement in loops as even though we can use print function after the loop like:
l = [1, 7, 8]
for item in l:
    print(item)

print("Done")

A. If we use print function it will print the elements in any condition but if we use else function then it will only execute once the 'for' loop is completely executed and if 'for' loop is broken by using 'break' then else statement will not execute.(like done above.)
'''