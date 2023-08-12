#!/usr/bin/python3
"""BaseModel class defined here"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel"""
        if kwargs:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """
        Returns the BaseModel instance representation with
        the form [<class name>] (<self.id>) <self.__dict__>
        """
        get_classname = self.__class__.__name__
        class_output = "[{}] ({}) {}".format(
                get_classname, self.id, self.__dict__)
        return class_output

    def save(self):
        """
        Updates the current updated_at instance attribute to the
        current time
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary that contains all key/value pairs
        of the instances
        """
        ins_dict = self.__dict__.copy()
        ins_dict["__class__"] = self.__class__.__name__
        ins_dict["created_at"] = self.created_at.isoformat()
        ins_dict["updated_at"] = self.updated_at.isoformat()
        return ins_dict
