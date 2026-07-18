from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."

class PayPal(Payment):
    def pay(self, amount):
        return f"Paid {amount} using PayPal."

credit = CreditCard()
paypal = PayPal()

print(credit.pay(500))
print(paypal.pay(300))
