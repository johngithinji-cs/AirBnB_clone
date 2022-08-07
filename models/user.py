#!/usr/bin/python3
"""Introduces the User class"""
from models.base_model import Basemodel



class User(BaseModel):
    """Models a User.
    
    Attributes:
        
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
