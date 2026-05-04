# Attributes establish has-a relationships.
# "People have names". The Person class has a name attribute (_name)
# Cities have names. Cities have populations. The City class has a name
#   attribute and a population attribute.

# Methods establish "can" relationships.
# Dogs can bark. The Dog class has a bark() method.
# Snakes can move. The Snake class has a move() method.

# Inheritance allows us to establish "is-a" relationships.
# A husky is a dog.

class Dog:
    _name: str
    def __init__(self, name: str) -> None:
        self._name = name

# A base class is another, existing class from which this class
# will inherit (or be derived from).
# The Husky class inherits from the Dog class.
# A Husky "is a" Dog.
class Husky(Dog):
    pass

class Labrador(Dog):
    pass

class GermanShepherd(Dog):
    pass


def main() -> None:
    pass

if __name__ == '__main__':
    main()
