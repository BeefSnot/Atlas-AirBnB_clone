#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, password):
        super().__init__()  # Call the superclass constructor
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def greet(self, custom_message=None):
        '''
        Generate a greeting message for the user.

        Parameters:
        - custom_message (str): an optional message to append to the greeting

        Returns:
        - str: a personalized greeting message.
        '''
        full_name = f"{self.first_name} {self.last_name}"
        if custom_message:
            return f"{custom_message}, {full_name}"
        else:
            return f"Hello, {full_name}!"

    @staticmethod
    def create_user(first_name, last_name, email, password):
        '''
        Create a new user profile.

        Parameters:
        - first_name (str): the user's first name.
        - last_name (str): the user's last name.
        - email (str): the user's email address.
        - password (str): the user's password.

        Returns:
        - User: a new user object representing the created profile.
        '''
        return User(first_name, last_name, email, password)

    @staticmethod
    def display_users(users):
        '''
        Display information about the given users.

        Parameters:
        - users (list of User objects): a list of user objects to display information
        '''
        for user in users:
            print(f"Name: {user.first_name} {user.last_name}")
            print(f"Email: {user.email}")
            print(user.greet())
