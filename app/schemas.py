from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class MusicianBase(BaseModel):
    name: str
    biography: str

class MusicianCreate(MusicianBase):
    pass

class MusicianOut(MusicianBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class AlbumBase(BaseModel):
    title: str
    description: str
    year: int
    musician_id: int

class AlbumCreate(AlbumBase):
    pass

class AlbumOut(AlbumBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class TrackBase(BaseModel):
    title: str
    duration: float
    album_id: int

class TrackCreate(TrackBase):
    pass

class TrackOut(TrackBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None