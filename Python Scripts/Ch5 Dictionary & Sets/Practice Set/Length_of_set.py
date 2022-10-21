# What will be the length of the following set:
'''
s = set()
s.add(20)
s.add(20.0)
s.add("20")
'''

s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))

'''
Here, as 20 is same as 20.0 so python will interpret it as one value hence, length of this set is 2.
'''