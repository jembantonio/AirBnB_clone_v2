#!/usr/bin/python3
''' database storage class for AirBnB
'''

from os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage:
    '''Database Storage class
    '''
    __engine = None
    __session = None

    def __init__(self):
    ''' initializes the Database Storage instance
    '''
    user = os.getenv("HBNB_MYSQL_USER")
    pswd = os.getenv("HBNB_MYSQL_PWD")
    host = os.getenv("HBNB_MYSQL_HOST")
    dbse = os.getenv("HBNB_MYSQL_DB")

    self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        user, pswd, host, dbse), pool_pre_ping=True)

    if os.getenv("HBNB_ENV") == "test":
        Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None)
    '''queries on the current database session (self.__session)
    '''
        cls_dict = {}
        if cls is not None:
            for cls_inst in self.__session.query(cls).all():
                cls_dict.append(cls_inst)

        if cls is None:
            for cls_inst in self.__session.query(
                User, State, City, Amenity, Place, Review).all():
                cls_dict.append(cls_inst)

        return(cls_dict)

    def new(self, obj):

    def save(self):
        self.__session