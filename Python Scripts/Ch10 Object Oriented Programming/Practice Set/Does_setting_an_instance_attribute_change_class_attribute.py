# Create a class with a class attribute 'a'; create an object from it and set 'a' directly using object. Does this change the class attribute?

class Sample:
    a = "Harsh"

obj = Sample()

obj.a = "Vicky"

print(obj.a)
print(Sample.a)

'''
Hence it doesn't change the class attribute instead it creates a new instance attribute.
'''

# To change a class attribute

# Sample.a = "Harry"
# print(Sample.a)