"""
CP1404 Practical
Car class
"""
from prac_08.car import Car
from prac_08.taxi import Taxi

class Taxi_P(Taxi, Car):
    """Specialised version of a Car and a Taxi that include fare costs"""

    def __init__(self, name, fuel, price_per_km):
        """Initialise a Taxi instance, based on parent class Car"""
        super().__init__(name, fuel, price_per_km)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(), self.current_fare_distance, self.price_per_km)

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        super().drive(distance)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0


"""1. Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km"""
prius1 = Taxi_P('Prius 1', 100, 1.23)
"""2. Drive the taxi 40km"""
prius1.drive(40)
"""3. Print the taxi's details and the current fare"""
print(prius1.fuel, prius1.get_fare())
"""4. Restart the meter (start a new fare) and then drive the car 100km"""
prius1.start_fare()
prius1.drive(100)
"""5. Print the details and the current fare"""
print(prius1.fuel, prius1.get_fare())

