import math

def age_of_person(name: str) -> int:
    if name == 'Muhammad Ali':
        return 84
    elif name == 'Alex Guyer':
        return 26
    else:
        # Two main ways to pass error messages back to the call site:
        # Option 1: Error codes as return values. Simple, traditional.
        # return -1

        # Alternative: Exceptions
        raise ValueError(f'Expected name to be Muhammad Ali or Alex Guyer, but got {name}')

        

def main() -> None:
    invalid_input = True
    while invalid_input:
        name = input('Enter the name of a person whose age you\'d '
            'like to retrieve: ')

        try:
            age = age_of_person(name)

            invalid_input = False
        except ValueError as ex:
            # Error-handling code goes here
            print(ex)
    
    print(f'The age of that person is {age}')

    

if __name__ == '__main__':
    main()
