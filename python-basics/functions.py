# Scope: A region of code where a symbol is accessible.
# Symbol: A named thing.

# Global scope / module scope / file scope.
#   In general, you shouldn't create variables in global
#   scope. It's generally okay to create constants in global
#   scope.
# Function scope / local scope
# Class scopes

my_cool_variable = 12

def add(value_a: float, value_b: float) -> float:
    value_c = value_a + value_b

    # print(var) # syntax error

    print(my_cool_variable)
    
    value_a = 7.0 # this does NOT change var

    return value_c
    #print('Goodbye, World!') # Dead code. This won't EVER run.

def main() -> None:
    # Function bodies MUST be indented in Python
    print('Hello, World!')

    print(my_cool_variable)

    var = 7.1 # var is scoped to the main function
    print(f'7.1 + 3.14 = {add(var, 3.14)}')
    print(var) # What does this print? 7.1

print(my_cool_variable)

if __name__ == '__main__':
    main()
    print(my_cool_variable)
print(my_cool_variable)

# print(var) # syntax error
