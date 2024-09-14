from fastapi import APIRouter, Depends, status, HTTPException
from .. import database, schemas, models 
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user


 

router = APIRouter(
    prefix= "/user",
    tags= ['Users']
)
get_db = database.get_db



@router.post('/', response_model=schemas.showuser)
def create_user(request: schemas.user, db: Session = Depends(get_db)):
  
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.showuser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.show(id, db)