def c() -> None:
    # raise IndexError('Error!')
    my_list = []
    print(my_list[0])

def b() -> None:
    c()

def a() -> None:
    try:
        b()
    except ValueError as ex:
        print('Error!')

    print('Hello')
    

def main() -> None:
    a()
    print('World!')


if __name__ == '__main__':
    main()
