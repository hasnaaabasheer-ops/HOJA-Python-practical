class GrandFather:
    def grandfather_feature(self):
        print("experienced")

class Father(GrandFather):
    def father_feature(self):
        print("hard worker")

class Aunt(GrandFather):
    def aunt_feature(self):
        print("kind")

class child(Father,Aunt):
    def child_feature(self):
        print("energetic")

c = child()
c.grandfather_feature()
c.father_feature()
c.aunt_feature()
c.child_feature()