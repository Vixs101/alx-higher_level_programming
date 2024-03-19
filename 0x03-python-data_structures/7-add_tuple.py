#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = tuple_a + (0, 0)
    if len(tuple_b) == 0:
        tuple_b = tuple_b + (0, 0)
        
    tuple_aM = tuple_a if len(tuple_a) > 1 else tuple_a + (0,)
    tuple_bM = tuple_b if len(tuple_b) > 1 else tuple_b + (0,)
    
    result = (tuple_aM[0] + tuple_bM[0], tuple_aM[1] + tuple_bM[1])
    return result
