from decoratorBaseClass.CoffeeDecorator import CoffeeDecorator

class WhippedCream(CoffeeDecorator):

    def get_description(self):
        return self.get_description()+", Whipped cream"

    def get_cost(self):
        return self.get_cost()+25