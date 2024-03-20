#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return my_list
    uniqueAdd = 0
    new_list = set(my_list)
    for i in new_list:
        uniqueAdd += i
    return uniqueAdd
