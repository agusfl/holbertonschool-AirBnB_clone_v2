#!/usr/bin/python3
"""define FileStorage"""
import json
from models.base_model import BaseModel
from os.path import exists
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            dict_of_classes = {}
            for key, value in self.__objects.items():
                # Si el nombre de la clase del objeto es igual a la clase
                # lo agregamos en el dic a retornar
                if value.__class__ == cls:
                    dict_of_classes[key] = self.__objects[key]
            return dict_of_classes

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Borrar un objeto"""
        if not obj:
            return
        else:
            cp_objects = FileStorage.__objects.copy()
            for key, value in cp_objects.items():
                if value == obj:
                    del FileStorage.__objects[key]
                    self.save()

    def close(self):
        """
        Deserialize JSON file to objects
        """
        self.reload()
