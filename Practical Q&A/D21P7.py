class Laptop:
    def __init__(self,brand,ram,storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def specs(self):
        print("Brand :",self.brand,", Ram :",self.ram,", Storage :",self.storage)

l1 = Laptop("ASUS","16 GB","512 GB")
l2 = Laptop("Dell","16 GB","512 GB")

l1.specs()
l2.specs()