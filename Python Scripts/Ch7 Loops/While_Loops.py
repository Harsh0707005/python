# # While loop
'''
In 'while' loops, the condition is checked first. If it evaluates to true, the boy of the loop is executed, otherwise not.
If the loop is executed, the process (condition check & execution) is continued until the condition becomes false.

Syntax:
While (condition):
    # Body of loop

This block continues until the condition is true.
 
For Example:
'''

i = 0

'''
while i<10:
    print(i,"is less than 10")
Here, the loop will be executed infinite times as i<10
To avoid it:
'''
while i<10:
    print(str(i), "is less than 10")
    i = i+1


'''
Note:
If the conition never becomes false the loop keeps getting executed.
'''

# # 'while' loop with else
'''
The else block is executed when the looping condition becomes false. In other words, when the loop terminates.
'''

i = 0
while(i < 2):
    print("i is less than 2")
    i += 1
else:
    print("The condition is False.")


# # Quick Quiz
'''
Write a program to print the contents of a list using 'while' loop.
'''

mylist = ["Apple", "Banana", "Grapes", "Orange", "Watermelon"]

a = 0

while a <len(mylist):
    print(mylist[a])
    a = a+1