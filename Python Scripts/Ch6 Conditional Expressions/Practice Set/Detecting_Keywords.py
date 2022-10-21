# A spam comment is defined as a text containing following keywords:
# "make a lot of money", "buy now", "subscribe this", "click this" Write a program to detect this spams.

text = input("Enter the text:\n")

if "make a lot of money" or "Buy Now" or "subscribe this" or "click this" in text:
    print("Your text contains spam keywords!")
else:
    pass

# OR

text = input("Enter the text:\n")

spam = False

if "make a lot of money" in text:
    spam = True
elif "Buy Now" in text:
    spam = True
elif "subscribe this" in text:
    spam = True
elif "click this" in text:
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam!")
else:
    print("This text is not spam!")