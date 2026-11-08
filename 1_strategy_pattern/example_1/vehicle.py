
class Vehicle():

    def __init__(self,driveStrategy):
        self.driveStrategy=driveStrategy

    def drive(self):
        self.driveStrategy.drive()