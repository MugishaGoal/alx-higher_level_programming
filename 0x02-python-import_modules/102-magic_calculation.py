#!/usr/bin/python3

def magic_calculation(a, b):
    add = __import__('magic_calculation_102').add
    sub = __import__('magic_calculation_102').sub

    if a < b:
        z = add(a, b)
        for x in range(4, 6):
            z = add(z, x)
        return z
    else:
        return sub(a, b)
