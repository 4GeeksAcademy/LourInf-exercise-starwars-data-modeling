import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


# We use declarative_base() from SQLAlchemy to create a base class (Base)
Base = declarative_base()

# We create a class (1 class = 1 table) that will inherit from the base class. Naming convention: PascalCase, plural:
class Users(Base):
    # 1. We create the table alias __tablename__. Naming convention: snake_case
    __tablename__ = "users"
    # 2. We define the columns of the table:
    # 2.1. We define the primary key, with data type,primary_key=True
    id = Column(Integer, primary_key=True)
    # 2.2. We define the model attributes, with data type
    email = Column(String, unique=True)
    password = Column(String,nullable=False)
    subscription_date = Column(Date)

# We create a class (1 class = 1 table) that will inherit from the base class. Naming convention: PascalCase, plural:
class Characters(Base):
    # 1. We create the table alias __tablename__. Naming convention: snake_case
    __tablename__ = "characters"
    # 2. We define the columns of the table:
    # 2.1. We define the primary key, with data type,primary_key=True
    id = Column(Integer, primary_key=True)
    # 2.2. We define the model attributes, with data type
    name = Column(String(100),nullable=False)
    description = Column(String(250), nullable=False)
    height = Column(String)
    mass = Column(String)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    homeworld = Column(String)
    url = Column(String)

# We create a class (1 class = 1 table) that will inherit from the base class. Naming convention: PascalCase, plural:
class Planets(Base):
    # 1. We create the table alias __tablename__. Naming convention: snake_case
    __tablename__ = "planets"
    # 2. We define the columns of the table:
    # 2.1. We define the primary key, with data type,primary_key=True
    id = Column(Integer, primary_key=True)
    # 2.2. We define the model attributes, with data type
    name = Column(String(100),nullable=False)
    description = Column(String(500), nullable=False)
    diameter = Column(String)
    rotation_period = Column(String)
    orbital_period = Column(String)
    gravity = Column(String)
    population = Column(String)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(String)
    url = Column(String)

# We create a class (1 class = 1 table) that will inherit from the base class. Naming convention: PascalCase, plural:
class FavoriteCharacters(Base):
    # 1. We create the table alias __tablename__. Naming convention: snake_case
    __tablename__ = "favorite_characters"
    # 2. We define the columns of the table:
    # 2.1. We define the primary key, with data type,primary_key=True
    id = Column(Integer, primary_key=True)
    # 2.2. We define the model attributes, with data type
    # no attributes here
    #2.3. We define the foreign key, with data type,ForeignKey("alias.id")
    users_id = Column(Integer, ForeignKey("users.id"))  # # many:many relationship: users_id int fk
    characters_id = Column(Integer, ForeignKey("characters.id"))  # characters_id int fk
    # 3. We define the relationships: relationship(Models)
    users = relationship(Users)  # users_id int fk >-< users.id
    characters = relationship(Characters)  # characters_id int fk >-< characters.id

# We create another class
class FavoritePlanets(Base):
    __tablename__ = "favorite_planets"
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey("users.id"))  # many:many relationship (many users can have many favorites)
    planets_id = Column(Integer, ForeignKey("planets.id")) 
    users = relationship(Users)  
    planets = relationship(Planets)

# We create another class
class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250)) 
    street_number = Column(String(250)) 
    post_code = Column(String(250), nullable=False) 
    users_id = Column(Integer, ForeignKey("users.id")) # 1:many relationship (1 user can have many addresses)
    users = relationship(Users)

    def to_dict(self):
        return{}

# We create another class, with relation 1:1
class Profiles(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50),nullable=False)
    lastname = Column(String(50),nullable=False)
    nickname = Column(String(50),nullable=False)
    image_url = Column(String(150),nullable=False)
    users_id = Column(Integer, ForeignKey("users.id"), unique=True)  # unique=True defines the 1:1 relationship (1 profile: 1 user)
    users = relationship(Users)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
