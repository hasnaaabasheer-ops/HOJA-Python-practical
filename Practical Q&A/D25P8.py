class Shape:
    def draw(self):
        return 0
    
class Traingle(Shape):
    def draw(self):
        return "Drawing Traingle..."
    
class Circle(Shape):
    def draw(self):
        return "Drawing Circle..."
    
shapes = [Traingle(),Circle()]

for s in shapes:
    print(s.draw())