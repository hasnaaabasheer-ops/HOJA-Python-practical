class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self):
        print("Calling from",self.brand,", Model :",self.model,", Price :",self.price)

p1 = Phone("Apple","iphone 17","100,000")
p2 = Phone("Samsung","Galaxy S25","80,000")

p1.call()
p2.call()