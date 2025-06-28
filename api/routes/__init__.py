from fastapi import APIRouter
from . import client, user, note, task

router = APIRouter()
router.include_router(client.router)
router.include_router(user.router)
router.include_router(note.router)
router.include_router(task.router)
