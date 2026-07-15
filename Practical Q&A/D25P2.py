class Animal:
    def sound(self):
        pass

class Lion(Animal):
    def sound(self):
        return "Roar"
    
class Elephant(Animal):
    def sound(self):
        return "Trumpet"
    
# Polymorphism
Animals =[Lion(),Elephant()]
for a in Animals:
    print(a.sound())