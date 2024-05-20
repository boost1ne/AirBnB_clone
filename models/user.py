#!/usr/bin/python3
"""
Defines the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):

    """Inherits from BaseModel and has the following attributes:
    email (str): The email address of the user.
    password (str): The password of the use.
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
