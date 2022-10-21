# Create a class programmer and for storing information of a few programmers working at microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(
            f"The name of the {self.company} Programmer is {self.name} is working on {self.product}.")


harsh = Programmer("Harsh", "Skype")
harry = Programmer("Harry", "GitHub")

harsh.getInfo()
harry   .getInfo()