#!/usr/bin/python3

"""
User module for AirBnB clone project.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.
        """
        super().__init__(*args, **kwargs)
