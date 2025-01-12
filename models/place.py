#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.city import City
from models.user import User
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship(
        "Review", backref="place", cascade="all, delete-orphan")

    amenities = relationship(
            'Amenity', secondary='place_amenity', viewonly=False)

#    amenity_id_list = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def reviews():
            """ getter for reviews that returns list of
                review instances with place_id equal to current Place.id
            """
            review_list = []
            for review_search in self.reviews:
                if review_search.place_id == self.id:
                    review_list.append(review_search)
            return review_list

    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def amenities(self):
            '''Returns value of amenity instances
            '''
            amenities_list = []
            for amenit_search in self.amenities:
                if amenit_search.place_id == self.id:
                    amenities_list.append(amenit_search)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            '''setter for amenities
            '''
            if type(obj).__name__ == 'Amenity':
                self.amenity_ids.append(obj)
