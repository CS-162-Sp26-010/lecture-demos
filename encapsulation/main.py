from zombie import Zombie, print_zombie, is_alive

def main() -> None:
    my_zombies = [Zombie(), Zombie(), Zombie()]
    print_zombie(my_zombies, 0) # The main function interacts with the a function's interface
    # An interface is the part of a component of code that describes WHAT it
    # is / WHAT it does, and HOW to interact with it.
    print_zombie(my_zombies, 2)
    if is_alive(my_zombies[1]):
        print('The second zombie is still alive!')
    else:
        print('The second zombie is dead!')

if __name__ == '__main__':
    main()
