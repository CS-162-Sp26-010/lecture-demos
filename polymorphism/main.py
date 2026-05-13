from monster import Monster
from player import Player
from zombie import Zombie
from vampire import Vampire

def do_monster_turns(
        monsters: list[Monster],
        player: Player) -> None:
    for m in monsters: # Static type of m is Monster.
        # Dynamic type of m will change between Zombie and Vampire throughout
        # the for loop.
        m.attack_player(player)

def main() -> None:
    the_player = Player() # 100 hp

    # From Python interpreter's perspective, every object has a type.
    # This is known as the object's dynamic type. It's the object's "actual"
    # type.

    # From Mypy's perspective, every expression has a type. This is known
    # as the expression's static type. Static types cannot change.

    # In some cases, a variable's static type is not the same as the
    # actual / dynamic type of the object that it will refer to at runtime.
    # Dynamic types CAN change, so long as they're always compatible with
    # the static types.

    # Mypy is okay with this.
    # Subtype polymorphism.
    # Polymorphism means "many forms". It refers to a variable that can take
    # on one of many types.
    # Subtype polymorphism is polymorphism done through subtyping
    # (subtype == subclass == child class == derived class)
    monsters: list[Monster] = [Zombie(), Zombie(), Zombie(), Vampire(), Vampire(), Vampire(), Vampire(), Vampire()]

    do_monster_turns(monsters, the_player)

    # Player should have 95 hp at this point

    the_player.print()


if __name__ == '__main__':
    main()
