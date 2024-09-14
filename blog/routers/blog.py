from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import  schemas, database, models
from sqlalchemy.orm import Session


router = APIRouter(
    tags= ['Blogs']
)
get_db = database.get_db


@router.get('/blog', response_model=List[schemas.showBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs 

@router.post('/blog',status_code=status.HTTP_201_CREATED)     # Here status code of response is changed to 201 instead of 200, Because documented code for creation is 201.
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    blog= db.query(models.Blog).filter(models.Blog.id==id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id{id} nt found")

    blog.delete(synchronize_session=False)
    db.commit()
    return "Done"


@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog,  db: Session = Depends(get_db) ):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id{id} nt found")
    blog.update(request.dict())
    db.commit()
    return 'updated'

@router.get('/blog/{id}', status_code=200, response_model=schemas.showBlog)
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id ==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the id {id} is not avialable")
    
           # or alternative but above one is better.
        # response.status_code = status.HTTP_404_NOT_FOUND   
        # return {'detail': f"Blog with the id {id} is not avialable"}
    return blog
