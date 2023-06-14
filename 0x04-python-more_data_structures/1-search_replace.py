#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = len(my_list)*[0]

    if len(my_list) < 1:
        return my_list
    else:
        for i in range(len(my_list)):
            if my_list[i] == search:
                new_list[i] = replace
            else:
                new_list[i] = my_list[i]

    return new_list
