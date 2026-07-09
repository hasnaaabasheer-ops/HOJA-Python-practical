# class = blueprint
class person:

    # constructor = runs when object is created
    def __init__(self,name,age):
        self.name = name
        self.age =age

    # method = function inside class
    def greet(self):
        print("Hello",self.name)

# object = created from class
p = person("Alice",22)
p2 = person("rahul",30)

p.greet()
p2.greet()