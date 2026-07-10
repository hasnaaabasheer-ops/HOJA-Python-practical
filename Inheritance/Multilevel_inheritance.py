class GrandParent:
    def Feature_grandparent(self):
        print("he is a hard working man")

class parent(GrandParent):
    def Feature_parent(self):
        print("he is very smart")

class child(parent):
    def Feature_child(self):
        print("he study well")

c = child()
c.Feature_grandparent()
c.Feature_parent()
c.Feature_child()