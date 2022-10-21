# # Opening a file
'''
Python has an open() function for opening files.
It takes 2 parameters: filename and mode
Example:
open("this.txt", "r") =>'r' is the mode of opening(read mode) 
'this.txt' is the name of file.
'''

# # Example

f = open("sample.txt", "r")  # => Open a file
data = f.read()   # Read its contents
print(data)   # Print its contents
f.close()   # Close the file


'''
A file onnce open should be closed by using .close() function.
'''

'''
Note:
If no parameter is specified for mode then it will take 'r' by-default.
'''

# Reading only a certain number of characters
'''
We can also read only a certain number of charcters as follows:
'''

r = open("sample.txt", "r")
text = r.read(5)
print(text)
r.close()

# # Readline Function
'''
This function is used to read one full line at a time.
'''

a = open("sample.txt", "r")

# Read the first line

txt = a.readline()
print(txt)
r.close()

# Read the second line
txt = a.readline()
print(txt)
r.close()

# Read the third line
txt = a.readline()
print(txt)
r.close()

# And so on...
