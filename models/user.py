#!/usr/bin/python3
"""
This module has one class: User
inherited from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class:

    Attributes:
        email: str, email address
        password: str, password
        first_name: str, first name of user
        last_name: str, last name of user
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
