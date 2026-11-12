from __future__ import annotations

from items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when character attacks without a weapon (default = 10)
            weapon (Weapon | None): Optional weapon. If given, attack damage is rolled with it (default = None)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicates private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, damage: int) -> None:
        """Reduces character's hp by damage amount"""
        self._hp -= damage
        self._hp = max(self._hp, 0)  # HP cannot be lower than 0

    def heal(self, amount: int) -> None:
        """Restores character's HP by the specified amount, up to hp_max."""
        if amount > 0:
            self._hp = min(self._hp + amount, self.hp_max)

    def attack(self, target: "Character") -> None:
        """Attack and deal damage to target character.

        Uses the weapon's damage roll if the character has a weapon,
        otherwise the fixed damage value.
        """
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage
        target.take_damage(damage)

    def introduce(self) -> None:
        """Prints a string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Returns True if character is alive (hp > 0), False otherwise"""
        return self._hp > 0



class Warrior(Character):
    """A Warrior class that inherits from Character"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, armor: int = 5,
                 weapon: Weapon | None = None) -> None:
        """
        Initialise the Warrior

        Args:
            name (str): The name of the warrior.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when warrior attacks (default = 10)
            armor (int): Armor value that reduces incoming damage (default = 5)
            weapon (Weapon | None): Optional weapon (default = None)
        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor
        

    def take_damage(self, damage: int) -> None:
        """Reduces warrior's hp by damage amount, considering armor"""
        reduced_damage = max(damage - self.armor, 0)  # Ensure low damage doesn't heal the warrior
        super().take_damage(reduced_damage)




class Mage(Character):
    """A Mage class that inherits from Character"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, mana: int = 30, mana_max: int = 30,
                 weapon: Weapon | None = None) -> None:
        """
        Initialise the Mage

        Args:
            name (str): The name of the mage.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when mage attacks (default = 10)
            mana (int): Current mana value (default = 30)
            mana_max (int): Max mana value (default = 30)
            weapon (Weapon | None): Optional weapon (default = None)
        """
        super().__init__(name, hp_max, damage, weapon)
        self.mana = min(mana, mana_max)
        self.mana_max = mana_max

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character, consuming mana"""
        if self.mana >= 10:  # Check if the mage has enough mana to perform a special attack
            double_damage = self.damage * 2  # Double the damage for a special attack
            self.mana -= 10
            target.take_damage(double_damage)
        else:
            super().attack(target)  # Regular attack if not enough mana
            self.mana += 5 # Regenerate some mana if not enough to perform a special attack
            self.mana = min(self.mana, self.mana_max)  # Ensure mana doesn't exceed max value
