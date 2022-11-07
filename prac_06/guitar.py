"""
CP1404/CP5632 Practical
Guitars
Estimate: 25 minutes
Actual: 18 minutes
"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar object."""

    def __init__(self, name='', year=0, cost=0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of guitar object."""
        return f'{self.name} ({self.year}) : ${self.cost}'

    def get_age(self):
        """Return the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE
