class Vehicle:
    def start(self):
        print("vehicle starting")

class car(Vehicle):
    pass

class Bike(Vehicle):
    pass

c = car()
c.start()

b = Bike()
b.start()