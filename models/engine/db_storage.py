#!/usr/bin/python3
"""Define methods and attributes for DBStorage class"""
from os import getenv
from models.base_model import Base
from models.user import User
from models.review import Review
from models.place import Place
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from models.state import State
from models.city import City
from models.amenity import Amenity
from sqlalchemy.orm import scoped_session


class DBStorage:
    """Def class DBStorage engine for database like mysql"""
    __engine = None
    __session = None

    def __init__(self):
        """def method init that initialized an objetc of DBStorage"""
        env = getenv("HBNB_ENV")
        userDB = getenv("HBNB_MYSQL_USER")
        passwordDB = getenv("HBNB_MYSQL_PWD")
        hostDB = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(userDB, passwordDB,
                                              hostDB, database),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        def method all that return all objects depending of the class name
        or return all if no class name is passed.
        """
        dic_return = {}
        classes = {
               'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
        # Si no se pasa una clase, es porque se quiere todos los datos
        if cls is None:
            for clase in classes:
                # Se obtiene la data en la query por todas las clases
                data = self.__session.query(classes[clase]).all()
                for obj in data:
                    # Se obtiene la key para setear el obj en el dic a retornar
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    # Se agregan los objetos en el diccionario a retornar
                    dic_return[key] = obj
            return dic_return
        else:
            # Esto es para cuando se pasa un clase especifica:
            if classes[cls.__name__]:
                # Se obtiene la data en la query por todas las clases
                objects = self.__session.query(classes[cls.__name__]).all()
                for obj in objects:
                    key = type(obj).__name__ + '.' + obj.id
                    dic_return[key] = obj
            return dic_return

    def new(self, obj):
        """
        Add the object to the current database session
        --> add object to the database using add( method)
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        --> Save changes using commit() method
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None
        --> Use of delete method() with session
        """
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
        """
        * Create all tables in the database (feature of SQLAlchemy)
        --> WARNING: all classes who inherit from Base must be imported before
        calling Base.metadata.create_all(engine).
        * Create the current database session (self.__session) from the engine
        (self.__engine) by using a sessionmaker - the option expire_on_commit
        must be set to False ; and scoped_session - to make sure your Session
        is thread-safe.
        """
        # Create all tables in the database
        Base.metadata.create_all(self.__engine)
        # Create a new session for the current database using sessionmaker
        new_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # Scoped session only one session per thread
        Session = scoped_session(new_session)
        self.__session = Session

    def close(self):
        '''
        Call remove() method on the private session attribute
        Info: https://docs.sqlalchemy.org/en/13/orm/contextual.html
        '''
        self.__session.remove()
