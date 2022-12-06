"""
CP1404 Practical
Unreliable Car
"""

import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Construct the UnreliableCar object."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability."""
        if random.uniform(0, 100) >= self.reliability:
            distance = 0
        return super().drive(distance)
