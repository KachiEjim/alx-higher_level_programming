#!/usr/bin/python3
for character in range(122, 96, -1):
    if character % 2 != 0:
        character = character - 32
    print(f"{character:c}", end="")
