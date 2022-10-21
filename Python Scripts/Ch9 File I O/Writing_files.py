# # Writing files in Python

'''
In order to write a file, we first open it in write or append mode after which, we use python's .write() method.
'''

f = open("another.txt", "w")
f.write("Please write to this file.") # can be called muyltiple times.
f.close()

'''
Note:
If a file is not present then it will create new and if it is present it will overwrite it and delete the existing contents.
'''
