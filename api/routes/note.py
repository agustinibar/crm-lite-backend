from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.note import Note as NoteModel
from schemas.note import Note, NoteCreate
from typing import List

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("/", response_model=Note)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = NoteModel(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.get("/client/{client_id}", response_model=List[Note])
def list_notes(client_id: int, db: Session = Depends(get_db)):
    return db.query(NoteModel).filter(NoteModel.client_id == client_id).all()
