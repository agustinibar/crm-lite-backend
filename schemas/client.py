from pydantic import BaseModel
from typing import Optional

class ClientBase(BaseModel):
    nombre: str
    email: str
    telefono: Optional[str]
    empresa: Optional[str]

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True
