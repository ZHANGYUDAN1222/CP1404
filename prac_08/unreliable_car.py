"""
CP1404/CP5632 Practical
Car class
"""

from prac_08.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs"""

    def __init__(self, reliability=0, **kwargs):
        """Initialise a Taxi instance, based on parent class Car"""
        super().__init__(**kwargs)
        self.reliability = reliability
