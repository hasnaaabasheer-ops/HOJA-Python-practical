class Teacher:
    def __init__(self,name,subject,experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def introduce(self):
        print("Name :",self.name,", Subject :",self.subject,", Experience :",self.experience)

t1 = Teacher("Hasna","English","Good")
t2 = Teacher("Joe","Maths","Hard")

t1.introduce()
t2.introduce()