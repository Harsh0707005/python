# Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not present, a message without exiting the program must be printed prompting the same.

def readFile(filename):
    try:
        with open(filename, 'r') as f:
            print((f.read()))
    except:
        print(f"File named {filename} is not found ")


readFile("1.txt")
readFile("2.txt")
readFile("3.txt")
