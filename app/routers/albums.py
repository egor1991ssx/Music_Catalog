from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..security import get_current_user

router = APIRouter(
    prefix="/albums",
    tags=["albums"]
)

@router.post("/", response_model=schemas.AlbumOut)
def create_albums(
    album: schemas.AlbumCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)  # Защищённый эндпоинт
):
    db_album = models.Album(**album.dict())
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album

@router.get("/", response_model=list[schemas.AlbumOut])
def read_albums(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Album).offset(skip).limit(limit).all()
