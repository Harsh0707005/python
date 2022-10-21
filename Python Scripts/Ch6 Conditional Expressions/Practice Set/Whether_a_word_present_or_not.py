# Write a program to find out whether a given post is talking about "Money" or not.

post = "It is the most important and essential tool of modern economic life. One cannot imagine modern economic life without money. Barter economies or self-sufficient economies are the thing of past and historical significance. Money is the foundation stone of modern economic life."

if "money" in post.lower():
    print("Yes it is present in the post")
else:
    print("No it is not present")

'''
Here, it is done so because if in the post Money is written as MoNeY then python would not identify it so by post.lower() whole string is converted to lowercase and python is asked to find if money is present or not.
It can also be done as:
'''

if "MONEY" in post.upper():
     print("Yes it is present in the post")
else:
    print("No it is not present")