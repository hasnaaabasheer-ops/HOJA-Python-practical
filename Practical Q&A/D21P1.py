class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print("Brand is ",self.brand,"Model is ",self.model,"Year is ",self.year)

c1 = Car("BMW","M5","2024")
c2 = Car("Mercedes","G-Class","2025")

c1.display()
c2.display()