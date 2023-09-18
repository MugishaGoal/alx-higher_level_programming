#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """Base model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        obj_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        with open(filename, "w") as file:
            file.write(cls.to_json_string(obj_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set from a
        dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Invalid class name")
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                instance_list = [cls.create(**d) for d in dict_list]
                return instance_list
        except FileNotFoundError:
            return []
