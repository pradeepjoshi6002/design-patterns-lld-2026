from concreteDecorator import Milk
from concreteComponent.BasicCoffee import BasicCoffee

coffee=BasicCoffee()

add1=Milk(coffee)

print(add1.get_description())
print(add1.get_cost())