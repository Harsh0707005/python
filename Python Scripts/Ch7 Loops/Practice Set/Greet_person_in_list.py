# Write a program to greet all the person names stored in a list l1 and which starts with 's'.
'''
l1 = ["Harry","Sohan","Sachin","Rahul"]
'''

l1 = ["Harry","Sohan","Sachin","Rahul"]

for item in l1:
    if item.startswith("S"):
        print("Hello,"+item)