def main() -> None:
    age = int(input('How old are you?: '))

    # Relational operators
    # <
    # >
    # <=
    # >=
    # ==
    # !=

    # Logical operators
    # and
    # or
    # not (unary operator)

    # not True == False
    # not False == True

    i_like_spaghetti = False
    if age < 18 and age >= 0:
        # The if statement body goes here.
        print('You\'re too young to use this adult application')
    elif age < 0:
        # Body goes here
        print('Error: Your age can\'t possibly be negative. That makes no sense.')
    else:
        # Else body goes here
        print('You\'re old enough to use this adult application')

        # If statements do NOT have their own scopes in Python.
        i_like_spaghetti = True

    print(i_like_spaghetti)

    print('Hello, World!')

if __name__ == '__main__':
    main()
