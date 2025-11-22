# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")

car = Car()
motorcycle = Motorcycle()
boat = Boat()

car.go()
motorcycle.go()
boat.go()
print()
car.stop()
motorcycle.stop()
boat.stop()