import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    created_at=Column(DateTime(timezone=False))

class Favorites(Base):
    __tablename__='favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))


class Character(Base):
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(15))
    skin_color = Column(String(15))
    eye_color = Column(String(15))
    birth_year = Column(String(30))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planets(Base):
    __tablename__='planets'
    id=Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    rotation_period=Column(Integer)
    orbital_period=Column(Integer)
    diameter=Column(Integer)
    climate=Column(String(255))
    gravity=Column(String(20))
    terrain=Column(String(255))
    population=Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
