# Write a class Train which has methods to book a ticket, get status(no of seats), and get fare information of trains running under Indian Railways.

class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatusInfo(self):
        print(f"The name of the train is {self.name}.")
        print(f"Number of seats available are {self.seats}.")
        print("************")
    def getFareInfo(self):
        print(f"The fare of the ticket is Rs. {self.fare}")
        print("************")
    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked and your seat number is {self.seats}.")
            self.seats = self.seats - 1
            print("************")
        else:
            print("Sorry! The train is full.")
            print("************")

intercity = Train("Intercity Express: 14015", 1, 90)
intercity.getStatusInfo()
intercity.getFareInfo()
intercity.bookTicket()
intercity.getStatusInfo()
print("************")
intercity.bookTicket()
intercity.getStatusInfo()