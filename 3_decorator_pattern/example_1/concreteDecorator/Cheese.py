from decoratorBaseClass.ToppingDecorator import ToppingDecorator

class Cheese(ToppingDecorator):

    def get_description(self):
        return self.pizza.get_description()+", Cheese"

    def get_cost(self):
        return self.pizza.get_cost()+30