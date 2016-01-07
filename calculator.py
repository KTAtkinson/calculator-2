"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from fancy_arithmetic import *

def get_int_list(str_list):
    int_list = []

    for element in str_list:
        try:
            int_list.append(int(element))
        except ValueError:
            print "{} is not a number.".format(element)
            return []

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
        elif operator == "mod":
            answer = mod(get_int_list(tokens))
        elif operator == "cube":
            if len(tokens) != 1:
                print "Only one number can be processed."
            else:
                answer = cube(int(tokens[0]))
        elif operator == "pow":
            answer = power(get_int_list(tokens))
        elif operator == "square":
            if len(tokens) != 1:
                print "Only one number can be processed."
            else:
                answer = square(int(tokens[0]))
        else:
            print "I don't understand."

        if answer:
            print answer


calculator()
