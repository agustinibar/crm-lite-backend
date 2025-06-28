from pydantic import BaseModel

class TaskBase(BaseModel):
    description: str
    done: bool = False
    client_id: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
