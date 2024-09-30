!/usr/bin/python3
"""defines the city class
"""

from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city."""

    def __init__(self, state_id: str = "", name: str = "", **kwargs):
        """
        Initializes a City instance.

        Args:
            state_id (str): The state id.
            name (str): The name of the city.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(**kwargs)
        self.state_id = state_id
        self.name = name

# Example usage
if __name__ == "__main__":
    city = City(state_id="NY", name="New York")
    print(city.state_id)  # Should output: NY
    print(city.name)      # Should output: New York
