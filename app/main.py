from fastapi import FastAPI
from .database import Base, engine
from .routers import users, musicians, albums, tracks

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(musicians.router)
app.include_router(albums.router)
app.include_router(tracks.router)

@app.get("/")
def root():
    return {"message": "Music Catalog API"}
