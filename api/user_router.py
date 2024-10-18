from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter,Depends

from api import user_schema
from api import user_crud

user = APIRouter(
        prefix="/user",
)

@user.post(path="/create", description="회원가입 - 유저 생성")
async def create_user(new_user:user_schema.CreateUser,db: Session = Depends(get_db)):
    return user_crud.insert_user(new_user, db)
