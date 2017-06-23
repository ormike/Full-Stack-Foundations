'''
Created on Jun 17, 2017

@author: bruns
'''

import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, Float
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'
    name = Column(String(80), nullable = False)
    address = Column(String(80))
    city = Column(String(80))
    state = Column(String(80))
    zipCode = Column(String(80))
    website = Column(String(80))
    id = Column(Integer, primary_key = True)
    
class Puppy(Base):
    __tablename__= 'puppy'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key=True)
    dateOfBirth = Column(Date)
    gender = Column(String(80))
    weight = Column(Float)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    picture = Column(String(250))
    
    
engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)
    
    

if __name__ == '__main__':
    pass