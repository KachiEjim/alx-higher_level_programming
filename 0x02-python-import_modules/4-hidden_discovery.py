#!/usr/bin/python3
import hidden_4


def main():
    i = 0
    names = dir(hidden_4)
    for name in sorted(names):
        if name[i][:2] != '__':
            print(name)
        i += 1


if __name__ == "__main__":
    main()
