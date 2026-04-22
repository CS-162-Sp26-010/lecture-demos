class City:
    name: str
    population: int

def print_city(city: City) -> None:
    print(f'The city, {city.name}, has a population of {city.population}')
