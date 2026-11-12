
import random


class Dice:
    """A class representing a dice with a specified number of sides."""

    def __init__(self, sides: int = 6) -> None:
        """Initializes a Dice object.
        
        Args:
            sides (int): The number of sides on the dice (default is 6).

        Raises:
            ValueError: If the number of sides is less than 2.
        """
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides.")
        self.sides = sides

    def roll(self) -> int:
        """Rolls the dice and returns a random integer between 1 and the number of sides."""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Returns a string representation of the Dice object."""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Allows the dice to be called like a function to roll it."""
        return self.roll()


#test
'''
d20 = Dice(sides=20)
print(d20())
'''