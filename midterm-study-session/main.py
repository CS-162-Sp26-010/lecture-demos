from typing import TextIO

# Module scope / global scope

class Dog:
    name: str
    _age: int
    def bark(self) -> None:
        print(self.name)
        print('Bark!')

def do_something_with_the_file(the_file: TextIO) -> None:
    # This is the ... function's scope
    y = 'Hello'

    print(y)

#print(y) # y is not accessible in this scope!

def main() -> None:

    #print(y) # y is not accessible in this scope!

    # This is the main function's scope

    x = 5
    # raise ValueError('Error!')

    #with open('data.txt', 'r') as my_cool_file:
    #    do_something_with_the_file(my_cool_file)
    
    #print(y) # y is not accessible in this scope!
        
    spot = Dog()
    spot.name = 'Spot'
    spot.bark()

    user_age = int(input('How old are you?: '))

    # my_circle = Circle(5)
    # my_circle._radius = 10 # You shouldn't do this

    spot._age = 12

if __name__ == '__main__':
    main()
