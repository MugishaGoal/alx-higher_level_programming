#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if it's derived from,
    a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or any subclass, otherwise False.
    """
    return isinstance(obj, a_class)
