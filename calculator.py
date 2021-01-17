"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes)


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
    operation = tokens[0]

    if len(tokens) == 3:
        num2 = float(tokens[2])
        num1 = float(tokens[1])
    if len(tokens) == 2:
        num1 = float(tokens[1])        

    if operation == 'q':
        print('Exiting calculator.')
        break

    elif operation == '+': 
        print(add(num1, num2))
    
    elif operation == '-':
        print(subtract(num1, num2))

    elif operation == '*':
        print(multiply(num1, num2))
        
    elif operation == 'square':
        print(square(num1))
    
    elif operation == 'cube':
        print(cube(num1))
    
    elif operation == 'pow':
        print(power(num1, num2))
    
    elif operation == 'mod':
        print(mod(num1, num2))
    
    elif operation == '/':
        print(divide(num1, num2))
    
