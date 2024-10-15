from pydantic import BaseModel
from typing import Optional

class NewUser(BaseModel):
    id:str
    pw:str