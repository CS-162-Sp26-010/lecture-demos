from player import Player
from monster import Monster

class Vampire(Monster):
    _strength: int
    def __init__(self) -> None:
        self._strength = 1

    def attack_player(self, player: Player) -> None:
        player.take_damage(self._strength)
        if self._strength < 3:
            self._strength += 1
