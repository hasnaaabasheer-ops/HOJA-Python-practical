class Car:
    def start(self):
        return "Car starting...."
    
class Bike:
    def start(self):
        return "Bike starting...."
    
# polymorphism
def vehicle_starts(vehicle):
    print(vehicle.start())

c = Car()
b = Bike()

vehicle_starts(c)
vehicle_starts(b)