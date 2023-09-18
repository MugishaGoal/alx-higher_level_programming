#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The identity of the new square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args: List of no-keyworded arguments (id, size, x, y).
            **kwargs: Double pointer to a dictionary of keyworded arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }            
