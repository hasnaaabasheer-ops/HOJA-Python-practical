class Dog:
    def speak(self):
        return "woof"
    
class Cat:
    def speak(self):
        return "meow"
    
# polymorphism
def animal_sound(animal):
    print(animal.speak())

d = Dog()
c = Cat()

animal_sound(d)
animal_sound(c)