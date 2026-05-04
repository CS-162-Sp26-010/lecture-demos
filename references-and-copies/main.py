# Python's object model

# The copy function creates a shallow copy
# The deepcopy function creates a deep copy
from copy import deepcopy

class Stats:
    hp: int

class Pokemon:
    stats: Stats

# Parameters are bound to the objects specified by their respective
# arguments
def foo(pokemon: Pokemon) -> None:
    print(id(pokemon)) # This is going to be the same id as id(squirtle)

    pokemon.stats.hp = 10

    pokemon = Pokemon()
    pokemon.stats = Stats()
    pokemon.stats.hp = 5


def main() -> None:
    # In Python, an object is simply any value

    # Variables are references that refer to objects
    # The assignment operator binds a variable (reference) to
    # a new object
    pi = 3.14 # Binds 'pi' to the object 3.14

    # All objects in Python have identifiers, which are basically numbers.
    # Every unique object has a unique identifier.

    print(id(3.14))
    print(id('Hello'))

    squirtle = Pokemon()
    squirtle.stats = Stats()
    squirtle.stats.hp = 18

    print(id(squirtle))
    foo(squirtle)

    print(squirtle.stats.hp) # Prints 10

    stats_copy = deepcopy(squirtle.stats)
    print(stats_copy.hp) # Prints 10

    stats_copy.hp = 3
    print(stats_copy.hp) # Prints 3
    print(squirtle.stats.hp) # Prints 10

    # In game.py
    current_head = deepcopy(self._snake.get_head())
    current_head.row += 1


    print(id(squirtle.stats))

if __name__ == '__main__':
    main()
