#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    l = len(argv)
    sum = 0

    if l > 1:
        for i in range(1, l):
            sum += int(argv[i])

    print(sum)
