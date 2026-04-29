from zombie import Zombie

def main() -> None:
    my_zombies = [Zombie(), Zombie(), Zombie()]
    my_zombies[0].print()
    # An interface is the part of a component of code that describes WHAT it
    # is / WHAT it does, and HOW to interact with it.
    my_zombies[2].print()
    if my_zombies[1].is_alive():
        print('The second zombie is still alive!')
    else:
        print('The second zombie is dead!')

if __name__ == '__main__':
    main()
