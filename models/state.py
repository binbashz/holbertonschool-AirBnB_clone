#!/usr/bin/python3
"""
State module for AirBnB clone project.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new State instance.
        """
        super().__init__(*args, **kwargs)
