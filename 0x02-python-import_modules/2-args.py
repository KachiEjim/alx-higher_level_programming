#!/usr/bin/python3
import sys

def main():
    l = len(sys.argv) - 1
    if l == 0:
        print("0 arguments.")
    elif l == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(l))

    for i in range(1, l + 1):
        print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()
