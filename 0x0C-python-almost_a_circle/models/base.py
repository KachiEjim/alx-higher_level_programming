#!/usr/bin/python3
"""Creates a class Base"""
import json


class Base:
    """Base of our program"""

    __nb_objects = 0
    def __init__(self, id=None):
        """Initalizes an instance of base
        
        args:
            id (int): Variable id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        filename = f"{type(list_objs[0]).__name__}.json"

        with open(filename, 'w') as file:
            to_dict = [item.to_dictionary() for item in list_objs]
            json_string = Base.to_json_string(to_dict)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        string representation json_string
        
        Args:
            json_string (json str): string representation
                                    of a json string
        """
        if json_string == None or len(json_string) == 0:
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            new = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file and return a list of instances."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                data = file.read()
                instances_data = cls.from_json_string(data)
                instances_list = [cls.create(**item) for item in instances_data]
                return instances_list
        except IOError:
            return []
