from sqlalchemy.orm import session
from .. import models, schemas
from fastapi import status, HTTPException


def get_all(db : session):
    blogs = db.query(models.Blog).all()
    return blogs 


def create(db: session, request: schemas.Blog):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int, db: session):
    blog= db.query(models.Blog).filter(models.Blog.id==id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id{id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return "Done"


def update(id:int, request:schemas.Blog, db: session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id{id} nt found")
    blog.update(request.dict())
    db.commit()
    return 'updated'

def show(id:int, db: session,):
    blog = db.query(models.Blog).filter(models.Blog.id ==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the id {id} is not avialable")
    return blog
