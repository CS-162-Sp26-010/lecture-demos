def modify(x: list[int]) -> None:
    x[0] = 10

def main() -> None:
    y = [100]
    modify(y)
    print(y[0]) # Prints 10

if __name__ == '__main__':
    main()
