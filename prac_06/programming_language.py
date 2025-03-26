"""CP1404/CP5632 Practical - ProgrammingLanguage class.
Estimated time: 15 minutes
Actual time: 11 minutes
"""

class ProgrammingLanguage:
    """Represent a programming language with relevant attributes."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a programming language object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
