#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    # creamos la tabla "cities" la clase City va a estar asociada a esta tabla
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
