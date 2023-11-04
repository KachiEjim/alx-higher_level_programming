#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    new = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return (new)
    for i in range(len(my_list)):
        if i == idx:
            new[i] = element
            return (new)
