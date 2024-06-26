#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ The state table
    class Attributes:
        __tablename__ (string): The name of table.
        name (String): The name of the State.
        cities (relationship): The State-City relationship.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete, delete-orphan",
        backref="state"
    )

    @property
    def cities(self):
        """ returns the list of City instances """
        list_city = []
        for city in list(models.storage.all(City).values()):
            if city.state_id == self.id:
                list_city.append(city)
        return list_city
