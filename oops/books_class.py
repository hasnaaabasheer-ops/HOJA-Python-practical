# class = blueprint
class Book:

    # constructor = runs when object is created
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # method = function inside class
    def details(self):
        print("Book:", self.title, "| Author:", self.author)

# object = created from class
b1 = Book("Python Basics", "John Smith")
b2 = Book("AI for Beginners", "Sara Khan")

b1.details()
b2.details()
