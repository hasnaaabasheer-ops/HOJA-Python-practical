def display(obj):
    print(obj.show())

class Jump:
    def show(self):
        return "Jumb heigh."
    
class Run:
    def show(self):
        return "run fast"
    
actions = [Jump(),Run()]
for a in actions:
    display(a)