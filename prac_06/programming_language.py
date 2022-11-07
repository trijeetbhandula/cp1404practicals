"""
CP1404/CP5632 Practical
Programming Language Class
Estimate: 30 minutes
Actual:   26 minutes
"""


class ProgrammingLanguage:
    """Represent a program language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a program language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if programming language is dynamic or not"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of program language object"""
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"
