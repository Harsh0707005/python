from numpy import swapaxes


story = "once upon a time there lived a young and vibrant person. He was very hard working and wanted to earn more. He chopped wood every day to earn for his food"

# String Functions

# # 1. len() function.
'''
It prints the number of characters in a string.
'''
print(len(story))

print("***************************")

# # 2. string.endswith("") function
'''
It prints either 'true' or 'false' on the basis whether the string end with the specified word/letter or not.
'''

# => It will print false as the string does not end with "day"
print(story.endswith("day"))
# => It will print true as the string ends with "food"
print(story.endswith("food"))
# => It will print true as the string ends with "od" letters.
print(story.endswith("od"))


'''
Note: If there is "." at the end of string then one needs to put "." also alongwith the ending word/character else it will print "false".
for ex. 
if story ends with "." then one code as print(story.endswith("food.")) else it will print false. 
'''

print("***************************")

# # 3. string.startswith("") function
'''
It prints either 'true' or 'false' on the basis whether the string starts with the specified word/letter or not.
'''

# => It will print true as the string does starts with "o"
print(story.startswith("o"))
# => It will print true as the string does starts with "once"
print(story.startswith("once"))
# => It will print false as the string does not starts with "upon"
print(story.startswith("upon"))

print("***************************")

# # 4. string.count("") function
'''
It counts the total number of occurrence of any word/character.
'''

print(story.count("a"))  # => counting number of "a's" in the string.
# => counting number of times "earn" occurs in the string.
print(story.count("earn"))

print("***************************")

# # 5. string.capitalize() function
'''
This function capitalizes the first character of a given string.
'''

print(story.capitalize())  # => capitalizing first character of 'story'.

print("***************************")

# # 6. string.find("word") function
'''
This function finds a word and returns the index of first occurence of first character of that word in the string.
If there is no word like the word to find then it will print -1.
'''

print(story.find("time"))

print("***************************")

# # 7. string.replace("old word","new word") function
'''
This function replaces the old word with the new word specified from the entire string.
'''

print(story.replace("vibrant", "sensitive"))
# OR:
'''
story = story.replace("vibrant", "sensitive") 
print(story)

Here, 'story' variable is assigned to the replaced word of original story variable (type of overwriting) 
'''

'''
Note: replace function replaces each and every old word with a new specified word.
'''

print("***************************")

# # 8. string.strip() function
'''
This function basicaly removes the extra spaces in a string if no argument passed, and removes the specified characters if passed as argument
For Example:
'''
Praise = "    Harsh is Awesome!    "
Praise2 = "__Harsh is Awesome!__"
print(Praise)
print(Praise.strip())
print(Praise2.strip("_"))

print("***************************")

# # 9. split() function
'''
This function splits the string into a list where each word is a list itemm.
For Exammple: 
'''
greet = "welcome to the jungle"
gr = greet.split()
print(gr)

print("***************************")

# # 10. .ljust(width) function
'''
This method returns a left aligned string
For Exammple: 
'''
print("Hello".ljust(10, '-'))  # '-' to identify the left alignment.

# # 11. .center(width) function
'''
This method returns a centered string of length width.
For Exammple: 
'''
print("Hello".center(10, '-'))  # '-' to identify the center alignment.

# # 12. .rjust(width) function
'''
This method returns a right aligned string of length width.
For Exammple: 
'''
print("Hello".rjust(10, '-'))  # '-' to identify the right alignment.

print("***************************")

# # 13. .index() function
'''
This function is used to get the starting index of the first occurrence of specified string in given string.
'''

print("Hello World World".index("World"))

print("***************************")

# # 14 .rindex() function
'''
This function is used to get the starting index of the last occurrence of specified string in given string.
'''

print("Hello World World".rindex("World"))

print("***************************")

# # 15. .upper() function
'''
This function converts the string to uppercase.
'''

print("hello".upper())

print("***************************")

# # 16. .isupper() function
'''
This function checks whether uppercase or not, return boolean value.
'''

print("HARSH".isupper())
print("Harsh".isupper())

print("***************************")

# # 17. .lower() function
'''
This function converts the string to lowercase.
'''

print("HELLO".lower())

print("***************************")

# # 18. .islower() function
'''
This function checks whether lowercase or not, return boolean value.
'''
print("harsh".islower())

print("Harsh".islower())

print("***************************")

# # 19. .swapcase() function
'''
It swaps the case of character.
'''

print("HaRsH".swapcase())

print("***************************")
