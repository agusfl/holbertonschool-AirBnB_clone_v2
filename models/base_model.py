#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
# Import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()  # this is for sqlalchemy


class BaseModel:
    """A base class for all hbnb models"""
    # Se crean las variables que va a tener la tabla "states":
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs and kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                elif key == "__class__":
                    pass  # No le seteamos nada,solo usamos pass
                else:
                    setattr(self, key, value)
            # ID - para agregar en la TASK 10 cuando se pasa como kwargs
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())  # convert the id to string
            self.created_at = datetime.now()  # Use method now of datetime mod
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance
        --> Print to_dict() method
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        # Creamos una copia para poder recorrer y borrar el elemnto buscado
        # en "dictionary", si no se recorre la copia da error porque no se
        # puede borrar un elemento mientras se esta iterando el dic.
        dictionary_copy = dictionary.copy()
        # Buscamos si existe "_sa_instanca_state" y si esta la borramos
        for key, value in dictionary_copy.items():
            if key == "_sa_instance_state":
                dictionary.pop(key)
        return dictionary

    def delete(self):
        """
        Delete the current instance from the storage (models.storage) by
        calling the method delete (from storage).
        """
        # Se llama al metodo delete creado en "file_storage.py"
        models.storage.delete(self)
