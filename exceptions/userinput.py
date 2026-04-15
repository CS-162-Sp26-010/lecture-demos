def main() -> None:
    while True:
        try:
            age = int(input('How old are you?: '))
            if age < 0:
                print('That\'s not a valid age!')
            else:
                break
        except ValueError as cool_exception:
            print('That\'s not a valid age!')



if __name__ == '__main__':
    main()
