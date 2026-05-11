from player import Player

# abc stands for abstract base class
from abc import ABC, abstractmethod

# We want the Monster class to be an abstract base class,
# and the way to do that in Python is to have the Monster
# class inherit from ABC. An abstract base class is simply
# a class that can have abstract methods.
class Monster(ABC):
    # An abstract method is a method that you don't intend to
    # implement here. Instead, you're strictly going to implement
    # it via overrides.
    @abstractmethod
    def attack_player(self, player: Player) -> None:
        pass
