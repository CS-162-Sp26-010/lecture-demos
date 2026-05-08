def foo(y: float | None) -> None:
    # There must be a present if statement that looks like this in order
    # for Mypy to be able to determine whether y + 2 is valid.
    if y is not None:
        print(y + 2)

def main() -> None:
    # Union types. Sum types.
    # A union type is a type that can be one of many other types

    x: int | str = 1 # x can be an int
    x = 'hello' # but it can also be a string

    # None is an object, its type is NoneType. The purpose of None is to
    # represent the absence of data.

    # y is an Optional (a variable whose type is a union type that includes None
    # as one of the possibilities)
    y: float | None = 3.14
    y = None

    foo(y)


if __name__ == '__main__':
    main()
