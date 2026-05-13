from player import Player

# abc stands for abstract base class
from abc import ABC, abstractmethod

# We want the Monster class to be an abstract base class,
# and the way to do that in Python is to have the Monster
# class inherit from ABC. An abstract base class is simply
# a class that can have abstract methods.
class Monster(ABC):
    # An abstract method is a method that you intend to override
    # in derived classes. An abstract method is a PROMISE that you WILL
    # override the method in the derived classes.
    @abstractmethod
    def attack_player(self, player: Player) -> None:
        pass

    # Abstract classes have constraints. The biggest constraint on abstract
    # classes is that they cannot be instantiated.

    # Classes derived from abstract classes are also abstract, unless they
    # override all abstract methods.
