from pydantic import BaseModel
from typing import Optional

class CreateUser(BaseModel):
    id: str
    pw: str
    name: str

class DeleteUser(BaseModel):
    id: str
    pw: str
    name: str

class UpdateUser(BaseModel):
    id: str
    pw: str
    name: str