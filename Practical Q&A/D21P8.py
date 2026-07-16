class Song:
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print("Title :",self.title,", Artist :",self.artist,", Duration :",self.duration)

s1 = Song("Malbari Banger","Dabzee","4:06")
s2 = Song("Beevi","Rish","2:59")

s1.play()
s2.play()