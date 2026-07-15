class Dog:
    def speak(self):
        return "woof"
    
class Cat:
    def speak(self):
        return "Meow"
    
class Cow:
    def speak(self):
        return "Moo"
    
animals = [Dog(),Cat(),Cow()]

for a in animals:
    print(a.speak())