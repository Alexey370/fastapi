from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: str | None = None

class STask_read(STaskAdd):
    id: int

class STask_Id(BaseModel):
    ok: bool = True
    task_id: int