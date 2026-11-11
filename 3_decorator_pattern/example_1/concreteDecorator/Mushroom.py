from decoratorBaseClass.ToppingDecorator import ToppingDecorator

class Mushroom(ToppingDecorator):

    def get_description(self):
        return self.pizza.get_description()+", Mushroom"

    def get_cost(self):
        return self.pizza.get_cost()+20