# Object-oriented programming (OOP). Programming centered around objects.

# In the context of  OOP, an object is something with data and behaviors
# that operate on that data (and identity).

class Dog:
    # Attributes are a kind of variable (i.e., data)
    owner: str
    birth_year: int

    # You can define functions inside class bodies. Such functions are
    # known as "methods".
    def print_info(self, x: int, y: float, z: bool) -> None:
        print(f'The dog\'s owner\'s name is {self.owner}, and it was born'
            f' in {self.birth_year}')

    # Constructors are very special methods that are automatically called on
    # objects the MOMENT they're created. If you don't define a constructor
    # for a class, it will have an empty constructor by default. 
    # The purpose of a constructor is to "set up" the object that has just
    # been created. I might create a Dog class constructor that accepts
    # an owner and a birth year as arguments, and stores them inside
    # the dog's owner and birth_year attributes.
    def __init__(self, o: str, b: int) -> None:
        self.owner = o
        self.birth_year = b



#def print_dog_info(dog: Dog) -> None:
#    print(f'The dog\'s owner\'s name is {dog.owner}, and it was born in {dog.birth_year}')
