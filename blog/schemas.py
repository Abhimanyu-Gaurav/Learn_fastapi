from typing import List
from pydantic import BaseModel


class Blog(BaseModel):
    title : str
    body : str



class user(BaseModel):
     name : str
     email : str
     password : str 
 
class showuser(BaseModel):
     name : str
     email : str
     blogs : List [Blog]

       
class showBlog(BaseModel):
     title : str
     body : str
     creator : showuser


class Login(BaseModel):
     username : str
     password : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

    