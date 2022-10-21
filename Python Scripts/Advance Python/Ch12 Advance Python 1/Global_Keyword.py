# # Global Keyword
'''
There are two types of variables namely Global and Local variables.

Global Keyword is used to modify the variable outside of the current scope.
'''

a = 54  # global variable


def func1():
    a = 8  # local variable
    print(f"Printing fun1(): {a}")


def func2():
    global a
    print(f"Printing initial: {a}")
    a = 10
    print(f"Printing after modifying:{a}")


func1()
print(a)  # 'a' changed again to its global value after completion of fun1().

func2()

print(a)  # 'a' changed to 10 as we modified the global value of 'a' in func2() by using 'global' keyword.
