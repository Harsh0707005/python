# Write a program to mine a log file and find out whether it contains "python"

with open("log.txt") as f:
    content = f.read()

if "python" in content.lower():    # As "python" may be present in uppercase like "Python" then it will not detect because this condition is case-sensitive.
    print("Yes, 'python' is present")
else:
    print("No, 'python' is not present")