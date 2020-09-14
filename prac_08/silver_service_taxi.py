"""
CP1404/CP5632 Practical
Taxi class
"""

from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that is a Car."""

    """Add class variable flagfall"""
    flagfall = 4.5

    """Add a new attribute, fanciness, which is a float that scales the price_per_km"""
    def __init__(self, name='', fuel=0, finances=0):
        super().__init__(name, fuel)
        """Get price_per_km from Taxi"""
        self.finances = finances
        self.price_per_km = self.finances * Taxi.price_per_km
        self.current_fare_distance = 0

    """Add flagfall to the fare"""
    def get_fare(self):
        """Return the price for the taxi trip."""
        return "{:.2f}".format(round(((self.price_per_km * self.current_fare_distance)+ self.flagfall),1))
        """change the output to be 10c"""

    def __str__(self):
        return super().__str__() + " plus flagfall of ${}".format(self.flagfall)