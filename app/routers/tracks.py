from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Musician

router = APIRouter(
    prefix="/tracks",
    tags=["tracks"]
)

@router.get("/")
def get_top_tracks(db: Session = Depends(get_db)):
    musicians = db.query(Musician).all()
    musician_ratings = []
    for musician in musicians:
        if musician.albums:
            avg_rating = sum(album.rating for album in musician.albums) / len(musician.albums)
            musician_ratings.append({"musician": musician.name, "avg_rating": avg_rating})
    top = sorted(musician_ratings, key=lambda x: x["avg_rating"], reverse=True)[:3]
    return top
