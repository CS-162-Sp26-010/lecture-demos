# import math
from math import sqrt, sin

def modify_list(the_list: list[int]) -> None:
    the_list[0] = 1000

def main() -> None:
    print(sqrt(100))

    # A list is a sequence of objects that supports random access (direct
    # access). It also supports adding / removing objects.
    # [1, 7, 2, -1, 4]

    # Create list
    my_list = [1, 7, 2, -1, 4]

    # Access elements
    print(my_list[1]) # Prints 7
    my_list[1] = my_list[0] + my_list[2]
    print(my_list[1]) # Prints 3

    # my_list[5] = 1 # IndexError

    # Append element
    my_list.append(21)
    print(my_list[5])
    
    # Insert element
    my_list.insert(3, -100)

    print(my_list)

    # Delete element
    del my_list[1]

    print(my_list)

    # Length of list
    print(len(my_list))

    #for j in range(len(my_list)):
    #    print(my_list[j] * 2)

    for i in my_list:
        print(i * 2)

    # Type hints, lists in functions
    
    # Modifying list elements in function
    modify_list(my_list)
    print(my_list[0]) # Prints 1000!

    '''
    value_is_in_list = False
    for value in my_list:
        if value == 1000:
            value_is_in_list = True

    if value_is_in_list:
        print('1000 is in my_list!')
    '''

    # in operator
    if 1000 in my_list:
        print('1000 is in my_list!')

    # List comprehensions: We'll come back to this if we have time

    # Tracebacks. Reverse backtraces.

    # Code style

    # Explicit type annotations of local variables
    my_new_cool_variable: list[bool] = []
    # my_new_cool_variable.append(1) # Mypy generates error
    my_new_cool_variable.append(True)


if __name__ == '__main__':
    main()
