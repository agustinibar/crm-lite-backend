from pydantic import BaseModel
from typing import Optional

class NoteBase(BaseModel):
    content: str
    client_id: int

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int

    class Config:
        orm_mode = True
