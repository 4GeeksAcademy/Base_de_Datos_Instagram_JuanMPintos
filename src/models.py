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
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name= Column(String(20), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), unique=True)

    relation_follower = relationship('Follower', backref = 'user')
    relation_post = relationship('Post', backref = 'user')
    relation_comment = relationship('Comment', backref = 'user')


class MyEnum(enum.Enum):
    image= "image"
    video = "video"
    

class Media(Base):
    __tablename__= 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum("image", "video", "audio", name="media_types"), nullable=False)
    url = Column(String(200))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    relation_media = relationship('Media', backref = 'post')
    relation_comment = relationship('Comment', backref = 'post')


class Comment(Base):
    __tablename__= 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
