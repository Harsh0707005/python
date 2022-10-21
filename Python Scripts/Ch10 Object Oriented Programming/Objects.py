# # Objects

'''
An object is an instantiation of a class. When class is defined, a template(info) is defined. Memory is allocated only after object instantiation.

Objects of a given class can invoke the methods available to it without revealing the implementation details to the user.     # Abstraction & Encapsulation!
'''

# What is abstraction?
'''
In simple word, hidding the implementation details from the user.
OR not bothering the user as he/she doesn't want to know about how a class is made or other details.
'''

# What is Encapsulation?
'''
It simply means wrapping entities in a class like putting the entities's data in a capsule.
'''

# # Modelling a problem in OOPs
'''
We identify the following in our problem

Noun -> Class -> Example: Employee

Adjective -> Attributes -> Example: name,age,salary

Verbs -> Methods -> Example: getSalary(), increment()
'''

# # Class Attributes
'''
An attribute that belongs to a class rather than a object.
For Example
'''

class Employee:
	company = "Google" 	#Specific to each class
harsh = Employee()	#Object instantiation
harsh.company
Employee.company = "YouTube"	#changing class attribute

# # Instance Attribute
'''
An attribute that belongs to the Instance (object).

Assuming the class from the previous example:

harry.name = “Harry”
harry.salary = “30K”	#Adding instance attributes
'''
'''
Note: Instance attributes take preference over class attributes during assignment and retrieval.
Complete example and explanation in Instance_class_attributes.py
'''