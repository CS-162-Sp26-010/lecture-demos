def main() -> None:
    # There are two main kinds of loops in Python:
    # for loops
    # while loops

    # A while loop looks exactly like an if statement, but it uses the
    # word while instead of the word if
    
    '''
    i = 0
    while i < 10:
        # Body goes here
        print(i)
        i = i + 1

    print('Done')

    print(i) # What does this print? 10
    '''

    # Before I can tell you about for loops, I should tell you about ranges

    # A range is a sequence of numbers with a start, a stop, and a step
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # start: 0
    # stop: 10
    # step: 1

    # For loops iterate through iterables. Ranges are iterables. This
    # prints values 0 through 9
    for j in range(10):
        # Body goes here
        print(j)


    print(j) # Prints 9 as well

if __name__ == '__main__':
    main()
