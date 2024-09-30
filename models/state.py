#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    '''
    Base model class for all entities in the application
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"
