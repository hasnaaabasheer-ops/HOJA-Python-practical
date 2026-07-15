import math

def show_area(shape):
    print("Area :",shape.area())

class Square:
    def area(self):
        return self.side * self.side
    
class Circle:
    def area(self):
        return math.pi * self.radius * self.radius

s = Square()    
c = Circle()

s.side = 4
c.radius =3

show_area(s)
show_area(c)