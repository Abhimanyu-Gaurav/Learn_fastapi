 ## To perform CURD operation

from fastapi import FastAPI
from . import schemas, models
from .database import engine


app = FastAPI()


models.Base.metadata.create_all(bind=engine)  # this will create Table in db.


@app.post('/blog')
def create(request: schemas.Blog):
    return request

