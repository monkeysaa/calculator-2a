"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes)

from functools import reduce

# Replace this with your code
"""
while exit_condition_not_reached:
    input = consume_input()
    *option: error-handle input*
    output = evaluate_input(input) 
    print(output)

repeat forever:
    read input
    tokenize input
    ex. ocean_animals.split(',')  # => ['shark', 'squid', 'tuna', 'flounder']
        if the first token is "q":
            quit
        else:
            (decide which math function to call based on first token)
            if the first token is 'pow':
                  call the power function with the other two tokens

"""
user_input = " "
print("Welcome to our prefix-notation calculator")

while (user_input != 'q'):
    user_input = input('Enter your equation > ')  # > + 2 1
    
    tokens = user_input.split(' ')      # tokens = ['+', '2', '1']
    operation = tokens.pop(0)
    values = []
    for item in tokens: 
        values.append(float(item))

    
    
    """
        if len(tokens) > 3:

            
            # pop off the symbol at token[0] and then turn the rest into floats
            # pass that into reduce


        if len(tokens) == 3:
            num2 = float(tokens[2])
            num1 = float(tokens[1])
        if len(tokens) == 2:
            num1 = float(tokens[1])        
    """
    if operation == 'q':
        print('Exiting calculator.')
        break

    if operation == 'square' or operation == 'cube':
        print('This feature needs to be implemented.')
        break

    elif operation == '+': 
        math_function = add
    
    elif operation == '-':
        math_function = subtract

    elif operation == '*':
        math_function = multiply
        
    elif operation == 'square':
        math_function = square
    
    elif operation == 'cube':
        math_function = cube
    
    elif operation == 'pow':
        math_function = power
    
    elif operation == 'mod':
        math_function = mod
    
    elif operation == '/':
        math_function = divide
    
    print(reduce(math_function, values))
    
