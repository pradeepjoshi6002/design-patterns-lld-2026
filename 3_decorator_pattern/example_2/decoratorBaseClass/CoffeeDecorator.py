from componentInterface.Coffee import Coffee

class CoffeeDecorator(Coffee):

    def __init__(self,coffee):
        self.coffee=coffee

    def get_description(self):
        return self.coffee.get_description()

    def get_cost(self):
        return self.coffee.get_cost()