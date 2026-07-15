from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "woof"
    
class Cat(Animal):
    def sound(self):
        return "meow"
    

d = Dog()
c = Cat()
print(d.sound())
print(c.sound)