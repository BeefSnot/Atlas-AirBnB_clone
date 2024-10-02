#!/usr/bin/python3
"""
FileStorage class module for AirBnB clone
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Class serializes/deserializes instances to/from JSON file

    Attributes:
        __file_path (str):  path to JSON file
        __objects (dict):   dictionary of objects

    Methods:
        all(self):          returns dictionary of objects
        new(self, obj):     sets obj in __objects with key <obj class name>.id
        save(self):         serializes __objects to JSON file
        reload(self):       deserializes JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initializes FileStorage class
        """
        self.__objects = {}
        self.reload()

    def all(self):
        """
        Returns dictionary of objects

        Returns:
            dict:  __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Pairs objects with keys in __objects

        Attributes:
            obj (BaseModel):  object to set in __objects
        """
        key = self.key_create(obj)  # create key
        self.__objects[key] = obj  # set object in __objects

    def save(self):
        """
        Serializes __objects to JSON file

        Attributes:
            obj_dict (dict):  dictionary to store objects
        """
        obj_dict = {}  # dictionary to store objects
        for key, value in self.__objects.items():  # iterate through __objects
            obj_dict[key] = value.to_dict()  # add object to dictionary
        with open(self.__file_path, "w", encoding="utf-8") as file:  # open
            json.dump(obj_dict, file)  # write to file

    def reload(self):
        """
        Deserializes JSON file to __objects

        Attributes:
            obj_dict (dict):  dictionary to store objects
            obj_class (dict): dictionary of classes
        """
        try:
            with open(self.__file_path, "r") as file:  # open file
                obj_dict = json.load(file)  # load file
            classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Place": Place,
                "Amenity": Amenity,
                "Review": Review,
            }  # dictionary of classes
            for key, value in obj_dict.items():  # iterate through obj_dict
                class_name = value.get("__class__")  # get class name
                if class_name in classes:
                    self.__objects[key] = classes[class_name](**value)  # creat
        except FileNotFoundError:  # if file not found
            pass  # do nothing

    def key_create(self, obj):
        """
        Creates key for object

        Attributes:
            obj (BaseModel):  object to create key for

        Returns:
            str:  key for object
        """
        return type(obj).__name__ + "." + obj.id
