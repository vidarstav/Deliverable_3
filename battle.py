from character import Character


class Battle:
    """Manages turn-based combat between two characters."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """Initializes a Battle object.

        Args:
            hero (Character): The character that attacks first each round.
            enemy (Character): The character that fights back.
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Plays one round: hero attacks enemy, and enemy strikes back if still alive."""
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> Character:
        """Plays rounds until one character is no longer alive.

        Returns:
            Character: The winner of the battle.
        """
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()
        return self.hero if self.hero.is_alive else self.enemy


if __name__ == "__main__":
    from character import Mage, Warrior
    from Dice import Dice
    from items import Weapon

    hero = Warrior("Conan", weapon=Weapon("Sword", Dice(sides=8)))
    enemy = Mage("Merlin")
    winner = Battle(hero, enemy).simulate_battle()
    print(f"{winner.name} wins with {winner.hp} HP left!")
    assert hero.is_alive != enemy.is_alive
