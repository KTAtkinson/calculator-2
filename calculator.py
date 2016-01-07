"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from fancy_arithmetic import *

def get_int_list(str_list):
    int_list = []

    for element in str_list:
        int_list.append(int(element))
    return int_list

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
            answer = add(get_int_list(tokens))
        elif operator == "-":
            answer = subtract(get_int_list(tokens))
        elif operator == "*":
            answer = multiply(get_int_list(tokens))
        elif operator == "/":
            answer = divide(get_int_list(tokens))
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
