#!/usr/bin/python3
"""
This module has one class: State
inherited from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class:

    Attributes:
        name: str, state name
    """
    name = ''
