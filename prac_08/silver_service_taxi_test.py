"""
CP1404/CP5632 Practical
Taxi class
"""
from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    """test 18km trip in a SilverServiceTaxi with fanciness of 2, the fare should be $48.78 (yikes!)"""

    """Create a new taxi with name "tesla", 100 units of fuel and fanciness of 2"""
    tesla = SilverServiceTaxi("Tesla", 100, 2)
    """Drive 18km"""
    tesla.drive(18)
    """Test fare"""
    print(tesla.get_fare())
    """test __str__"""
    print(tesla)

main()