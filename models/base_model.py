#!/usr/bin/python3
"""BaseModel class defined here"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel"""

    def __init__(self):
        """Initializes a new BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """
        Returns the BaseModel instance representation with
        the form [<class name>] (<self.id>) <self.__dict__>
        """
        get_classname = self.__class__.__name__
        return f"[{get_classname}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the current updated_at instance attribute to the
        current time
        """
        self.updated_at = datetime.today()

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
