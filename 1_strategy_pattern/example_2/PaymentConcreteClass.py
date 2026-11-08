from PaymentStrategyInterface import PaymentStrategtyInterface

class CreditCard(PaymentStrategtyInterface):

    def pay(self, amount):
        return print(f"you are paying {amount} using credit card")

class Upi(PaymentStrategtyInterface):

    def pay(self, amount):
        return print(f"you are paying {amount} using UPI")