#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review."""
    place_id = ""
    user_id = ""
    text = ""
