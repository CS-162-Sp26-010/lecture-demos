# Attributes establish has-a relationships.
# "People have names". The Person class has a name attribute (_name)
# Cities have names. Cities have populations. The City class has a name
#   attribute and a population attribute.

# Methods establish "can" relationships.
# Dogs can bark. The Dog class has a bark() method.
# Snakes can move. The Snake class has a move() method.

# Inheritance allows us to establish "is-a" relationships.
# A husky is a dog.

# The Pet class is the "grandparent" of the Husky class.

class Pet:
    _owner: str

    def __init__(self, owner: str) -> None:
        self._owner = owner

    def print(self) -> None:
        print(f'Owner: {self._owner}')

class Dog(Pet):
    _name: str
    def __init__(self, owner: str, name: str) -> None:
        # self._owner = owner # This is wrong
        super().__init__(owner) # Call the Pet constructor on self
        self._name = name

    # This is an override
    def print(self) -> None:
        super().print()
        print(f'Name: {self._name}')

# A base class is another, existing class from which this class
# will inherit (or be derived from).
# The Husky class inherits from the Dog class.
# A Husky "is a" Dog.

class Sled:
    distance_pulled: int
    def __init__(self) -> None:
        self.distance_pulled = 0

# Base class == superclass == parent class.
# Derived class == subclass == child class
# The Husky class inherits from the Dog class.
# The Husky class is "derived from" the Dog class.
class Husky(Dog):
    # Extension: When you "extend" a base class by inheriting from it
    # and then adding additional attributes and / or methods in the
    # derived class(es)
    _energy: int

    # This is known as an override
    def __init__(self, owner: str, name: str, energy: int) -> None:
        # self._name = name
        # Call an inherited method of the Dog class, giving it the
        # name, and let IT initialize the husky's _name attribute
        
        # self.__init__(owner, name) # This is wrong. It has this method call itself.
        super().__init__(owner, name) # This is right! It calls the Dog constructor on self.

        self._energy = energy

    def pull_sled(self, sled: Sled) -> None:
        if self._energy > 0:
            sled.distance_pulled += 1000
            self._energy -= 1
        else:
            print('The husky is too tired to pull the sled!')
    
    # This is an override
    def print(self) -> None:
        super().print()
        print(f'Energy: {self._energy}')

class Labrador(Dog):
    pass

class GermanShepherd(Dog):
    pass

def main() -> None:
    spot = Dog('Jannette', 'Spot')

    spot.print() # What does this print?

    princess = Husky('Jannette', 'Princess', 10)
    sled = Sled()
    princess.pull_sled(sled)

    print(sled.distance_pulled)

    # spot.pull_sled(sled) # This won't work!

    princess.print()

    super(Dog, princess).print()





# NOTE: Multiple inheritance is possible.
# Some people will tell you that it should be avoided.
# At the very least, if you're interested in doing it,
# you should be aware of the diamond problem.


if __name__ == '__main__':
    main()
