from abc import ABC, abstractmethod

class Observable(ABC):

    @abstractmethod
    def add(self,observer):
        pass

    @abstractmethod
    def remove(self,observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def set_data(self,temperature):
        pass

    @abstractmethod
    def get_data(self):
        pass