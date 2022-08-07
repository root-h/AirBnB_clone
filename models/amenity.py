#!/usr/bin/python3
"""
This module has one class: Amenity
inherited from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class:

    Attributes:
        name: str, amenity name
    """
    name = ''
