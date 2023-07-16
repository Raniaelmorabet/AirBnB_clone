#!/usr/bin/python3
"""Defines the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city."""
    state_id = ""
    name = ""
