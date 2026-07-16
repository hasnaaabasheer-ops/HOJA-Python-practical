class Food:
    def __init__(self,name,type,taste):
        self.name = name
        self.type = type
        self.taste = taste

    def describe(self):
        print("Name :",self.name,", Type :",self.type,", Taste :",self.taste)

f1 = Food("Mango","Fruit","Sweet")
f2 = Food("Chilli","Vegetable","Spicy")

f1.describe()
f2.describe()