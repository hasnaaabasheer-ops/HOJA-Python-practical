class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def read(self):
        print("roll no",self.rollno,self.name,"is reading")

s1 = student("alice",4)
s2 = student("rahul",7)
s3 = student("joe",8)

s1.read()
s2.read()
s3.read()
