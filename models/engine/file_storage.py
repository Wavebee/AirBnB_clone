#!/usr/bin/python3
"""file_storage module"""

import json
import os


class FileStorage:
    """FileStorage class definition"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            obj_dict = {key: val.to_dict() \
                    for key, val in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)

            for obj in obj_dict.values():
                cls_name = obj["__class__"]
                del obj["__class__"]
                self.new(eval(cls_name)(**o))
