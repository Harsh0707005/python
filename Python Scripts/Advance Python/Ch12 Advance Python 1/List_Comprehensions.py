# # List Comprehensions
'''
List Comprehensions is an elegant way to create a list based on existing lists.
'''

a = [15, 98, 203, 2, 59, 102, 83, 78, 123, 49]
# for even numbers; % is used for remainder here if remainder = 0 then append.
b = [i for i in a if i % 2 == 0]

print(b)

'''
It can also be written as:
'''
c = []

for item in a:
    if item > 85:
        c.append(item)
print(c)

'''
The one at first is basically a  shortcut to save time.
'''

'''
We cann also use these for sets, dictionary like set comprehensions or dictionary comprehensions.
'''
