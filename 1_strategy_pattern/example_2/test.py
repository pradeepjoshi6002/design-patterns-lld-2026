from Transaction import Transaction
from PaymentConcreteClass import CreditCard, Upi


p1=Transaction(CreditCard())
p1.pay(200)

p2=Transaction(Upi())
p2.pay(100)