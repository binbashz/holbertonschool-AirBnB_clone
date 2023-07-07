#!/usr/bin/python3
"""
City module for AirBnB clone project.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new City instance.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
