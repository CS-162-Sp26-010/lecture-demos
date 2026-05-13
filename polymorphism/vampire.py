from typing import override

from player import Player
from monster import Monster

class Vampire(Monster):
    _strength: int
    def __init__(self) -> None:
        self._strength = 1

    # An override is a method in a derived class with the same header
    # as the inherited method. Common convention: Use the override decorator
    # whenever you can. Helps you diagnose errors where they occur.
    @override
    def attack_player(self, player: Player) -> None:
        player.take_damage(self._strength)
        if self._strength < 3:
            self._strength += 1
