#!/usr/bin/python3
""" module to manipulate file storage """

import json


class FileStorage:
    """ class to serialize and deserialize json files """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns object dictionary """

        return self.__objects

    def new(self, obj):
        """ sets an object into __objects dictionary """

        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """ serialize object to JSON file """

        new_dict = {}
        for key, value in self.__objects.items():
            new_dict.update({key: value.to_dict()})
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ deserializes objects from a saved JSON file """

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

        try:
            with open(self.__file_path, 'r') as f:
                json_dict = json.load(f)
            for value in json_dict.values():
                self.new(class_dict[value["__class__"]](**value))
                """
                The object is an instance of BaseModel
                initialized with kwargs
                """
        except IOError:
            pass
