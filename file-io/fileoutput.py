def main() -> None:
    # 'w' stands for 'write'. It opens the file in truncate mode.
    # 'a' stands for 'append'. It opens the file in append mode.
    with open('saveddata.csv', 'a') as save_file:
        # \n escape sequence inside string literal means "newline
        # character sequence"
        save_file.write('Alex,26\n')
        save_file.write('Muhammad,84\n')


if __name__ == '__main__':
    main()
