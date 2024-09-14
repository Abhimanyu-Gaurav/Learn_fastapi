from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class Blog(Base):         # Here Blog is actually extended base of database.
     __tablename__ = "blogs"
     id = Column(Integer, primary_key=True)
     title = Column(String)
     body = Column(String)


class User(Base):
     __tablename__ = "users"
     id = Column(Integer, primary_key=True)
     name = Column(String) 
     email = Column(String)
     password = Column(String)