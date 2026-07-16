class Movie:
    def __init__(self,name,gender,rating):
        self.name = name
        self.gender = gender
        self.rating = rating

    def review(self):
        print("Name :",self.name,"Gender :",self.gender,"Rating :",self.rating)

m1 = Movie("John","male","4")
m2 = Movie("jenny","female","5")

m1.review()
m2.review()