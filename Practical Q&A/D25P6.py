class Laptop:
    def price(self):
        pass

class GamingLaptop:
    def price(self):
        return "90,000"
    
class BusinessLaptop:
    def price(self):
        return "100,000"
    
def laptop_price(system):
    print(system.price())

g = GamingLaptop()
b = BusinessLaptop()

laptop_price(g)
laptop_price(b)