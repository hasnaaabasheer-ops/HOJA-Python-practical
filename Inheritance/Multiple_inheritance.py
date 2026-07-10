class Mother:
    def cook(self):
        print("cooking")

class Father:
    def drive(self):
        print("Driving")

class child(Mother,Father):
    pass

c = child()
c.cook()
c.drive()