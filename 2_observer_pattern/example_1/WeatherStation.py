from ObservableInterface import Observable

class WeatherStation(Observable):

    def __init__(self):
        self.observers=[]
        self.temperature=0

    def add(self, observer):
        return self.observers.append(observer)

    def remove(self, observer):
        return self.observers.remove(observer)

    def notify(self):
        for ob in self.observers:
            ob.update()

    def set_data(self, temperature):
        self.temperature=temperature
        self.notify()

    def get_data(self):
        return self.temperature
    