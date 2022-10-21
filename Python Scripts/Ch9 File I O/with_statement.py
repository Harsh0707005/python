# # 'With' statement
'''
The best way to open and close the file automatically is the 'with' statement.
'''

with open("sample.txt") as f:
    a = f.read()
    # There is no need to close file in 'with' statement, it is closed automatically.
print(a)