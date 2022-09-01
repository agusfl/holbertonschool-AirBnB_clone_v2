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
        # Si se llega a este else es porque se esata en el storage: FileStorage
        # Seteamos un getter (usando el decorador: @property)
        @property
        def cities(self):
            all_cities = models.storage.all(City).values()

            return_list = []
            for city in all_cities:
                # Se compara id del objeto de tipo State con City
                if (city.state_id == self.id):
                    # Se guarda el resultado en la lista a retornar
                    return_list.append(city)
            return return_list
