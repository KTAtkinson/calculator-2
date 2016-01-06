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
        operator = tokens.pop()

        #     if the first token is 'q', quit
        if operator == "q":
            break
        #     otherwise decide which math function to call based on the tokens we read
        elif operator == "+":
            answer = add(tokens.pop(), tokens.pop())
            for 



calculator()
