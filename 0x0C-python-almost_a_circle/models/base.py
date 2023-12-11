#!/usr/bin/python3
"""Module that defines a class"""
import json


class Base:
    """class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the class
        Args:
            id - if id is not None, and if so assign it to the public
            instance attribute; otherwise, increment __nb_objects and
            assign the new value to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """def to_dictionary(self):
        return dictionary  representation of an instance
        return {'id': self.id}
    """

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of list of dicts
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                content = f.read()
                list_dicts = cls.from_json_string(content)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []


if __name__ == "__main__":
    pass
