#!/usr/bin/python3
import hidden_4


def main():
    i = 0
    names = dir(hidden_4)
    for name in sorted(names):
        if name[i][:2] == '__':
            i += 1
            continue
        i += 1
        print(name)


if __name__ == "__main__":
    main()
