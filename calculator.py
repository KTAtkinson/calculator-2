"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator():
    while True:
        answer = None
        #     read input
        math = raw_input(">")
        #     tokenize input
        tokens = math.split(' ')
        operator = tokens.pop(0)

        #     if the first token is 'q', quit
        if operator == "q":
            break
        elif operator == "+":
            answer = add(int(tokens[0]), int(tokens[1]))
        elif operator == "-":
            answer = subtract(int(tokens[0]), int(tokens[1]))
        elif operator == "*":
            answer = multiply(int(tokens[0]), int(tokens[1]))
        elif operator == "/":
            answer = divide(int(tokens[0]), int(tokens[1]))
        elif operator == "%":
            answer = mod(int(tokens[0]), int(tokens[1]))
        elif operator == "cube":
            answer = cube(int(tokens[0]))
        elif operator == "pow":
            answer = power(int(tokens[0]), int(tokens[1]))
        elif operator == "square":
            answer = square(int(tokens[0]))
        else:
            print "I don't understand."

        if answer:
            print answer


calculator()
