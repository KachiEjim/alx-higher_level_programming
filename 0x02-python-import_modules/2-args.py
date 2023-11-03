#!/usr/bin/python3
from sys import argv, exit

if __name__ == "__main__":
    l = len(argv) - 1

    if l == 0:
        print("0 arguments.")
        exit(0)

    s = "argument:" if l == 1 else "arguments:"
    print("{} {}".format(l, s))

    for i in range(1, l + 1):
        print("{}: {}".format(l, argv[i]))

    
    


