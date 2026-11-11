from decoratorBaseClass.CoffeeDecorator import CoffeeDecorator

class Chocolate(CoffeeDecorator):

    def get_description(self):
        return self.get_description()+", Coffee"

    def get_cost(self):
        return self.get_cost()+30
    