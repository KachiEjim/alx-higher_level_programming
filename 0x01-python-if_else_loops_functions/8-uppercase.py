#!/usr/bin/python3
def uppercase(s):
    for c in s:
        newChar = c
        if ord(c) >= 97 and ord(c) <= 122:
            newChar = ord(c) - 32
        print("{:c}".format(newChar), end='')
    print()
