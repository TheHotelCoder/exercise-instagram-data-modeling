import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable =False)
    Followers = Column(Integer)
    Following = Column(Integer)
    Description = Column(String(250))
    LikedPosts= relationship('liked_posts_byuser', back_populates="Users")
 
    
class Post(Base):
    __tablename__ = 'Posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Description = Column(String(250))
    Comments = Column(String(250))
    person_id = Column(Integer, ForeignKey('Users.id'))
    person = relationship(User)
    
class User_Liked_Posts(Base):
    __tablename__ = 'liked_posts_byuser'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user= relationship(User, back_populates="liked_posts_byuser")
    post_id = Column(Integer, ForeignKey('Posts.id'))
    post = relationship(Post)
   

class Post_Comments_By_User(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    user_id= Column(Integer, ForeignKey('Users.id'))
    user=relationship(User)
    post_id= Column(Integer, ForeignKey('Posts.id'))
    post=relationship(Post)


# class Followers(Base):
#     __tablename__ = 'User_Followers'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     post_id = Column(Integer, ForeignKey('Posts.id'))
#     post = relationship(Post) 
    

    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e