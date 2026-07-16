class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print("Reading ",self.title,"by ",self.author,"page ",self.pages)

b1 = Book("5 AM Club","Robin Sharma","67")
b2 = Book("Rich Dad Poor Dad","Robert Kiyosaki","101")

b1.read()
b2.read()