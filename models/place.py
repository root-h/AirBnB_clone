#!/usr/bin/python3
"""
This module has one class: Place
inherited from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class:

    Attributes:
        city_id: str, City.id
        user_id: str, User.id
        name: str, place name
        description: str, description of place
        number_rooms: int, number of rooms
        number_bathrooms: int, number of bathrooms
        max_guest: int, max number of guests
        price_by_night: int, price per night
        latitude: float, latitude of place
        longitude: float, longitude of place
        amenity_ids: list of strs, list of Amenity.id
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
