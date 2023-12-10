#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = my_list[:]
    for idx, x in enumerate(new_list):
        if x == search:
            new_list[idx] = replace
    return new_list
