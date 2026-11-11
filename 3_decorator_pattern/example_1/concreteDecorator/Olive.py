from decoratorBaseClass.ToppingDecorator import ToppingDecorator

class Olive(ToppingDecorator):

    def get_description(self):
        return self.pizza.get_description()+", Olive"

    def get_cost(self):
        return self.pizza.get_cost()+10