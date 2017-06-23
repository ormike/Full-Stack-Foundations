'''
Created on Jun 17, 2017

@author: bruns
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from puppies_database_setup import Base, Shelter, Puppy

import datetime


engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def query_one():
    """Query all of the puppies and return the results in ascending alphabetical order"""
    result = session.query(Puppy.name).order_by(Puppy.name.asc())   #.all()
    for name in result:
        print name[0]
    pass

def query_two():
    """Query all of the puppies that are less than 6 months old organized by the youngest first"""
    today = datetime.date.today()
    print "today is " + str(today)
    sixMonthsAgo = today - datetime.timedelta(days = 182)
    print "six months ago it was " + str(sixMonthsAgo)
    result = session.query(Puppy.name, Puppy.dateOfBirth).filter(Puppy.dateOfBirth >= sixMonthsAgo).order_by(Puppy.dateOfBirth.desc())
    for name in result:
        print name[0] + " born on " + str(name[1])

def query_three():
    """Query all of the puppies by ascending weight"""
    result = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight.asc())   #.all()
    for name in result:
        print name[0] + " weighs " + str(name[1])
    pass

def query_four():
    """Query all puppies grouped by the shelter in which they are staying"""
    shelters = session.query(Shelter.name, Shelter.id).order_by(Shelter.name.asc())
    print "here is the list of shelters:"
    for shelter in shelters:
        print shelter[0]
    print
    #result = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id)
    result = session.query(Shelter.name, Puppy.name).join(Puppy).order_by(Shelter.id)
    for item in result:
        print item

    for shelter in shelters:
        print "puppies in "+ shelter[0] + ":"
        puppies = session.query(Puppy.name).filter(Puppy.shelter_id == shelter[1]) #.order_by(Puppy.name.asc())
        for puppy in puppies:
            print puppy[0]


if __name__ == '__main__':
#     query_one()
#     query_two()
#     query_three()
    query_four()
    pass