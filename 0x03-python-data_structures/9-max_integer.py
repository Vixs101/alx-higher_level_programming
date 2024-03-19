#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    i = len(my_list) - 1
    while i > 0:
        j = 0
        while j < i:
            if my_list[j] >= my_list[j + 1]:
                a = my_list[j]
            j += 1
        i -= 1
    return a
