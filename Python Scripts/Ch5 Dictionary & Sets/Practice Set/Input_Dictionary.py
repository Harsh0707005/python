# Create an Empty Dictionary. Allow 4 Friends to enter their favourite language as values and use keys as their names. Assume the names are unique.

FavLang = {}

a = input("Enter your Favourite language Ankit:\n")
b = input("Enter your Favourite language Shubham:\n")
c = input("Enter your Favourite language Ankush:\n")
d = input("Enter your Favourite language Preet:\n")

updateDict = {
    "Ankit" : a,
    "Shubham" : b,
    "Ankush" : c,
    "Preet" : d
}

FavLang.update(updateDict)
print(FavLang)

# OR

favLang = {}
a = input("Enter your Favourite language Ankit:\n")
b = input("Enter your Favourite language Shubham:\n")
c = input("Enter your Favourite language Ankush:\n")
d = input("Enter your Favourite language Preet:\n")

favLang["Ankit"] = a
favLang["Shubham"] = b
favLang["Ankush"] = c
favLang["Preet"] = d

print(favLang)