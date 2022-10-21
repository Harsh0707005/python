# Write a program to print the third, fifth & seventh element from a list using enumerate function

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, item in enumerate(l):
    if index == 2:
        print(f"The third element in the list is {item}.")
    elif index == 4:
        print(f"The fifth element in the list is {item}.")
    elif index == 6:
        print(f"The seventh element in the list is {item}.")
    else:
        pass

'''
It can also be done as :
if index == 2 or index == 4 or index == 6:
    print(f"{index} -- {item})
'''