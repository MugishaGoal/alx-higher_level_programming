#!/usr/bin/python3

def magic_calculation(a, b):
    add = __import__('magic_calculation_102').add
    sub = __import__('magic_calculation_102').sub

    if x < y:
        z = add(x, y)
        for i in range(4, 6):
            z = add(z, i)
        return z
    else:
        return sub(x, y)
