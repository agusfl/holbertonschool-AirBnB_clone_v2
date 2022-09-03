#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    # creamos la tabla "states" la clase City va a estar asociada a esta tabla
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        # Relacionamos State con City - si se elimina un Estado, se tendrian
        # que eliminar todas las ciudades dentro de ese Estado.
        cities = relationship('City', backref="state", cascade="all ,\
                                delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """devolver una lista de instancias de city"""
        inst_list = []
        list_objects = models.storage.all(City)
        for city in list_objects.values():
            if city.state_id == self.id:
                inst_list.append(city)
        return inst_list
