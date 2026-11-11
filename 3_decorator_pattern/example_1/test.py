from concreteComponent.Margherita import Margherita
from concreteDecorator import Mushroom,Olive,Cheese

base_pizza=Margherita()

add_1=Cheese(base_pizza)
add_2=Mushroom(add_1)

bill=f"""
Description: {add_2.get_description()}\n
Cost: {add_2.get_cost()}
"""

print(bill)