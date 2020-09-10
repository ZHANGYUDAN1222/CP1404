"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from prac_08.unreliable_car import UnreliableCar

def main():
    """Test if the unreliableCar works."""
    """set reliability to 23.55, name 'limo', fuel 100"""
    limo= UnreliableCar(23.55, 'limo', 100)
    """Drive 50km"""
    limo.drive(50)
    """Print detail"""
    print(limo.fule)


main()