from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.client import Client as ClientModel
from schemas.client import Client, ClientCreate
from typing import List

router = APIRouter(prefix="/clients", tags=["Clients"])

@router.post("/", response_model=Client)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = ClientModel(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.get("/", response_model=List[Client])
def list_clients(db: Session = Depends(get_db)):
    return db.query(ClientModel).all()

@router.get("/{client_id}", response_model=Client)
def get_client(client_id: int, db: Session = Depends(get_db)):
    return db.query(ClientModel).get(client_id)

@router.put("/{client_id}", response_model=Client)
def update_client(client_id: int, client: ClientCreate, db: Session = Depends(get_db)):
    db_client = db.query(ClientModel).get(client_id)
    for key, value in client.dict().items():
        setattr(db_client, key, value)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    db_client = db.query(ClientModel).get(client_id)
    db.delete(db_client)
    db.commit()
    return {"detail": "Client deleted"}
