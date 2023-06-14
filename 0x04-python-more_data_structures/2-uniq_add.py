#!/usr/bin/python3
def uniq_add(my_list=[]):
    map = {}
    for value in my_list:
        if value not in map.keys():
            map[value] = value

    sum = 0
    for key in map:
        sum += key

    return sum
