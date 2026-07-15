class shape:
    def area(self):
        return 0 
    
class Circle(shape):
    def area(self):
        return 3.14 * 5 * 5
    
class Rectangle(shape):
    def area(self):
        return 10 * 5
    
# polymorphism
shapes = [Circle(),Rectangle()]

for s in shapes:
    print(s.area())