#!/usr/bin/python3
"""Module for amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Custom amenity class

    Attributes:
        name (str): amenity name
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if "name" not in kwargs:
            self.name = ""

# Example usage
if __name__ == "__main__":
    amenity = Amenity(name="Pool")
    print(amenity.name)  # Should output: Pool
