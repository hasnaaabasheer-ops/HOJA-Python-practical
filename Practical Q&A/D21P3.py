class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print("Name :",self.name,"Age :",self.age,"Grade :",self.grade)

s1 = Student("Rahul","19","A+")
s2 = Student("Joe","G-Class","A")

s1.introduce()
s2.introduce()