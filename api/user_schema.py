from pydantic import BaseModel
from typing import Optional

class CreateUser(BaseModel):
    id: str
    pw: str
    name: str
    phone:str

    class Config:
        json_schema_extra = {
            "example" : {
                "id" : "아이디",
                "pw" : "비번",
                "name": "이름",
                "phone" : "010-1234-1234"
            }
        } 

class DeleteUser(BaseModel):
    id: str
    pw: str

    class Config:
        json_schema_extra = {
            "example" : {
                "id" : "아이디",
                "pw" : "비번"
            }
        } 

class UpdateUser(BaseModel):
    pw: str
    name: str
    phone:str

    class Config:
        json_schema_extra = {
            "example" : {
                "pw" : "비번",
                "name": "이름",
                "phone" : "010-1234-1234"
            }
        } 