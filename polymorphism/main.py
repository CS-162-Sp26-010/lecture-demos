from monster import Monster
from player import Player
from zombie import Zombie
from vampire import Vampire

def do_monster_turns(
        monsters: list[Monster],
        player: Player) -> None:
    for m in monsters:
        m.attack_player(player)

def main() -> None:
    the_player = Player() # 100 hp

    # Mypy is okay with this.
    monsters: list[Monster] = [Zombie(), Zombie(), Zombie(), Vampire(), Vampire(), Vampire(), Vampire(), Vampire()]

    do_monster_turns(monsters, the_player)

    # Player should have 95 hp at this point

    the_player.print()


if __name__ == '__main__':
    main()
