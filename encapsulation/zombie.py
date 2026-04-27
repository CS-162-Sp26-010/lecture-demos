# Coupling: A situation wherein changing one line of code requires
# also changing one or more other lines of code

# Coupling, to some extent, is inevitable. Coupling occurs at interfaces.
# Components of code interact with each other through their interfaces.
# (A dependency). Therefore, dependencies are coupled.  And dependencies
# are everywhere (inevitable).

# The problem with coupling is that it makes certain things harder to change.
# There's "pervasive" coupling, and "local" coupling. Pervasive is worse.

# There's also tight coupling and loose coupling.

# What you really want to avoid is tight, pervasive coupling on
# components of code that are LIKELY to need to be changed one day.

# However, coupling can often be "reduced" and "managed".
# Sneak peek: A common tool to managing coupling is known as encapsulation.

# Encapsulation: Co-location (bundling) of data with the behaviors that
# operate on that data.

class Zombie:
    hp: int
    #alive: bool
    sanity: int

    # In some programming languages, you might call this
    # a "default constructor"
    def __init__(self) -> None:
        self.hp = 10
        #self.alive = True
        self.sanity = 3

# This is encapsulation! These are behaviors (functions) that operate
# on data (attributes), and we've colocated them (bundled them)
# with said attributes, placing them in the same module.

# "Things that change together go together"
def print_zombie(zombies: list[Zombie], index: int) -> None:
    print(f'HP: {zombies[index].hp}, sanity: {zombies[index].sanity}')

def is_alive(z: Zombie) -> bool:
    if z.hp > 0: # Zombies don't have hp anymore!
        return True
    else:
        return False
