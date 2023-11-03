#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def main():

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = ['-', '+', '*', '/']
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    func = {'-': sub, '+': add, '/': div, '*': mul}

    for key, value in func.items:
        if key == operator:
            print("{} {} {} = {}".format(a, operator, b, value(a, b)))
            return


if __name__ == "__main__":
    main()
