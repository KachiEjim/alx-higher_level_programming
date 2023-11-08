#!/usr/bin/python3

def roman_to_int(roman_string):
    s = roman_string
    if not isinstance(s, str) or s is None:
        return 0

    rlist = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev = 0
    for i in reversed(s):
        value = rlist[i]
        if value >= prev:
            total += value
        else:
            total -= value
        prev = value

    return total
