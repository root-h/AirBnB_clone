#!/usr/bin/python3
"""
This is the filestorage
"""

import json

class FileStorage:
    """
    This class serializes instances to JSON and deserializes JSON to instances 
    """

    __file_path= "file.json"
    __objects ={}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]=obj
    
    def save(self):
        """
        Serializes __objects to JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage={}
            for k, v in self.__objects.items():
                dict_storage[k]=v.to_dict()
            json.dumps(dict_storage, f)
    
    def reload(self):
        """
        Deserializes JSON file to __objects if it exists
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
            