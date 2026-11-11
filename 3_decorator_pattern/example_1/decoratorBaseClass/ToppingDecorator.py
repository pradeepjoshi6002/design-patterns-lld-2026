from componentInterface.PizzaInterface import Pizza

class ToppingDecorator(Pizza):

    def __init__(self,pizza):
        self.pizza=pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

