from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/musicians",
    tags=["musicians"]
)

@router.post("/", response_model=schemas.MusicianOut)
def create_musician(musician: schemas.MusicianCreate, db: Session = Depends(get_db)):
    db_musician = models.Musician(**musician.dict())
    db.add(db_musician)
    db.commit()
    db.refresh(db_musician)
    return db_musician

@router.get("/", response_model=list[schemas.MusicianOut])
def read_musicians(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Musician).offset(skip).limit(limit).all()
