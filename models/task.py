from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(200))
    done = Column(Boolean, default=False)
    client_id = Column(Integer, ForeignKey("clients.id"))

    client = relationship("Client", backref="tasks")
