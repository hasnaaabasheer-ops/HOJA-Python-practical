from abc import ABC,abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass

class MyBankATM(ATM):
    def withdraw(self):
        self.__verifyPin()
        self.__checkBalance()
        self.__updateServer()
        print("cash withdraw successfully ")

    def __verifyPin(self):
        print("Pin Verified")

    def __checkBalance(self):
        print("Balance Checked")

    def __updateServer(self):
        print("Server updated")

atm = MyBankATM()
atm.withdraw()