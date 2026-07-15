from abc import ABC , abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(payment):
    def pay(self,amount):
        print("Paid",amount,"using up")

class Card(payment):
    def pay(self,amount):
        print("Paid",amount,"using up")

p1 = UPI()
c1 = Card()
p1.pay(500)
c1.pay(1000)