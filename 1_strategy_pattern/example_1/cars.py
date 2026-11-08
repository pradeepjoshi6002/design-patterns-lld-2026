from vehicle import Vehicle
from SportsDrive import SportsDrive
from NormalDrive import NormalDrive


class CommuterCar(Vehicle):

    def __init__(self):
        super().__init__(NormalDrive())

class SportsCar(Vehicle):

    def __init__(self):
        super().__init__(SportsDrive())
