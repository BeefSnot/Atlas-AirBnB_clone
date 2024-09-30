#!/usr/bin/python3
'''models base_model module'''

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    '''A base model class providing common fields and behaviors
    for all models

    Attributes:
    id (str): a unique identifier for the model instance
    created_at (datetime): the timestamp when the model instance was created
    updated_at (datetime): the timestamp when the model was last updated
    '''

    def __init__(self):
        '''Initializes a new instance of the BaseModel class.
        Creates a unique identifier for the instance and sets the creation
        and last update timestamp.
        '''
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        '''Converts the model instance to a dictionary.'''
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'is_deleted': self.is_deleted
        }

    def save(self):
        '''Updates the updated_at timestamp to the current UTC time.
        This method simulates updating the record in a database.
        '''
        self.updated_at = datetime.utcnow()

    def delete(self):
        '''Marks the model instance as deleted
        by setting the updated_at timestamp to None.
        This method simulates deleting the record from a database.
        '''
        self.updated_at = None

    def __str__(self):
        """Returns a concise string representation of the model instance."""
        return "[{}]{}{}".format(self.__class__.__name__, self.id, self.__dict__)
