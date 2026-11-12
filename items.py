from dice import Dice


class Weapon:
    """A class representing a weapon that deals damage using a dice."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Initializes a Weapon object.

        Args:
            name (str): The name of the weapon, e.g. "Sword".
            damage_dice (Dice): The dice used to roll the weapon's damage.
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Rolls the weapon's damage dice and returns the damage dealt."""
        return self.damage_dice.roll()


if __name__ == "__main__":
    sword = Weapon("Sword", Dice(sides=8))
    damage = sword.roll_damage()
    print(f"{sword.name} rolled {damage} damage")
    assert 1 <= damage <= 8
