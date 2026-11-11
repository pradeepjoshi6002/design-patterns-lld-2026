from componentInterface.PizzaInterface import Pizza

class Margherita(Pizza):

    def get_description(self):
        return "Margherita"

    def get_cost(self):
        return 100