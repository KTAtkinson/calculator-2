"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator():
    answer = None
    # repeat forever:
    while True:
        #     read input
        math = raw_input(">")
        #     tokenize input
        tokens = math.split(' ')
        operator = tokens.pop(0)

        #     if the first token is 'q', quit
        if operator == "q":
            break
        #     otherwise decide which math function to call based on the tokens we read
        elif operator == "+":
            answer = add(tokens[0], tokens[1])
        elif operator == "-":
            answer = subtract(tokens[0], tokens[1])
        elif operator == "*":
            answer = multiply(tokens[0], tokens[1])
        elif operator == "/":
            answer = divide(tokens[0], tokens[1])
        elif operator == "%":
            answer = mod(tokens[0], tokens[1])
        elif operator == "cube":
            answer = cube(tokens[0], tokens[1])
        elif operator == "pow":
            answer = power(tokens[0], tokens[1])
        elif operator == "square":
            answer = square(tokens[0], tokens[1])
        else:
            print "I don't understand."

        if answer:
            print answer


calculator()
