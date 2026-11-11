from componentInterface.Coffee import Coffee

class BasicCoffee(Coffee):

    def get_description(self):
        return "Basic coffee"

    def get_cost(self):
        return 100