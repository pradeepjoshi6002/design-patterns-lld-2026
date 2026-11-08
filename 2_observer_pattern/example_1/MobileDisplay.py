from ObserverInterface import Observer

class MobileDisplay(Observer):

    def __init__(self,weather_station):
        self.weather_station=weather_station

    def update(self):
        temperature=self.weather_station.get_data()
        print(f"Mobile Display: Temperature is {temperature}°C")