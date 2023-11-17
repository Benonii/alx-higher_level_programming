#!/usr/bin/python3

''' This module contains the base class for the States table '''

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    ''' This class definition of the State '''

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State', back_populates='cities')
