from fastapi import FastAPI
from typing import Optional 

app = FastAPI()


@app.get("/")
def index():
    return {"Hello! World"}


@app.get("/about")
def about():
    return {"data" : "Welcome to FastAPI"}


@app.get("/")
def blogs():
    return {"data" : "blog list"}

