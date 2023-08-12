#!/usr/bin/python3
"""user class
"""

from models.base_model import BaseModel


class User(BaseModel):
    '''Represents User class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
