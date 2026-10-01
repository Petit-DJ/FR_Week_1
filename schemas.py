# #schemas.py
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=3)
    done: bool = False


class Task(TaskCreate):
    id: int
