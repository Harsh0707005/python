# Write a Python Program to fill in a letter template given below with name and date:

#   Letter = ''' Dear <|NAME|>
#   Greetings from ABC coding house. I am happy to tell you about your selection.
#   You are Selected !
#   Have a Great day ahead!
#   Thanks and regards,
#   Harsh
#   <|DATE>'''

# Starting from here...

letter = '''Dear <|NAME>,
Greetings from ABC coding house. I am happy to tell you about your selection.
You are Selected !
Have a Great day ahead!
Thanks and regards,
Harsh

Date: <|DATE>
'''

name = input("Enter the recipient\'s name...\n")
date = input("Enter the date...\n")
letter = letter.replace("<|NAME>", name)
letter = letter.replace("<|DATE>", date)

print(letter)
