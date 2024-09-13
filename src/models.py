import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Enum

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer)
    user_to_id = Column(Integer)
    
    #es asi???
    user_id = Column(Integer, ForeignKey('user_id'))
    user = relationship(User)
 
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name= Column(String(20), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), unique=True)



class MyEnum(enum.Enum):
    image= "image"
    video = "video"
    

class Media(Base):
    __tablename__= 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MyEnum))
    url = Column(String(200))
    post_id = Column(Integer)

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)

class Comment(Base):
    __tablename__= 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer)
    post_id = Column(Integer)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
