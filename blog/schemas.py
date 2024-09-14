from pydantic import BaseModel

class Blog(BaseModel):
    title : str
    body : str

class showBlog(BaseModel):
     title : str
     body : str

class user(BaseModel):
     name : str
     email : str
     password : str 

    