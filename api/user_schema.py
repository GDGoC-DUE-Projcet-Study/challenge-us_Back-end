from pydantic import BaseModel
from typing import Optional

class CreateUser(BaseModel):
    id: str
    pw: str
    name: str
    phone:str

class DeleteUser(BaseModel):
    id: str
    pw: str

class UpdateUser(BaseModel):
    pw: str
    name: str
    phone:str