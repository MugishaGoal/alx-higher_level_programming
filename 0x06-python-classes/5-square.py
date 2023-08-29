#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    def __init__(self, size=0):
        """Initializes a new square class

        Args:
            size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
