from fastapi import FastAPI
from typing import Optional 
from pydantic import BaseModel


app = FastAPI()

      ## GEt method
# @app.get("/")    # Here,("/") is path, .get is operation, @app is decorator. on whole it is called path     operation decorator. In operation we can also use Post, Put and Delete method. 
# def index():     # path operation function.
#     return {"Hello! World"}


# @app.get("/about")
# def about():
#     return {"data" : "Welcome to FastAPI"}


# @app.get("/")
# def blogs():
#     return {"data" : "blog list"}

@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str]= None):
    # only get 10 published blog or whatever we set.
    if published:
        return {"data" : f'{limit} published blogs from the db'}
    else:
        return {"data" : f'{limit} blogs from the db'}



@app.get("/blog/unpublished")
def unpublished():
    return {"data" : "all unpublished blogs"}


@app.get("/blog/{id}") # when we need dynamic routing then we put {id} in it. Mainly use Curly bracket.
def show(id : int):
    # fetch blog with id = id
    return {"data" : id}



@app.get("/blog/{id}/comments")
    # fetch comments of blog with id = id
def comments(id, limit=10):
    return {"data" : {'1','2'}}


        ## POST method

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool] 


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data" : f"Blog is created with tittle as {blog.title} "}