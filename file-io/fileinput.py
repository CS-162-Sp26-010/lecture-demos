import typing

def find_oldest_person(the_file: typing.TextIO) -> str:
    oldest_person = ''
    oldest_age = -1
    itr_count = 0
    for line in the_file:
        itr_count += 1
        if itr_count == 1:
            continue

        # Stripping newlines
        line = line.strip()

        # print(line)

        # split()
        # Tokens: Smaller strings within a larger string as separated by
        # token separators
        tokens = line.split(',') # list[str]
        
        if int(tokens[1]) > oldest_age:
            oldest_age = int(tokens[1])
            oldest_person = tokens[0]

    return oldest_person

def main() -> None:
    # File I/O: Reading from and / or writing to files
    
    # File input:
    try:
        with open('data.csv', 'r') as my_file: # typing.TextIO
            # Do whatever you need to do with the file here
            
            print(find_oldest_person(my_file))
    except OSError as ex:
        print('Failed to open file for some reason!')
        
    # You can no longer do useful things with my_file. It's now "closed"
    # since the with block has ended.
    

if __name__ == '__main__':
    main()
