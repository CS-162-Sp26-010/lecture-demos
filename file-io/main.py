def main() -> None:
    # File I/O: Reading from and / or writing to files
    
    # File input:
    with open('data.csv', 'r') as my_file:
        # Do whatever you need to do with the file here
        
        for line in my_file:
            print(line)
        
    # You can no longer do useful things with my_file. It's now "closed"
    # since the with block has ended.
    

if __name__ == '__main__':
    main()
