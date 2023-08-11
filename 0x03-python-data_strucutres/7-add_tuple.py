#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b, c, d = tuple_a[0], tuple_b[0], tuple_a[1], tuple_b[1]
    if tuple_a[0] is None:
        a == 0
    if tuple_a[1] is None:
        b == 0
    if tuple_b[0] is None:
        c == 0
    if tuple_b[1] is None:
        d == 0

    new_tuple = (a + b,  c + d)
    return new_tuple
