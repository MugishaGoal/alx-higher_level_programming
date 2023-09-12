#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj inherits from a_class (directly or indirectly),
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
