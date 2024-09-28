#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = 'i.niwemwana@alustudent.com'
    password = 'jojo2003'
    first_name = 'Innocente'
    last_name = 'Aline'