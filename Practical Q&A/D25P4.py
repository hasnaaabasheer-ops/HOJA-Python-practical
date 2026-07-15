class EnglishGreeting:
    def greet(self):
        return "Hello"
    
class SpanishGreeting:
    def greet(self):
        return "Hola"
    
def accept(greeting):
    print(greeting.greet())

e = EnglishGreeting()
s = SpanishGreeting()

accept(e)
accept(s)