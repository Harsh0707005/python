# # Appending files
'''
This method is used to add contents to existing files.
'''

f = open("another.txt", "a")
f.write("Appending to this file.") # -> It adds this string to the end of the specified file
f.close()

'''
The number of times this is executed it will append the the string to the file.
'''