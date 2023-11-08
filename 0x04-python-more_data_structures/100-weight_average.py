#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    func = lambda x, y: x * y
    total = 0
    div = 0
    for item in my_list:
        total += func(item[0], item[1])
        div += item[1]
    return total / div
