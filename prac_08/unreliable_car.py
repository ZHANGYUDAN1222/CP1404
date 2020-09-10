"""
CP1404/CP5632 Practical
Car class
"""
from random import uniform
from prac_08.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs"""

    def __init__(self, reliability=0, name='', fuel=0):
        """Initialise a Taxi instance, based on parent class Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        inherited from Car
        """
        reliability = uniform(0, 100)
        """only drive the car if the random number is less than the car's reliability"""
        if reliability > self.reliability:
            super().drive(distance)
        else:
            print("This car is below the reliability")
        return self.reliability, distance

    def __str__(self):
        return "{}, fuel={}, reliability={}".format(self.name, self.fuel, self.reliability)