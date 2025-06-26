from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository

from schemas import STask_read, STaskAdd, STask_Id

router = APIRouter(
    prefix="/tasks"
)


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STask_Id:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}    

@router.get("")
async def get_tasks() -> list[STask_read]:
    tasks = await TaskRepository.find_all()
    return tasks