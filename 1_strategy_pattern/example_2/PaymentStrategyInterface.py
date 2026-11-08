from abc import ABC, abstractmethod

class PaymentStrategtyInterface(ABC):

    @abstractmethod
    def pay(self,amount):
        pass