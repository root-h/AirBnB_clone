#!/usr/bin/python3
"""
This module has one class: Review
inherited from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class:

    Attributes:
        place_id: str, State.id
        user_id: str, User.id
        text: str, text containing the review
    """
    place_id = ''
    user_id = ''
    text = ''
