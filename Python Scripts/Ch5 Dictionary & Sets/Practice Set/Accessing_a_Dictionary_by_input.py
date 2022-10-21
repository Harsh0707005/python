# Write a program to create a dictionary of Hindi Words with values as their English Translation. Provide user with an option to look it up.

myDict = {
    "Pankha" : "Fan",
    "Vastu" : "Item", 
    "Dabba" : "Box"
}

a = input("Enter the Hindi Word:\n")

print("The translation of your Hindi Word is", myDict[a])

# It can also be done as :

myDict = {
    "Pankha" : "Fan",
    "Vastu" : "Item", 
    "Dabba" : "Box"
}

a = input("Enter the Hindi Word:\n")

# print("The translation of your Hindi Word is", myDict.get(a))

# This code will not throw error if the word is not present in the dictionary.

if myDict.get(a) == None :
    print("Sorry the word is not present in our dictionary...")
else:
    print("The translation of your Hindi Word is", myDict.get(a))