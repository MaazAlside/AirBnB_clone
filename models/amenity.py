#!/usr/bin/python3
"""Class amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
