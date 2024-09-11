 ## To perform CURD operation

from fastapi import FastAPI, Depends, status, Response, HTTPException
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



@app.post('/blog',status_code=status.HTTP_201_CREATED)     # Here status code of response is changed to 201 instead of 200, Because documented code for creation is 201.
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

@app.get('/blog/{id}', status_code=200)
def show(id, response:Response,  db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id ==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the id {id} is not avialable")
           # or alternative but above one is better.
        # response.status_code = status.HTTP_404_NOT_FOUND   
        # return {'detail': f"Blog with the id {id} is not avialable"}
    return blog