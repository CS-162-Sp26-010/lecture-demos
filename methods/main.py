from dog import Dog

def main() -> None:
    jeffs_dog = Dog('Jeff', 1942) # This is a constructor call  

    sallys_dog = Dog('Sally', 2011)
    
    # To call a method within an object, you use the dot operator
    jeffs_dog.print_info(12, 3.14, True)

    sallys_dog.print_info(-1, 9.81, False)



if __name__ == '__main__':
    main()
