#!/usr/bin/python3
"""
Module Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    represents place class
    """
    city_id = ""
    user_id = ""
    description = ""
    name = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
