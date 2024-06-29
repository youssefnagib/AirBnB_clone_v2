#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """_summary_
    create for Tables some Attributes represents amenity in MySql database,
    use SQLAlchemy

    class Attributes:
        __tablename__: class attribute string represents
                        the table name, amenities
        name : string represent Amenity name
        place_amenities: Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
