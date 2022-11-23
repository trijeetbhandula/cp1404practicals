"""
CP1404 Practical
Silver Service Taxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare."""
        return f"{(self.flagfall + super().get_fare()):.2f}"
