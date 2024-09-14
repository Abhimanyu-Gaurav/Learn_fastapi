from .. import schemas, models
from ..hashing import Hash
from sqlalchemy.orm import Session
from fastapi import status,HTTPException


def create(request: schemas.user, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

def show(id:int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with the id {id} is not avialable")
    return user