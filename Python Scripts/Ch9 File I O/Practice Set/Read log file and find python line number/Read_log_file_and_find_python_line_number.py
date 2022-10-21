# Write a program to mine a log file and find out the line number in which "python" is present.

content = True
i = 1
with open("log2.txt") as f:  
        while content:
            
            content = f.readline()
            
            if "python" in content.lower():
                print(content)
                print(f"Yes, 'python' is present in line number {i}")
            # else:
            #     print("No, 'python' is not present")
            i += 1