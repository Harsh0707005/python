# Write a program to rename a file as "renamed_by_python.txt"

'''
Basically, File I/O doesn't have any specific function to rename a file but we can do one thing:
We can copy the content of the file to a new file and delete the original file.
'''

import os   # We can delete the file using os module

filename = "sample.txt"
with open(filename) as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)

os.remove(filename)  # Deletes the file