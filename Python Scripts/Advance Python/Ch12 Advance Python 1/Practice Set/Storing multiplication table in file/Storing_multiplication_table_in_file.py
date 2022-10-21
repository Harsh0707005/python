# Store the multiplication table from list comprehensions to a file named "Tables.txt"

num = int(input("Enter a number for multiplication table:\n"))

table = [num*i for i in range(1, 11)]
print(table)

with open("Tables.txt", "a") as f: # append creates as well as appends the content to existing files 
    f.write(str(table)) # to store the content in a file we need to convert it to string.
    f.write("\n")

'''
If we used write (w) mode then everytime we would run this program it will empty the file and then write into it,
But, append just adds the content to file without deleting the older ones and if file is not present then it creates one.
'''