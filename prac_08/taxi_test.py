"""
CP1404 Practical
Car class
"""
from prac_08.taxi import Taxi

def main():

    """1. Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km"""
    prius1 = Taxi('Prius 1', 100)
    """2. Drive the taxi 40km"""
    prius1.drive(40)
    """3. Print the taxi's details and the current fare"""
    print(prius1.fuel, prius1.get_fare())
    """4. Restart the meter (start a new fare) and then drive the car 100km"""
    prius1.start_fare()
    prius1.drive(100)
    """5. Print the details and the current fare"""
    print(prius1.fuel, prius1.get_fare())

main()

