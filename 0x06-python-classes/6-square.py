#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    def __init__(self, size=0):
        """Initializes a new square class

        Args:
            size (int): The size of a new square
            position (int, int): The position of a new square
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
        """Returns the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            """Print the square with a # character"""
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
