from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.task import Task as TaskModel
from schemas.task import Task, TaskCreate
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/client/{client_id}", response_model=List[Task])
def list_tasks(client_id: int, db: Session = Depends(get_db)):
    return db.query(TaskModel).filter(TaskModel.client_id == client_id).all()
