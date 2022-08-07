#!/usr/bin/python3
"""Module for FileStorage class."""

import datetime
import json
import os
from models import base_model
from models.user import User

BaseModel = base_model.BaseModel
nameClass = ["BaseModel"]

class FileStorage:
    """Class for JSON serializtion and deserialization and storing of base classes."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        className = obj.__class__.__name__
        id = obj.id
        classId = className + "." + id
        FileStorage.__objects[classId] = obj

    def save(self): 
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Serializes the JSON file to __objects"""
        dic_obj = {}
        FileStorage.__objects = {}
        if (os.path.exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as file_:
                dictObj = json.load(file_)
                for key, value in dictObj.items():
                    className = key.split(".")[0]
                    if className in nameClass:
                        FileStorage.__objects[key] = eval(className)(**value)
                    else:
                        pass
