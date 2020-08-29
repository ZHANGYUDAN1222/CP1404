"""CP1404/CP5632 Practical - Client code to use the Guitar class."""

from prac_06.guitar import Guitar

def main():
    """Test if the two methods works"""
    gibson = Guitar('Gibson L-5 CES', 1922, 16035.4)
    another=Guitar("Another Guitar", 2013, 0)
    print(gibson)
    print(another)
    print(gibson.get_age())
    print(another.get_age())
    print(gibson.is_vintage())
    print(another.is_vintage())

main()
