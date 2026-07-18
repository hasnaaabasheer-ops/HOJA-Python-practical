from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine started!"

class Bike(Vehicle):
    def start(self):
        return "Bike engine started!"

car = Car()
bike = Bike()

print(car.start())
print(bike.start())
