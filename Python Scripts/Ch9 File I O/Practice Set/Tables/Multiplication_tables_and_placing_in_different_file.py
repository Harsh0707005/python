# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 year old.

for i in range(2, 21):
    with open(f"tables/Multiplication table of {i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}")
            if j!=10:  # It is used to not print a new line after ending the table.
                f.write("\n")