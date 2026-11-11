from decoratorBaseClass.CoffeeDecorator import CoffeeDecorator

class Milk(CoffeeDecorator):

    def get_description(self):
        return self.coffee.get_description()+", Milk"

    def get_cost(self):
        return self.coffee.get_cost()+20