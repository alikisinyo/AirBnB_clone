#!/usr/bin/python3
"""A city class is created by this module"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""
