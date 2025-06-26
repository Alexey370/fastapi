from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: str | None = None

class STask_read(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True) #«Разреши создавать эту модель не только из dict, но и из объектов с атрибутами (например, SQLAlchemy ORM).»

class STask_Id(BaseModel):
    ok: bool = True
    task_id: int