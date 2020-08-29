class ProgrammingLanguage:
    """Create class ProgrammingLanguage"""
    def __init__(self,name='',typing='',reflection='',year=''):
        """Initialise a ProgrammingLanguage instance."""
        self.name=name
        self.typing=typing
        self.reflection=reflection
        self.year=year
    def __str__(self):
        """Return string representation of ProgrammingLanguage object"""
        return("%s, %s Typing, Reflection=%s, First appeared in %i"%(self.name,self.typing,self.reflection,self.year))