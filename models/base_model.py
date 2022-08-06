#!/usr/bin/python3
"""
This is the base model for the BNB project
"""

from datetime import datetime
import models
from uuid import uuid4

class BaseModel:
    """
    Defines all common attributes 
    """

    def __init__(self, *args, **kwargs):
        """
        Base class init method
        """
        if kwargs:
            for arg, val in kwargs.items():
                val=datetime.strftime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg,val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at=datetime.now()
            self.updated_at=self.created_at
            models.storage.new(self)
   
    def __str__(self):
        """
        Prints the content of base model in $ [<class name>](<self.id>)<self.__dict__>
        """

        return '[{0}] ({1}) {2}'.format(
            self.__class__.__name__,self.id, self.__dict__
        )
    
    def save(self):
        """
            Updates the base model instance 
            Updates the public instance attribute 'updated_at'
            with current date time and dumps the data into a file
        """
        self.updated_at=datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """
            converts infomaion in class to human readable format
            return new dictionary containing all key/values of __dict__instance 
        """
        class_info=self.__dict__.copy()
        class_info['__class__']=self.__class__.__name__
        class_info['created_at']= self.created_at.isoformat()
        class_info['updated_at']= self.updated_at.isoformat()

        return class_info
