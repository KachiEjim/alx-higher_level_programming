#!/usr/bin/python3
from sys import argv


def main():
    l = len(argv) - 1
    if l == 0:
        print("0 arguments.")
    elif l == 1:
        print("1 argument:")
    else:
        print("{0} arguments:".format(l))

    for i in range(1, l + 1):
        print("{0}: {1}".format(i, argv[i]))


if __name__ == "__main__":
    main()