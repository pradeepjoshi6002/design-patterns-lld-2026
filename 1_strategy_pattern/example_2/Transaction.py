
class Transaction():

    def __init__(self,paymentMethod):
        self.paymentMethod=paymentMethod

    def pay(self,amount):
        self.paymentMethod.pay(amount)