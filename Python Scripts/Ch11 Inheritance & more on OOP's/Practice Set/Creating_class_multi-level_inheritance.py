# Create a class pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog.


class Animals:
    animalType = "Mammals"

class Pets(Animals):
    petColor = "White"

class Dog:

    @staticmethod  # as bark method is not using any class or instance attribute
    def bark():
        print("Bow....Bow...!")

d = Dog()
d.bark()