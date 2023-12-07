#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a, len_b = len(tuple_a), len(tuple_b)
    """For each element position (0 and 1), it checks if the index is within the bounds of
    the respective tuple (using conditional expressions). If the index is within bounds,
    it takes the value from the tuple; otherwise, it uses 0.
    """
    new_tuple = ((tuple_a[0] if len_a >= 1 else 0) + 
                 (tuple_b[0] if len_b >= 1 else 0),
                 (tuple_a[1] if len_a >= 2 else 0) +
                 (tuple_b[1] if len_b >= 2 else 0))
    return new_tuple
