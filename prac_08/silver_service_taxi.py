"""
CP1404/CP5632 Practical
Taxi class
"""

from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that is a Car."""

    """Add a new attribute, fanciness, which is a float that scales the price_per_km"""
    def __init__(self, name='', fuel=0, finances=0):
        super().__init__(name, fuel)
        """Get price_per_km from Taxi"""
        self.price_per_km = Taxi.price_per_km
        self.finances = finances * self.price_per_km