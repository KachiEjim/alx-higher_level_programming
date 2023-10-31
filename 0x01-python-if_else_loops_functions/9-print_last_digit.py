#!/usr/bin/python3
def print_last_digit(number):
    x = (number % 10) if number >= 0 else (abs(number) % 10)
    print(x, end='')
    return (x)
