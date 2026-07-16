class City:
    def __init__(self,state,population,country):
        self.state = state
        self.population = population
        self.country = country

    def info(self):
        print("State :",self.state,", Population :",self.population,", Country :",self.country)

c1 = City("Kerala","1.47 billion people","India")
c2 = City("Goa","1.6 million","India")

c1.info()
c2.info()