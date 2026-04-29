# A class invariant is a property of objects of a certain class
# that is ALWAYS true, guaranteed. We could say that every Circle object
# ever created anywhere in this program is guaranteed to always
# have a non-negative radius.
class Circle:
    # Now that _radius is private, we can be confident that it will
    # only be accessed by methods of this class
    _diameter: float
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError('Error! Circles can\'t have negative radii')
        self._diameter = radius * 2

    # Getters and setters.

    # A getter is a method that simply returns a value contained somewhere
    # within an object.
    def get_radius(self) -> float:
        return self._diameter / 2

    # A setter is a method that simply modifies a value contained somewhere
    # within an object to the specified value
    def set_radius(self, radius: float) -> None:
        if radius < 0:
            raise ValueError('Error! Circles can\'t have negative radii')
        self._diameter = radius * 2

def main() -> None:
    my_circle = Circle(10)
    my_circle.set_radius(2)
    print(my_circle.get_radius())

if __name__ == '__main__':
    main()
