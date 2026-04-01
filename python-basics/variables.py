def main() -> None:
    # Primitive types:
    # int: integer (whole number)
    # float: Floating point number
    # bool: Boolean (True/False)
    # str: string (text)
    
    # int literals: 1, 7, -1000
    # float literals: 1.5, -8.2, .1, 1.
    # bool literals: True, False
    # str literals: 'Text', "Hello"

    # An expression: any piece of code with a type
    # and a value.
    # Arithmetic operators:
    # +: addition
    # -: subtraction
    # *: multiplication
    # /: division
    # **: exponentiation
    # %: modulo (remainder after division)
    # // (integer division)

    # Arithmetic in python follows PEMDAS

    print((3.14 + 7.1) * 7.1 - 2 / 2)
    print(2 ** 5)

    # Variables are named references that refer to
    # objects. Objects are basically just values.

    # Variables are named storage locations.
    # Variable names can contain letters, digits,
    # and underscores. However, they cannot start
    # with a digit. Also, they shouldn't start
    # with an underscore unless you know what you're
    # doing.

    # The assignment operator has incredibly low
    # precedence. It takes the computed value on
    # the right and stores it in the variable on
    # the left. If the variable on the left doesn't
    # already exist, it automatically creates it.
    my_cool_variable = (3.14 + 7.1) * 7.1 - 2 / 2

    print(my_cool_variable)

    # In python, a variable TECHNICALLY can change
    # types throughout a program.

    my_cool_variable = 'Hello'

    # HOWEVER, you SHOULDN'T do this, in most cases.

    # In fact, it's such a bad idea that there are
    # static analysis tools that detect when you make
    # these sorts of mistakes. The industry-standard
    # static analysis tool for Python is called Mypy.
    # Although the above line of code (my_cool_variable = 'Hello')
    # is okay from the interpreter's perspective, Mypy
    # will complain about it, prompting us to fix it.

if __name__ == '__main__':
    main()
