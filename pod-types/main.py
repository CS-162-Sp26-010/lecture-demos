# A class is a custom, programmer-defined data type
class City:
    # Class body goes here
    # We're just going to work with POD types in today's lecture
    # (plain-old data). A class that has attributes but no
    # methods.

    # An attribute is a variable inside a class.
    # Attributes establish "has-a" relationships.
    name: str
    population: int

def print_city(city: City) -> None:
    print(f'The city, {city.name}, has a population of {city.population}')

def print_cities(my_cities: list[City]) -> None:
    for my_city in my_cities:
        print_city(my_city)

def main() -> None:
    # POD types via classes.
    #my_cool_city = City()
    # The dot operator (.) reaches inside the object
    # on the left and accesses its member whose name
    # is on the right
    #my_cool_city.name = 'Corvallis'
    #my_cool_city.population = 70000

    #print(my_cool_city.name)
    #print(my_cool_city.population)

    
    
    # Every city has a name and a population
    cities = [City(), City()]
    cities[0].name = 'Corvallis'
    cities[0].population = 70000
    cities[1].name = 'Manhattan'
    cities[1].population = 6000000

    # int, float, bool, str
    # City

    # names.insert(1, 'Albany')
    # populations.insert(1, 10000)

    new_city = City()
    new_city.name = 'Albany'
    new_city.population = 1000
    cities.insert(1, new_city)


    print_cities(cities)




if __name__ == '__main__':
    main()
