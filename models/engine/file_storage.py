#!/usr/bin/python3
"""FileStorage class defined here"""
import json
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    Represents a class that serializes instances to a
    JSON FILE  to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """For returning the dictionay onjects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        For setting in objects with key
        <obj class name>.id
        """
        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        For serializing objects to the JSON file
        which is file.json
        """
        objs = FileStorage.__objects
        objdict = {i: objs[i].to_dict() for i in objs.keys()}
        with open(FileStorage.__file_path, "w") as myfile:
            json.dump(objdict, myfile)

    def reload(self):
        """
        For deserializing the JSON file
        Only if the File exists
        """
        try:
            with open(FileStorage.__file_path) as myfile:
                obj_dicts = json.load(myfile)
                for i in obj_dicts.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i))
        except FileNotFoundError:
            pass
