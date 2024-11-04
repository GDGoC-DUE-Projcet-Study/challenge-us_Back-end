from pydantic import BaseModel
from typing import Optional

class CreateTodo(BaseModel):
    title: str
    description:str

class DeleteTodo(BaseModel):
    title: str
    description:str

class UpdateTodo(BaseModel):
    title: str
    description:str