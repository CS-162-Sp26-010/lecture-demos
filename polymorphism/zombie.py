from player import Player
from monster import Monster

class Zombie(Monster):
    _sanity: int
    
    def __init__(self) -> None:
        self._sanity = 3

    def attack_player(self, player: Player) -> None:
        if self._sanity > 0:
            self._sanity -= 1
        else:
            player.take_damage(2)
