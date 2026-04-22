# Packages: Directories (folders) that contain python files and / or other
# packages / directories

# Modules: Python files (.py)

# import utils.city
from utils.city import City, print_city

def main() -> None:
    #my_city = utils.city.City()
    my_city = City() # Only works with from x import y syntax
    my_city.name = 'Corvallis'
    my_city.population = 70000
    # utils.city.print_city(my_city)
    print_city(my_city) # Only works with from x import y syntax

if __name__ == '__main__':
    main()
