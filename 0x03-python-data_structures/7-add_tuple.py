#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 0:
        a = 0
        c = 0
    elif len(tuple_a) == 1:
        a = tuple_a[0]
        c = 0
    else:
        a = tuple_a[0]
        c = tuple_a[1]

    if len(tuple_b) == 0:
        b = 0
        d = 0
    elif len(tuple_b) == 1:
        b = tuple_b[0]
        d = 0
    else:
        b = tuple_b[0]
        d = tuple_b[1]

    new_tuple = (a + b, c + d)
    return new_tuple
