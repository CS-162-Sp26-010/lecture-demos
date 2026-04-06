def main() -> None:
    # Every process has a standard output stream. In most simple cases,
    # it's hooked up to the terminal by default. print() simply writes
    # text into the process's standard output stream.
    print('Hello, World!')

    # There's also standard input.

    # Type casting.
    user_input = float(input('Enter your favorite number: '))

    print(f'The number you entered was: {user_input}')

    # The variable user_input is of type str.
    print(user_input * 2.5)

if __name__ == '__main__':
    main()
