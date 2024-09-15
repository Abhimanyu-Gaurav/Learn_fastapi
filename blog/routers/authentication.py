
from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models, token
from sqlalchemy.orm import session
from ..hashing import Hash
from datetime import timedelta

router = APIRouter(tags= ['Authentication'])


@router.post('/login')
def login(request: schemas.Login, db: session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
    
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}