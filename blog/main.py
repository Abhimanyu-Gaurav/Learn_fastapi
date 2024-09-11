 ## To perform CURD operation

from fastapi import FastAPI, Depends, status
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()


models.Base.metadata.create_all(bind=engine)  # this will create Table in db.

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()



@app.post('/blog',status_code=status.HTTP_201_CREATED)  # Here status code of response is changed to 201 instead of 200, Because documented code for creation is 201.
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs 

@app.get('/blog/{id}')
def show(id, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id ==id).first()
    return blogs