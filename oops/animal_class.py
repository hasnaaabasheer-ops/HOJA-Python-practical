class Animal:
    def __init__(self,name,type,lives,sound):
        self.name=name
        self.type=type
        self.lives=lives
        self.sound=sound

    def introduce(self):
        print("This is ",self.name,". It's a ",self.type,". It Lives in ",self.lives)

    def make_sound(self):
        print(self.name,"is making",self.sound)


a1 = Animal("Leo","Lion","Forest","grr")
a2 = Animal("Bella","Kitten","House","meow")

a1.introduce()
a2.introduce()

a1.make_sound()
a2.make_sound()
