def age_of_person(name: str) -> int:
    if name == 'Muhammad Ali':
        return 84
    elif name == 'Alex Guyer':
        return 26
    else:
        # Two main ways to pass error messages back to the call site:
        # Option 1: Error codes as return values
        return -1

        # Alternative: Exceptions

        

def main() -> None:
    name = input('Enter the name of a person whose age you\'d '
        'like to retrieve: ')
    age = age_of_person(name)
    if age == -1:
        print('Error. Age of that person is unknown')
    else:
        print(f'The age of that person is {age}')

if __name__ == '__main__':
    main()
