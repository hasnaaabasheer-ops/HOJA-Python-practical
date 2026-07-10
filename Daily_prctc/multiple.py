class Mother:
    def cook(self):
        print("can cook")

class Father:
    def drive(self):
        print("can drive")

class child(Mother,Father):
    pass

c = child()
c.cook()
c.drive()