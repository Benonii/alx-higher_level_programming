#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            a = 0
            b = 0
        else:
            b = 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            c = 0
            d = 0
        else:
            d = 0

    else:
         a = tuple_a[0]
         b = tuple_b[0]
         c = tuple_a[1]
         d = tuple_b[1]

    b = tuple_b[0]
    new_tuple = (a + b,  c + d)
    return new_tuple
