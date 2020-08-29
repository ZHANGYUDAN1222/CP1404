class Guitar:
    """Represent a guitar object"""

    def __init__(self, name='', year=0, cost=0):
        """Initialise a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return how old the guitar is in years"""
        age = 2020-self.year
        return age

    def is_vintage(self):
        """Return True if the guitar is in 50 or more years old, False otherwise"""
        if self.get_age() > 50:
            return True
        else:
            return False

    def __str__(self):
        """Return string representation of Guitar object"""
        return("%s (%i) : $%.2f" %(self.name, self.year, self.cost))
