'''
In Simple words, this is used to just print the given string as it is and don't 
execute the escape characters, it can be 'r' or 'R'.
For Example:
'''

# # Without using raw string
s = "C:\project\name.py"  # here, \n will be treated as newline character
print(s)

print("***************************")

# # with raw string
s = r"C:\project\name.py"
print(s)
