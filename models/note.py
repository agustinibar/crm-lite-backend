from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(500))
    client_id = Column(Integer, ForeignKey("clients.id"))

    client = relationship("Client", backref="notes")
